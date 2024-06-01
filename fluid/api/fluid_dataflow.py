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

from fluid import FluidK8sClient
from fluid import models
from fluid import constants
from kubernetes import client

from typing import List, Dict

logger = logging.getLogger("fluidsdk")


class FluidDataFlow(object):
    """
    Flow manager for running multiple data operations in a flow.

    Fluid provides a dataflow API that allows users to run multiple data operations(e.g. DataLoad, DataProcess, DataMigrate)
    in a flow. Operations in the flow are executed in the order they are added to the flow.

    RECOMMEND: Not use this API directly, use fluid.Dataset instead. See below for a detailed example.

    Parameters
    ----------
    param dataset_name: str
        The name of the dataset for the flow. All the operations defined in the flow should rely on a bound Dataset, otherwise
        the flow cannot be executed until the referred dataset is bound.

    Examples
    --------
    >>> from fluid import FluidK8sClient
    >>> fluid_client = FluidK8sClient()
    >>> ds = fluid_client.get_dataset(name="my_dataset")
    >>> flow_handle = ds.migrate(...).preload(...).process(...).run(run_id="my_flow")
    >>> flow_handle.wait() # wait until the flow is finished
    """

    def __init__(
            self,
            dataset_name,
            dataset_namespace,
    ):
        self.fluid_client = FluidK8sClient()
        self.dataset_name = dataset_name
        self.dataset_namespace = dataset_namespace
        self.flow_ops = []

    def preload(self, target_path: str = "/", load_metadata: bool = False):
        """
        PreLoad data from Under File Storage(UFS) to the Dataset's data cache.

        Parameters
        ----------
        target_path: str
            The path to preload, both directory and file path are supported. Note
            that the path is relative to the Dataset's mount path. For example, when mounting s3://bucket/path to the
            Dataset's root path ("/"), you preloads s3://bucket/path/dir by using dataset.preload(target_path="/dir")
            instead of the full path s3://bucket/path/dir. load_metadata: bool Whether to load metadata.

        Returns
        -------
        The FluidDataFlow object with a preload operation appended.
        """

        op = models.DataLoad(
            api_version=constants.API_VERSION,
            kind=constants.DATA_LOAD_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.dataset_namespace,

            ),
            spec=models.DataLoadSpec(
                load_metadata=load_metadata,
                dataset=models.TargetDataset(
                    name=self.dataset_name,
                    namespace=self.dataset_namespace
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
        """
        Migrate data from/to an external storage.

        Parameters
        ----------
        path: str
            The path to migrate, both directory and file path are supported. Note
            that the path is relative to the Dataset's mount path. For example, when mounting s3://bucket/path to the
            Dataset's root path ("/"), you migrate s3://bucket/path/dir by using dataset.migrate(path="/dir")
            instead of the full path s3://bucket/path/dir.
        migrate_direction: str
            The direction of migration. Must be either "from"(fluid.constants.DATA_MIGRATE_DIRECTION_FROM) or "to"(fluid.constants.DATA_MIGRATE_DIRECTION_TO).
            "from" means migrate from external storage to the Dataset. "to" means migrate from the Dataset to external storage.
        external_storage: fluid.models.ExternalStorage
            The external storage uri and credentials used for migration.

        Returns
        -------
        The FluidDataFlow object with a migrate operation appended.
        """
        global spec
        if migrate_direction == "from":
            spec = models.DataMigrateSpec(
                _from=models.DataToMigrate(
                    external_storage=external_storage
                ),
                to=models.DataToMigrate(
                    dataset=models.DatasetToMigrate(
                        name=self.dataset_name,
                        namespace=self.dataset_namespace,
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
                        namespace=self.dataset_namespace,
                        path=path
                    )
                )
            )

        op = models.DataMigrate(
            api_version=constants.API_VERSION,
            kind=constants.DATA_MIGRATE_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.dataset_namespace,
            ),
            spec=spec
        )

        self.flow_ops.append(op)
        return self

    def process(self, dataset_mountpath, processor, sub_path=None):
        """
        Process the data in the Dataset in a customized way. Submitting a DataProcess custom resource object to the cluster,
        which launches Pods to process data mounted on a given path in the Pods.

        Parameters
        ----------
        dataset_mountpath: str
            The path where the Dataset will be mounted on the processor Pods.
        processor: fluid.models.Processor
            The actual processor to run in processor Pods. Only script or job processor is supported.
            Script processor executes a customized script with given command(e.g. bash, python, etc.).
            Job processor is backended by a Kubernetes Job.
        sub_path: str
            If set, the given Dataset's subPath will be mounted on the processor Pods.

        Returns
        -------
        The FluidDataFlow object with a process operation appended.
        """
        op = models.DataProcess(
            api_version=constants.API_VERSION,
            kind=constants.DATA_PROCESS_KIND,
            metadata=client.V1ObjectMeta(
                name=f"<flow_name_placeholder>-step{len(self.flow_ops) + 1}",
                namespace=self.dataset_namespace,
            ),
            spec=models.DataProcessSpec(
                dataset=models.TargetDatasetWithMountPath(
                    name=self.dataset_name,
                    namespace=self.dataset_namespace,
                    mount_path=dataset_mountpath,
                    sub_path=sub_path
                ),
                processor=processor
            )
        )
        self.flow_ops.append(op)
        return self

    def run(self, run_id, ttl_seconds_after_finished=constants.DEFAULT_DATAFLOW_TIME_TO_LIVE):
        """
        Execute the dataflow by submitting all the defined operations to the cluster.

        Parameters
        ----------
        run_id: str
            The run id of the dataflow.
        ttl_seconds_after_finished: int
            Seconds to live after finished for each operation in the dataflow.

        Returns
        -------
        The FlowHandle object which may track the flow's status.
        """
        try:
            dataset = self.fluid_client.get_dataset(self.dataset_name, self.dataset_namespace)
        except Exception as e:
            raise RuntimeError(f"failed to get dataset {self.dataset_name}: {e}")

        if dataset.status is None or dataset.status.phase != "Bound":
            raise RuntimeError(f"dataset {self.dataset_name} is not bound")

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
            op.spec.ttl_seconds_after_finished = ttl_seconds_after_finished
            self.fluid_client.create_data_operation(op)
            last_step = op
        return FlowHandle(run_id, steps_to_execute)


class FlowHandle:
    """
    The handle of a executed dataflow for tracking its status.

    RECOMMEND: Not directly initialize a FlowHandle but get one from FluidDataFlow.run()

    Parameters
    ----------
    run_id: str
        The run id of the dataflow.
    flow_steps: list
        The list of steps defined in the dataflow.
    """

    def __init__(self, run_id, flow_steps):
        self.fluid_client = FluidK8sClient()
        self.run_id = run_id
        self.flow_steps = flow_steps

    def get_current_status(self):
        """
        Report current status of the dataflow by returning status of all the operations in the dataflow.

        Returns
        -------
        list
            The list of status of each operation in the dataflow.

        Examples
        --------
        >>> flow_handle.get_current_status()
        [
            {
                'testflow-step1': {
                    'conditions': [],
                    'duration': 'Unfinished',
                    'infos': None,
                    'last_schedule_time': None,
                    'last_successful_time': None,
                    'phase': 'Executing',
                    'waiting_for': {'operation_complete': None}}}
            {
                'testflow-step2': {
                    'conditions': [],
                    'duration': 'Unfinished',
                    'infos': None,
                    'last_schedule_time': None,
                    'last_successful_time': None,
                    'phase': 'Pending',
                    'waiting_for': {'operation_complete': True}}}
        ]
        """
        flow_status = []
        for op in self.flow_steps:
            op_obj = self.fluid_client.get_data_operation(op.metadata.name, op.kind)
            flow_status.append({op.metadata.name: op_obj.status})
        return flow_status

    def wait(self, timeout_for_each_step=constants.DEFAULT_POLL_TIMEOUT):
        """
        Wait in a block way until the dataflow is finished.

        Parameters
        ----------
        timeout_for_each_step: int
            Timeout seconds for waiting each step to finish.
        """
        for step in self.flow_steps:
            try:
                self.fluid_client.wait_data_operation_completed(step.metadata.name, step.kind,
                                                                poll_timeout=timeout_for_each_step)
                logger.info(f"{step.kind} {step.metadata.name} completed")
            except Exception as e:
                raise RuntimeError(f"failed to wait data operation {step.metadata.name}: {e}")
