import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aocd-brtwrst", # Replace with your own username
    version="0.0.1",
    author="brtwrst",
    author_email="brtwrst@outlook.com",
    description="AOCD data handling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brtwrst/aocd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        'requests',
    ]
)
