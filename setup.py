from setuptools import find_packages, setup

setup(
    name='myPackageExample',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Moj paket',
    long_description=open('README.txt').read(),
    install_requires=['numpy'],
    url='https://github.com/kljuco/python-package-test',
    author='Emir Kljucanin',
    author_email='emir.kljucanin@gmail.com'
)
