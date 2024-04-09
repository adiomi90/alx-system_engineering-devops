#!/usr/bin/python3
""" A module that returns a list of titles of hot articles for a subreddit """
import requests
import json

after = None


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns the top ten post titles recursively.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the top post titles. Defaults to an empty list.

    Returns:
        list: A list of the top ten post titles from the subreddit.

    """
    global after
    user_agent = {'User-Agent': 'dtik'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    response = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)

    if response.status_code == 200:
        result = response.json().get("data").get("after")
        if not result:
            after = result
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title in all_titles:
            hot_list.append(title.get("data").get("title"))
        return hot_list
    else:
        return None
