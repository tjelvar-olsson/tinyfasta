Quick Guide
===========

TinyFasta is a Python package for parsing biological sequences from FASTA
files.

There are already several Python packages available for parsing FASTA files.
However, many of these packages do much more than just parse FASTA files and as
such have dependencies on NumPy and SciPy . These are quite heavy weight
dependencies if all you want to do is a little bit of text processing. This is
where TinyFasta fits in. It is a lightweight Python package with no
dependencies outside of the Python standard library.

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

- Documentation: http://tinyfasta.readthedocs.org/en/latest/
- Source: https://github.com/tjelvar-olsson/tinyfasta
