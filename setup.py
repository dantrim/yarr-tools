import pathlib
from setuptools import setup, find_packages

# the directory containing this file
HERE = pathlib.Path(__file__).parent

# the text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="yarr_tools",
    version="1.0.0",
    description="Utilities for interacting with the YARR DAQ software",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dantrim/yarr-tools",
    author="Daniel Joseph Antrim",
    author_email="dantrim1023@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=["numpy", "click", "matplotlib", "typing", "pytest"],
    entry_points={"console_scripts": []},
)
