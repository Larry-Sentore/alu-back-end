#!/usr/bin/python3
"""
Fetch and display an employee's TODO progress from JSONPlaceholder.

Usage: ./0-gather_data_from_an_API.py <EMPLOYEE_ID>
"""

import sys
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def main():
    """Entry point when run as a script."""
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <EMPLOYEE_ID>".format(sys.argv[0]))
        sys.exit(1)

    emp_id = int(sys.argv[1])

    # 1. Get employee name
    user_resp = requests.get("{}/users/{}".format(BASE_URL, emp_id))
    if user_resp.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    employee_name = user_resp.json().get("name")

    # 2. Get todos
    todos_resp = requests.get("{}/todos".format(BASE_URL),
                              params={"userId": emp_id})
    todos = todos_resp.json()

    # 3. Completed tasks
    completed = [t for t in todos if t.get("completed")]

    # 4. Print report
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed), len(todos)))

    for task in completed:
        # one tab + one space exactly
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
