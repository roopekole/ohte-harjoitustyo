import codecs
import os
from config.whoosh_config import Config
from whoosh.qparser import QueryParser


def search(search_string, limit):
    # Note! Searcher is not closed explicitly, check if problematic
    searcher = Config.ix.searcher()
    query = QueryParser("content", Config.ix.schema).parse(search_string)
    return searcher.search(query, limit=limit)

def get_file_contents(file):
    with codecs.open(file, "r", "ISO-8859-1") as f:
        content = f.read()
        return content

def upload_to_index(file):
    # Add file to index-search
    writer = Config.ix.writer()
    writer.add_document(title=os.path.basename(file), path=u"/a",
                        content=get_file_contents(file))
    writer.commit()

def save_file(file):
    if not os.path.exists("file_storage"):
        os.mkdir("file_storage")

    # Naive file identicality check
    file_exists = os.path.exists("file_storage/" + os.path.basename(file))
    if file_exists:
        return
    else:
        save_path = "file_storage/"
        filename = os.path.join(save_path, os.path.basename(file))
        newfile = open(filename, "w")
        newfile.write(get_file_contents(file))
        newfile.close()
        upload_to_index(file)

def download_file(directory):
    print(os.path(directory))
