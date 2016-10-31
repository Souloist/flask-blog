import os
from setuptools import setup

def read(*args):
    with open(os.path.join(*args), "r") as f:
        return f.read().splitlines()

setup(
    # Metadata
    name="flask-blog",
    version="0.1.0",
    description="blog made with flask, SQLAlchemy, and SQLite",
    author="Richard Shen",
    install_requires=read("requirements.txt")
)


