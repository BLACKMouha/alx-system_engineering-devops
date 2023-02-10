#!/usr/bin/python3
'''Gather data from an API'''


if __name__ == '__main__':
    from sys import argv
    import requests

    try:
        '''Argument passed to the program'''
        userId = '' if not argv[1] else argv[1]

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

        numberTasks, numberTasksCompleted = len(todos), 0

        '''Computing the number of completed tasks'''
        for todo in todos:
            if todo['completed'] is True:
                numberTasksCompleted += 1

        print('Employee {} is done with tasks({}/{}):'
              .format(the_user['name'], numberTasksCompleted, numberTasks))

        for todo in todos:
            if todo['completed'] is True:
                print('\t {}'.format(todo['title']))

    except Exception:
        raise
