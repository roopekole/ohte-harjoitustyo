from os import path
from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from document.document import Document
from utilities import background_progress

class UploadView:

    # pylint: disable=too-many-instance-attributes
    # All instance attributes are needed

    def __init__(self, root, handle_start, handle_search, handle_browse):
        self.root = root
        self.handle_start = handle_start
        self.handle_search = handle_search
        self.handle_browse = handle_browse
        self.frame = None
        self.frame_footer = None
        self.short_filename = None
        self.long_filename = None
        self.project = None
        self.customer = None
        self.instruction_text = None
        self.bar = None
        self.file_text = None

        self.initialize()


    def check_file_type(self, file):
        return str(file[-4:]).lower() == ".pdf"

    def handle_upload_button_click(self):
        filename = filedialog.askopenfilename()

        if not(self.check_file_type(filename)):
            # Todo: one can work around the check,
            #  by selecting PDF first and then other file type
            self.instruction_text.set("You must select a PDF file type!")

        if filename and self.check_file_type(filename):

            self.short_filename.set(path.basename(filename))
            self.long_filename = filename

            self.file_text.set("Selected file: " + self.short_filename.get())

            project_label = ttk.Label(self.frame, text="Enter the name of the reference project:")
            project_label.pack(pady=(20,0))
            self.project = tkinter.Entry(master=self.frame, width=40)
            self.project.pack()

            customer_label = ttk.Label(self.frame, text="Enter the name of the customer:")
            customer_label.pack(pady=(20,0))
            self.customer = tkinter.Entry(master=self.frame, width=40)
            self.customer.pack()

            self.instruction_text.set("Enter the metadata and press save \n"
                                      "or select a different document file")

            save_file_button = tkinter.Button(self.frame,
                                              text="SAVE", width=10, height=2, bg="#2B7a78",
                                                command=self.handle_save_button_click)
            save_file_button.pack(pady=20)

    def handle_save_button_click(self):
        self.instruction_text.set("Uploading")
        doc_funcs.save_file(Document(self.project.get(), self.customer.get(),
                                     self.short_filename.get()), self.long_filename)

        background_progress.show_progress(self.root, self.bar)

        self.destroy()
        self.handle_start()

    def initialize(self):
        self.short_filename = StringVar()
        self.short_filename.set("")

        self.instruction_text = StringVar()
        self.instruction_text.set("Start storing documents by selecting a file "
                                                       "\n to be stored")

        self.file_text = StringVar()

        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)


        upload_file_button = tkinter.Button(self.frame,
                                            text="Select a file (.PDF allowed)", width=40, height=1, bg="#DEF2F1",
                                            command=self.handle_upload_button_click)
        upload_file_button.pack()

        upload_file_label = ttk.Label(self.frame, textvariable=self.file_text)
        upload_file_label.pack(pady=(5,0))

        self.bar = ttk.Progressbar(self.frame_footer, style="custom.Horizontal.TProgressbar")
        self.bar.pack(fill="x")
        instruction_label = tkinter.Label(self.frame_footer, textvariable=self.instruction_text,
                                          bg="#E2F0FA", height=2, width=65, justify="center")
        instruction_label.pack(fill="x")

        return_button = tkinter.Button(self.frame_footer,
                                       text="Back to start", width=65, height=1, bg="#DEF2F1",
                                       command=self.handle_start)
        return_button.pack(pady=10, fill="x")

        search_button = tkinter.Button(self.frame_footer,
                                       text="Search", width=20, height=3, bg="#2B7a78",
                                       command=self.handle_search)
        search_button.pack(side=tkinter.LEFT, padx=10, pady=10)

        browse_button = tkinter.Button(self.frame_footer,
                                       text="Browse", width=20, height=3, bg="#3AAFA9",
                                       command=self.handle_browse)
        browse_button.pack(side=tkinter.LEFT)

        upload_label = tkinter.Label(self.frame_footer,
                                     text="Upload documents", width=20, height=3, bg="#FEFFFF")
        upload_label.pack(side=tkinter.LEFT, padx=10)

    def pack(self):
        self.frame.pack(fill="none", expand=True)
        self.frame_footer.pack(side=constants.BOTTOM)

    def destroy(self):
        self.frame.destroy()
        self.frame_footer.destroy()
