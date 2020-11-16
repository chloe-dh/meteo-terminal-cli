from setuptools import setup, find_packages

setup(
    name='meteo_terminal',
    version='1.0',
    author="Chloé d'Hardemare",
    url='',
    description='',
    licence='',
    packages=find_packages(),
    install_requires=[''],
    entry_points={
        'console_scripts': ['meteo=displaymeteo.app:run'],
    }
)
