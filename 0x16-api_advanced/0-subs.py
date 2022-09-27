#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
for a given subreddit. If an invalid subreddit is given,
the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {"User-Agent": "Zenkaizer:0x16_api_advanced"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.status_code == 404:
        return 0

    result = data.json().get("data").get("subscribers")

    return result
