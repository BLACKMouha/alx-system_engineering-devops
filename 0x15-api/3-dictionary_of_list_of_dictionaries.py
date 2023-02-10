#!/usr/bin/python3
'''Gather data from an API'''


if __name__ == '__main__':
    from sys import argv
    import requests
    import json

    try:
        '''URLs'''
        todos_url = 'https://jsonplaceholder.typicode.com/todos/'
        users_url = 'https://jsonplaceholder.typicode.com/users/'

        '''Responses'''
        todos_res = requests.get(todos_url)
        users_res = requests.get(users_url)

        '''Data'''
        all_users = users_res.json()
        all_todos = todos_res.json()

        all_todos_users = dict()
        for user in all_users:
            list_todos_by_user = list()
            for todo in all_todos:
                dict_todos_user = dict()
                if todo['userId'] == user['id']:
                    dict_todos_user['username'] = user['username']
                    dict_todos_user['task'] = todo['title']
                    dict_todos_user['completed'] = todo['completed']
                    list_todos_by_user.append(dict_todos_user)
                    del todo
            all_todos_users.update({user['id']: list_todos_by_user})

        with open('todo_all_employees.json', 'w') as f:
            json.dump(all_todos_users, f)

    except Exception:
        raise
