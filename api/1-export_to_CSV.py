"""
This script fetches and displays a specified employee's completed tasks
from the JSONPlaceholder API. It takes an employee ID as a command-line
argument and prints the total number of completed tasks along with their titles.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import csv
import requests
import sys
import os

def user_info(employee_id):
    """
    Fetches employee's completed tasks and exports the data to CSV.

    Args:
        employee_id (str): Employee ID.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print(f"No data available for employee with ID {employee_id}")
        return
    
    # Ensure the CSV file exists or create a new one
    csv_filename = f'{employee_id}.csv'
    header = ['Task ID', 'Employee ID', 'Employee Name', 'Completed', 'Task Title']
    file_exists = os.path.exists(csv_filename)
    with open(csv_filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        # Write header only if the file is newly created
        if not file_exists:
            csv_writer.writerow(header)

        # Write tasks to the CSV file
        for todo in todos:
            csv_writer.writerow([todo.get('id'), employee_id, todo.get("userId"), todo.get("completed"), todo.get("title")])

    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        user_info(employee_id)


