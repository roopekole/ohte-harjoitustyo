from config.database_initialize import initialize_database
from config.whoosh_initialize import initialize_index
from config.file_storage_initialize import initialize_doc_storage

def build():
    initialize_database()
    initialize_index()
    initialize_doc_storage()



# This allows us to call the build function using command line
if __name__ == '__main__':
    build()
