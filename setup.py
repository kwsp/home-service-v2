from setuptools import setup, find_packages
import os
import re


def read(path):
    with open(path, "r") as fp:
        return fp.read()


def find_version(file_paths):
    version_file = read(file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read("README.md")
requirements = read("requirements.txt").split("\n")
requirements_dev = read("requirements-dev.txt").split("\n")
extras = {"dev": requirements_dev}

setup(
    name="home_service",
    version=find_version("home_service/__init__.py"),
    description="A simple home monitoring system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiega/home-service-v2",
    author="Tiger Nie",
    author_email="nhl0819@gmail.com",
    maintainer="Tiger Nie",
    maintainer_email="nhl0819@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    scripts=["bin/home-service"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    extras_require=extras,
)
