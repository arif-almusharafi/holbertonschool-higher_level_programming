#!/usr/bin/python3
"""Script that lists the states whose name matches the user input."""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()

    state = sys.argv[4]
    query = ("SELECT * FROM states WHERE name = BINARY '{}' "
             "ORDER BY id ASC").format(state)
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
