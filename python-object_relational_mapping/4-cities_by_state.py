#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract command-line arguments
    username, password, database = sys.argv[1:]

    # Establish a database connection
    conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute SQL query to select cities with state names
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""

    # Execute the query
    cursor.execute(query)

    # Fetch all results
    cities = cursor.fetchall()

    # Print cities with state names
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    conn.close()

