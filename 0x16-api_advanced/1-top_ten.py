#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of
the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles
    of the first 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {"User-Agent": "Zenkaizer:0x16_api_advanced"}

    data = requests.get(url, headers=headers, allow_redirects=False)

    if data.status_code == 404:
        print("None")

    for result in data.json().get("data").get("children"):
        print("{}".format(result.get("data").get("title")))
