import os
import unittest
import document.document_functions as docfuncs
from document.document import Document
from config.whoosh_config import Config
from whoosh.fields import Schema, ID, TEXT
from config import database_connect, database_config, database_initialize
from utilities import pdf_parser

class TestFunctions(unittest.TestCase):


    def test_search_gets_schema_from_config(self):
        self.assertEqual(Config.schema, Schema(title=TEXT(stored=True),
                                               content=TEXT(stored=True),
                                               path=ID(stored=True),))

    def test_search_yields_no_results_with_bogus_string(self):
        # In the test indices there are no hits with keywork "somebogusstring"
        self.assertEqual(len(docfuncs.search("somebogusstring", 10)), 0)

    def test_searching_yields_res_objects(self):
        #There are two docs with hits "ipsum"
        self.assertEqual(len(docfuncs.search("ipsum", 10)), 2)

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


    def test_upload_metadata_to_db(self):
        # Test should return id 3 when new document is inserted
        # At last the inserted row is removed
        doc = Document("Test project", "Test customer", "test_file.xyz")
        self.assertEqual(docfuncs.upload_document_to_db(doc), 3)
        conn = database_connect.get_database_connection()
        cur = conn.cursor()
        sql = '''DELETE FROM documents WHERE id = 3 '''
        cur.execute(sql)
        conn.commit()
        cur.close()

    def test_uploading_content_to_index(self):
        # Search for term, add similar content and check that hits increase
        doc = Document("Test project", "Test customer", "test_file")
        hits = len(docfuncs.search("test", 999999999999999999))
        docfuncs.upload_to_index(doc, "src/tests/test_upload_files/one_page_test_file.pdf")
        self.assertEqual(len(docfuncs.search("test", 99999999999999999)), hits+1)

    def test_downloading_file(self):
        # "Download" file to test storage and assert the parsed content
        docfuncs.download_file(2, "src/tests/test_upload_files/download/")
        downloaded_content = pdf_parser.parse_pdf("src/tests/test_upload_files/download/sample2.pdf")
        self.assertEqual(downloaded_content[:28], "Aeque enim contingit omnibus")
        os.remove("src/tests/test_upload_files/download/sample2.pdf")

