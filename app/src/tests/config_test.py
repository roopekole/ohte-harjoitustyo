import os
import unittest
from config.file_storage_initialize import initialize_doc_storage

class TestConfigs(unittest.TestCase):

    def test_document_file_path_initialization(self):
        initialize_doc_storage()
        self.assertTrue(os.path.exists("src/tests/test_doc_files"))
        initialize_doc_storage()
        self.assertTrue(os.path.exists("src/tests/test_doc_files"))
        os.rmdir("src/tests/test_doc_files")