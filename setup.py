from setuptools import setup

setup(
    name='solar',
    py_modules=['solar'],
    packages = ['solar'],
    entry_points={
        'console_scripts': [
            'solar = solar.cli:main',
        ],
    }
)
