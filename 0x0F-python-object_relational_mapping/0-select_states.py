#!/usr/bin/python3
"""imported modules"""
import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           charset="utf8")
    # Start cursor object
    cur = conn.cursor()

    # Query to excuted
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    # Print query
    for row in query_rows:
        print(row)

    # Close cursor
    cur.close()
    conn.close()
