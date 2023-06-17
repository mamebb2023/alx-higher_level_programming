#!/usr/bin/python3
# Filter states from the user's input
import MySQLdb
import sys

if __name__ == "__main__":
    fil = sys.argv[4]
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[] == sys.argv[4]]
