#!/usr/bin/python3
"""
It will list all the states from the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This will give access to the data base and get the state from db
    """
    datadata = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                               passwd=argv[2], datadata=argv[3])

    curd = datadata.cursor()
    curd.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    rows = curd.fetchall()

    for row in rows:
        print(row)
