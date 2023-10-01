#!/usr/bin/python3
"""
Lists all cities of a specific state from the database hbtn_0e_4_usa.

Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>

Parameterized query is used to prevent SQL injection. The state_name is passed as a parameter in the execute() method.
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

    # Execute SQL query to select cities of the specified state
    query = """SELECT cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    # Execute the query with state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # Extract city names from the result set
    city_names = [city[0] for city in cities]

    # Print cities of the specified state as a comma-separated string
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    conn.close()

