from whoosh.fields import Schema, ID, TEXT


class Config:
    schema = Schema(
        title=TEXT(stored=True),
        content=TEXT(stored=True),
        path=ID(stored=True),
    )
