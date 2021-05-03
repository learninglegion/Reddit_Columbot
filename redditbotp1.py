#!/usr/bin/python
import praw

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("pythonforengineers")
suspect = input("Give me a username to investigate: ")

