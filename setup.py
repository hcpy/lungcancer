import setuptools

with open("README.md") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.readlines()

setuptools.setup(
    name="lungcancer",
    version="0.0.1",
    author="Team 2 FAES",
    author_email="workdeadline@outlook.com",
    description="Lung Cancer Risk Factors",
    long_description=long_description,
    long_description_content_type = "text/markdown",
    url="Trimmed Data Set for Team Project.csv",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
