#!/usr/bin/python3
'''3-dictionary_of_list_of_dictionaries module'''
import json
import requests

if __name__ == '__main__':
    u = 'https://jsonplaceholder.typicode.com/users/'
    r = requests.get(u)
    u_ids = set()
    for k in r.json():
        u_ids.add(int(k.get('id', None)))

    for q in u_ids:
        u = 'https://jsonplaceholder.typicode.com/users/' + str(q)
        r = requests.get(u)
        n = r.json().get('username', None)

        u = 'https://jsonplaceholder.typicode.com/todos/'
        r = requests.get(u)
        d = []
        for k in r.json():
            i = {}
            if q == k.get('userId', None):
                i.update({
                    "username": n,
                    "task": k.get('title', None),
                    "completed": k.get('completed')
                    })
                d.append(i)

        with open('todo_all_employees.json', 'a') as f:
            f.write(json.dumps({str(q): d}))
