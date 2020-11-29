import codecs
import os
import re
from whoosh import index
from whoosh.qparser import QueryParser
from config import database_connect as db_conn
from document.document import Document

def modify_highlight(string):
    string = re.sub(r'<.*?>*</b>', lambda m: m.group(0).upper(), string)
    return re.sub(r'\<.*?>', '', string)


def search(search_string, limit):
    # Note! Searcher is not closed explicitly, check if problematic
    ix = index.open_dir("indexfiles")
    searcher = ix.searcher()
    query = QueryParser("content", ix.schema).parse(search_string)
    return searcher.search(query, limit=limit)

def get_file_contents(file):
    with codecs.open(file, "r", "ISO-8859-1") as f:
        content = f.read()
        return content

def upload_document_to_db(document):
    conn = db_conn.get_database_connection()
    """
        Create new document into DOCUMENTS table
        :param conn:
        :param document:
        :return: document id
        """
    sql = ''' INSERT INTO documents(PROJECT,FILE)
                  VALUES(?,?) '''
    cur = conn.cursor()
    values = [document.project,document.file]
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    return cur.lastrowid

def get_document_from_db(doc_id):
    conn = db_conn.get_database_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM documents WHERE id=?", (doc_id,))
    doc_query_object = cur.fetchall()[0]
    doc = Document(doc_query_object[1], doc_query_object[2])
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
        document = Document(doc[1],doc[2])
        document.set_doc_id(doc[0])
        doc_list.append(document)
    cur.close()
    return doc_list

def upload_to_index(document,long_file_name):
    # Add file to index-search
    ix = index.open_dir("indexfiles")
    writer = ix.writer()
    writer.add_document(title=os.path.basename(str(document.id)), path=u"/a",
                        content=get_file_contents(long_file_name),
                        _stored_content=get_file_contents(long_file_name))
    writer.commit()

def save_file(document, long_file_name):
    if not os.path.exists("file_storage"):
        os.mkdir("file_storage")

    # Naive file identicality check
    file_exists = os.path.exists("file_storage/" + document.file)
    if file_exists:
        return
    else:
        document.id = upload_document_to_db(document)
        save_path = "file_storage/"
        filename = os.path.join(save_path, str(document.id))
        newfile = open(filename, "w")
        newfile.write(get_file_contents(long_file_name))
        newfile.close()
        upload_to_index(document, long_file_name)

def download_file(doc_id, directory):
    doc = get_document_from_db(doc_id)
    file_path = "file_storage/" + str(doc_id)
    save_path = os.path.join(directory + "/" + doc.file)
    newfile = open(save_path, "w")
    newfile.write(get_file_contents(file_path))
    newfile.close()