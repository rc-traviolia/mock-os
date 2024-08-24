from setuptools import setup, find_packages

setup(
    name="mock-os",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
        "gitignore-parser",  # Add the gitignore-parser library here
    ],
    entry_points={
        "console_scripts": [
            "mock-os=mock_os.cli:app",
        ],
    },
)
