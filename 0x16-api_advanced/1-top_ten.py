#!/usr/bin/python3
'''1-top_ten module'''
import requests
from sys import argv
from itertools import islice


def top_ten(subreddit):
    '''Queries the Reddit API and returns the first ten host posts listed
    for a given subreddit'''
    if (subreddit is None or subreddit == ''):
        print(None)
        return
    req = "https://www.reddit.com/r/{}.json".format(subreddit)
    res = requests.get(req, all_redirects=False)
    if (str(res.status_code)[0] != '2'):
        print(None)
        return
    first_ten_posts = list(islice(res.json()['data']['children'], 10))
    for k in sorted(first_ten_posts):
        print(k['data']['title'])
