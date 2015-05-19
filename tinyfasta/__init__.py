"""tinyfasta package."""

__version__ = "0.0.2"

class _FastaRecordComponent(object):
    """Component of a FastaRecort."""

    def contains(self, search_term):
        """Return True if the component contains the search term."""
        if hasattr(search_term, "search"):
            return search_term.search(self._content) is not None
        return self._content.find(search_term) != -1

class Sequence(_FastaRecordComponent):
    """Class representing a biological sequence."""
          
    def __init__(self):
        self._sequences = []

    def __str__(self):
        return self._content

    @property
    def _content(self):
        return ''.join(self._sequences)

    def add_sequence_line(self, sequence_line):
        """
        Add a sequence line to the FastaRecord instance.
        This function can be called more than once.
        """
        self._sequences.append( sequence_line.strip() )

    def format_line_length(self, line_length=80):
        """Format the sequence to use the specified line length."""
        def string_to_list(seq, n):
            """Return list strings of length n."""
            return [seq[i:i+n] for i in range(0, len(seq), n)]
        self._sequences = string_to_list(self._content, line_length)
    
class FastaRecord(object):
    """Class representing a FASTA record."""

    class Description(_FastaRecordComponent):
        """Class representing the description line in a FastaRecord."""
        
        def __init__(self, description):
            self._content = description.strip()

        def __str__(self):
            return self._content

    @staticmethod
    def create(description, sequence):
        """Return a FastaRecord."""
        fasta_record = FastaRecord(description)
        fasta_record.add_sequence_line(sequence)
        fasta_record.sequence.format_line_length()
        return fasta_record

    def __init__(self, description_line):
        """Initialise an instance of the FastaRecord class."""
        self.description = FastaRecord.Description(description_line)
        self.sequence = Sequence()

    def __str__(self):
        """String representation of the FastaRecord instance."""
        lines = [str(self.description),]
        lines.extend(self.sequence._sequences)
        return '\n'.join(lines)

    def add_sequence_line(self, sequence_line):
        """
        Add a sequence line to the FastaRecord instance.
        This function can be called more than once.
        """
        self.sequence.add_sequence_line(sequence_line)

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
