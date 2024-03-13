#  Copyright 2024 The Fluid Authors.
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

import inspect
import textwrap
from typing import Optional, Callable, List, Dict, Any, Tuple, Union

from fluid import models

DEFAULT_PIP_INDEX_URL = "https://pypi.org/simple"
DEFAULT_BASE_IMAGE = "python:3.10"


# Credits to kubeflow/training-operator. Fork from https://github.com/kubeflow/training-operator/blob/57aa34d5eaa55cd410b1309df8fe5dfa868811f0/sdk/python/kubeflow/training/utils/utils.py#L108C1-L127C38
def get_script_for_python_packages(
        packages_to_install: List[str], pip_index_url: str, quiet: bool = False
) -> str:
    """
    Get init script to install Python packages from the given pip index URL.
    """
    packages_str = " ".join([str(package) for package in packages_to_install])

    quiet_opt = "--quiet" if quiet else ""
    script_for_python_packages = textwrap.dedent(
        f"""
        if ! [ -x "$(command -v pip)" ]; then
            python3 -m ensurepip || python3 -m ensurepip --user || apt-get install python3-pip
        fi

        PIP_DISABLE_PIP_VERSION_CHECK=1 python3 -m pip install {quiet_opt} \
        --no-warn-script-location --index-url {pip_index_url} {packages_str}
        """
    )

    return script_for_python_packages


# Credits to kubeflow/training-operator. Fork from https://github.com/kubeflow/training-operator/blob/57aa34d5eaa55cd410b1309df8fe5dfa868811f0/sdk/python/kubeflow/training/utils/utils.py#L130.
def make_processor_from_func(
        process_func: Optional[Callable],
        process_func_params: Optional[Dict[str, Any]] = None,
        packages_to_install: Optional[List[str]] = None,
        pip_index_url: str = DEFAULT_PIP_INDEX_URL,
        base_image: str = DEFAULT_BASE_IMAGE,
        debug_mode: bool = False,
        **kwargs
):
    # Check if function is callable.
    if not callable(process_func):
        raise ValueError(
            f"Process function must be callable, got function type: {type(process_func)}"
        )

    # Extract function implementation.
    func_code = inspect.getsource(process_func)

    # Function might be defined in some indented scope (e.g. in another function).
    # We need to dedent the function code.
    func_code = textwrap.dedent(func_code)

    # Wrap function code to execute it from the file. For example:
    # def train(parameters):
    #     print('Start Training...')
    # train({'lr': 0.01})
    if process_func_params is None:
        func_code = f"{func_code}\n{process_func.__name__}()\n"
    else:
        params = []
        for key, value in process_func_params.items():
            if isinstance(value, str):
                value = f"'{value}'"
            params.append(f"{key}={value}")
        func_code = f"{func_code}\n{process_func.__name__}(**{process_func_params})\n"

    # Prepare execute script template.
    shell_options = "set -ex" if debug_mode else "set -e"
    exec_script = textwrap.dedent(
        """
                {shell_options}
                program_path=$(mktemp -d)
                read -r -d '' SCRIPT << EOM\n
                {func_code}
                EOM
                printf "%s" \"$SCRIPT\" > \"$program_path/ephemeral_script.py\"
                python3 -u \"$program_path/ephemeral_script.py\""""
    )

    # Add function code to the execute script.
    exec_script = exec_script.format(func_code=func_code, shell_options=shell_options)

    # Install Python packages if that is required.
    if packages_to_install is not None:
        exec_script = (
                get_script_for_python_packages(packages_to_install, pip_index_url, quiet=not debug_mode)
                + exec_script
        )

    return models.Processor(
        script=models.ScriptProcessor(
            command=["bash"],
            source=f'{exec_script}',
            image=base_image.split(':')[0],
            image_tag=base_image.split(':')[1],
            **kwargs
        )
    )
