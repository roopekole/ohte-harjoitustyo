import unittest
from document.document import Document

class TestFunctions(unittest.TestCase):

    def test_create_new_document(self):
        doc = Document("Test", "testfile.txt")
        self.assertEqual(doc.document_id, None)
        self.assertEqual(doc.project, "Test")
        self.assertEqual(doc.file, "testfile.txt")

    def test_set_document_id(self):
        doc = Document("Test", "testfile.txt")
        doc.set_doc_id(1)
        self.assertEqual(doc.document_id, 1)