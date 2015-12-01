"""Package for parsing and generating FASTA files of biological sequences.

Use the :class:`tinyfasta.FastaParser` class to parse FASTA files. 

To generate FASTA files use the  :func:`tinyfasta.FastaRecord.create` static
method to create :class:`tinyfasta.FastaRecord` instances, which can be written
to file.
"""

__version__ = "0.1.0"

class _FastaRecordComponent(object):
    """Component of a FastaRecort."""

    def contains(self, search_term):
        """Return True if the component contains the search term.
        
        :param search_term: string or compiled regular expression to search for
        :returns: bool
        """
        if hasattr(search_term, "search"):
            return search_term.search(self._content) is not None
        return self._content.find(search_term) != -1

class Sequence(_FastaRecordComponent):
    """Class representing a biological sequence."""
          
    def __init__(self):
        self._sequences = []

    def __str__(self):
        return self._content

    def __len__(self):
        """Return the length of the biological sequence."""
        return sum(len(s) for s in self._sequences)

    @property
    def _content(self):
        """Return the sequence as a string.
        
        :returns: str
        """
        return ''.join(self._sequences)

    def add_sequence_line(self, sequence_line):
        """
        Add a sequence line to the :class:`tinyfasta.Sequence` instance.

        This function can be called more than once. Each time the function is
        called the :class:`tinyfasta.Sequence` is extended by the sequence line
        provided.

        :param sequence_line: string representing (part of) a sequence
        """
        self._sequences.append( sequence_line.strip() )

    def format_line_length(self, line_length=80):
        """Format line length used to represent the sequence.

        The full sequence is stored as list of shorter sequences. These shorter
        sequences are used verbatim when writing out the
        :class:`tinyfasta.FastaRecord` over several lines.
        
        :param line_length: length of the sequences used to make up the full
                            sequence
        """
        def string_to_list(seq, n):
            """Return list of strings of length n."""
            return [seq[i:i+n] for i in range(0, len(seq), n)]
        self._sequences = string_to_list(self._content, line_length)
    
class FastaRecord(object):
    """Class representing a FASTA record."""

    class Description(_FastaRecordComponent):
        """Description line in a :class:`tinyfasta.FastaRecord`."""
        
        def __init__(self, description):
            self.update(description)

        def __str__(self):
            return self._content

        def update(self, description):
            """Update the content of the description.

            This function can be used to replace the existing description with
            a new one.
            
            :param description: new description string
            """
            if not description.startswith(">"):
                description = ">{}".format(description)
            self._content = description.strip()


    @staticmethod
    def create(description, sequence):
        """Return a FastaRecord.
        
        :param description: description string
        :param sequence: full sequence string
        :returns: :class:`tinyfasta.FastaRecord`
        """
        fasta_record = FastaRecord(description)
        fasta_record.add_sequence_line(sequence)
        fasta_record.sequence.format_line_length()
        return fasta_record

    def __init__(self, description):
        """Initialise an instance of the :class:`tinyfasta.FastaRecord` class.
        
        :param description: description string
        """
        self.description = FastaRecord.Description(description)
        self.sequence = Sequence()

    def __str__(self):
        """String representation of the :class:`tinyfasta.FastaRecord` instance."""
        lines = [str(self.description),]
        lines.extend(self.sequence._sequences)
        return '\n'.join(lines)

    def __len__(self):
        """Return the length of the biological sequence."""
        return len(self.sequence)

    def add_sequence_line(self, sequence_line):
        """Add a sequence line to the :class:`tinyfasta.FastaRecord` instance.

        This function can be called more than once. Each time the function is
        called the :attr:`tinyfasta.sequence` is extended by the sequence line
        provided.

        :param sequence_line: string representing (part of) a sequence
        """
        self.sequence.add_sequence_line(sequence_line)

class FastaParser(object):
    """Class for parsing FASTA files.

    To parse a gzipped FASTA file import the gzip module and pass the gzip.open
    function to the fopen argument::

        import gzip
        fasta_parser = FastaParser("uniprot_sprot.fasta.gz", fopen=gzip.open)

    """

    def __init__(self, fpath, fopen=open):
        """Initialise an instance of the FastaParser.

        :param fpath: path to the FASTA file to be parsed
        :param fopen: function for opening the file
        """
        self.fpath = fpath
        self.fopen = fopen

    def __iter__(self):
        """Yield FastaRecord instances."""
        fasta_record = None
        with self.fopen(self.fpath, 'r') as fh:
            for line in fh:
                if line.startswith('>'):
                    if fasta_record:
                        yield fasta_record
                    fasta_record = FastaRecord(line)
                else:
                    fasta_record.add_sequence_line(line)
        yield fasta_record
