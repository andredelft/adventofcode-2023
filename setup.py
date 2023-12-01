from setuptools import setup, find_packages

setup(
    name="adventofcode-2023",
    version="1.0",
    description="Advent of code 2023",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "prepare=cli:prepare",
            "test-sol=cli:test",  # We can't use `test`
            "solve=cli:solve",
            "submit=cli:submit",
        ]
    },
)
