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
    state_name = sys.argv[4].split(';')[0].strip("'")

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC", (state_name,)
                )
                
    rows = cur.fetchall()
    elements = []
    for row in rows:
        elements.append("{}".format(row[0]))
    print(", ".join(elements))


    cur.close()
    conn.close()
