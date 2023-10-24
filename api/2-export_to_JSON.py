#!/usr/bin/python3
"""
3-dictionary_of_list_of_dictionaries.py Script to export TODO list data from an API about multiple employees in JSON format.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then organizes the data in the
specified format and exports it to a JSON file.

Format must be: 
{ "USER_ID": [
    {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, 
    {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, 
    ... 
]}

Args:
  None

Returns:
  None
"""

import json
import requests

# Function to normalize a string (trim spaces and ensure 20 characters)
def normalize_string(s):
    return s.strip()[:20]

# Function to export TODO list data to a JSON file
def export_to_JSON():
    # Make a request to get all users' TODO list from the API
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()

    # Prepare the data in the specified format as a dictionary
    output_data = {}
    for user in users:
        user_id = str(user["id"])
        username = normalize_string(user["username"]).lower()  # Normalize and limit to 20 characters

        tasks = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
        ).json()

        tasks_data = []
        for task in tasks:
            task_dict = {
                "username": username,
                "task": normalize_string(task["title"]).lower(),  # Normalize and limit to 20 characters
                "completed": task["completed"]
            }
            tasks_data.append(task_dict)

        output_data[user_id] = tasks_data

    # Write the data to a JSON file named todo_all_employees.json
    with open("todo_all_employees.json", "w", encoding="UTF8", newline="") as f:
        json.dump(output_data, f, indent=4, sort_keys=True)

# Entry point of the script
if __name__ == "__main__":
    # Call the export function
    export_to_JSON()

