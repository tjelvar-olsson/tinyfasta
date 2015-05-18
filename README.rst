Quick Guide
===========

*What is "tinyfasta"?*

It is a Python package for parsing biological sequences from FASTA files.

*Why do we need another Python FASTA parser?*

There are already several Python packages available for parsing FASTA files.
However, many of these packages do much more than just parse FASTA files and as
such have dependencies on `NumPy <http://www.numpy.org>`_ and `SciPy
<http://www.scipy.org>`_. These are quite heavy weight dependencies if all you
want to do is a little bit of text processing. This is where :mod:`tinyfasta`
fits in. It is a lightweight Python package with no dependencies outside of the
Python standard library.

*How do I install ``tinyfasta``?*

To install the :mod:`tinyfasta` package.

.. code-block:: bash

    cd tinyfasta
    python setup.py install
