from setuptools import find_packages, setup


version = {}
with open("home_service/__init__.py") as fp:
    exec(fp.read(), version)


with open("requirements.txt") as f:
    requirements = f.read().split("\n")

with open("requirements-dev.txt") as f:
    requirements_dev = f.read().split("\n")

extras = {"dev": requirements_dev}

setup(
    name="home_service",
    version=version["__version__"],
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
    extra_requires=extras,
)
