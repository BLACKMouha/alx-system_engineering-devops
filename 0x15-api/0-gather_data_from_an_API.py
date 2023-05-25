#!/usr/bin/python3
'''0-gather_data_from_an_API module'''

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        import requests
        import json

        try:
            q = int(argv[1])
        except Exception as e:
            raise Exception

        u = 'https://jsonplaceholder.typicode.com/todos/'
        r = requests.get(u)
        d = []
        td = 0
        for k in json.loads(r.text):
            if q == k.get('userId', None):
                if k.get('completed'):
                    td += 1
                d.append(k)

        u = 'https://jsonplaceholder.typicode.com/users/' + str(q)
        r = requests.get(u)
        n = json.loads(r.text).get('name', None)
        print("Employee {} is done with tasks({}/{}):".format(n, td, len(d)))
        for k in d:
            if k.get('completed', None):
                print('\t {}'.format(k.get('title', None)))
