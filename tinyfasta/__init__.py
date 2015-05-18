"""tinyfasta package."""

__version__ = "0.0.1"


class FastaRecord(object):
    """Class representing a FASTA record."""

    @staticmethod
    def _match(string, search_term):
        """Return True if the search_term is in the string.

        :param string: string to be searched
        :param search_term: string or compiled regex
        :returns: bool
        """
        if hasattr(search_term, "search"):
            return search_term.search(string) is not None
        return string.find(search_term) != -1

    @staticmethod
    def create(description, sequence):
        """Return a FastaRecord."""
        fasta_record = FastaRecord(description)
        fasta_record.add_sequence_line(sequence)
        fasta_record.format_sequence_line_length()
        return fasta_record

    def __init__(self, description_line):
        """Initialise an instance of the FastaRecord class."""
        self.description = description_line.strip()
        self._sequences = []

    def __repr__(self):
        """Representation of the FastaRecord instance."""
        lines = [self.description,]
        lines.extend(self._sequences)
        return '\n'.join(lines)

    @property
    def sequence(self):
        """Return the full sequence as a string."""
        return ''.join(self._sequences)

    def add_sequence_line(self, sequence_line):
        """
        Add a sequence line to the FastaRecord instance.
        This function can be called more than once.
        """
        self._sequences.append( sequence_line.strip() )

    def description_contains(self, search_term):
        """Return True if the search_term is in the description.

        :param search_term: string or compiled regex
        :returns: bool
        """
        return FastaRecord._match(self.description, search_term)

    def sequence_contains(self, search_motif):
        """Return True if the motif is in the sequence.

        :param search_motif: string or compiled regex
        :returns: bool
        """
        return FastaRecord._match(self.sequence, search_motif)

    def format_sequence_line_length(self, line_length=80):
        """Format the sequence to use the specified line length."""
        def string_to_list(seq, n):
            """Return list strings of length n."""
            return [seq[i:i+n] for i in range(0, len(seq), n)]
        self._sequences = string_to_list(self.sequence, line_length)

class FastaParser(object):
    """Class for parsing FASTA files."""

    def __init__(self, fpath):
        """Initialise an instance of the FastaParser."""
        self.fpath = fpath

    def __iter__(self):
        """Yield FastaRecord instances."""
        fasta_record = None
        with open(self.fpath, 'r') as fh:
            for line in fh:
                if line.startswith('>'):
                    if fasta_record:
                        yield fasta_record
                    fasta_record = FastaRecord(line)
                else:
                    fasta_record.add_sequence_line(line)
        yield fasta_record
