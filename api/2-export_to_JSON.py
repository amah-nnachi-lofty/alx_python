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

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)
    
# Extract employee ID from command line arguments
employee_id = sys.argv[1]

# Make a request to the API endpoint to get employee details
url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response_user = requests.get(url_user)
user_data = response_user.json()

# Check if the employee with the given ID exists
if not user_data:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

# Make a request to the API endpoint to get employee's TODO list
url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response_todos = requests.get(url_todos)
todos = response_todos.json()

# Create a list of TODO items with the specified format
todo_list = []
for todo in todos:
    task_data = {
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": user_data.get("username")
    }
    todo_list.append(task_data)

# Create the output dictionary with user ID as the key and a list of TODO items as the value
output_data = {employee_id: todo_list}

# Export data to JSON file
output_file_name = f"{employee_id}.json"
with open(output_file_name, "w") as json_file:
    json.dump(output_data, json_file, indent=4)

print(f"Data exported to {output_file_name} successfully.")

