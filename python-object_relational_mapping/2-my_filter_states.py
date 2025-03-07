#!/usr/bin/python3
"""Module to list all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    cur = conn.cursor()
    state = sys.argv[4]
    cur.execute("SELECT * FROM states \
        WHERE name LIKE BINARY '%{}' ORDER BY id ASC".format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
