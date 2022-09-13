#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get('{}users/'.format(url))
    dict_result = {}

    for id_user in range(1, len(users.json()) + 1):
        user = requests.get('{}users/{}'.format(url, id_user))

        todo = requests.get('{}todos?userId={}'.format(url, id_user))

        USERNAME = user.json().get("username")
        TOTAL_NUMBER_OF_TASKS = len(todo.json())
        list_task = []
        dict_task = {}

        for i in range(TOTAL_NUMBER_OF_TASKS):
            dict_task = {"username": USERNAME,
                         "task": todo.json()[i].get("title"),
                         "completed": todo.json()[i].get("completed")}

            list_task.append(dict_task)

        dict_result[id_user] = list_task

    filename = "todo_all_employees.json"
    with open(filename, mode="w", encoding="utf-8")as myFile:
        json.dump(dict_result, myFile)
