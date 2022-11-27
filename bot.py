import praw
import random
import datetime
import time
import argparse
import markovify

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "The [MARINERS] are the [BEST] team in [BASEBALL]. They will win the [WORLDSERIES] in [2023].",
    "I want the [MARINERS] to [SIGN] [MIKETROUT]. If they do, [JULIO] will be happy. The season will go [GREAT].",
    "[JERRY] needs to [SIGN] a [GREAT] [SHORTSTOP]. If they don't, they will [SUCK].",
    "The last season was [GREAT]. The [MARINERS] made the [POSTSEASON] for the first time in [YEARS]. I am [EXCITED] for when they win the [WORLDSERIES]",
    "[JULIO] is the [BEST] player in [BASEBALL]. He is even better than [MIKETROUT] and will take your favorite pitcher [DEEP].",
    "I can't wait for the year [2023]. This is the year where I [WANT] the [MARINERS] to win the [WORLDSERIES]. First, they need to [SIGN] [MIKETROUT]."
    ]

replacements = {
    'YEARS' : ['years', 'a long time', '20 years'],
    'POSTSEASON' : ['post-season', 'playoffs'],
    'SUCK' : ['suck', 'play bad', 'lose games'],
    'SHORTSTOP' : ['shortstop', 'pitcher', 'outfielder'],
    'JERRY' : ['Jerry Dipoto', 'Dipoto', 'Trader Jerry'],
    'SIGN' : ['sign', 'get', 'trade for'],
    'WORLDSERIES' : ['World Series', 'championship', 'pennant'],
    'MARINERS' : ['Mariners', 'Ms', 'Ners'],
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
    'EXCITED' : ['excited', 'stoaked', 'hyped'],
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
def generate_comment():

    madlib = random.choice(madlibs)
    for replacement in replacements.keys():
        madlib = madlib.replace('['+replacement+']', random.choice(replacements[replacement]))
    return madlib

def generate_comment_markovify(c):

    # Get raw text as string.
    with open("/Users/jackpotter/Desktop/CMC/Classes/Soph Fall/CS 40/topic_10_reddit_bot/sentences.txt") as f:
        sentences = f.read()

    # Build the models.
    text_model_JROD = markovify.Text(sentences)
    text_model_comment = markovify.Text(str(c.body))

    # Comine the models 
    model_combo = markovify.combine([ text_model_JROD, text_model_comment ], [ 1, 4 ])
    

    # Print five randomly-generated sentences
    return (model_combo.make_sentence())

# FIXME:
# connect to reddit 
# using argparse to get the bot name from the command line (extra credit)
parser = argparse.ArgumentParser(description='Takes bot number from command line + posts to reddit')
parser.add_argument('--botname', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.botname)
bot_name = 'masterfulcoolbot' + args.botname

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/yx0xm8/masterfulcoolbots_zone/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once

while True:
    try:
        # printing the current time will help make the output messages more informative
        # since things on reddit vary with time
        print()
        print('new iteration at:',datetime.datetime.now())
        print('submission.title=',submission.title)
        print('submission.url=',submission.url)

        # FIXME (task 0): get a list of all of the comments in the submission
        # HINT: this requires using the .list() and the .replace_more() functions
        print('before .replace_more()')
        submission.comments.replace_more(limit=None, threshold=0)
        print('after .replace_more()')
        all_comments = submission.comments.list()
        # HINT: 
        # we need to make sure that our code is working correctly,
        # and you should not move on from one task to the next until you are 100% sure that 
        # the previous task is working;
        # in general, the way to check if a task is working is to print out information 
        # about the results of that task, 
        # and manually inspect that information to ensure it is correct; 
        # in this specific case, you should check the length of the all_comments variable,
        # and manually ensure that the printed length is the same as the length displayed on reddit;
        # if it's not, then there are some comments that you are not correctly identifying,
        # and you need to figure out which comments those are and how to include them.
        print('len(all_comments)=',len(all_comments))

        # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
        # HINT: 
        # use a for loop to loop over each comment in all_comments,
        # and an if statement to check whether the comment is authored by you or not
        not_my_comments = []
        for c in submission.comments.list():
            if c.author != bot_name:
                not_my_comments.append(c)
                
        

        # HINT:
        # checking if this code is working is a bit more complicated than in the previous tasks;
        # reddit does not directly provide the number of comments in a submission
        # that were not gerenated by your bot,
        # but you can still check this number manually by subtracting the number
        # of comments you know you've posted from the number above;
        # you can use comments that you post manually while logged into your bot to know 
        # how many comments there should be. 
        print('len(not_my_comments)=',len(not_my_comments))

        # if the length of your all_comments and not_my_comments lists are the same,
        # then that means you have not posted any comments in the current submission;
        # (your bot may have posted comments in other submissions);
        # your bot will behave differently depending on whether it's posted a comment or not
        has_not_commented = len(not_my_comments) == len(all_comments)

        if has_not_commented:
            # FIXME (task 2)
            # if you have not made any comment in the thread, then post a top level comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # a top level comment is created when you reply to a post instead of a message
            print(datetime.datetime.now(), ': made a top level comment')
            submission.reply(generate_comment())

        else:
            # FIXME (task 3): filter the not_my_comments list to also remove comments that 
            # you've already replied to
            # HINT:
            # there are many ways to accomplish this, but my solution uses two nested for loops
            # the outer for loop loops over not_my_comments,
            # and the inner for loop loops over all the replies of the current comment from the outer loop,
            # and then an if statement checks whether the comment is authored by you or not
            comments_without_replies = []
            
            for comment in not_my_comments:
                comment_reply_author =[]
                for reply in comment.replies:
                    comment_reply_author.append(str(reply.author))
                if bot_name in comment_reply_author:
                    pass
                else:
                    comments_without_replies.append(comment)
                
                    

            # HINT:
            # this is the most difficult of the tasks,
            # and so you will have to be careful to check that this code is in fact working correctly;
            # many students struggle with getting a large number of "valid comments"
            print('len(comments_without_replies)=',len(comments_without_replies))

            # FIXME (task 4): randomly select a comment from the comments_without_replies list,
            # and reply to that comment
            #
            # HINT:
            # use the generate_comment() function to create the text,
            # and the .reply() function to post it to reddit;
            # these will not be top-level comments;
            # so they will not be replies to a post but replies to a message
            try:
                # despite not randomly replying anymore, doing this line will help me figure out if all of the comments are my comments # 
                comment_random = random.choice(comments_without_replies)
                try:
                    #comment_random.reply(generate_comment())
                    # replying to the comment with the most upvotes instead #
                    
                    most_upvotes = 0
                    for c in comments_without_replies:
                        if c.score >= most_upvotes:
                            most_upvotes = c.score
                            most_upvoted = c 
                    most_upvoted.reply(generate_comment_markovify(most_upvoted))
                    
                except praw.exceptions.APIException:
                    print('this comment is deleted, so you cannnot reply')
                    pass
            except IndexError:
                print('all are my comments')
                pass
            

        # FIXME (task 5): select a new submission for the next iteration;
        # your newly selected submission should be randomly selected from the 5 hottest submissions
        submission = random.choice(list(reddit.subreddit('cs40_2022fall').hot(limit=5)))

        # We sleep just for 1 second at the end of the while loop.
        # This doesn't avoid rate limiting
        # (since we're not sleeping for a long period of time),
        # but it does make the program's output more readable.
        time.sleep(1)
    except Exception as e:
        pass
