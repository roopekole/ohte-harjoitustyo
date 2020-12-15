import os
from whoosh.fields import Schema, ID, TEXT


class Config:
    """Whoosh Config class which defines the schema of the index
    and the variable file path for indexing
        title: document database ID
        content: extracted text of the file
        path: OS file basename

    """
    schema = Schema(
        title=TEXT(stored=True),
        content=TEXT(stored=True),
        path=ID(stored=True),
    )
    WHOOSH_FILEPATH = os.getenv("WHOOSH_FILEPATH") or 'index_files'