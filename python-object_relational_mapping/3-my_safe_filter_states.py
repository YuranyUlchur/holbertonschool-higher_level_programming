#!/usr/bin/python3
"""
script that takes in arguments and displays all values
"""


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_name = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name='%s'"(search_name,))
    results = cursor.fetchall()

    for row in results:
        print(row)
    cursor.close()
    conn.close()
