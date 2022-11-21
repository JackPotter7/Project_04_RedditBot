import argparse
from textblob import TextBlob
import time
import praw


parser = argparse.ArgumentParser(description='Takes bot number from command line + posts to reddit')
parser.add_argument('--botname', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.botname)
bot_name = 'masterfulcoolbot' + args.botname
submissions_ran = 0
comments_ran = 0
for submission in list(reddit.subreddit("cs40_2022fall").hot(limit=100)):
    if 'biden' in submission.title.lower():
        textblob_submission = TextBlob(submission.title)
        polarity_submission = textblob_submission.sentiment.polarity
        if polarity_submission >= 0.0:
            submission.upvote()
            print('just upvoted' + submission.title)
            submissions_ran += 1
            print('submissions ran = ', submissions_ran)
        else:
            submission.downvote()
            print('just downvoted' + submission.title)
            submissions_ran += 1
            print('submissions ran = ' , submissions_ran)
    print('before .replace_more()')
    submission.comments.replace_more(limit=None, threshold=0)
    print('after .replace_more()')
    for c in submission.comments.list():
        if 'biden' in c.body.lower():
            textblob_c = TextBlob(c.body)
            polarity_c = textblob_c.sentiment.polarity
            if polarity_c >= 0.0: 
                c.upvote()
                print('just upvoted' + c.body)
                comments_ran += 1
                print('comments ran = ', comments_ran)
            else:
                c.downvote()
                print('just downvoted' + c.body)
                comments_ran += 1
                print('comments ran = ', comments_ran)
    
                
