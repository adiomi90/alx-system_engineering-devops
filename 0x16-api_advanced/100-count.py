#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after="", count=[]):
    """
    Count the occurrences of words from a given word list in the titles of the hot posts of a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of words to count.
        after (str, optional): A token used for pagination. Defaults to "".
        count (list, optional): A list to store the count of each word. Defaults to [].

    Returns:
        None
    """
    if after == "":
        count = [0] * len(word_list)

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'after': after}
    user_agent = {'user-agent': 'dtik'}
    response = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(word_list)):
                for j in range(i, len(word_list)):
                    if (count[j] > count[i] or
                            (word_list[i] > word_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = word_list[i]
                        word_list[i] = word_list[j]
                        word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
        else:
            count_words(subreddit, word_list, after, count)