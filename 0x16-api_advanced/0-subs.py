#!/usr/bin/python3
""" A module that returns the number of subscribers for a given subreddit """
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the given subreddit.
             Returns 0 if the subreddit is not provided or if an error occurs.
    """

    if not subreddit or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0