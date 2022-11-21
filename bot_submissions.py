import praw
import random
import datetime
import time

reddit = praw.Reddit('bot')

choice = ['text', 'link']

number = 0
while True:
    random_choice = random.choice(choice)
    try:
        if random_choice == 'text':
            # Getting the submission from the other subreddit #
            submission = random.choice(list(reddit.subreddit('conservative').hot(limit=None)))
            # Posting to CS40 subreddit #
            reddit.subreddit("cs40_2022fall").submit(submission.title, selftext=submission.selftext)
            number += 1
            print(number)
        if random_choice == 'link':
            # Getting the submission from the other subreddit #
            submission = random.choice(list(reddit.subreddit('conservative').hot(limit=None)))
            # Posting to CS40 subreddit #
            reddit.subreddit("cs40_2022fall").submit(submission.title, url=submission.url)
            number += 1
            print(number)
    except praw.exceptions.APIException:
        print('print sleeping for 5 seconds')
        time.sleep(5)