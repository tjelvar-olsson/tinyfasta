Creating FASTA records
======================

There are two ways of creating :class:`tinyfasta.FastaRecord` instances. We can
create them from a description and a long sequence string or we can build them
up from a description and several sequence strings. The latter approach is used
internally by the :class:`tinyfasta.FastaParser`.


Using a long sequence string
----------------------------

Let us import the :class:`tinyfasta.FastaRecord` class and create a
description and sequence strings.

.. code-block:: python

    >>> from tinyfasta import FastaRecord
    >>> description = '>My Sequence'
    >>> sequence = 'C' * 500

We can now create a :class:`tinyfasta.FastaRecord` from the description and
sequence strings by using the :func:`tinyfasta.FastaRecord.create` static
method.

.. code-block:: python

    >>> from tinyfasta import FastaRecord
    >>> fasta_record = FastaRecord.create(description, sequence)

Let us print out the record to verify what we got.

.. code-block:: python

    >>> print(fasta_record)
    >My Sequence
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
    CCCCCCCCCCCCCCCCCCCC


Using several sequence strings
------------------------------

However, suppose that we wanted to create a :class:`tinyfasta.FastaRecord`
from a file containing the input sequence split over several lines. In this
scenario we can simply add the sequence lines one by one.

Let us create a :class:`tinyfasta.FastaRecord` to add the sequence lines to.


.. code-block:: python

    >>> fasta_record = FastaRecord('>Yet Another Record')

Now we can start adding sequence lines to it.

.. code-block:: python

    >>> fasta_record.add_sequence_line("AAAAAAAA")
    >>> fasta_record.add_sequence_line("TTTTTTTTTTTT")
    >>> fasta_record.add_sequence_line("CCCCCC")
    >>> fasta_record.add_sequence_line("GGGGGGGGGGGGGGG")

Note that by default the string representation of the
:class:`tinyfasta.FastaRecord` will contain the original sequence line splits.

.. code-block:: python

    >>> print(fasta_record)
    >Yet Another Record
    AAAAAAAA
    TTTTTTTTTTTT
    CCCCCC
    GGGGGGGGGGGGGGG

However, using the :func:`tinyfasta.FastaRecord.format_sequence_line_length`
function we can standardised line length.

.. code-block:: python

    >>> fasta_record.sequence.format_line_length(30)
    >>> print(fasta_record)
    >Yet Another Record
    AAAAAAAATTTTTTTTTTTTCCCCCCGGGG
    GGGGGGGGGGG
