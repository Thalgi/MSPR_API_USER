from setuptools import setup, find_packages

setup(

    name="POC-API-MSPR",
    version="0.1",


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
            "POC-API-MSPR = app:src/main",
        ],
    },
)
