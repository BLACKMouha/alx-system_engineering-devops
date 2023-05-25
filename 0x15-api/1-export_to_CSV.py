#!/usr/bin/python3
'''1-export_to_CSV module'''
import csv
import requests
from sys import argv

if __name__ == '__main__':

    if len(argv) == 2:
        try:
            q = int(argv[1])
        except Exception as e:
            raise Exception
        h = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
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
                    "USER_ID": k.get('userId', None),
                    "USERNAME": n,
                    "TASK_COMPLETED_STATUS": k.get('completed', None),
                    "TASK_TITLE": k.get('title', None)
                    })
                d.append(i)

        with open('{}.csv'.format(q), 'w', newline='') as f:
            csv_writer = csv.DictWriter(f, fieldnames=h, quoting=csv.QUOTE_ALL)
            csv_writer.writerows(d)
