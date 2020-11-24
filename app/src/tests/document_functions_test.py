import unittest
import document.document_functions as docfuncs
from config.whoosh_config import Config
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
import re


class TestFunctions(unittest.TestCase):

    def test_upload_can_access_file_contents(self):
        self.assertEqual(docfuncs.get_file_contents("src/tests/upload_test_file.txt"), "This is the content of the file")

    def test_search_gets_schema_from_config(self):
        self.assertEqual(Config.schema, Schema(title=TEXT(stored=True), content=TEXT,
                    path=ID(stored=True), tags=KEYWORD, icon=STORED))

    def test_search_yields_results(self):
        # Test that the numerical value in the query result object equals 10
        res = re.findall(r'\d+',
                         str(docfuncs.search(
                             "luottamus", 10))[0:15])  #Extract integer with regex
        self.assertEqual(res[0], "10")

    def test_search_yields_no_results_with_bogus_string(self):
        # Test that the numerical value in the query result object is 0
        res = re.findall(r'\d+',
                         str(docfuncs.search(
                            "bogus_content_qpwoeiurowieurpoqwieurpoqwieurpwqopoweiurpowqeiurowieru", 9999999))[0:15])  # Extract integer with regex
        self.assertEqual(int(res[0]), 0)
