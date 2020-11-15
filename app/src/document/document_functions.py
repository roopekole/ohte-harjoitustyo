import codecs
import os
from whoosh_config.index import Config
from whoosh.qparser import QueryParser

class DocumentFunctions:

    def search(self, search_string):
        with Config.ix.searcher() as searcher:
            query = QueryParser("content", Config.ix.schema).parse(search_string)
            results = searcher.search(query)
        return results

    def get_file_contents(file):
        with codecs.open(file, "r", "ISO-8859-1") as f:
            content = f.read()
            return content

    def upload(self, file):
        writer = Config.ix.writer()
        writer.add_document(title=os.path.basename(file), path=u"/a",
                            content=self.get_file_contents(file))
        writer.commit()