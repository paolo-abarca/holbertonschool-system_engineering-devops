#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == "__main__":

    id_user = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(id_user))

    todo = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(id_user))

    USERNAME = user.json().get("username")
    TOTAL_NUMBER_OF_TASKS = len(todo.json())
    list_task = []
    dict_task = {}

    for i in range(TOTAL_NUMBER_OF_TASKS):
        dict_task = {"task": todo.json()[i].get("title"),
                     "completed": todo.json()[i].get("completed"),
                     "username": USERNAME}

        list_task.append(dict_task)

    dict_task = {id_user: list_task}

    filename = id_user + ".json"
    with open(filename, mode="w", encoding="utf-8")as myFile:
        json.dump(dict_task, myFile)
