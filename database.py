"""Class for Database."""
#!/usr/bin/python

import MySQLdb


class Database(object):
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password

        # self.root = 'admin'
        # self.host = 'http://localhost/addressbook/'
        # self.rootpw = 'password'

    def open_connection(self):
        """Open database connection."""
        self.db_connection = MySQLdb.connect(self.hostname, self.username, self.password)

    def load_dump(self, file_path):
        """Load dump file into database."""
        self.open_connection()

        # prepare a cursor object using cursor() method
        cursor = self.db_connection.cursor()

        # Execute dump.sql file
        # with self.connection as cursor:
        cursor.execute(open(file_path, "r").read()).store_result()
        self.close_connection()

    def close_connection(self):
        """Disconnect from server."""
        self.db_connection.close()
