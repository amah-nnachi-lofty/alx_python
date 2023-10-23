#!/usr/bin/python3
"""
Script to gather data from an API about an employee's TODO list progress.

This script uses the requests module to make requests to the API endpoints for
getting employee details and TODO list items. It then calculates the employee's
TODO list progress and prints it to the standard output in the following format:
Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)

where:

* EMPLOYEE_NAME: name of the employee
* NUMBER_OF_DONE_TASKS: number of completed tasks
* TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum of completed
  and non-completed tasks

Args:
  employee_id: The integer employee ID.

Returns:
  None
"""

import requests
import sys

# Check if the correct number of command line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)
    
# Extract employee ID from command line arguments
employee_id = sys.argv[1]

# Make a request to the API endpoint to get employee details
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("name")

# Check if the employee with the given ID exists
if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

# Make a request to the API endpoint to get employee's TODO list
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

# Calculate the total number of tasks and the number of completed tasks
total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

# Print employee's TODO list progress
print(
    f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t {todo.get('title')}")
