#!/usr/bin/python3
""" List all states form a database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states \
                ORDER BY id ASC")
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
    c.close()
    db.close()
