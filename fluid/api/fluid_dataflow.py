#  Copyright 2023 The Fluid Authors.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import copy
import logging

from fluid import FluidClient
from fluid import models
from fluid import constants
from kubernetes import client

from typing import List, Dict

logger = logging.getLogger("fluidsdk")


class FluidDataFlow(object):
    def __init__(
            self,
            dataset_name,
    ):
        self.fluid_client = FluidClient()

        try:
            dataset = self.fluid_client.get_dataset(dataset_name)
        except Exception as e:
            raise RuntimeError(f"failed to get dataset {dataset_name}: {e}")

        if dataset.status is None or dataset.status.phase != "Bound":
            raise RuntimeError(f"dataset {dataset_name} is not bound")

        self.dataset_name = dataset_name
        self.flow_ops = []

    def preload(self, target_path="/", load_metadata=False):
        op = models.DataLoad(
            api_version=constants.API_VERSION,
            kind=constants.DATA_LOAD_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.fluid_client.namespace,

            ),
            spec=models.DataLoadSpec(
                load_metadata=load_metadata,
                dataset=models.TargetDataset(
                    name=self.dataset_name,
                    namespace=self.fluid_client.namespace
                ),
                target=[]
            )

        )

        if isinstance(target_path, List):
            for path in target_path:
                op.spec.target.append(models.TargetPath(path=path, replicas=1))
        elif isinstance(target_path, Dict):
            for path, replicas in target_path.items():
                op.spec.target.append(models.TargetPath(path=path, replicas=replicas))
        elif isinstance(target_path, str):
            op.spec.target.append(models.TargetPath(path=target_path, replicas=1))

        self.flow_ops.append(op)
        return self

    def migrate(self, path, migrate_direction, external_storage):
        global spec
        if migrate_direction == "from":
            spec = models.DataMigrateSpec(
                _from=models.DataToMigrate(
                    external_storage=external_storage
                ),
                to=models.DataToMigrate(
                    dataset=models.DatasetToMigrate(
                        name=self.dataset_name,
                        namespace=self.fluid_client.namespace,
                        path=path
                    )
                )
            )
        elif migrate_direction == "to":
            spec = models.DataMigrateSpec(
                to=models.DataToMigrate(
                    external_storage=external_storage
                ),
                _from=models.DataToMigrate(
                    dataset=models.DatasetToMigrate(
                        name=self.dataset_name,
                        namespace=self.fluid_client.namespace,
                        path=path
                    )
                )
            )

        op = models.DataMigrate(
            api_version=constants.API_VERSION,
            kind=constants.DATA_MIGRATE_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.fluid_client.namespace,
            ),
            spec=spec
        )

        self.flow_ops.append(op)
        return self

    def process(self, dataset_mountpath, processor, sub_path=None):
        op = models.DataProcess(
            api_version=constants.API_VERSION,
            kind=constants.DATA_PROCESS_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.fluid_client.namespace,
            ),
            spec=models.DataProcessSpec(
                dataset=models.TargetDatasetWithMountPath(
                    name=self.dataset_name,
                    namespace=self.fluid_client.namespace,
                    mount_path=dataset_mountpath,
                    sub_path=sub_path
                ),
                processor=processor
            )
        )
        self.flow_ops.append(op)
        return self

    def run(self, run_id):
        steps_to_execute = []
        for step in self.flow_ops:
            st = copy.deepcopy(step)
            if st.metadata.labels is None:
                st.metadata.labels = {}
            st.metadata.labels["fluid.io/dataflow"] = run_id
            st.metadata.name = st.metadata.name.replace("<flow_name_placeholder>", run_id)
            steps_to_execute.append(st)

        last_step = None
        for op in steps_to_execute:
            if last_step is not None:
                op.spec.run_after = models.OperationRef(
                    name=last_step.metadata.name,
                    namespace=last_step.metadata.namespace,
                    kind=last_step.kind
                )
            self.fluid_client.create_data_operation(op)
            last_step = op
        return FlowHandle(run_id, steps_to_execute)


class FlowHandle:
    def __init__(self, run_id, flow_steps):
        self.fluid_client = FluidClient()
        self.run_id = run_id
        self.flow_steps = flow_steps

    def get_current_status(self):
        flow_status = []
        for op in self.flow_steps:
            op_obj = self.fluid_client.get_data_operation(op.metadata.name, op.kind)
            flow_status.append({op.metadata.name: op_obj.status})
        return flow_status

    def wait(self, timeout_for_each_step=constants.DEFAULT_POLL_TIMEOUT):
        for step in self.flow_steps:
            try:
                self.fluid_client.wait_data_operation_completed(step.metadata.name, step.kind,
                                                                poll_timeout=timeout_for_each_step)
                logger.info(f"{step.kind} {step.metadata.name} completed")
            except Exception as e:
                raise RuntimeError(f"failed to wait data operation {step.metadata.name}: {e}")
