"""
A Python 3 script that uses the requests module to gather information about an employee's
TODO list progress, given the employee ID.

This script is modified to export the data to a JSON file in the following format:

{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}

The file name will be `USER_ID.json`.

Usage:

    python 2-export_to_JSON.py EMPLOYEE_ID
"""

import json
import requests


def get_employee_todo_items(employee_id: int) -> list:
    """
    Gets the TODO list items for an employee.

    Args:
        employee_id: The employee ID.

    Returns:
        A list of dictionaries, where each dictionary represents a TODO list item.
    """

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    response.raise_for_status()
    todo_items = response.json()
    return todo_items


def get_employee_details(employee_id: int) -> dict:
    """
    Gets the employee details for an employee.

    Args:
        employee_id: The employee ID.

    Returns:
        A dictionary representing the employee details.
    """

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    response.raise_for_status()
    employee_details = response.json()
    return employee_details


def export_employee_todo_list_to_json(employee_id: int, filename: str):
    """
    Exports the employee's TODO list to a JSON file.

    Args:
        employee_id: The employee ID.
        filename: The name of the JSON file.
    """

    todo_items = get_employee_todo_items(employee_id)
    employee_details = get_employee_details(employee_id)

    json_data = {
        "USER_ID": employee_id,
        "tasks": [
            {
                "task": todo_item["title"],
                "completed": todo_item["completed"],
                "username": employee_details["name"],
            }
            for todo_item in todo_items
        ],
    }

    with open(filename, "w") as f:
        json.dump(json_data, f, indent=4)


def main():
    """
    The main function.
    """

    employee_id = int(input("Enter the employee ID: "))

    filename = f"{employee_id}.json"
    export_employee_todo_list_to_json(employee_id, filename)

    print(f"Successfully exported employee TODO list to JSON file: {filename}")


if __name__ == "__main__":
    main()

