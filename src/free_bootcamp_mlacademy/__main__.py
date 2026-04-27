"""free-bootcamp-mlacademy file for ensuring the package is executable
as `free-bootcamp-mlacademy` and `python -m free_bootcamp_mlacademy`
"""
import sys
from pathlib import Path
from typing import Any

from kedro.framework.cli.utils import find_run_command #find_run_command → finds the function that executes pipelines
from kedro.framework.project import configure_project #configure_project → initializes your Kedro project


def main(*args, **kwargs) -> Any:
    package_name = Path(__file__).parent.name
    configure_project(package_name)

    interactive = hasattr(sys, 'ps1')
    kwargs["standalone_mode"] = not interactive

    run = find_run_command(package_name)
    return run(*args, **kwargs)


if __name__ == "__main__":
    main()


# python -m free_bootcamp_mlacdemy
#         ↓
# __main__.py
#         ↓
# configure_project()
#         ↓
# find_run_command()
#         ↓
# execute pipeline (kedro run)