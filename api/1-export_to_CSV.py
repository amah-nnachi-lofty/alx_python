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

if __name__ == "__main__":

    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    # Details of the employer
    employee_url = "{}/users/{}".format(base_url, employee_id)
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if 'name' not in employee_data:
        print("Employee not found.")
        sys.exit(1)

    employee_username = employee_data.get('username')

    # Employee TODO list and status of progress
    todo_url = "{}/users/{}/todos".format(base_url, employee_id)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # computation of tasks
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get("completed"))

    # Print taks level
    print("Employee {} is done with tasks({}/{}):".format(employee_username,
                                                          completed_tasks, total_tasks))

    # show completed task titles
    for task in todo_data:
        if task.get("completed"):
            formatted_task_title = "\t {}".format(task.get("title"))
            print(formatted_task_title)

    # Write tasks to the CSV file
    file_name = '{}.csv'.format(employee_id)
    with open(file_name, mode='w', newline='',) as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_ALL)

        # Ensure the CSV file exists or create a new one
        #  header = ['Task ID', 'Employee ID', 'Employee Name', 'Completed', 'Task Title']

        # writing to each rows of the csv file 
        for task in todo_data:
            csv_writer.writerow([employee_id, employee_username,
                                task['completed'], task['title']])
