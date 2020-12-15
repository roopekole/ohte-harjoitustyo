import os
import unittest


class TestEnvVariables(unittest.TestCase):

    def test_env_paths(self):
        # Make sure that environment paths are correctly picked
        # from .env-test environment variable configuration
        self.assertEqual(os.getenv("DOCUMENT_FILEPATH"), "src/tests/test_doc_files")
        self.assertEqual(os.getenv("DATABASE_FILENAME"), "test-database.sqlite")
        self.assertEqual(os.getenv("WHOOSH_FILEPATH"), "src/tests/test_index_files")

    def test_directories_and_files_exits(self):
        self.assertTrue(os.path.exists(os.path.join("data", "test-database.sqlite")))
        self.assertTrue(os.path.exists("src/tests/test_index_files"))


