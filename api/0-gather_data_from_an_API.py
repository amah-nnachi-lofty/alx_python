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


