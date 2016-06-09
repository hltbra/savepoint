from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='savepoint',
    version=version,
    description="A context manager that creates savepoints",
    long_description=open("README.md").read(),
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='context manager savepoint hack',
    author='Roberto De Almeida, Marinexplore Inc., Hugo Lopes Tavares',
    author_email='rob@marinexplore.com',
    url='https://github.com/hltbra/savepoint',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
