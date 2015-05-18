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
                if f.description_contains('seq3')]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].description,
            ">seq3|ends with ATTA motif in second line")

    def test_sequence_contains(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.sequence_contains('ATTA')]
        self.assertEqual(len(hits), 4)

    def test_formatting_sequence(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description_contains('crazy formatting')]
        fasta_record = hits[0]
        fasta_record.format_sequence_line_length(78)
        self.assertEqual(str(fasta_record), """>seq6|crazy formatting
AAATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTAAAAAAATTTTTTTTTTTTTTTTTTT""")

    def test_sequence_regex_match(self):
        import re
        regex = re.compile(r"A[C,T]{3}A")
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.sequence_contains(regex)]
        self.assertEqual(len(hits), 2)
        self.assertTrue(hits[0].description.startswith(">seq7"))
        self.assertTrue(hits[1].description.startswith(">seq8"))

    def test_description_regex_match(self):
        import re
        regex = re.compile(r">seq[7,8]\|")
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description_contains(regex)]
        self.assertEqual(len(hits), 2)
        self.assertTrue(hits[0].description.startswith(">seq7"))
        self.assertTrue(hits[1].description.startswith(">seq8"))

        
if __name__ == "__main__":
    unittest.main()
