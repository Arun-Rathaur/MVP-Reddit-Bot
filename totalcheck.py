import praw

def create_reddit_instance():
    # Use PRAW to create a Reddit instance
    reddit = praw.Reddit(client_id='your_client_id',
                         client_secret='your_client_secret',
                         username='your_username',
                         password='your_password',
                         user_agent='your_user_agent')
    return reddit

def check_post_for_mvp(post, reddit_instance):
    mvp_mentions = 0
    # Check the post title for MVP
    if 'MVP' in post.title:
        mvp_mentions += 1
        # Send a message to the post author
        post.author.message('MVP mention', f'You added to the MVP mention count with your post "{post.title}"')
    # Check the post content for MVP
    if 'MVP' in post.selftext:
        mvp_mentions += 1
        # Send a message to the post author
        post.author.message('MVP mention', f'You added to the MVP mention count with your post "{post.title}"')
    return mvp_mentions

def check_comments_for_mvp(post, reddit_instance):
    mvp_mentions = 0
    # Check the post comments for MVP
    for comment in post.comments:
        if 'MVP' in comment.body:
            mvp_mentions += 1
            # Send a message to the comment author
            comment.author.message('MVP mention', f'You added to the MVP mention count with your comment "{comment.body}"')
    return mvp_mentions

def main():
    reddit_instance = create_reddit_instance()
    total_mvp_mentions = 0
    # Listen for new posts in the NBA subreddit
    for post in reddit_instance.subreddit('nba').new():
        total_mvp_mentions += check_post_for_mvp(post, reddit_instance)
        total_mvp_mentions += check_comments_for_mvp(post, reddit_instance)
    # Print the total number of MVP mentions
    print(f'Total MVP mentions: {total_mvp_mentions}')

if __name__ == "__main__":
    main()
