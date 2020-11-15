import unittest
from store.storage import Upload
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.upload = Upload()
