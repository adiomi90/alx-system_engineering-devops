import praw

# Initialize the Reddit API
reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT')

def count_words(subreddit, word_list, posts=None, counts=None):
    if posts is None:
        try:
            # Fetch hot articles from the specified subreddit
            posts = reddit.subreddit(subreddit).hot(limit=100)
        except Exception as e:
            print(f"An error occurred: {e}")
            return

    if counts is None:
        counts = {}

    try:
        post = next(posts)
    except StopIteration:
        # No more posts to process
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word.lower()}: {count}")
        return

    # Recursive call to process the next post
    count_words(subreddit, word_list, posts, update_counts(post, word_list, counts))

def update_counts(post, word_list, counts):
    title = post.title.lower()
    for word in word_list:
        if word.lower() in title:
            if word.lower() in counts:
                counts[word.lower()] += title.count(word.lower())
            else:
                counts[word.lower()] = title.count(word.lower())
    return counts

# Example usage:
count_words("python", ["python", "javascript", "java"])
