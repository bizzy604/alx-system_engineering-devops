#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'MyRedditApp/0.1'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    
    try:
        response = get(url, headers=user_agent, allow_redirects=False)

        if response.status_code == 200 and response.headers.get('Content-Type') == 'application/json; charset=utf-8':
            results = response.json()
            return results.get('data', {}).get('subscribers', 0)
        else:
            return 0

    except Exception:
        return 0

