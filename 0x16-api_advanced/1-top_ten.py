#!/usr/bin/python3

from requests import get


def top_ten(subreddit):
    """
    Retrieves and prints the titles of the top 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    Raises:
        None
    """

    if not subreddit or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'dtik'}
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