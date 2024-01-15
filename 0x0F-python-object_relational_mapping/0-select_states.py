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
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    co = db.cursor()
    co.execute("SELECT * FROM states")
    rows = co.fetchall()

    for row_t in rows:
        print(row_t)
