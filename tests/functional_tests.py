import os
import os.path
import shutil

HERE = os.path.dirname(__file__)
DATA_DIR = os.path.join(HERE, 'data')
TMP_DIR = os.path.join(HERE, 'tmp')

import unittest
class FunctionalTests(unittest.TestCase):

    def setUp(self):
        if not os.path.isdir(TMP_DIR):
            os.mkdir(TMP_DIR)

    def tearDown(self):
        shutil.rmtree(TMP_DIR)

    def test_output_is_consistent_with_input(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        output_fasta = os.path.join(TMP_DIR, "tmp.fasta")
        with open(output_fasta, "w") as fh:
            for fasta_record in FastaParser(input_fasta):
                fh.write("{}\n".format(fasta_record))
        input_data = open(input_fasta, "r").read()
        output_data = open(output_fasta, "r").read()
        self.assertEqual(input_data, output_data)

    def test_descritpion_contains(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description.contains('seq3')]
        self.assertEqual(len(hits), 1)
        self.assertEqual(str(hits[0].description),
            ">seq3|ends with ATTA motif in second line")

    def test_seqence_contains_function_no_file(self):
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("AAAT")
        fasta_record.add_sequence_line("TAAA")
        self.assertTrue(fasta_record.sequence.contains("ATTA"))
        self.assertFalse(fasta_record.sequence.contains("ACCA"))

    def test_seqence_contains_function_with_regex_no_file(self):
        import re
        regex_match = re.compile(r"A[T]{2}A")
        regex_no_match = re.compile(r"A[T]{3}A")
        from tinyfasta import FastaRecord
        fasta_record = FastaRecord(">seq101|testing\n")
        fasta_record.add_sequence_line("AAAT")
        fasta_record.add_sequence_line("TAAA")
        self.assertTrue(fasta_record.sequence.contains(regex_match))
        self.assertFalse(fasta_record.sequence.contains(regex_no_match))

    def test_sequence_contains(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.sequence.contains('ATTA')]
        self.assertEqual(len(hits), 4)

    def test_formatting_sequence(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description.contains('crazy formatting')]
        fasta_record = hits[0]
        fasta_record.sequence.format_line_length(78)
        self.assertEqual(str(fasta_record), """>seq6|crazy formatting
AAATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTAAAAAAATTTTTTTTTTTTTTTTTTT""")

    def test_sequence_regex_match(self):
        import re
        regex = re.compile(r"A[C,T]{3}A")
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.sequence.contains(regex)]
        self.assertEqual(len(hits), 2)
        self.assertTrue(str(hits[0].description).startswith(">seq7"))
        self.assertTrue(str(hits[1].description).startswith(">seq8"))

    def test_description_regex_match(self):
        import re
        regex = re.compile(r">seq[7,8]\|")
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description.contains(regex)]
        self.assertEqual(len(hits), 2)
        self.assertTrue(str(hits[0].description).startswith(">seq7"))
        self.assertTrue(str(hits[1].description).startswith(">seq8"))

    def test_gzipped_input(self):
        from tinyfasta import FastaParser
        import gzip
        raw_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        gzipped_fasta = os.path.join(TMP_DIR, "tmp.fasta.gz")
        with gzip.open(gzipped_fasta, "wb") as fh:
            with open(raw_fasta, "r") as fh2:
                try:
                    # Python 2.
                    fh.write(fh2.read())
                except TypeError:
                    # Python 3.
                    fh.write(bytes(fh2.read(), "UTF-8"))
        output_fasta = os.path.join(TMP_DIR, "tmp.fasta")
        with open(output_fasta, "w") as fh:
            for fasta_record in FastaParser(gzipped_fasta, fopen=gzip.open):
                fh.write("{}\n".format(fasta_record))
        raw_data = open(raw_fasta, "r").read()
        output_data = open(output_fasta, "r").read()
        self.assertEqual(raw_data, output_data)

        
if __name__ == "__main__":
    unittest.main()
