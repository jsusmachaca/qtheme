from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setup(
    name="qtheme",
    version="1.0",
    description="Tools for management qtile environment",
    long_description=README,
    long_description_content_type="text/markdown",
    author="jsusmachaca",
    author_email="falcorgd@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "qtheme = qtheme.main:main"
        ]
    },
)
