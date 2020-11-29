import unittest
from unittest import mock
import document.document_functions as docfuncs
from document.document import Document
from config.whoosh_config import Config
from whoosh.fields import Schema, ID, TEXT
from config import database_connect, database_config, database_initialize
import re


class TestFunctions(unittest.TestCase):

    def test_upload_can_access_file_contents(self):
        self.assertEqual(docfuncs.get_file_contents("src/tests/upload_test_file.txt"), "This is the content of the file")

    def test_search_gets_schema_from_config(self):
        self.assertEqual(Config.schema, Schema(title=TEXT(stored=True),
                                               content=TEXT(stored=True),
                                               path=ID(stored=True),))

    def test_search_yields_no_results_with_bogus_string(self):
        # Test that the numerical value in the query result object is 0
        res = re.findall(r'\d+',
                         str(docfuncs.search(
                            "bogus_content_qpwoeiurowieurpoqwieurpoqwieurpwqopoweiurpowqeiurowieru", 9999999))[0:15])  # Extract integer with regex
        self.assertEqual(int(res[0]), 0)

    def test_string_highlight_removes_html_tags_and_creates_uppercase(self):
        self.assertEqual(docfuncs.modify_highlight("test string which is not highlighted"),
                         "test string which is not highlighted")
        self.assertEqual(docfuncs.modify_highlight(""),"")
        self.assertEqual(docfuncs.modify_highlight("<b></b>"), "")
        self.assertEqual(docfuncs.modify_highlight("<b>test</b> string, <b>every</b> second <b>is</b> highlighted"),
                         "TEST string, EVERY second IS highlighted")

    def test_get_all_documents_lenght_equal_db_row_count(self):
        conn = database_connect.get_database_connection()
        cur = conn.cursor()
        cur.execute("SELECT max(rowid) from documents")
        n = cur.fetchone()[0]
        self.assertEqual(len(docfuncs.get_all_documents_from_db()), n)
        cur.close()

