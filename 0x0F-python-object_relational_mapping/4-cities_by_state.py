#!/usr/bin/python3
"""
    created by Mugisha Prosper
    at Fri, 15,09,23
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 4):
        exit()
    my_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=my_user,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
