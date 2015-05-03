"""tinyfasta package."""

__version__ = "0.0.1"


class FastaRecord(object):
    """Class representing a FASTA record."""

    def __init__(self, description_line):
        """Initialise an instance of the FastaRecord class."""
        self.description = description_line.strip()

class FastaParser(object):
    """Class for parsing FASTA files."""

    def __init__(self, fpath):
        """Initialise an instance of the FastaParser."""
        self.fpath = fpath

    def __iter__(self):
        """Yield FastaRecord instances."""
        yield None
