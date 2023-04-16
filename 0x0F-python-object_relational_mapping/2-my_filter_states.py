#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table where name matches the argument
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
    search_arg = sys.argv[4]
    query = """SELECT * FROM states WHERE name == '{:s}' ORDER BY id ASC""".format(search_arg)
    cur_obj.execute(query)
    row_states = cur_obj.fetchall()
    for row in row_states:
        if row[1] == search_arg
        print(row)
    cur_obj.close()
    conn_obj.close()


if __name__ == "__main__":
"0-select_states.py" 29L, 669C                                                                                        8,0-1         Top
~                                                                                                                                       
"1-filter_states.py" 30L, 836C                                                                                        23,25         All
