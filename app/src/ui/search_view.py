from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs

class SearchView:
    def __init__(self, root, handle_upload, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_start = handle_start
        self.frame = None
        self.entry = None
        self.initialize()

    def handle_file_click(self):
        print(self)
        folder = tkinter.filedialog.askdirectory(mustexist=True)
        doc_funcs.save_file(folder)

    def handle_search_button_click(self):
        # Returns whoosh Query result object containing the specified number of hits
        res = doc_funcs.search(self.entry.get(), 10)


        heading_label = ttk.Label(master=self.frame, text="Results")
        heading_label.pack(padx=5, pady=5)

        # Unpack the object into result grid
        for r in res:
            username_label = ttk.Button(master=self.frame, text=r,
                                        command=self.handle_file_click)
            username_label.pack(padx=5, pady=5)

        self.pack()

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
