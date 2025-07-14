#!/usr/bin/python3
"""
Using a REST API and an EMP_ID, save info about their TODO list in a csv file
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """Fetch and print the TODO progress for *employee_id*.

    Args:
        employee_id (int): The JSONPlaceholder user ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos"

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        return

    employee_name = user_response.json().get("name")

    # Fetch all todos for that user
    todos_response = requests.get(todos_url, params={"userId": employee_id})
    todos = todos_response.json()

    # Separate completed tasks
    completed_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    # Display summary and list of completed task titles
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    fetch_employee_todo_progress(int(sys.argv[1]))
