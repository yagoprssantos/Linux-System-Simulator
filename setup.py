"""
Setup script for Linux System Simulator
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="linux-system-simulator",
    version="1.0.0",
    author="Yago Santos",
    description="Um simulador interativo de sistema operacional Linux",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yagoprssantos/Linux-System-Simulator",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "linux-simulator=main:main",
        ],
    },
)
