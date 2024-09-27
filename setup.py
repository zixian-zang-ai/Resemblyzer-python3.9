from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements_demos.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="Resemblyzer-python3.9",
    version="2.0.3",
    packages=find_packages(),
    package_data={
        "resemblyzer": ["pretrained.pt"]
    },
    python_requires=">=3.5",
    install_requires=requirements,
    # author="Corentin Jemine",
    # author_email="corentin@resemble.ai",
    description="Analyze and compare voices with deep learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zixian-zang-ai/Resemblyzer-python3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)