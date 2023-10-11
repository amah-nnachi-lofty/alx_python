"""
Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys

def get_employee_data(employee_id):
    """
    Get employee data from the given employee ID using JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: Employee data in JSON format.
    """
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    return response.json()

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

def gather_employee_progress(employee_id):
    """
    Display employee TODO list progress as per the given employee ID.

    Args:
        employee_id (int): The ID of the employee.
    """
    employee_data = get_employee_data(employee_id)
    todo_list = get_todo_list(employee_id)

    completed_tasks = [task for task in todo_list if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_list)

    print(f"Employee {employee_data['name']} is done with tasks "
            f"({num_completed_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_employee_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please provide a valid integer ID.")

