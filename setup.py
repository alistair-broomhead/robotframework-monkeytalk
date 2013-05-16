from setuptools import setup, find_packages
from os import path


def open_(fname):
    import sys
    filename = sys.executable if hasattr(sys, "frozen") else __file__
    return open(path.join(path.dirname(filename), fname))


def read(fname):
    return open_(fname).read()


def read_version():
    from json import load
    return '.'.join([str(i) for i in
                     load(open_("version.txt"))])


setup(
    name='robotframework-monkeytalk',
    package_data={'': ['*.md', '*.txt']},
    author='Alistair Broomhead',
    version=read_version(),
    author_email='alistair.broomhead@gmail.com',
    description='Bridge to MonkeyTalk',
    license='MIT',
    url='https://github.com/alistair-broomhead/robotframework-monkeytalk.git',
    download_url='https://github.com/alistair-broomhead/robotframework-monkeytalk.git/zipball/master',
    long_description=read('README.md'),
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
