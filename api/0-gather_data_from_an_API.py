<<<<<<< HEAD
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
=======
"""
This script interacts with the JSONPlaceholder API to retrieve and display
a specified employee's completed tasks. It takes an employee ID as a command-
line argument and prints the total number of completed tasks along with
their titles.

Usage:
    python gather_data_from_an_API.py <employee_id>
>>>>>>> 2a1201c79a65b7c03ea11fdcc03fdc2c07d01a6f
"""

import requests
import sys

<<<<<<< HEAD
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
=======
# Base URL for the JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"
# Retrieve employee ID from command-line argument
EMPLOYEE_ID = sys.argv[1]

# Fetch employee details using the provided employee ID
EMPLOYEE_URL = f"{BASE_URL}/users/{EMPLOYEE_ID}"
EMPLOYEE_RESPONSE = requests.get(EMPLOYEE_URL)
EMPLOYEE_DATA = EMPLOYEE_RESPONSE.json()

# Check if the employee exists
if 'name' not in EMPLOYEE_DATA:
    print("Employee not found.")
    sys.exit(1)

# Extract employee name from the retrieved data
EMPLOYEE_NAME = EMPLOYEE_DATA.get('name')

# Fetch the TODO list for the specified employee
TODO_URL = f"{BASE_URL}/users/{EMPLOYEE_ID}/todos"
TODO_RESPONSE = requests.get(TODO_URL)
TODO_DATA = TODO_RESPONSE.json()

# Calculate the total number of tasks and completed tasks
TOTAL_TASKS = len(TODO_DATA)
COMPLETED_TASKS = sum(1 for task in TODO_DATA if task.get("completed"))

# Display progress information
print(f"Employee {EMPLOYEE_NAME} is done with tasks({COMPLETED_TASKS}/{TOTAL_TASKS}):")

# Display titles of completed tasks
for task in TODO_DATA:
    if task.get("completed"):
        formatted_task_title = f"\t{task.get('title')}"
        print(formatted_task_title)


>>>>>>> 2a1201c79a65b7c03ea11fdcc03fdc2c07d01a6f
