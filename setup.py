from setuptools import setup, find_packages

setup(
    name="flask-ci-cd-demo",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
    ],
)
