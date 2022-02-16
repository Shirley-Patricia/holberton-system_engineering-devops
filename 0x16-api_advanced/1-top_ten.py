#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests


def top_ten(subreddit):
    url = "https://www.reddit.com//r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "aUserAgent"}
    response = requests.get(url, headers=headers)
    if response:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
