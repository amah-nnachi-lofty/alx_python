#!/usr/bin/python3
"""
Script to export data from an API about an employee's TODO list progress in CSV format.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then calculates the employee's
TODO list progress and exports it to a CSV file in the specified format.

Format must be: 
"USER_ID","EMPLOYEE_NAME","TASK_TITLE","TASK_COMPLETED_STATUS"

Args:
  employee_id: The integer employee ID.

Returns:
  None
"""

import csv
import requests
import sys

def export_to_CSV(employee_id, todos):
    """
    Export employee's TODO list progress to a CSV file.

    Args:
        employee_id (int): The ID of the employee.
        todos (list): List of employee's TODO tasks.
    """
    with open(f"{employee_id}.csv", "w", newline="", encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "EMPLOYEE_NAME", "TASK_TITLE", "TASK_COMPLETED_STATUS"])

        employee_name = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json().get("name")

        for todo in todos:
            task_title = todo.get("title")
            completed_status = str(todo.get("completed"))
            csv_writer.writerow([employee_id, employee_name, task_title, completed_status])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print(f"No tasks found for employee ID {employee_id}")
    else:
        export_to_CSV(employee_id, todos)
        print(f"Data exported to {employee_id}.csv successfully.")
