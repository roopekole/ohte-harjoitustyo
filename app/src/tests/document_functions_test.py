import unittest
from unittest import mock
import document.document_functions as docfuncs
from document.document import Document
from config.whoosh_config import Config
from whoosh.fields import Schema, ID, TEXT
from config import database_connect, database_config, database_initialize
import re


class TestFunctions(unittest.TestCase):

    def test_search_gets_schema_from_config(self):
        self.assertEqual(Config.schema, Schema(title=TEXT(stored=True),
                                               content=TEXT(stored=True),
                                               path=ID(stored=True),))

    @mock.patch("document.document_functions.search", return_value=0)
    def test_search_yields_no_results_with_bogus_string(self, mock_search):
        docfuncs.search("somebogusstring", 0)
        self.assertTrue(mock_search.called)
        self.assertEqual(docfuncs.search("somebogusstring", 0), 0)

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

    def test_get_doc_from_db(self):
        if len(docfuncs.get_all_documents_from_db()) == 0:
            self.assertIsNone(docfuncs.get_document_from_db(1))
        else:
            self.assertEqual(docfuncs.get_document_from_db(1).document_id, 1)


