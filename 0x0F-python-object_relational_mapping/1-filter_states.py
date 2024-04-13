#!/usr/bin/python3
"""Filter states Module"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY
                    states.id ASC""", )
    rows = cursor.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    db.close()
