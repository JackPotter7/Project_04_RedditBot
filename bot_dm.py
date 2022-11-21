import praw
import random
import datetime
import time
import argparse

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

parser = argparse.ArgumentParser(description='Takes bot number from command line + posts to reddit')
parser.add_argument('--botname', default='')
args = parser.parse_args()
reddit = praw.Reddit('bot' + args.botname)
bot_name = 'masterfulcoolbot' + args.botname

number=0
for i in range(100):
    reddit.redditor("botreceiverofdms").message(subject="EC SPAM", message=generate_comment())
    number += 1
    print(number)
    time.sleep(5)