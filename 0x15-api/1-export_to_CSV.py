#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
"""
import csv
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
    filename = id_user + ".csv"

    with open(filename, mode="w", encoding="utf-8")as myFile:
        for i in range(TOTAL_NUMBER_OF_TASKS):
            myFile.write('"{}","{}","{}","{}"\n'
                         .format(id_user,
                                 USERNAME,
                                 todo.json()[i].get("completed"),
                                 todo.json()[i].get("title")))
