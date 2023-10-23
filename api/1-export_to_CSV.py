#!/usr/bin/python3

"""
This script fetches and displays a specified employee's completed tasks
from the JSONPlaceholder API. It takes an employee ID as a command-line
argument and prints the total number of completed tasks along with their titles.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import csv
import os
import requests
import sys

def export_to_CSV(user_id):
    """
    Fetches completed tasks of a specified employee from the JSONPlaceholder API
    and exports the data to a CSV file.

    Args:
        user_id (str): The ID of the employee.
    """
    # Get employee name using the provided user ID
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
    ).json()[0]["username"]
    
    # Fetch tasks data for the specified employee
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    # Prepare the data for CSV export
    tasks_data = []
    for task in tasks:
        tasks_data.append([
            user_id,
            employee_name,
            task["completed"],
            task["title"],
        ])

    # Export tasks data to a CSV file named as the user ID
    with open(str(user_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks_data)

def user_info(id):
    """
    Reads and displays data from the CSV file if it exists.

    Args:
        id (str): The ID of the employee.
    """
    # Check if the CSV file exists
    if not os.path.exists(str(id) + ".csv"):
        print(f"Error: File {id}.csv not found.")
        return

    # Open the CSV file for reading
    with open(str(id) + ".csv", 'r') as f:
        reader = csv.reader(f)
        # Process and display data from the CSV file
        for row in reader:
            print(", ".join(row))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_to_CSV(employee_id)
            user_info(employee_id)
        except ValueError:
            print("Error: Invalid employee ID. Please provide a valid integer.")
