import praw

# Initialize the Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

def recurse(subreddit, hot_list=None):
    if hot_list is None:
        hot_list = []
    try:
        # Fetch hot articles from the specified subreddit
        subreddit_obj = reddit.subreddit(subreddit)
        hot_posts = subreddit_obj.hot(limit=100)
        # Recursively fetch titles from next pages
        hot_list.extend([post.title for post in hot_posts])
        return recurse(subreddit, hot_list)
    except Exception as e:
        # If the subreddit is invalid or no results found, return None
        print(f"An error occurred: {e}")
        return None

# Example usage:
# result = recurse("programming")
# if result is not None:
#     print(len(result))
# else:
#     print("None")
