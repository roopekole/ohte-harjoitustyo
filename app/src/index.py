from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT
import os.path
from whoosh.index import create_in

schema = Schema(title=TEXT(stored=True), content=TEXT,
                path=ID(stored=True), tags=KEYWORD, icon=STORED)

if not os.path.exists("indexfiles"):
    os.mkdir("indexfiles")
ix = create_in("indexfiles", schema)
writer = ix.writer()
writer.add_document(title=u"First document", path=u"/a",
                    content=u"This is the first document we've added!")
writer.add_document(title=u"Second document", path=u"/a",
                    content=u"This is the second document we've added!")
writer.commit()

from whoosh.qparser import QueryParser
with ix.searcher() as searcher:
    query = QueryParser("content", ix.schema).parse("add")
    results = searcher.search(query)
    for r in results:
        print(r)