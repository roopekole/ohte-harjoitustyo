import os
from shutil import rmtree
from whoosh import index
from config.whoosh_config import Config


def initialize_index():
    """
    Initializes the indexing storage given the Whoosh schema
    Returns:

    """
    if not os.path.exists(Config.WHOOSH_FILEPATH):
        os.mkdir(Config.WHOOSH_FILEPATH)
    else:
        rmtree(Config.WHOOSH_FILEPATH)
        os.mkdir(Config.WHOOSH_FILEPATH)
    index.create_in(Config.WHOOSH_FILEPATH, Config.schema)