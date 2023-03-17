#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON WHERE states.name = %s cities.state_id = states.id\
                ORDER BY cities.id ASC"
                )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
