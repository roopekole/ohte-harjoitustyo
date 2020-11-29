from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from document.document import Document



class SearchResultList:
    def __init__(self, root, res):
        self.root = root
        self.res = res
        self.frame = None

        self.initialize()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        title_frame = ttk.Frame(master=self.frame)
        project_name = ttk.Label(master=title_frame, text="Project")
        customer_name = ttk.Label(master=title_frame, text="Customer")
        file_name = ttk.Label(master=title_frame, text="File name")
        dl_dummy = ttk.Label(master=title_frame, text="                 ")
        project_name.grid(row=0, column=0, padx=5, pady=0, sticky=constants.W)
        customer_name.grid(row=0, column=1, padx=5, pady=0, sticky=constants.W)
        file_name.grid(row=0, column=2, padx=5, pady=0, sticky=constants.W)
        dl_dummy.grid(row=0, column=3, padx=5, pady=0, sticky=constants.EW)
        file_highlight = ttk.Label(master=title_frame, text="Content highlight")
        file_highlight.grid(row=1, column=0, columnspan=4, padx=5, pady=0, sticky=constants.W)
        title_frame.grid_columnconfigure(0, weight=3)
        title_frame.grid_columnconfigure(1, weight=3)
        title_frame.grid_columnconfigure(2, weight=3)
        title_frame.grid_columnconfigure(3, weight=1)
        title_frame.pack(fill=constants.X)
        for r in self.res:
            self.initialize_result(r)

    def initialize_result(self, r):
        document = doc_funcs.get_document_from_db(r['title'])

        result_frame = ttk.Frame(master=self.frame)
        content_highlight = ttk.Label(master=result_frame, text=doc_funcs.modify_highlight(r.highlights("content")))
        project_name = ttk.Label(master=result_frame, text=document.project)
        customer_name = ttk.Label(master=result_frame, text="Customer")
        file_name = ttk.Label(master=result_frame, text=document.file)

        download_button = ttk.Button(
            master=result_frame,
            text='Download',
            command=lambda: self.handle_file_click(r)
        )
        ttk.Separator(result_frame).place(x=0, y=0, relwidth=1)
        project_name.grid(row=0, column=0, padx=5, pady=3, sticky=constants.W)
        customer_name.grid(row=0, column=1, padx=5, pady=3, sticky=constants.W)
        file_name.grid(row=0, column=2, padx=5, pady=3, sticky=constants.W)
        content_highlight.grid(row=1, column=0, columnspan=4, padx=5, pady=3, sticky=constants.W)


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
        result_frame.pack(fill=constants.X)


    def handle_file_click(self, r):
        folder = tkinter.filedialog.askdirectory(mustexist=True)
        doc_funcs.download_file(r['title'], folder)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

class SearchView:
    def __init__(self, root, handle_upload, handle_browse, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_browse = handle_browse
        self.handle_start = handle_start
        self.frame = None
        self.entry = None
        self.search_list_view = None
        self.search_list_frame = None
        self.initialize()

    def handle_search_button_click(self):
        # Initializes the search list view with query results
        res = doc_funcs.search(self.entry.get(), 10)
        if self.search_list_view:
            self.search_list_view.destroy()


        self.search_list_view = SearchResultList(
            self.search_list_frame,
            res,
        )

        self.search_list_view.pack()


    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)


        self.entry = tkinter.Entry(master=self.frame)
        self.entry.pack()

        search_file_button = tkinter.Button(self.frame, text="Search for a file", width=40, height=1, bg="#DEF2F1", command=self.handle_search_button_click)
        search_file_button.pack()


        return_button = tkinter.Button(self.frame_footer, text="Back to start", width=65, height=1, bg="#DEF2F1", command=self.handle_start)
        return_button.pack(pady=10)

        search_label = tkinter.Label(self.frame_footer, text="Search", width=20, height=3, bg="#FEFFFF")
        search_label.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Button(self.frame_footer, text="Browse", width=20, height=3, bg="#3AAFA9",
                                       command=self.handle_browse)
        browse_button.pack(side=tkinter.LEFT)

        upload_button = tkinter.Button(self.frame_footer, text="Upload documents", width=20, height=3, bg="#DEF2F1",
                                      command=self.handle_upload)
        upload_button.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        if self.search_list_view:
            self.search_list_view.destroy()
        self.frame_footer.destroy()
