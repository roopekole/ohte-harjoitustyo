from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from document.document import Document
from os import path
import time

class BrowseView:
    def __init__(self, root, handle_upload, handle_search, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_start = handle_start
        self.handle_search = handle_search
        self.frame = None
        self.frame_footer = None
        self.short_filename = None
        self.long_filename = None
        self.project = None

        self.initialize()

    def handle_file_click(self, id):
        folder = tkinter.filedialog.askdirectory(mustexist=True)
        doc_funcs.download_file(id, folder)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)

        title_frame = ttk.Frame(master=self.frame)
        project_name = ttk.Label(master=title_frame, text="Project")
        customer_name = ttk.Label(master=title_frame, text="Customer")
        file_name = ttk.Label(master=title_frame, text="File name")
        dl_dummy = ttk.Label(master=title_frame, text="                 ")
        project_name.grid(row=0, column=0, padx=5, pady=0, sticky=constants.W)
        customer_name.grid(row=0, column=1, padx=5, pady=0, sticky=constants.W)
        file_name.grid(row=0, column=2, padx=5, pady=0, sticky=constants.W)
        dl_dummy.grid(row=0, column=3, padx=5, pady=0, sticky=constants.EW)
        title_frame.grid_columnconfigure(0, weight=3)
        title_frame.grid_columnconfigure(1, weight=3)
        title_frame.grid_columnconfigure(2, weight=3)
        title_frame.grid_columnconfigure(3, weight=1)
        title_frame.pack(fill=constants.X)

        documents = doc_funcs.get_all_documents_from_db()
        for doc in documents:
            result_frame = ttk.Frame(master=self.frame)
            project_name = ttk.Label(master=result_frame, text=doc.project)
            customer_name = ttk.Label(master=result_frame, text="Customer")
            file_name = ttk.Label(master=result_frame, text=doc.file)

            download_button = ttk.Button(
                master=result_frame,
                text='Download',
                command=lambda: self.handle_file_click(doc.id)
            )
            ttk.Separator(result_frame).place(x=0, y=0, relwidth=1)
            project_name.grid(row=0, column=0, padx=5, pady=3, sticky=constants.W)
            customer_name.grid(row=0, column=1, padx=5, pady=3, sticky=constants.W)
            file_name.grid(row=0, column=2, padx=5, pady=3, sticky=constants.W)

            download_button.grid(
                row=0,
                column=3,
                padx=5,
                pady=3,
                sticky=constants.EW
            )

            result_frame.grid_columnconfigure(0, weight=3)
            result_frame.grid_columnconfigure(1, weight=3)
            result_frame.grid_columnconfigure(2, weight=3)
            result_frame.grid_columnconfigure(3, weight=1)
            result_frame.pack()


        return_button = tkinter.Button(self.frame_footer, text="Back to start", width=65, height=1, bg="#DEF2F1",
                                       command=self.handle_start)
        return_button.pack(pady=10)

        search_button = tkinter.Button(self.frame_footer, text="Search", width=20, height=3, bg="#2B7a78",
                                       command=self.handle_search)
        search_button.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Label(self.frame_footer, text="Browse", width=20, height=3, bg="#FEFFFF")
        browse_button.pack(side=tkinter.LEFT)

        upload_label = tkinter.Button(self.frame_footer, text="Upload documents", width=20, height=3, bg="#DEF2F1",
                                      command=self.handle_upload)
        upload_label.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        self.frame_footer.destroy()