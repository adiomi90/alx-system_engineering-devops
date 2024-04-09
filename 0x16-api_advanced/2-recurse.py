#!/usr/bin/python3
import requests

after = None


def recurse(subreddit, hot_list=[]):
    """
    Recursively retrieves the titles of the hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of the hot posts (default=[]).

    Returns:
        list: A list of titles of the hot posts from the subreddit, or None if the request fails.
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
