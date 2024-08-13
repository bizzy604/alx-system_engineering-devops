#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {'User-agent': 'MyRedditApp/0.1'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)

        if response.status_code == 200 and response.headers.get('Content-Type') == 'application/json; charset=utf-8':
            data = response.json().get('data', {}).get('children', [])
            for post in data:
                print(post.get('data', {}).get('title', ''))
        else:
            print(None)

    except Exception:
        print(None)

