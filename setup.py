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
    long_description="""
A context manager that creates savepoints, avoiding recalculting expensive
parts of the code.

An example:

.. code-block:: python

    from savepoint import SavePoint

    a = 10
    b = 20

    # do some expensive calculation here
    with SavePoint("stuff.p"):
        print "doing stuff"
        a += 10
        c = 30

    print a, b, c

The first time the code is ran the `with` block is executed, and the modifed 
scope is pickled to `stuff.p`. Subsequent calls will update the global scope
from the pickle file, and skip the block completely.
    """,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='context manager savepoint hack',
    author='Roberto De Almeida',
    author_email='roberto@dealmeida.net',
    url='',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
    }
)