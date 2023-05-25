#!/usr/bin/python3
'''0-gather_data_from_an_API module'''
import json
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2:

        try:
            q = int(argv[1])
        except Exception as e:
            raise Exception

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
                    "task": k.get('title', None),
                    "completed": k.get('completed'),
                    "username": n
                    })
                d.append(i)

        with open(str(q) + '.json', 'w') as f:
            f.write(json.dumps({str(q): d}))
