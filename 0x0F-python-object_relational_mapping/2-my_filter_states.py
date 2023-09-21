#!/usr/bin/python3
"""
    created by Mugisha Prosper
    at Fri, 15,09,23
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 5):
        exit()
    my_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_item = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=my_user,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    query = ("SELECT * FROM states"
             " WHERE name COLLATE utf8mb4_bin = '{}'"
             " ORDER BY states.id ASC"
             .format(search_item))
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
