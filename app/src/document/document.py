
class Document:
    """Document class. Currently sets the ID for the document object.


    """
    def __init__(self, project, customer, file):
        self.document_id = None
        self.project = project
        self.customer = customer
        self.file = file

    def set_doc_id(self, document_id):
        self.document_id = document_id
