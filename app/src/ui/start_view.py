from tkinter import ttk
import tkinter

class StartView:
    def __init__(self, root, handle_upload, handle_search, handle_browse):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_search = handle_search
        self.handle_browse = handle_browse
        self.frame = None

        self.initialize()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        lbl1 = tkinter.Button(self.frame, text="Search", width=20, height=5, bg="#2B7a78",
                              command=self.handle_search)
        lbl1.pack(side=tkinter.LEFT, padx=10, pady=10)

        lbl2 = tkinter.Button(self.frame, text="Browse", width=20, height=5, bg="#3AAFA9",
                              command=self.handle_browse)
        lbl2.pack(side=tkinter.LEFT)

        lbl3 = tkinter.Button(self.frame, text="Upload documents", width=20, height=5, bg="#DEF2F1",
                              command=self.handle_upload)
        lbl3.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)

    def destroy(self):
        self.frame.destroy()
