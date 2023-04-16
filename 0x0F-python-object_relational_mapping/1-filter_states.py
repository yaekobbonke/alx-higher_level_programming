#!/usr/bin/python3
"""
imported modules
"""

import MySQLdb
import sys


def state():
    conn_obj = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur_obj = conn_obj.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur_obj.execute(query)
    row = cur_obj.fetchall()
    for r in row:
        if r[1][0] == 'N':
            print(r)
    cur.close()
    conn.close()


if __name__ == "__main__":
    state()
