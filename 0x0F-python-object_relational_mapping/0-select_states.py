#!/usr/bin/python3
"""
Imported modules
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
    query = "SELECT id,name FROM states ORDER by id ASC"
    cur_obj.execute(query)
    row = cur_obj.fetchall()
    for row in row:
        print(row)
    cur_obj.close()
    conn_obj.close()


if __name__ == "__main__":
    state()
