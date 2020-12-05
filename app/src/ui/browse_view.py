from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from utilities import background_progress

class BrowseView:
    def __init__(self, root, handle_upload, handle_search, handle_start):
        self.root = root
        self.handle_upload = handle_upload
        self.handle_start = handle_start
        self.handle_search = handle_search
        self.frame = None
        self.frame_footer = None
        self.project = None
        self.instruction_text = None
        self.bar = None
        self.document_amount = 0

        self.initialize()

    def handle_file_click(self, document_id, file):
        folder = filedialog.askdirectory(mustexist=True)
        if folder:
            self.instruction_text.set("Downloading " + file)
            background_progress.show_progress(self.root, self.bar)
            doc_funcs.download_file(document_id, folder)
            self.bar["value"] = 0
            self.instruction_text.set("There are " + self.document_amount.get() + " documents in the database. \n"
                                                                           "Click Download to save the file")


    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)

        documents = doc_funcs.get_all_documents_from_db()

        self.document_amount = StringVar()
        self.document_amount.set(str(len(documents)))

        self.instruction_text = StringVar()
        self.instruction_text.set("There are " + self.document_amount.get() + " documents in the database. \n"
                                                                  "Click Download to save the file")

        title_frame = ttk.Frame(master=self.frame)
        project_name = ttk.Label(master=title_frame, text="Project")
        customer_name = ttk.Label(master=title_frame, text="Customer")
        file_name = ttk.Label(master=title_frame, text="File name")
        dl_dummy = ttk.Label(master=title_frame, text="                 ")
        project_name.grid(row=0, column=0, padx=5, pady=0, sticky=constants.EW)
        customer_name.grid(row=0, column=1, padx=5, pady=0, sticky=constants.EW)
        file_name.grid(row=0, column=2, padx=5, pady=0, sticky=constants.EW)
        dl_dummy.grid(row=0, column=3, padx=5, pady=0, sticky=constants.EW)
        title_frame.grid_columnconfigure(0, weight=3)
        title_frame.grid_columnconfigure(1, weight=3)
        title_frame.grid_columnconfigure(2, weight=3)
        title_frame.grid_columnconfigure(3, weight=1)
        title_frame.pack(fill=constants.X)


        for doc in documents:
            result_frame = ttk.Frame(master=self.frame)
            project_name = ttk.Label(master=result_frame, text=doc.project)
            customer_name = ttk.Label(master=result_frame, text=doc.customer)
            file_name = ttk.Label(master=result_frame, text=doc.file)

            download_button = ttk.Button(
                master=result_frame,
                text='Download',
                command=lambda: self.handle_file_click(doc.document_id, doc.file)
            )
            ttk.Separator(result_frame).place(x=0, y=0, relwidth=1)
            project_name.grid(row=0, column=0, padx=5, pady=3, sticky=constants.EW)
            customer_name.grid(row=0, column=1, padx=5, pady=3, sticky=constants.EW)
            file_name.grid(row=0, column=2, padx=5, pady=3, sticky=constants.EW)

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
            result_frame.pack(fill="x")



        self.bar = ttk.Progressbar(self.frame_footer, style="custom.Horizontal.TProgressbar")
        self.bar.pack(fill="x")
        instruction_label = tkinter.Label(self.frame_footer, textvariable=self.instruction_text,
                                          bg="#E2F0FA", width=65, justify="center")
        instruction_label.pack(fill="x")

        return_button = tkinter.Button(self.frame_footer,
                                       text="Back to start", width=65, height=1, bg="#DEF2F1",
                                       command=self.handle_start)
        return_button.pack(pady=10)

        search_button = tkinter.Button(self.frame_footer,
                                       text="Search", width=20, height=3, bg="#2B7a78",
                                       command=self.handle_search)
        search_button.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Label(self.frame_footer,
                                      text="Browse", width=20, height=3, bg="#FEFFFF")
        browse_button.pack(side=tkinter.LEFT)

        upload_label = tkinter.Button(self.frame_footer,
                                      text="Upload documents", width=20, height=3, bg="#DEF2F1",
                                      command=self.handle_upload)
        upload_label.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="x", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        self.frame_footer.destroy()
