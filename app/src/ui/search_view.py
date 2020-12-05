from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from utilities import background_progress

class SearchResultList:
    def __init__(self, root, res, bar, window, instruction_text, keywords, result_amount):
        self.root = root
        self.results = res
        self.frame = None
        self.bar = bar
        self.window = window
        self.instruction_text = instruction_text
        self.keywords = keywords
        self.amount = result_amount

        self.initialize()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        title_frame = ttk.Frame(master=self.frame)


        project_name = ttk.Label(master=title_frame, text="Project")
        customer_name = ttk.Label(master=title_frame, text="Customer")
        file_name = ttk.Label(master=title_frame, text="File name")
        score = ttk.Label(master=title_frame, text="Search score")

        project_name.grid(row=0, column=0, padx=5, pady=0, sticky=constants.W)
        customer_name.grid(row=0, column=1, padx=5, pady=0, sticky=constants.W)
        file_name.grid(row=0, column=2, padx=5, pady=0, sticky=constants.W)
        score.grid(row=1, column=3, padx=5, pady=0, sticky=constants.EW)

        file_highlight = ttk.Label(master=title_frame, text="Content highlight")
        file_highlight.grid(row=1, column=0, columnspan=3, padx=5, pady=0, sticky=constants.W)

        title_frame.grid_columnconfigure(0, weight=3)
        title_frame.grid_columnconfigure(1, weight=3)
        title_frame.grid_columnconfigure(2, weight=3)
        title_frame.grid_columnconfigure(3, weight=1)
        title_frame.pack(fill=constants.X)

        for result in self.results:
            self.initialize_result(result)

    def initialize_result(self, result):
        document = doc_funcs.get_document_from_db(result['title'])

        result_frame = ttk.Frame(master=self.frame)
        content_highlight = ttk.Label(master=result_frame,
                                      text=doc_funcs.modify_highlight(result.highlights("content")))
        project_name = ttk.Label(master=result_frame, text=document.project)
        customer_name = ttk.Label(master=result_frame, text=document.customer)
        file_name = ttk.Label(master=result_frame, text=document.file)
        score_name = ttk.Label(master=result_frame, text=result.score)

        download_button = ttk.Button(
            master=result_frame,
            text='Download',
            command=lambda: self.handle_file_click(result)
        )
        ttk.Separator(result_frame).place(x=0, y=0, relwidth=1)
        project_name.grid(row=0, column=0, padx=5, pady=3, sticky=constants.W)
        customer_name.grid(row=0, column=1, padx=5, pady=3, sticky=constants.W)
        file_name.grid(row=0, column=2, padx=5, pady=3, sticky=constants.W)
        content_highlight.grid(row=1, column=0, columnspan=3, padx=5, pady=3, sticky=constants.W)
        score_name.grid(row=1, column=3, sticky=constants.W)


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


    def handle_file_click(self, result):
        folder = filedialog.askdirectory(mustexist=True)
        if folder:
            self.instruction_text.set("Downloading " + result['path'])
            background_progress.show_progress(self.window, self.bar)
            doc_funcs.download_file(result['title'], folder)
            self.bar["value"] = 0
            self.instruction_text.set("Found " + self.amount + " results with keyword(s) " + self.keywords)

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

class SearchView:
    # pylint: disable=too-many-instance-attributes
    # All instance attributes are needed
    def __init__(self, root, handle_upload, handle_browse, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_browse = handle_browse
        self.handle_start = handle_start
        self.frame = None
        self.entry = None
        self.search_list_view = None
        self.search_list_frame = None
        self.instruction_text = None
        self.bar = None

        self.initialize()

    def handle_search_button_click(self):
        # Initializes the search list view with query results
        res = doc_funcs.search(self.entry.get(), 10)
        if self.search_list_view:
            self.search_list_view.destroy()


        self.search_list_view = SearchResultList(
            self.search_list_frame,
            res,
            self.bar,
            self.root,
            self.instruction_text,
            self.entry.get(),
            str(len(res))
        )

        self.search_list_view.pack()
        self.instruction_text.set("Found " + str(len(res)) + " results with keyword(s) " + self.entry.get())


    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)

        self.instruction_text = StringVar()
        self.instruction_text.set("Enter keywords and press search")

        self.entry = tkinter.Entry(master=self.frame, width=50)
        self.entry.pack()

        search_file_button = tkinter.Button(self.frame,
                                            text="Search for a file",
                                            width=40, height=1, bg="#DEF2F1",
                                            command=self.handle_search_button_click)
        search_file_button.pack(pady=10)

        self.bar = ttk.Progressbar(self.frame_footer, style="custom.Horizontal.TProgressbar")
        self.bar.pack(fill="x")
        instruction_label = tkinter.Label(self.frame_footer, textvariable=self.instruction_text,
                                          bg="#E2F0FA", height=2, width=65, justify="center")
        instruction_label.pack(fill="x")

        return_button = tkinter.Button(self.frame_footer,
                                       text="Back to start", width=65, height=1, bg="#DEF2F1",
                                       command=self.handle_start)
        return_button.pack(pady=10, fill="x")

        search_label = tkinter.Label(self.frame_footer,
                                     text="Search", width=20, height=3, bg="#FEFFFF")
        search_label.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Button(self.frame_footer,
                                       text="Browse", width=20, height=3, bg="#3AAFA9",
                                       command=self.handle_browse)
        browse_button.pack(side=tkinter.LEFT)

        upload_button = tkinter.Button(self.frame_footer,
                                       text="Upload documents", width=20, height=3, bg="#DEF2F1",
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
