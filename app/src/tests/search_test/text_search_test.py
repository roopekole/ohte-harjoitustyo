import unittest
from search.text_search import Search


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.search = Search()

    def test_search_can_access_index(self):
        print(Search.ix)
        self.assertTrue(Search.ix)