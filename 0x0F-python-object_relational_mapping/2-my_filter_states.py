#!/usr/bin/python3
"""
a script that takes in an argument and displas
all values in the states table
where name matches the argument
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
    query = """SELECT * FROM states where name = '{:s}'
            ORDER by id ASC""".format(search)
    cur_obj.execute(query)
    row = cur_obj.fetchall()
    for r in row:
        if r[1] == search:
            print(r)
    cur_obj.close()
    conn_db.close()


if __name__ == "__main__":
    state()
