#!/usr/bin/python3
""" Filter states list form the user safely """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states\
        WHERE BINARY name = %s;", (sys.argv[4], ))
    [print(states) for states in c.fetchall()]
    c.close()
    db.close()
