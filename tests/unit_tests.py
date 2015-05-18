import unittest

class PackageUnitTests(unittest.TestCase):

    def test_can_import_package(self):
        # Raises import error if the package cannot be imported.
        import tinyfasta

    def test_package_has_version_string(self):
        import tinyfasta
        self.assertTrue(isinstance(tinyfasta.__version__, str))

class FastaParserUnitTests(unittest.TestCase):

    def test_FastaParser_initialisation(self):
        from tinyfasta import FastaParser
        fasta_parser = FastaParser('test.fasta')
        self.assertTrue(isinstance(fasta_parser, FastaParser))

    def test_fpath(self):
        from tinyfasta import FastaParser
        fasta_parser = FastaParser('test.fasta')
        self.assertEqual(fasta_parser.fpath, 'test.fasta')

    def test_FastaParser_is_iterable(self):
        from tinyfasta import FastaParser
        fasta_parser = FastaParser('test.fasta')
        self.assertTrue(hasattr(fasta_parser, '__iter__'))

class FastaRecordUnitTests(unittest.TestCase):

    def test_FastaRecord_initialisation(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(isinstance(fasta_record, FastaRecord))

    def test_description(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertEqual(fasta_record.description, ">seq101|testing")

    def test_add_sequence_line(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("atta\n")
        fasta_record.add_sequence_line("TAAT")
        self.assertEqual(fasta_record.sequence, "attaTAAT")

    def test_string_representation(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("atta\n")
        fasta_record.add_sequence_line("TAAT")
        self.assertEqual(str(fasta_record),
            '\n'.join([">seq101|testing", "atta", "TAAT"]))

    def test_has_description_contains_function(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(callable(fasta_record.description_contains))

    def test_description_contains_function(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(fasta_record.description_contains("seq101"))
        self.assertTrue(fasta_record.description_contains("testing"))
        self.assertFalse(fasta_record.description_contains("seq102"))

    def test_description_contains_function_with_regex(self):
        import re
        regex_match = re.compile(r">seq1[0-9]{2}\|")
        regex_no_match = re.compile(r">seq1[0-9]{3}\|")
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertEqual(fasta_record.description, ">seq101|testing")
        self.assertTrue(fasta_record.description_contains(regex_match))
        self.assertFalse(fasta_record.description_contains(regex_no_match))

    def test_has_seqence_contains_function(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(callable(fasta_record.sequence_contains))

    def test_seqence_contains_function(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("AAAT")
        fasta_record.add_sequence_line("TAAA")
        self.assertTrue(fasta_record.sequence_contains("ATTA"))
        self.assertFalse(fasta_record.sequence_contains("ACCA"))

    def test_seqence_contains_function_with_regex(self):
        import re
        regex_match = re.compile(r"A[T]{2}A")
        regex_no_match = re.compile(r"A[T]{3}A")
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("AAAT")
        fasta_record.add_sequence_line("TAAA")
        self.assertTrue(fasta_record.sequence_contains(regex_match))
        self.assertFalse(fasta_record.sequence_contains(regex_no_match))

    def test_has_format_sequence_line_length(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(callable(fasta_record.format_sequence_line_length))

    def test_format_sequence_line_length(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("A"*80)
        self.assertEqual(len(fasta_record._sequences), 1)
        fasta_record.format_sequence_line_length(60)
        self.assertEqual(len(fasta_record._sequences), 2)
        self.assertEqual(len(fasta_record._sequences[0]), 60)
        self.assertEqual(len(fasta_record._sequences[1]), 20)
        
    def test_create_fasta_record(self):
        from tinyfasta import FastaRecord
        description = ">seq101|testing"
        sequence = "ATCG"*30
        fasta_record = FastaRecord.create(description, sequence)
        self.assertEqual(repr(fasta_record),
""">seq101|testing
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG""")

if __name__ == "__main__":
    unittest.main()
