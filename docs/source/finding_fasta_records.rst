Finding FASTA records
=====================

To find specific FASTA records one can simply iterate over the individual
records in a particular FASTA file and check if the description and/or sequence
contains a particular string or regular expression. Let us therefore start by
creating a :class:`tinyfasta.FastaParser` instance.

.. code-block:: python

    >>> from tinyfasta import FastaParser
    >>> fasta_parser = FastaParser('tests/data/dummy.fasta')


Matching based on the description line
--------------------------------------

Now let us look for a FASTA record where the description contains the string
``seq1``.

.. code-block:: python

    >>> for fasta_record in fasta_parser:
    ...     if fasta_record.description_matches('seq1'):
    ...         print(fasta_record)
    ...
    >seq1|contains 2x78 A's
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

Suppose we wanted to find all the FASTA records where the description line
started with ``>seq1|``, ``>seq2|`` or ``>seq3|``. This query can be expressed
using the regular expression below.

.. code-block:: python

    >>> import re
    >>> search_term = re.compile(r'^>seq[1-3]\|')

We can use compiled regular expression to identify FASTA records of interest.

.. code-block:: python

    >>> for fasta_record in fasta_parser:
    ...     if fasta_record.description_matches(search_term):
    ...         print(fasta_record)
    ...
    >seq1|contains 2x78 A's
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq2|starts with ATTA motif in first line
    ATTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq3|ends with ATTA motif in second line
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTA


Matching based on the sequence
------------------------------

We can use a similar approach to check if a :class:`tinyfasta.FastaRecord`
contains a sequence motif.

Let us first look for records containing a simple ``ATTA`` motif.

.. code-block:: python

    >>> for fasta_record in fasta_parser:
    ...     if fasta_record.sequence_matches('ATTA'):
    ...         print(fasta_record)
    ...
    >seq2|starts with ATTA motif in first line
    ATTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq3|ends with ATTA motif in second line
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTA
    >seq4|contains ATTA motif in middle of first line
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq5|contains ATTA motif split over two lines
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT
    TAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

More complicated sequence motifs can be searched for by compiling regular
expressions. Suppose we wanted to be able to identify any of the sequences
below::

    ACCCA
    ACCTA
    ACTTA
    ATTTA
    ATTCA
    ATCCA

This could be achieved with the regular expression ``A[C,T]{3}A``.

.. code-block:: python

    >>> motif = re.compile(r"A[C,T]{3}A")

Now let us find all the FASTA records that contain this motif.

.. code-block:: python

    >>> for fasta_record in fasta_parser:
    ...     if fasta_record.sequence_matches(motif):
    ...         print(fasta_record)
    ...
    >seq7|contains ACCCA motif
    AAAAAAAAAAAAAAAAAAAAAAAAAAACCCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    >seq8|contains ATTTA motif
    AAAAAAAAAAAAAAAAAAAAAAAAAAATTTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
