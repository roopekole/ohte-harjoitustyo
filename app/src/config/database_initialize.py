from config.database_connect import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists documents;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY,
            PROJECT TEXT,
            CUSTOMER TEXT,
            FILE TEXT
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


# This allows us to call the initialize_database function using command line
if __name__ == '__main__':
    initialize_database()
