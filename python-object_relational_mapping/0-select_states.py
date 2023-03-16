#!/usr/bin/python3
'''script that lists all states from the database
'''


import MySQLdb
import sys

if __name__ == '__main__':

    mysql_user = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_pwd,
        db=db_name,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)
    cur.close()
    conn.close()
