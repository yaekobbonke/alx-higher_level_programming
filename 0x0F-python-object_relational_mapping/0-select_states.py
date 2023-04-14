#!/usr/bin/python3
"""
Imported modules
"""
import sys
import MySQLdb


def state():
    conn = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur = conn.cursor()
    query = "SELECT id,name FROM states ORDER by id ASC"
    cur.execute(query)
    row = cur.fetchall()
    for row in row:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    state()
