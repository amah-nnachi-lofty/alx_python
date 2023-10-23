"""
This script fetches and displays a specified employee's completed tasks
from the JSONPlaceholder API. It takes an employee ID as a command-line
argument and prints the total number of completed tasks along with their titles.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import csv
import requests
import sys


def export_to_CSV(user_id):
    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users?id={}".format(user_id)
    ).json()[0]["username"]
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    ).json()

    tasks_data = []

    for task in tasks:
        tasks_data.append(
            [
                user_id,
                employee_name,
                task["completed"],
                task["title"],
            ]
        )

    with open(str(user_id) + ".csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(tasks_data)


if __name__ == "__main__":
    export_to_CSV(sys.argv[1])