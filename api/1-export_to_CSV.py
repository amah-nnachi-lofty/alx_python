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

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

# Retrieve the employee ID from the command-line argument
employee_id = sys.argv[1]

# Fetch employee details using the provided employee ID
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("username")

# Verify if the employee exists; exit if not found
if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

# Fetch the employee's TODO list from the API
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

# Calculate the total number of tasks and completed tasks
total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

# Display progress information
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")

# Display titles of completed tasks
for todo in todos:
    if todo.get("completed"):
        print(f"\t{todo.get('title')}")

# Export data to CSV file
csv_filename = f'{employee_id}.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    # Write tasks to the CSV file
    for todo in todos:
        csv_writer.writerow([todo.get('id'), employee_id, employee_name,
                             todo.get("completed"), todo.get("title")])

print(f"Data exported to {csv_filename}")


