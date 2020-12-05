import os
import re
from whoosh import index
from whoosh.qparser import QueryParser
from config import database_connect as db_conn
from document.document import Document
from utilities import pdf_parser

def modify_highlight(string):
    string = re.sub(r'<.*?>*</b>', lambda m: m.group(0).upper(), string)
    return re.sub("\n|\r", "", re.sub(r'\<.*?>', '', string))


def search(search_string, limit):
    # Note! Searcher is not closed explicitly, check if problematic
    indexer = index.open_dir("indexfiles")
    searcher = indexer.searcher()
    query = QueryParser("content", indexer.schema).parse(search_string)
    return searcher.search(query, limit=limit)

def upload_document_to_db(document):
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
    # Add file to index-search
    indexer = index.open_dir("indexfiles")
    writer = indexer.writer()
    writer.add_document(title=os.path.basename(str(document.document_id)), path=document.file,
                        content=pdf_parser.parsePDF(long_file_name),
                        _stored_content=pdf_parser.parsePDF(long_file_name))
    writer.commit()

def save_file(document, long_file_name):
    if not os.path.exists("file_storage"):
        os.mkdir("file_storage")

    # Naive file identicality check
    file_exists = os.path.exists("file_storage/" + document.file)
    if file_exists:
        return

    document.document_id = upload_document_to_db(document)
    save_path = "file_storage/"
    filename = os.path.join(save_path, str(document.document_id))

    newfile = open(filename, "w+b")
    newfile.write(open(long_file_name, "r+b").read())
    newfile.close()

    upload_to_index(document, long_file_name)

def download_file(doc_id, directory):
    doc = get_document_from_db(doc_id)
    file_path = "file_storage/" + str(doc_id)
    save_path = os.path.join(directory + "/" + doc.file)
    newfile = open(save_path, "w+b")
    newfile.write(open(file_path, "r+b").read())
    newfile.close()
