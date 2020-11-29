
class Document:
    def __init__(self, project, file):
        self.document_id = None
        self.project = project
        self.file = file

    def set_doc_id(self, document_id):
        self.document_id = document_id
