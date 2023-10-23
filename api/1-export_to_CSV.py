#!/usr/bin/python3
"""
Script to export data from an API about an employee's TODO list progress in JSON format.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then calculates the employee's
TODO list progress and exports it to a JSON file in the specified format.

Format must be: 
{ "USER_ID": [
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, 
    {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, 
    ... 
]}

Args:
  employee_id: The integer employee ID.

Returns:
  None
"""

import requests
import json
import sys

def export_to_JSON(employee_id, todos):
    """
    Export employee's TODO list progress to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        todos (list): List of employee's TODO tasks.
    """
    data = {str(employee_id): []}
    for todo in todos:
        task_data = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": todo.get("userId")
        }
        data[str(employee_id)].append(task_data)
    
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(data, json_file, indent=4)

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
        export_to_JSON(employee_id, todos)
        print(f"Data exported to {employee_id}.json successfully.")
