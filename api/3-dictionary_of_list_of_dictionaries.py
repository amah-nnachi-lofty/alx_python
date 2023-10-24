#!/usr/bin/python3
"""
Python script to export data in the JSON format
"""

import json
import requests
import sys

def get_all_employees_data():
    """
    Get data for all employees from JSONPlaceholder API.

    Returns:
        dict: Data for all employees in JSON format.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees_data = response.json()
    all_employees_data = {}

    for employee in employees_data:
        user_id = employee['id']
        username = employee['username']
        todo_list = get_todo_list(user_id)
        employee_tasks = []
        for task in todo_list:
            task_data = {
                "username": username,
                "task": task["title"],
                "completed": task["completed"]
            }
            employee_tasks.append(task_data)
        all_employees_data[user_id] = employee_tasks

    return all_employees_data

def get_todo_list(employee_id):
    """
    Get TODO list data for the given employee ID using JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        list: TODO list data in JSON format.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    return response.json()

def export_to_json(data):
    """
    Export employee TODO list data to a JSON file.

    Args:
        data (dict): Employee data in JSON format.
    """
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Data exported to todo_all_employees.json")

if __name__ == "__main__":
    employees_data = get_all_employees_data()
    export_to_json(employees_data)

