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

# Function to export TODO list data to a JSON file
def export_to_CSV(user_id):
    # Make a request to get employee's name from the API
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ).json()["username"]
    # Make a request to get employee's TODO list from the API
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    # Prepare the data in the specified format
    tasks_data = {str(user_id): []}

    for task in tasks:
        tasks_data[str(user_id)].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name,
            }
        )

    # Write the data to a JSON file with USER_ID.json as the filename
    with open(str(user_id) + ".json", "w", encoding="UTF8", newline="") as f:
        json.dump(tasks_data, f)

# Entry point of the script
if __name__ == "__main__":
    # Get the employee ID from the command-line argument and call the export function
    export_to_CSV(sys.argv[1])
