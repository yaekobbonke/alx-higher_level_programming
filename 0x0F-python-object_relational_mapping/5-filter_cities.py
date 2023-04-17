#!/usr/bin/python3
"""
 takes in the name of a state as an argument
 and lists all cities of that state, using the
database hbtn_0e_4_usa
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
    name_of_state = sys.argv[4]
    cur_obj = conn_db.cursor()
    cur_obj.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (name_of_state,))
    row = cur_obj.fetchall()
    re = ""
    for r in row:
        re += r[0] + ", "
    print(re[0:-2:])
    cur_obj.close()
    conn_db.close()


if __name__ == "__main__":
    state()
