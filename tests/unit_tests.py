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

class FastaRecordComponentUnitTests(unittest.TestCase):
    
    def test_component_initialisation(self):
        from tinyfasta import _FastaRecordComponent
        component = _FastaRecordComponent()
        self.assertTrue(isinstance(component, _FastaRecordComponent))
        
    def test_has_contains_function(self):
        from tinyfasta import _FastaRecordComponent
        component = _FastaRecordComponent()
        self.assertTrue(callable(component.contains))

    def test_contains_function(self):
        from tinyfasta import _FastaRecordComponent
        component = _FastaRecordComponent()
        component._content = ">seq101|testing"
        self.assertTrue(component.contains("seq101"))
        self.assertTrue(component.contains("testing"))
        self.assertFalse(component.contains("seq102"))

    def test_contains_function_with_regex(self):
        from tinyfasta import _FastaRecordComponent
        import re
        regex_match = re.compile(r">seq1[0-9]{2}\|")
        regex_no_match = re.compile(r">seq1[0-9]{3}\|")
        component = _FastaRecordComponent()
        component._content = ">seq101|testing"
        self.assertTrue(component.contains(regex_match))
        self.assertFalse(component.contains(regex_no_match))

class DescriptionUnitTests(unittest.TestCase):

    def test_Description_initialisation(self):
        from tinyfasta import FastaRecord
        description = FastaRecord.Description(">seq101|testing\n")
        self.assertTrue(isinstance(description, FastaRecord.Description))

    def test_Description_initialisation_withount_leading_arrow(self):
        from tinyfasta import FastaRecord
        description = FastaRecord.Description("seq101|testing\n")
        self.assertEqual(str(description), ">seq101|testing")

    def test_content(self):
        from tinyfasta import FastaRecord
        description = FastaRecord.Description(">seq101|testing\n")
        self.assertEqual(description._content, ">seq101|testing")

    def test_str(self):
        from tinyfasta import FastaRecord
        description = FastaRecord.Description(">seq101|testing\n")
        self.assertEqual(str(description), ">seq101|testing")
        
    def test_update_description(self):
        from tinyfasta import FastaRecord
        description = FastaRecord.Description(">seq101|testing\n")
        self.assertEqual(str(description), ">seq101|testing")
        description.update(">seq102|testing\n")
        self.assertEqual(str(description), ">seq102|testing")
        description.update(">seq103|testing")
        self.assertEqual(str(description), ">seq103|testing")
        description.update(">seq104|testing")
        self.assertEqual(str(description), ">seq104|testing")

class SequenceUnitTests(unittest.TestCase):

    def test_Sequence_initialisation(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        self.assertTrue(isinstance(sequence, Sequence))

    def test_add_sequence_line(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        sequence.add_sequence_line("atta\n")
        sequence.add_sequence_line("TAAT")
        self.assertEqual(sequence._sequences, ["atta", "TAAT"])

    def test_content(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        sequence.add_sequence_line("atta\n")
        sequence.add_sequence_line("TAAT")
        self.assertEqual(sequence._content, "attaTAAT")

    def test_str(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        sequence.add_sequence_line("atta\n")
        sequence.add_sequence_line("TAAT")
        self.assertEqual(str(sequence), "attaTAAT")

    def test_has_format_line_length(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        self.assertTrue(callable(sequence.format_line_length))

    def test_format_line_length(self):
        from tinyfasta import Sequence
        sequence = Sequence()
        sequence.add_sequence_line("A"*80)
        self.assertEqual(len(sequence._sequences), 1)
        sequence.format_line_length(60)
        self.assertEqual(len(sequence._sequences), 2)
        self.assertEqual(len(sequence._sequences[0]), 60)
        self.assertEqual(len(sequence._sequences[1]), 20)
        

class FastaRecordUnitTests(unittest.TestCase):

    def test_FastaRecord_initialisation(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(isinstance(fasta_record, FastaRecord))

    def test_description(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertEqual(str(fasta_record.description), ">seq101|testing")

    def test_add_sequence_line(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("atta\n")
        fasta_record.add_sequence_line("TAAT")
        self.assertEqual(str(fasta_record.sequence), "attaTAAT")

    def test_string_representation(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("atta\n")
        fasta_record.add_sequence_line("TAAT")
        self.assertEqual(str(fasta_record),
            '\n'.join([">seq101|testing", "atta", "TAAT"]))

    def test_description_type(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(isinstance(fasta_record.description,
            FastaRecord.Description))

    def test_seqence_type(self):
        from tinyfasta import FastaRecord, Sequence
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertTrue(isinstance(fasta_record.sequence, Sequence))

    def test_create_fasta_record(self):
        from tinyfasta import FastaRecord
        description = ">seq101|testing"
        sequence = "ATCG"*30
        fasta_record = FastaRecord.create(description, sequence)
        self.assertEqual(str(fasta_record),
""">seq101|testing
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG
ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG""")

if __name__ == "__main__":
    unittest.main()
