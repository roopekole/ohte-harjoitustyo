import re
from tkinter import Tk, ttk
from unittest import TestCase, mock
from utilities import pdf_parser, background_progress

class TestFunctions(TestCase):

    def test_pdf_parser_extracts_correctly(self):
        self.assertEqual(re.sub(r"(?m)^\s+", "", pdf_parser.parse_pdf("src/tests/one_page_test_file.pdf")), "test\n")
        self.assertEqual(re.sub(r"(?m)^\s+", "", pdf_parser.parse_pdf("src/tests/two_page_test_file.pdf")), "test\npage 2\n")

    @mock.patch("utilities.background_progress.show_progress")
    def test_progress_bar_updates(self, mock_show_progress):
        background_progress.show_progress(Tk(),ttk.Progressbar)
        self.assertTrue(mock_show_progress.called)
