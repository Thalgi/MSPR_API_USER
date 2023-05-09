"""
Setup script for the POC-API-MSPR package
"""

from setuptools import setup, find_packages

setup(
    name="MSPR_API_USER",
    version="0.3",
    description='Python Distribution Utilities',
    author='Thomas Muller',
    author_email='espi-mastere-dev@ifagparis.onmicrosoft.com',
    url='https://blogs.motiondevelopment.top/products/ProjetMSPR',
    packages=find_packages(),
    install_requires=[
        "cherrypy",
    ],
    entry_points={
        "console_scripts": [
            "MSPR_API_USER = app:microservice/src/main",
        ],
    },
)
