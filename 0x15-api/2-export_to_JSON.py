#!/usr/bin/python3
'''Gather data from an API'''


if __name__ == '__main__':
    from sys import argv
    import requests
    import json

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

        list_todos = list()
        dict_todos_user = dict()
        for todo in todos:
            list_todos.append({'task': todo['title'],
                            'completed': todo['completed'],
                            'username': the_user['username']})
        dict_todos_user[userId] = list_todos
        with open('{}.json'.format(userId), 'w') as f:
            json.dump(dict_todos_user, f)

    except Exception:
        raise
