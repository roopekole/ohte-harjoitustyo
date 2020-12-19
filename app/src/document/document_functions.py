import os
import re
from whoosh import index
from whoosh.qparser import QueryParser
from document.document import Document
from utilities import pdf_parser
from config import database_connect as db_conn
from config.whoosh_config import Config
from config.file_storage_config import DOCUMENT_FILEPATH

def modify_highlight(string):
    """

    Args:
        string: Whoosh search hit highlight string which contains HTML formating

    Returns: String without HTML formatting and unnecessary linebreaks,
    hit emphasized with upper case

    """
    string = re.sub(r'<.*?>*</b>', lambda m: m.group(0).upper(), string)
    return re.sub("\n|\r", "", re.sub(r'\<.*?>', '', string))


def search(search_string, limit):
    """

    Args:
        search_string: user entered search keyword(s)
        limit: maximum threshold for queried Hit objects. If applied, the lowest scored
        results are neglected.

    Returns:

    """
    # Note! Searcher is not closed explicitly, check if problematic

    indexer = index.open_dir(Config.WHOOSH_FILEPATH)
    searcher = indexer.searcher()
    query = QueryParser("content", indexer.schema).parse(search_string)
    return searcher.search(query, limit=limit)

def upload_document_to_db(document):
    """

    Args:
        document: Document object to be inserted to the database

    Returns:

    """
    conn = db_conn.get_database_connection()
    sql = ''' INSERT INTO documents(PROJECT,CUSTOMER,FILE)
                  VALUES(?,?,?) '''
    cur = conn.cursor()
    values = [document.project,document.customer, document.file]
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    return cur.lastrowid

def get_document_from_db(doc_id):
    """

    Args:
        doc_id: Document id to be retreived from the database

    Returns: Document object given the id

    """
    conn = db_conn.get_database_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM documents WHERE id=?", (doc_id,))
    doc_query_object = cur.fetchall()[0]
    # Construct Document object with params: project, customer, file
    doc = Document(doc_query_object[1], doc_query_object[2], doc_query_object[3])
    doc.set_doc_id(doc_query_object[0])
    cur.close()
    return doc

def get_all_documents_from_db():
    """

    Returns: All document objects from the database

    """
    conn = db_conn.get_database_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM documents")
    doc_records = cur.fetchall()
    doc_list = []
    for doc in doc_records:
        document = Document(doc[1],doc[2], doc[3])
        document.set_doc_id(doc[0])
        doc_list.append(document)
    cur.close()
    return doc_list

def upload_to_index(document,long_file_name):
    """Adds document and its text content to the Whoosh full-text search index

    Args:
        document: document object to be added to the index
        long_file_name: OS path to the file from which the content text is to be extracted

    Returns:

    """
    # Add file to index-search
    indexer = index.open_dir(Config.WHOOSH_FILEPATH)
    writer = indexer.writer()
    writer.add_document(title=os.path.basename(str(document.document_id)), path=document.file,
                        content=pdf_parser.parse_pdf(long_file_name),
                        _stored_content=pdf_parser.parse_pdf(long_file_name))
    writer.commit()

def save_file(project,customer,file, long_file_name):
    """ Processes the server functions of the file upload request.

    Args:
        document: Document object to be added to the database and Whoosh index
        long_file_name: OS path to the file to be stored to server and extracted
        added to search index.

    Returns:

    """
    
    document = Document(project, customer, file)

    document.document_id = upload_document_to_db(document)
    save_path = DOCUMENT_FILEPATH
    filename = os.path.join(save_path, str(document.document_id))

    newfile = open(filename, "w+b")
    newfile.write(open(long_file_name, "r+b").read())
    newfile.close()

    upload_to_index(document, long_file_name)

def download_file(doc_id, directory):
    """Processes the server functions of a download request.

    Args:
        doc_id: Database id of a document to be downloaded
        directory: Directory selected by the user, to which the requested file is downloaded.

    Returns:

    """
    doc = get_document_from_db(doc_id)
    file_path = DOCUMENT_FILEPATH + "/" + str(doc_id)
    save_path = os.path.join(directory + "/" + doc.file)
    newfile = open(save_path, "w+b")
    newfile.write(open(file_path, "r+b").read())
    newfile.close()

def check_file_type(file):
    """

    Args:
        file: File selected by the application user

    Returns: True if file is PDF file, else False

    """
    return str(file[-4:]).lower() == ".pdf"


class InvalidDataEntry(Exception):
    pass
