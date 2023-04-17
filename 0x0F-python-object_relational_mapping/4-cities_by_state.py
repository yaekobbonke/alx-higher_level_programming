#!/usr/bin/python3
"""
 a script that lists all cities
 from the database hbtn_0e_4_usa
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
    query = """SELECT  cities.id, cities.name, states.name
                FROM cities INNER JOIN states ON cities.state_id=states.id"""
    cur_obj.execute(query)
    row = cur_obj.fetchall()
    for r in row:
        print(r)
    cur_obj.close()
    conn_obj.close()


if __name__ == "__main__":
    state()
