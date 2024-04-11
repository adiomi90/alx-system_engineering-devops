#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
            Returns 0 if the subreddit is not provided or is not a string.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome  Version 123.0.6312.122'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = get(url, headers=user_agent, allow_redirects=False)
    results = response.json()

    if (response.status_code == requests.codes.ok):
        return result.get('data').get('subscribers')
    return 0
