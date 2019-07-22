from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from semantic_text_similarity import __version__, __authors__
import sys

packages = find_packages()

def readme():
    with open('README.md') as f:
        return f.read()

class PyTest(TestCommand):

    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ""

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest

        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

setup(
    name='semantic_text_similarity',
    version=__version__,
    license='MIT',
    description='N2C2 2019 Dredze Lab Johns Hopkins',
    long_description=readme(),
    packages=packages,
    url='',
    author=__authors__,
    author_email='contact@andriymulyar.com',
    keywords='',
    classifiers=[
        '( Status :: 4 - Beta',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Topic :: Text Processing :: Linguistic',
        'Intended Audience :: Science/Research'
    ],

    install_requires=[
        'torch',
        'strsim',
        'pytorch-transformers',
        'scipy'
    ],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    include_package_data=True,
    zip_safe=False

)