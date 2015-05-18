Parsing FASTA files
-------------------

To parse a FASTA file we make use of the :class:`tinyfasta.FastaParser` class.

.. code-block:: python

    >>> from tinyfasta import FastaParser

To create a :class:`tinyfasta.FastaParser` instance we simply need the path to
the FASTA file of interest.

.. code-block:: python

    >>> fasta_parser = FastaParser('tests/data/dummy.fasta')
    >>> fasta_parser.fpath
    'tests/data/dummy.fasta'

We can then iterate over all the :class:`tinyfasta.FastaRecord` instances in
the FASTA file.

.. code-block:: python

    >>> for fasta_record in fasta_parser:  # doctest: +ELLIPSIS
    ...     print(fasta_record)
    ...
    >seq1|contains 2x78 A's
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq2|starts with ATTA motif in first line
    ATTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    ...
