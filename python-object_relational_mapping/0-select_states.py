#!/usr/bin/python3
"""script that lists all states from the database
"""


import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port = 3306,
        user = username,
        passwd = password,
        db = database,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.execute:
        print(row)

    cur.close()
    conn.close()
