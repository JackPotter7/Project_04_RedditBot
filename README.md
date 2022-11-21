# Project_04_RedditBot

# Favorite Thread #

Here is a [link](https://old.reddit.com/r/cs40_2022fall/comments/z0h7ar/dont_give_them_what_they_want/) to my favorite thread involving my bot. Below is an image of the comments in this thread. I think this thread is funny because the original comments/submission are very formal and discuss serious topics. On the contrary, my bot's posts are very informal and use terms like "drippiest" which I think is pretty funny. Overall, I like the juxtaposition of my silly comments and the origal serious comments. 



![FavoriteThread](https://github.com/JackPotter7/Project_04_RedditBot/blob/main/favoritethread.png)


# Bot_counter.py #

Running the `bot_counter.py` file on my bot *masterfulcoolbot* yields these results: 
```
len(comments)= 1000
len(top_level_comments)= 338
len(replies)= 662
len(valid_top_level_comments)= 332
len(not_self_replies)= 659
len(valid_replies)= 655
========================================
valid_comments= 987
========================================
NOTE: the number valid_comments will be used to determine your grade
```
Note: I orignally had 1000 valid comments but something happend in my code as I was working on EC. Instead of spending the time to debug, I decided to work on more EC.

# Extra Credit

**Bot_vote.py**

I used `bot_vote.py` to upvote/downvote comments related to the candidate that my bot is supporting (Joe Biden). I ran this code on the 100 hottest submissions and all of the associated comments while using TextBlob. 

**Bot_submissions.py**

I used `bot_submissions.py` to post submissions (both text and link posts) to the class subreddit. I posted submissions mostly from the r/conservative subreddit. 

**Bot Army**

I was able to create an army of bots (masterfulcoolbot0, masterfulcoolbot1, masterfulcoolbot2, masterfulcoolbot3, masterfulcoolbot4) in addition to my main bot. All of these bots were able to run simultaneously and get at least 500 valid comments. 

**Bot_dm.py**

I used `bot_dm.py` to send randomly generated direct messages to another reddit account I created called botreceiverofdms. I sent/received over 100 messages. 

**Replying to Most Upvoted**

Within my `bot.py` file, I utlized the following code to only reply to the most upvoted comment rather than randomly replying:
```
most_upvotes = 0
for c in comments_without_replies:
    if c.score >= most_upvotes:
    most_upvotes = c.score
    most_upvoted = c 
most_upvoted.reply(generate_comment()
```

# Grading 

I completed each task in `bot.py` which should earn me 12 points. 

I also completed the github repo, posted my favorite thread, and included the candidate I am supporting (Joe Biden) which earns me 3 more points. 
