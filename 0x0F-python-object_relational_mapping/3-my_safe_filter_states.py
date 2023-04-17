#!/usr/bin/python3
"""
Once again, write a script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that
is safe from MySQL injections!
"""
import MySQLdb
import sys


def state():
    conn_db = MySQLdb.connect(
                        host="localhost",
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        charset="utf8"
                            )
    cur_obj = conn_db.cursor()
    search = sys.argv[4]
    cur_obj.execute("""SELECT id,name FROM states where name = %s
                ORDER by id ASC""", (search,))
    row = cur.fetchall()
    for r in row:
        print(r)
    cur_obj.close()
    conn_db.close()


if __name__ == "__main__":
    state()
