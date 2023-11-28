#!/usr/bin/python3
"""
    created by Mugisha Prosper
    at Fri, 15,09,23
"""
import MySQLdb
import sys
import re


if __name__ == "__main__":
    if (len(sys.argv) < 5):
        exit()
    my_user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    orignal_string = sys.argv[4]
    pattern = r"[;]"
    free_injection = re.sub(pattern, "", orignal_string)
    db = MySQLdb.connect(host="localhost", port=3306, user=my_user,
                         passwd=password, db=db_name, charset="utf8")
    cur = db.cursor()
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = '{}'"
             .format(free_injection)
             )
    cur.execute(query)
    rows = cur.fetchall()

    i = 1
    for row in rows:
        print(row[0], end=', ' if (i < len(rows)) else '')
        i += 1
    print()
    cur.close()
    db.close()
