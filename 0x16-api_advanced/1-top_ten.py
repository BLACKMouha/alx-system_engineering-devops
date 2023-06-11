#!/usr/bin/python3
'''1-top_ten module'''
import requests
from sys import argv
from itertools import islice


def top_ten(subreddit):
    '''Queries the Reddit API and returns the first ten host posts listed
    for a given subreddit'''
    if (subreddit is None):
        print(None)
        return
    req = "https://www.reddit.com/r/{}.json".format(subreddit)
    v = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101"
    v += " Firefox/15.0.1"
    h = {'User-agent': v}
    res = requests.get(req, headers=h, allow_redirects=False)
    if res.status_code == 200:
        first_ten_posts = list(islice(res.json()['data']['children'], 10))
        if (first_ten_posts is None):
            print(None)
            return
        titles = []
        for k in first_ten_posts:
            titles.append(k['data']['title'])
        for title in sorted(titles):
            print(title)
    else:
        print(None)
        return
