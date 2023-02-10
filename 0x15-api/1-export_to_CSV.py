#!/usr/bin/python3
'''Gather data from an API'''


if __name__ == '__main__':
    from sys import argv
    import requests
    import csv

    try:
        '''Argument passed to the program'''
        userId = 1 if not argv[1] else argv[1]

        '''URLs'''
        todos_url = ('https://jsonplaceholder.typicode.com/todos/?userId={}'
                     .format(userId))
        user_url = ('https://jsonplaceholder.typicode.com/users/{}'
                    .format(userId))
        '''Responses'''
        todos_res = requests.get(todos_url)
        user_res = requests.get(user_url)

        '''Data'''
        the_user = user_res.json()
        todos = todos_res.json()

        fieldnames = ['id', 'name', 'completed', 'title']
        rows = []
        for todo in todos:
            rows.append({'id': '{}'.format(the_user['id']),
                         'name': '{}'.format(the_user['username']),
                         'completed': '{}'.format(todo['completed']),
                         'title': '{}'.format(todo['title'])
                         })

        with open('{}.csv'.format(userId), 'w') as f:
            writer = csv.DictWriter(f,
                                    fieldnames=fieldnames,
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            writer.writeheader()
            writer.writerows(rows)

    except Exception:
        raise
