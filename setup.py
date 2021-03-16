from setuptools import setup

setup(
    name='solar',
    version="2.0.1-alpha",
    py_modules=['main'],
    packages = ['main'],
    entry_points={
        'console_scripts': [
            'main = main:main',
        ],
    }
)
