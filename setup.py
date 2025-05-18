"""Setup file for the task management system."""

from setuptools import setup, find_packages

setup(
    name="tasks",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "bcrypt>=4.0.1",
    ],
    author="EmpChief",
    description="A multi-language task management system",
    python_requires=">=3.6",
) 