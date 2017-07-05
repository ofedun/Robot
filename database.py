"""Class for Database."""
#!/usr/bin/python

# import sys
# import MySQLdb


# class Database():
#     def __init__(self):
#         self.root = 'admin'
#         self.host = 'http://localhost/addressbook/'
#         self.rootpw = 'secret'

        # Open database connection
        # db = MySQLdb.connect(self.host, self.root, self.rootpw)

        # prepare a cursor object using cursor() method
        # cursor = db.cursor()

        # Drop table if it already exist using execute() method.
        # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

        # Create table as per requirement
        # sql = """CREATE TABLE AddressBook (
        #          FIRST_NAME  CHAR(20) NOT NULL,
        #          LAST_NAME  CHAR(20),
        #          AGE INT,
        #          SEX CHAR(1),
        #          INCOME FLOAT )"""

        # cursor.execute(sql)

        # disconnect from server
        # db.close()






        # # execute SQL query using execute() method.
        # cursor.execute("SELECT VERSION()")
        #
        # # Fetch a single row using fetchone() method.
        # data = cursor.fetchone()
        #
        # print "Database version : %s " % data













        # try:
        #     print '\nChecking MySQL connection...'
        #     self.db = MySQLdb.connect(self.host, self.root, self.rootpw)
        #     self.cursor = self.db.cursor()
        #     self.cursor.execute('select version()')
        #     print 'Connection OK, proceeding.'
        # except MySQLdb.Error as error:
        #     print 'Error: %s ' % error + '\nStop.\n'
        #     sys.exit()