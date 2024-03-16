from setuptools import setup, find_packages

setup(
    name='zhtn',
    version='0.1',
    packages=find_packages(),
    description='Chinese Text Normalization',
    install_requires=[
        "opencc==1.1.6",
        "jiwer==3.0.3",
        "evaluate>=0.4.1",
    ],
)

