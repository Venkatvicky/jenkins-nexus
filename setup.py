from setuptools import setup, find_packages

setup(
    name='my-sample-pkg',
    version='0.0.1',
    author='Your Name',
    author_email='you@example.com',
    description='A sample Python package for Nexus pipeline demo',
    packages=find_packages(),
    install_requires=[],  # or ['requests', ...]
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
