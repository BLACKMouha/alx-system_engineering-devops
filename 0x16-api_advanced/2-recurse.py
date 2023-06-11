#!/usr/bin/python3
'''2-recurse module'''
import requests
from sys import argv
from itertools import islice


def recurse(subreddit, hot_list=[], after=None):
    '''Queries the Reddit API and returns host posts listed for a given
    subreddit'''

    if (subreddit is None):
        print(None)
        return
    req = "https://www.reddit.com/r/{}.json?after={}&limit=24".\
        format(subreddit, after)
    v = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101"
    v += " Firefox/15.0.1"
    h = {'User-agent': v}
    res = requests.get(req, headers=h, allow_redirects=False)
    if res.status_code == 200:
        hot_posts = res.json()['data']['children']
        if (hot_posts is None):
            return None
        titles = []
        for post in hot_posts:
            titles.append(post['data']['title'])

        for title in sorted(titles):
            hot_list.append(title)

        after = res.json()['data']['after']
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
