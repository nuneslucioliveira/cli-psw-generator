from setuptools import setup, find_packages

setup(
    name="cli-core",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "password-generator=cli_core.cli:main",
        ],
    },
    install_requires=[],
    author="Agent: curupira-companion",
    description="CLI password generator with cryptographically secure randomness",
    python_requires=">=3.6",
)