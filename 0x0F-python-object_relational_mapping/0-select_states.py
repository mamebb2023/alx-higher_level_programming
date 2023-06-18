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
    c.execute("SELECT * FROM states ORDER BY id ASC")
    [print(row) for row in c.fetchall()]
    c.close()
    db.close()
