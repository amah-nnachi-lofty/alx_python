#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches the provided argument.

Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>

The script utilizes parameterized queries to ensure safety from SQL injections
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    username, password, database, state_name = sys.argv[1:]

    # Establish a database connection
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # Pass the state_name as a parameter

    # Fetch all results
    states = cursor.fetchall()

    # Print states that match the criteria
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    conn.close()
