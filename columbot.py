#!/usr/bin/env python3
from collections import Counter
import praw
reddit = praw.Reddit('bot1')

#FOR SUBREDDIT CALLS
#subreddit = reddit.subreddit("pythonforengineers")

#GET USERNAME TO INVESTIGATE (i.e. uname2i) AND CREATE suspect INSTANCE
uname2i = input("Give me a username to investigate: ")
suspect = reddit.redditor(uname2i)

#GET NUMBER OF SUBMISSIONS/POSTS (postcounter)
postcounter = 0
submissions = suspect.submissions.new(limit=5)
for submission in submissions:
    postcounter += 1

#GET NUMBER OF COMMENTS (commentcounter)
commentcounter = 0
for comment in suspect.comments.new(limit=5):
    commentcounter += 1

#PREVIOUS COMMENT COUNTER - GETS COMMENT TEXT
#for comment in suspect.comments.new(limit=None):
#    onelinecomment = comment.body.split("\n", 1)[0][:79]
#    commentlist.append(onelinecomment)
#COMMENTLIST POST COUNT SANITY CHECK
#print(commentlist[0])
#

#GET SUSPECT COMMENT SUBREDDIT (suscomsubreds) COUNTS
suscomsubreds = []
for comment in suspect.comments.new(limit=None):
    suscomsubreds.append(comment.subreddit.display_name)
counted_subreds = Counter(suscomsubreds)
top5subreds = counted_subreds.most_common(5)
print(top5subreds)

#PRINT RESULTS
print(f"{suspect} has {suspect.link_karma} karma.")
print(f"{suspect} has {postcounter} submissions.")
print(f"{suspect} has {commentcounter} comments.")
print(f"{suspect} posts most frequently to {top5subreds}.")