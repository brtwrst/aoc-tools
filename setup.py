import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aoc-tools-brtwrst",
    version="0.1.0",
    author="brtwrst",
    author_email="brtwrst@outlook.com",
    description="Advent of Code tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brtwrst/aoc-tools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'requests',
        'colorama',
    ]
)
