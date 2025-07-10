#!/usr/bin/python3

import requests
list = []

userid = int(input("Enter the ID of the employee: "))

URL = "https://jsonplaceholder.typicode.com/todos/" 
USER = "https://jsonplaceholder.typicode.com/users/" + str(userid)

response = requests.get(URL)
names = requests.get(USER)

# Get the list of tasks and the name of the employee
todo = response.json()
datas = names.json()

name = datas.get('name')

for task in todo:
    if task['completed']:
        list.append(task['title'])

# Print the name of the employee and the completed tasks
print(f"Employee {name} is done with tasks {len(list)}/{len(todo)}")
for item in list:
    print(item)