from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='pyfandango',
    version='0.0.1',
    url='https://github.com/androbwebb/py-fandango',
    description=(
        'A fandango driver for python'
    ),
    author='Andrew Webb',
    author_email='androbwebb@gmail.com',
    packages=find_packages(),
    install_requires=required,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
    },
)