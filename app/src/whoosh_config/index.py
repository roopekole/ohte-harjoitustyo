from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
import os.path
from whoosh import index

class Config:
    schema = Schema(title=TEXT(stored=True), content=TEXT,
                    path=ID(stored=True), tags=KEYWORD, icon=STORED)


    # These most likely belong to _init_ in the root
    if not os.path.exists("indexfiles"):
        os.mkdir("indexfiles")
        ix = index.create_in("indexfiles", schema)
    else:
        ix = index.open_dir("indexfiles")