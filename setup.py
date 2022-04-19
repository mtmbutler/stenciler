"""Installation script for stenciler."""
from setuptools import find_packages, setup

from stenciler import __desc__

setup(
    name="stenciler",
    version="0.1.0",
    description=__desc__,
    author="Miles Butler",
    author_email="miles@milesbutler.dev",
    url="https://github.com/mtmbutler/stenciler",
    packages=["stenciler"] + ["stenciler." + i for i in find_packages("stenciler")],
    setup_requires=["wheel"],
    install_requires=[
        "pyyaml>=6.0",
        "Jinja2>=3.1",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["stenciler = stenciler.cli:cli"]},
)
