#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a database connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # SQL query to filter states by the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = sys.argv[4]

    # Execute the query with the provided state name
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    # Display results as specified
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

