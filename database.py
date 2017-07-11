"""Class for Database."""
#!/usr/bin/python
# from sqlite3 import dump

import MySQLdb


class Database():
    def __init__(self):
        self.root = 'admin'
        self.host = 'http://localhost/addressbook/'
        self.rootpw = 'secret'

        # Open database connection
        db = MySQLdb.connect(self.host, self.root, self.rootpw)

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Execute dump.sql file
        # with self.connection as cursor:
        cursor.execute(open("dump.sql", "r").read())

        # disconnect from server
        db.close()
