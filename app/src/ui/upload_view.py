from os import path
from tkinter import ttk, constants, filedialog, StringVar
import tkinter
import document.document_functions as doc_funcs
from utilities import background_progress

class MetaDataInputs:

    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-many-arguments
    # All instance attributes and related function arguments are needed

    def __init__(self, upload_class, window, root, file_text, short_filename, long_filename,
                 instruction_text, progress_bar, start):
        self.upload = upload_class
        self.window = window
        self.root = root
        self.file_text = file_text
        self.short_filename = short_filename
        self.long_filename = long_filename
        self.instruction_text = instruction_text
        self.progress_bar = progress_bar
        self.handle_start = start
        self.frame = None
        self.project = None
        self.customer = None

        self.initialize()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.file_text.set("Selected file: " + self.short_filename.get())

        project_label = ttk.Label(self.frame, text="Enter the name of the reference project:")
        project_label.pack(pady=(20, 0))
        self.project = tkinter.Entry(master=self.frame, width=40)
        self.project.pack()

        customer_label = ttk.Label(self.frame, text="Enter the name of the customer:")
        customer_label.pack(pady=(20, 0))
        self.customer = tkinter.Entry(master=self.frame, width=40)
        self.customer.pack()

        self.instruction_text.set("Enter the metadata and press save \n"
                                  "or select a different document file")

        save_file_button = tkinter.Button(self.frame,
                                          text="SAVE", width=10, height=2, bg="#2B7a78",
                                          command=self.handle_save_button_click)
        save_file_button.pack(pady=20)

    def handle_save_button_click(self):
        """Processes the Save button click after file has been selected and
        information has been entered.

        """
        try:
            self.instruction_text.set("Uploading")
            doc_funcs.save_file(self.project.get(), self.customer.get(),
                                self.short_filename.get(), self.long_filename.get())

            background_progress.show_progress(self.window, self.progress_bar)

            self.upload.destroy()
            self.handle_start()
        except doc_funcs.InvalidDataEntry:
            self.instruction_text.set('Invalid data - please check and try again!')

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()


class UploadView:

    # pylint: disable=too-many-instance-attributes
    # All instance attributes are needed

    def __init__(self, root, handle_start, handle_search, handle_browse):
        """

        Args:
            root: TKInter root frame
            handle_start: function to process Return to start button click
            handle_search: function to process Search button click
            handle_browse: function to process browse button click
        """
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
        self.progress_bar = None
        self.file_text = None
        self.metadata_view = None
        self.metadata_frame = None

        self.initialize()


    def handle_upload_button_click(self):
        """ Processes the Select file button click.

        """
        filename = filedialog.askopenfilename()
        self.long_filename.set(filename)
        try:
            self.process_loaded_file()
        except doc_funcs.InvalidDataEntry:
            self.instruction_text.set('File type incorrect - select a PDF file')


    def process_loaded_file(self):
        if self.metadata_view is not None:
            self.file_text.set("")
            self.metadata_view.destroy()

        self.short_filename.set(path.basename(self.long_filename.get()))
        if not doc_funcs.check_file_type(self.short_filename.get()):
            raise doc_funcs.InvalidDataEntry('')

        self.metadata_view = MetaDataInputs(
            self,
            self.root,
            self.metadata_frame,
            self.file_text,
            self.short_filename,
            self.long_filename,
            self.instruction_text,
            self.progress_bar,
            self.handle_start
        )
        self.metadata_view.pack()

    def initialize(self):
        """ Initializes the Upload view


        """
        self.short_filename = StringVar()
        self.short_filename.set("")

        self.instruction_text = StringVar()
        self.instruction_text.set("Start storing documents by selecting a file "
                                                       "\n to be stored")

        self.file_text = StringVar()

        self.long_filename = StringVar()
        self.long_filename.set("")

        self.frame = ttk.Frame(master=self.root)
        self.frame_footer = ttk.Frame(master=self.root)


        upload_file_button = tkinter.Button(self.frame,
                                            text="Select a file (.PDF allowed)",
                                            width=40, height=1, bg="#DEF2F1",
                                            command=self.handle_upload_button_click)
        upload_file_button.pack()

        upload_file_label = ttk.Label(self.frame, textvariable=self.file_text)
        upload_file_label.pack(pady=(5,0))

        self.progress_bar = ttk.Progressbar(self.frame_footer,
                                            style="custom.Horizontal.TProgressbar")
        self.progress_bar.pack(fill="x")
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
        if self.metadata_view:
            self.metadata_view.destroy()
        self.frame_footer.destroy()
