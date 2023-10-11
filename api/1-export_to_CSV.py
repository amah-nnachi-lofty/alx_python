"""
A Python 3 script that uses the requests module to gather information about an employee's
TODO list progress, given the employee ID.

This script is modified to export the data to a CSV file in the following format:

"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

The file name will be `USER_ID.csv`.

Usage:

    python 1-export_to_CSV.py EMPLOYEE_ID
"""

import csv
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


def export_employee_todo_list_to_csv(employee_id: int, filename: str):
    """
    Exports the employee's TODO list to a CSV file.

    Args:
        employee_id: The employee ID.
        filename: The name of the CSV file.
    """

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        todo_items = get_employee_todo_items(employee_id)
        employee_details = get_employee_details(employee_id)

        for todo_item in todo_items:
            writer.writerow([
                employee_id,
                employee_details["name"],
                todo_item["completed"],
                todo_item["title"],
            ])


def main():
    """
    The main function.
    """

    employee_id = int(input("Enter the employee ID: "))

    filename = f"{employee_id}.csv"
    export_employee_todo_list_to_csv(employee_id, filename)

    print(f"Successfully exported employee TODO list to CSV file: {filename}")


if __name__ == "__main__":
    main()

