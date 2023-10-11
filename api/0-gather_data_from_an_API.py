"""
This script interacts with the JSONPlaceholder API to retrieve and display
a specified employee's completed tasks. It takes an employee ID as a command-
line argument and prints the total number of completed tasks along with
their titles.

Usage:
    python gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_employee_data(employee_id):
    """
    Fetch employee details from JSONPlaceholder API.

    Args:
        employee_id (str): Employee ID.

    Returns:
        dict: Employee data in JSON format.
    """
    employee_url = f"{BASE_URL}/users/{employee_id}"
    response = requests.get(employee_url)
    return response.json()

def fetch_employee_tasks(employee_id):
    """
    Fetch employee's TODO list from JSONPlaceholder API.

    Args:
        employee_id (str): Employee ID.

    Returns:
        list: TODO list data in JSON format.
    """
    todo_url = f"{BASE_URL}/users/{employee_id}/todos"
    response = requests.get(todo_url)
    return response.json()

def main():
    """
    Main function to fetch and display employee TODO list progress.
    """
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    employee_data = fetch_employee_data(employee_id)
    if 'name' not in employee_data:
        print("Employee not found.")
        sys.exit(1)

    employee_name = employee_data.get('name')
    todo_list = fetch_employee_tasks(employee_id)
    
    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_list)

    print(f"Employee {employee_name} is done with tasks "
          f"({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    main()

