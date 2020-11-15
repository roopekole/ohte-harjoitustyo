from tkinter import Tk, ttk
from ui.start_view import StartView
from ui.upload_view import UploadView
from ui.search_view import SearchView

class UI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def handle_upload(self):
        self.show_upload_view()

    def handle_search(self):
        self.show_search_view()

    def handle_start(self):
        self.show_start_view()

    def show_start_view(self):
        self.hide_current_view()
        self.current_view = StartView(
            self.root,
            self.handle_upload,
            self.handle_search
        )
        self.current_view.pack()

    def show_search_view(self):
        self.hide_current_view()
        self.current_view = SearchView(
            self.root,
            self.handle_upload,
            self.handle_start
        )
        self.current_view.pack()

    def show_upload_view(self):
        self.hide_current_view()
        self.current_view = UploadView(
            self.root,
            self.handle_start,
            self.handle_search
        )
        self.current_view.pack()

    def start(self):
        self.show_start_view()
