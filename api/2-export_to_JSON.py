#!/usr/bin/python3
"""
2-export_to_JSON.py Script to export data from an API about an employee's TODO list progress in JSON format.

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

import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("username")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()
employee_tasks = []
for todo in todos:
    task_data = {
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": employee_name
    }
    employee_tasks.append(task_data)


output_file = f"{employee_id}.json"

with open(output_file, 'w') as json_file:
    json.dump({employee_id: employee_tasks}, json_file, indent=4)

print(f"Data exported to {output_file}")
