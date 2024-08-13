import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyRedditApp/0.1'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200 (OK) and Content-Type is JSON
        if response.status_code == 200 and response.headers['Content-Type'] == 'application/json; charset=utf-8':
            data = response.json()
            return data['data']['subscribers']
        
        # If not successful or not JSON, return 0
        return 0

    except Exception as e:
        # If any other error occurs, return 0
        return 0

