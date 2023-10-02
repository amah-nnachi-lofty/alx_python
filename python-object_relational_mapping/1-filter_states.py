#!/usr/bin/python3
"""
Lists all unique states with a name starting with N (uppercase N) from
the database hbtn_0e_0_usa.

Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a database connection
    conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute SQL query to select unique states with names starting with 'N'
    cursor.execute("SELECT DISTINCT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    # Print states that match the criteria
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    conn.close()

