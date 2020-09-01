"""Setup for panik."""
import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="panik",
    version="1.0.0",
    author="Tom Simonart",
    author_email="tom.simonart@gmail.com",
    description="Will change problem into panik",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomsimonart/panik",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    python_requires='>=3.0',
)
