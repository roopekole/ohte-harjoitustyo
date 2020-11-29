
class Document:
    def __init__(self, project, file):
        self.id = None
        self.project = project
        self.file = file

    def set_doc_id(self, id):
        self.id = id


