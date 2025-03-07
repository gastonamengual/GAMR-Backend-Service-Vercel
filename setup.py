from pathlib import Path

import dparse
from setuptools import find_packages, setup

from gamr_backend_api_service import __version__

content = Path("Pipfile").read_text()
df = dparse.parse(content, file_type=dparse.filetypes.pipfile)
required = [
    dependency.line
    for dependency in df.dependencies
    if dependency.section == "packages"
]

setup(
    name="gamr_backend_api_service",
    version=__version__,
    install_requires=[required],
    include_package_data=True,
    long_description=open("README.md").read(),  # noqa: PTH123, SIM115
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["secrets"]),
)
