'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
<https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/>
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.

in order to make a reply   .reply() you'll have to figure out the details 
'''

madlibs = [
    "My favorite food is [FOOD]. [FOOD2] is so [GREAT] because it tastes so [GOOD]. I prefer to [EAT] it all the time.",
    "I really [ENJOY] to play [SPORT]. [SPORT2] is so [FUN] to play. I'm very [SKILLED] and [EXCITED] to become a pro.",
    "My favorite language is [LANG]. I am still [LEARNING], but I think you greet [SOMEONE] by saying [GREETING]. Let me know if I am [WRONG].",
    "Let me tell you a story. There once was a [MAN] who liked to [ACTION]. One [DAY], he went to the [BAR] and [DIED].",
    "[JULIO] is the [BEST] player in [BASEBALL]. He is even better than [MIKETROUT] and will take your favorite pitcher [DEEP].",
    "I can't wait for the year [2023]. This is the year where I [WANT] to [GRADUATE] [COLLEGE]. It is going to be [GREAT]."
    ]

replacements = {
    'COLLEGE' : ['college', 'med school', 'preschool', 'high school'],
    'GRADUATE' : ['graduate', 'finish','complete'],
    'WANT' : ['want', 'desire', 'plan'],
    '2023' : ['2677', '26969','2023'],
    'DEEP' : ['deep','yard','out of the park'],
    'MIKETROUT':['Mike Trout', 'Aaron Judge', 'Yordan Alvarez'],
    'BASEBALL':['baseball', 'the MLB', 'the show'],
    'BEST': ['best', 'greatest','drippiest'],
    'JULIO' : ['Julio', 'JROD', '#JRODSHOW', 'Julio Rodriguez'],
    'DIED' : ['died', 'stopped eating', 'ceased to exist'],
    'BAR' :  ['bar', 'town', 'saloon'],
    'DAY' : ['day', 'morning', 'Tuesday'],
    'ACTION' : ['eat', 'frolick', 'sleep'],
    'MAN' : ['man', 'woman', 'frog'],
    'WRONG' : ['mistaken', 'wrong', 'incorrect'],
    'GREETING' : ['bounjour', 'hola', 'hashalavash'],
    'SOMEONE' : ['someone', 'another person', 'a friend', 'a stranger'],
    'LEARNING' : ['learning', 'getting better', 'improving', 'practicing'],
    'LANG' : ['Korean', 'Spanish', 'French', 'Italian'],
    'FOOD' : ['sushi', 'rice', 'pasta'],
    'FOOD2': ['Sushi','Rice','Pasta'],
    'GREAT' : ['great', 'magnificent', 'fantastic', 'wonderful'],
    'GOOD' : ['yummy', 'bountiful','tasty','good'],
    'EAT' :  ['eat','inhale','consume'],
    'SPORT' : ['baseball', 'soccer', 'ping pong'],
    'SPORT2' : ['Baseball', 'Soccer', 'Ping pong'],
    'ENJOY' : ['enjoy', 'like','love'],
    'FUN' : ['fun', 'engaging', 'pleasing'],
    'SKILLED' : ['skilled', 'skillful', 'proficient'],
    'EXCITED' : ['excited', 'stoaked', 'cannot wait'],
    'TOOL' : ['tool', 'skill'],
    'CAN_DO' : ['can do', 'is able to do', 'accomplishes', 'enables me to do', 'helps me do'],
    'LOTS'  : ['lots', 'a whole lot', 'ridiculous amounts'],
    'STUFF' : ['stuff', 'things', 'fun things'],
    'LOVE' : ['love', 'adore', 'like'],
    'EVERYONE' : ['Everyone', 'Everyone (even humanities majors)', 'Everyone, yes that means you,', 'All students', 'People everywhere', 'You'],
    'SHOULD' : ['should', 'must', 'need to'],
    'BECOME' : ['become', 'turn into', 'try to be'],
    'PROGRAMMER' : ['programmer', 'developer', 'pythonista', 'software engineer'],
    'LEARN' : ['learn', 'master', 'study'],
    }

import random
#random.choice(list)
def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''
    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

import praw
reddit = praw.Reddit('bot')

import time
import datetime

url = "https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/"
# you have to post things to this link for this class
submission = reddit.submission(url=url)


comments = submission.comments.list()
print(comments[3].author)


for i in range(1000000):
    print(datetime.datetime.now(), ': made a comment, i=',i)
    try:
        submission.reply(generate_comment())
        random_choice_reply = random.choice(comments)
        print('random author=', random_choice_reply.author)
        random_choice_reply.reply(generate_comment())
    except praw.exceptions.APIException:
        print('print sleeping for 5 seconds')
        time.sleep(5)
    except AttributeError:
        pass




