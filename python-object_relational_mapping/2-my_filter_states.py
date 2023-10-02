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

    # State name provided as command line argument
    state_name = sys.argv[4]

    # SQL query using format method to insert the state_name
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query
    cursor.execute(query)
    states = cursor.fetchall()

    # Display results as specified
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

