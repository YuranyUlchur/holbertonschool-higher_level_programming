#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    matchname = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name={}".format(matchname))
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
