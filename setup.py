from setuptools import find_packages, setup

setup(
    author="Giliard Almeida de Godoi",
    name="sapcovid",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts' : [
            'sapcovid=src.__main__:app'
        ]
    }
)