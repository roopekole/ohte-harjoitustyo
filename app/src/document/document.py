import codecs
import os
from whoosh_config.index import Config
from whoosh.qparser import QueryParser

class Documents:

    def search(search_string):
        with Config.ix.searcher() as searcher:
            query = QueryParser("content", Config.ix.schema).parse(search_string)
            results = searcher.search(query)
            print("I'm now searching with string: " + search_string)
        return results

    def upload(file):
        with codecs.open(file, "r", "ISO-8859-1") as f:
            content = f.read()
            writer = Config.ix.writer()
            writer.add_document(title=os.path.basename(file), path=u"/a",
                                content=content)
            writer.commit()