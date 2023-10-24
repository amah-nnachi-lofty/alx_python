#!/usr/bin/python3
"""
2-export_to_JSON.py Script to export an employee's TODO list progress in JSON format.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then calculates the employee's
TODO list progress and exports it to a JSON file in the specified format.

USER_ID's value type is a list of dicts: OK

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

# Function to export TODO list data to a JSON file
def export_to_JSON(user_id):
    # Make a request to get employee's name from the API
    employee_name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}"
    ).json()["username"]
    
    # Make a request to get employee's TODO list from the API
    tasks = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    ).json()

    # Prepare the data in the specified format as a list of dictionaries
    tasks_data = []
    for task in tasks:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        }
        tasks_data.append(task_dict)

    # Create a dictionary with USER_ID as key and list of dictionaries as value
    output_data = {str(user_id): tasks_data}

    # Write the data to a JSON file with USER_ID.json as the filename
    with open(f"{user_id}.json", "w", encoding="UTF8", newline="") as f:
        json.dump(output_data, f, indent=4)

# Entry point of the script
if __name__ == "__main__":
    # Get the employee ID from the command-line argument and call the export function
    export_to_JSON(sys.argv[1])

