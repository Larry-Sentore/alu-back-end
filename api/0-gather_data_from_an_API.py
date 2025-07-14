#!/usr/bin/python3
import sys
import requests

def fetch_employee_todo_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee info
    user_resp = requests.get(f"{base_url}/users/{employee_id}")
    if user_resp.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return

    user = user_resp.json()
    employee_name = user.get("name")

    # Fetch TODO list for the employee
    todos_resp = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_resp.status_code != 200:
        print(f"Error: Could not fetch TODO list for employee ID {employee_id}.")
        return

    todos = todos_resp.json()
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print the progress summary
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")

    # Print titles of completed tasks with one tabulation and one space before the title
    for task in done_tasks:
        print(f"\t {task.get('title')}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        return

    fetch_employee_todo_progress(employee_id)

if __name__ == "__main__":
    main()
