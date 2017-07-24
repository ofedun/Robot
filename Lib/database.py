"""Class for Database."""
#!/usr/bin/python

import MySQLdb

CONNECTION_TIMEOUT = 100


class Database(object):
    def __init__(self, hostname, username, password, db_name):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db_name = db_name

    def open_connection(self):
        """Open database connection."""
        self.db_connection = MySQLdb.connect(
            self.hostname,
            self.username,
            self.password,
            self.db_name,
            connect_timeout=CONNECTION_TIMEOUT)

    def load_dump(self, file_path):
        """Load dump file into database."""
        self.open_connection()

        # prepare a cursor object using cursor() method
        cursor = self.db_connection.cursor()

        # Execute dump.sql file
        cursor.execute(open(file_path, "r").read())

    def close_connection(self):
        """Disconnect from server."""
        self.db_connection.close()
