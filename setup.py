from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().split("\n")

setup(
    name="home_service",
    version="2.0.0",
    description="",
    url="https://github.com/tiega/home-service-v2",
    author="Tiger Nie",
    author_email="nhl0819@gmail.com",
    maintainer="Tiger Nie",
    maintainer_email="nhl0819@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
)
