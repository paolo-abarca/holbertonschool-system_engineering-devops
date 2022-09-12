#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import requests
from sys import argv


if __name__ == "__main__":

    id_user = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(id_user))

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(id_user))

    EMPLOYEE_NAME = user.json().get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = len(todo.json())

    for i in range(TOTAL_NUMBER_OF_TASKS):
        if todo.json()[i].get("completed"):
            NUMBER_OF_DONE_TASKS = NUMBER_OF_DONE_TASKS + 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_NUMBER_OF_TASKS
                                                          ))
    for i in range(TOTAL_NUMBER_OF_TASKS):
        if todo.json()[i].get("completed"):
            print("\t {}".format(todo.json()[i].get("title")))
