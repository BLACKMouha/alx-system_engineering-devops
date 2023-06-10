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
    v = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101"
    v += "Firefox/15.0.1"
    h = {'User-agent': v}
    res = requests.get(req, headers=h, allow_redirects=False)
    if (str(res.status_code)[0] == '4'):
        return 0
    return ((res.json()['data']['subscribers']))
