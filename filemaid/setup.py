from setuptools import setup

setup(
    name="filemaid",
    version="1.0",
    py_modules=["cli", "main", "watcher"],
    entry_points={
        "console_scripts": [
            "filemaid=cli:main",
        ],
    },
) 