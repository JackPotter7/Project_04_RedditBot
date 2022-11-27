## IMPORTS ##
import praw


## LOGGING INTO REDDIT ##
reddit = praw.Reddit('bot')

## GETTING URL AND SUBMISSION ##
url = 'https://www.reddit.com/r/cs40_2022fall/comments/yoc6la/rcs40_2022fall_lounge/'
submission = reddit.submission(url=url)

## USING REPLACE MORE ATTRIBUTE ## 
print('before .replace_more()')
submission.comments.replace_more(limit=None)
print('after .replace_more()')


## LOOPS THROUGH ALL COMMENTS ## 
dict = {}
num_titles = 0
titles = []
for comment in submission.comments.list():
    try:
        body = comment.body
        if comment.author == 'ArmisticeBot':
            asterisk = body.find('*')
            body = body [asterisk+1:]
            asterisk = body.find('*')
            title = body[:asterisk]
            titles.append(title)
            num_titles = titles.count(title)
            dict[title]=num_titles
    except AttributeError:
        print('Not a comment')

## PRINT FINAL RESULTS ##
print(dict)

