TinyFasta
=========

.. image:: https://badge.fury.io/py/tinyfasta.svg
   :target: http://badge.fury.io/py/tinyfasta
   :alt: PyPI package

.. image:: https://travis-ci.org/tjelvar-olsson/tinyfasta.svg?branch=master
   :target: https://travis-ci.org/tjelvar-olsson/tinyfasta
   :alt: Travis CI build status (Linux)

.. image:: https://ci.appveyor.com/api/projects/status/a7n80uibbsh0s4h8/branch/master?svg=true
   :target: https://ci.appveyor.com/project/tjelvar-olsson/tinyfasta
   :alt: AppVeyor CI build status (Windows)

.. image:: https://codecov.io/github/tjelvar-olsson/tinyfasta/coverage.svg?branch=master
   :target: https://codecov.io/github/tjelvar-olsson/tinyfasta?branch=master
   :alt: Code Coverage

.. image:: https://readthedocs.org/projects/tinyfasta/badge/?version=latest
   :target: https://readthedocs.org/projects/tinyfasta/?badge=latest
   :alt: Documentation Status

Python package for working with biological sequences from FASTA files.

- Documentation: http://tinyfasta.readthedocs.io
- GitHub: https://github.com/tjelvar-olsson/tinyfasta
- PyPI: https://pypi.python.org/pypi/tinyfasta
- Free software: MIT License


Features
--------

- Easy to use: intuitive API for parsing, searching and writing FASTA files
- Lightweight: no dependencies outside Python's standard library
- Cross-platform: Linux, Mac and Windows are all supported
- Works with with Python 2.7, 3.3, 3.4 and 3.5


Quick Guide
-----------

To install the TinyFasta package::

    sudo pip install tinyfasta

To parse a FASTA file::

    >>> from tinyfasta import FastaParser
    >>> for fasta_record in FastaParser("tests/data/dummy.fasta"):
    ...     if fasta_record.description.contains('seq1'):
    ...         print(fasta_record)
    ...
    >seq1|contains 2x78 A's
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

To create a FASTA record::

    >>> from tinyfasta import FastaRecord
    >>> sequence = "C" * 100
    >>> fasta_record = FastaRecord.create("My Sequence", sequence)
    >>> print(fasta_record)
    >My Sequence
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCC

