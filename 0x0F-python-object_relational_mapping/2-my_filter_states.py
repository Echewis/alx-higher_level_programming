#!/usr/bin/python3
"""
This script will take an argument and
displays all the values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Will give access to the database and get the states
    from the database.
    """

    data_b = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], data_b=argv[3])

    cur = data_b.cursor()
    cur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
