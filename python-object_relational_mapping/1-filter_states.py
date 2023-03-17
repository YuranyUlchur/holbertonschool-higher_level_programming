#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'")
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
