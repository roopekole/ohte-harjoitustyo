import os
from shutil import rmtree
from whoosh import index
from config.file_storage_config import DOCUMENT_FILEPATH

def initialize_doc_storage():
    """
    Initializes the document file storage
    Returns:

    """
    if not os.path.exists(DOCUMENT_FILEPATH):
        os.mkdir(DOCUMENT_FILEPATH)
    else:
        rmtree(DOCUMENT_FILEPATH)
        os.mkdir(DOCUMENT_FILEPATH)