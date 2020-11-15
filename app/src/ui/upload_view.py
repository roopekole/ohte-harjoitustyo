from tkinter import ttk, constants, filedialog, StringVar
import tkinter
from document.document_functions import DocumentFunctions as doc_funcs
from os import path

class UploadView:
    def __init__(self, root, handle_start, handle_search):
        self.root = root
        self.handle_start = handle_start
        self.handle_search = handle_search
        self.frame = None
        self.short_filename = None
        self.long_filename = None

        self.initialize()

    def handle_upload_button_click(self):
        filename = tkinter.filedialog.askopenfilename()
        #Upload the file to Whoosh index
        doc_funcs.get_file_contents(filename)
        self.short_filename.set(path.basename(filename))
        self.long_filename.set(filename)

    def initialize(self):
        self.short_filename = StringVar()
        self.short_filename.set("")

        self.long_filename = StringVar()
        self.long_filename.set("")

        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)

        bar = ttk.Separator()
        bar.pack()

        upload_file_button = tkinter.Button(self.frame, text="Select a file", width=40, height=1, bg="#DEF2F1",
                                            command=self.handle_upload_button_click)
        upload_file_button.pack()

        upload_file_label = ttk.Label(self.frame, textvariable=self.short_filename)
        upload_file_label.pack()

        return_button = tkinter.Button(self.frame_footer, text="Back to start", width=65, height=1, bg="#DEF2F1",
                                       command=self.handle_start)
        return_button.pack(pady=10)

        search_button = tkinter.Button(self.frame_footer, text="Search", width=20, height=3, bg="#2B7a78",
                                       command=self.handle_search)
        search_button.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Button(self.frame_footer, text="Browse", width=20, height=3, bg="#3AAFA9")
        browse_button.pack(side=tkinter.LEFT)

        upload_label = tkinter.Label(self.frame_footer, text="Upload documents", width=20, height=3, bg="#FEFFFF")
        upload_label.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        self.frame_footer.destroy()


"""    def initialize(self):
        lbl1 = tkinter.Button(self.root, text="Search", width=20, height=5, bg='SlateGray2')
        lbl1.pack(side=tkinter.LEFT, padx=10, pady=10)

        lbl2 = tkinter.Button(self.root, text="Browse", width=20, height=5, bg='SlateGray3')
        lbl2.pack(side=tkinter.LEFT)

        lbl3 = tkinter.Button(self.root, text="Upload documents", width=20, height=10, bg='SlateGray4')
        lbl3.pack(side=tkinter.LEFT, padx=10)
"""