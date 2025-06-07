from setuptools import find_packages, setup

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="figureFactory",
    version="1.0.0",
    description="Package is used for creating figures and calculating it's area",
    package_dir={"": "app"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[],
    url="https://github.com/albdvtinterview/figure_factory",
    author="Albert Davtyan",
    author_email="albusdavtyanbledore@gmail.com",
    license="MIT",
    classifiers=[
        "License :: osi Approved :: MIT License",
        "Programming Language :: Python :: 3.12.1",
        "Operating System :: OS Independent",
    ],
)
