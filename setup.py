from setuptools import setup, find_packages

setup(
    name='sample-python-pkg',
    version='0.1.0',
    author='Venkat',
    author_email='venkat@example.com',
    description='A simple Python package to demo Jenkins + Nexus',
    packages=find_packages(),
    python_requires='>=3.6',
)
