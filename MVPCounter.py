from urllib import request
import praw
import json

# Use PRAW to create a Reddit instance
reddit = praw.Reddit(client_id='your_client_id',
                     client_secret='your_client_secret',
                     username='your_username',
                     password='your_password',
                     user_agent='your_user_agent')

# Use API-NBA to get a list of 500 NBA players
players = json.loads(request.get('#').text)

# Initialize a dictionary to store player mentions
player_mentions = {}

# Scrape comments in the NBA subreddit
subreddit = reddit.subreddit('nba')
for comment in subreddit.comments(limit=7000):
    # Split the comment into words
    words = comment.split()
    # Iterate through the words
    for word in words:
        # Check if the word is an MVP acronym
        if word == 'MVP':
            # Iterate through the players
            for player in players:
                # Check if the player's name is in the comment
                if player['first_name'] + ' ' + player['last_name'] in comment:
                    # Increment the player's mention count
                    if player['first_name'] + ' ' + player['last_name'] in player_mentions:
                        player_mentions[player['first_name'] + ' ' + player['last_name']] += 1
                    else:
                        player_mentions[player['first_name'] + ' ' + player['last_name']] = 1

# Print the player mentions
for player, mentions in player_mentions.items():
    print(f'{player}: {mentions}')