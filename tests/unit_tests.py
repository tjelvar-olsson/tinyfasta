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
        self.assertEqual(fasta_parser.fpath, 'test.fasta')

    def test_FastaParser_is_iterable(self):
        from tinyfasta import FastaParser
        fasta_parser = FastaParser('test.fasta')
        self.assertTrue(hasattr(fasta_parser, '__iter__'))

class FastaRecordUnitTests(unittest.TestCase):

    def test_FastaRecord_initialisation(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        self.assertEqual(fasta_record.description, ">seq101|testing")

    def test_add_sequence_line(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("atta\n")
        fasta_record.add_sequence_line("TAAT")
        self.assertEqual(fasta_record.sequence, "attaTAAT")


if __name__ == "__main__":
    unittest.main()
