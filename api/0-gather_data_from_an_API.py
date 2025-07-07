#!/usr/bin/python3

import requests

id = int(input("Enter the ID of the employee: "))

URL = "https://jsonplaceholder.typicode.com/todos/" + str(id)

response = requests.get(URL)

print(response.data)
