import unittest
from document.document_functions import DocumentFunctions as docfuncs
import os, sys


class TestFunctions(unittest.TestCase):

    def test_upload_can_access_file_contents(self):
        self.assertEqual(docfuncs.get_file_contents("src/tests/upload_test_file.txt"), "This is the content of the file" + "\r\n"
                                                                                       "This is the second row of the file")