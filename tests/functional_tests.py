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

    def test_descritpion_matches(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description_matches('seq3')]
        self.assertEqual(len(hits), 1)
        self.assertEqual(hits[0].description,
            ">seq3|ends with ATTA motif in second line")

    def test_sequence_matches(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.sequence_matches('ATTA')]
        self.assertEqual(len(hits), 4)

    def test_formatting_sequence(self):
        from tinyfasta import FastaParser
        input_fasta = os.path.join(DATA_DIR, "dummy.fasta")
        hits = [f for f in FastaParser(input_fasta)
                if f.description_matches('crazy formatting')]
        fasta_record = hits[0]
        fasta_record.format_sequence_line_length(78)
        self.assertEqual(str(fasta_record), """>seq6|crazy formatting
AAATTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
TTTTTTAAAAAAATTTTTTTTTTTTTTTTTTT""")

        
if __name__ == "__main__":
    unittest.main()
