#!/usr/bin/python3
""" Lists all cities of that state, using the database
  hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    c = db.cursor()
    c.execute("SELECT cities.name\
        FROM cities\
        JOIN states\
        ON cities.state_id=states.id\
        WHERE BINARY states.name = %s\
        ORDER BY cities.id ASC;", (sys.argv[4], ))
    rows = c.fetchall()
    cities_list = []
    for row in rows:
        cities_list.append(row[0])
    print(", ".join(cities_list))
    c.close()
    db.close()
