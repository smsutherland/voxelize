import subprocess

from setuptools import setup
from setuptools.command.build import build


class Build(build):
    def run(self):
        subprocess.check_call("make python_cpu", shell=True)
        super().run()


setup(
    name="voxelize",
    description="Fast 3D fields from particle catalogs",
    version="1",
    packages=[
        "voxelize",
    ],
    python_requires=">=3.5",
    include_package_data=True,
    url="https://github.com/leanderthiele/voxelize",
    cmdclass={"build": Build},
)
