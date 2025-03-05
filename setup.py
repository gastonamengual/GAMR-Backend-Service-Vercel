from pathlib import Path

import dparse
from setuptools import setup

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
    description="An example Python package",
    url="https://github.com/example/example_package",
    author="Your Name",
    author_email="your.email@example.com",
    install_requires=[required],
    include_package_data=True,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "deploy-render=gamr_backend_api_service.deployment.render_deployment:trigger_render_deployment",
        ],
    },
)
