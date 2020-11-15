from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as docfuncs


class SearchView:
    def __init__(self, root, handle_upload, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_start = handle_start
        self.frame = None
        self.entry = None
        self.search_results = []
        self.search_row = None

        self.initialize()

    def handle_search_button_click(self):
        res = docfuncs.search(self.entry.get())
        print(res)

    def initialize(self):
        self.search_row = StringVar()
        self.search_row.set("")

        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)

        bar = ttk.Separator()
        bar.pack()

        self.entry = tkinter.Entry(master=self.frame)
        self.entry.pack()
        search_file_button = tkinter.Button(self.frame, text="Search for a file", width=40, height=1, bg="#DEF2F1", command=self.handle_search_button_click)
        search_file_button.pack()


        result_label = ttk.Label(master=self.root, textvariable=self.search_row)
        result_label.pack()

        return_button = tkinter.Button(self.frame_footer, text="Back to start", width=65, height=1, bg="#DEF2F1", command=self.handle_start)
        return_button.pack(pady=10)

        search_label = tkinter.Label(self.frame_footer, text="Search", width=20, height=3, bg="#FEFFFF")
        search_label.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Button(self.frame_footer, text="Browse", width=20, height=3, bg="#3AAFA9")
        browse_button.pack(side=tkinter.LEFT)

        upload_button = tkinter.Button(self.frame_footer, text="Upload documents", width=20, height=3, bg="#DEF2F1",
                                      command=self.handle_upload)
        upload_button.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        self.frame_footer.destroy()
