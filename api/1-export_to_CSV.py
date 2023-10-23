#!/usr/bin/python3
"""
Script to gather data from an API about an employee's TODO list progress.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then calculates the employee's
TODO list progress and prints it to the standard output in the following format:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

where:

* USER_ID: ID of the employee
* USERNAME: username of the employee
* TASK_COMPLETED_STATUS: True if the task is completed, False otherwise
* TASK_TITLE: title of the task

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
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        employee_name = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json().get("username")

        for todo in todos:
            task_title = todo.get("title")
            completed_status = str(todo.get("completed"))
            csv_writer.writerow([employee_id, employee_name, completed_status, task_title])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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

