#!/usr/bin/python3
'''0-sub module'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''Queries the Reddit API and returns the number of subscribers
    for a given subreddit'''
    if (subreddit is None):
        return 0
    req = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(req)
    if (res.status_code == 404):
        return 0
    return ((res.json()['data']['subscribers']))
