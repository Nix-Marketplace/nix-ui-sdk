from setuptools import setup, find_packages

setup(
    name='nixgui',
    version='0.0.4',
    packages=find_packages(),
    install_requires=[
        'nicegui',
        'requests'
    ],
    author='Nix',
    author_email='kay@nix.tech',
    description='An opinionated UI library based on NiceGUI for use in Nix tools',
    url='https://www.nix.tech'
)
