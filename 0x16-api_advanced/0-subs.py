#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of 
subscribers (not active users, total subscribers) for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com//r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "aUserAgent"}
    response = requests.get(url, headers=headers)
    if response:
        dict = response.json()
        for key, value in dict.items():
            if key == "data":
                for i, j in value.items():
                    if i == "subscribers":
                        return j
    return 0
