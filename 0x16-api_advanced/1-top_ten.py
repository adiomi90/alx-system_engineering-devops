#!/usr/bin/python3
""" A module that prints titles of first 10 hot posts for a given subreddit """

from requests import get


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'My-User-Agent'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)
    results = response.json()

    try:
        data_set = results.get('data').get('children')

        for d in data_set:
            print(d.get('data').get('title'))

    except Exception:
        print("None")
