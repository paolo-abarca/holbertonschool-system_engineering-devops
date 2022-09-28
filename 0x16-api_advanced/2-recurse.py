#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given
    subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)

    headers = {"User-Agent": "Zenkaizer:0x16_api_advanced"}

    if after is not None:
        data = requests.get(url, headers=headers, allow_redirects=False)

        if data.status_code == 404:
            return None

        for result in data.json().get("data").get("children"):
            hot_list.append(result.get("data").get("title"))

        after = data.json().get("data").get("after")
        recurse(subreddit, hot_list, after)

    return hot_list
