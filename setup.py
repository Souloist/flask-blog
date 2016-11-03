from __future__ import absolute_import

import os

from setuptools import find_packages, setup

def read(filename):
    return open(os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        filename,
    )).read()

third_party_dependencies = read("requirements.txt").splitlines()

tests_require = (
    "nose",
)

setup(
    name="flask-blog",
    version="0.1.0",
    author="Richard Shen",
    author_email="rich.shen@nyu.edu",
    description="blog made with flask, SQLAlchemy, and SQLite",
    long_description=read("README.rst"),
    packages=find_packages(exclude=["ez_setup"]),
    include_package_data=True,
    zip_safe=False,
    test_suite="nose.collector",
    install_requires=third_party_dependencies,
    test_require=tests_require,
    classifiers=[
        "Framework :: Flask",
        "Programming Language :: Python",
        "Topic :: INternet :: WWW/HTTP :: Dymanic Content",
    ],
    entry_points="""
        [console_scripts]
        flask=flask.cli:main
    """,
)
