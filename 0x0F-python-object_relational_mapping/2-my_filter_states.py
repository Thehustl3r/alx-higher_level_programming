#!/usr/bin/python3
import MySQLdb
import sys
"""
    created by Mugisha Prosper
    at Fri, 15,09,23
"""


if __name__ == "__main__":
    if (len(sys.argv) < 5):
        exit()
    my_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    query = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=my_user,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name= %s", (query,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
