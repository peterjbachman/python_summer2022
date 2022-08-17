# Homework 3
import tweepy
import os
import importlib
import time


# Set the right directory
os.chdir("/Users/peter/Code/python_summer2022/HW")

# Set up API
twitter = importlib.import_module("start_twitter")
api = twitter.api

wustl = api.get_user(screen_name="@WUSTLPoliSci")
wustlFollowers = api.get_follower_ids(screen_name="@WUSTLPoliSci")
mostFollowers = 0
first = True
for i in wustlFollowers:
    try:
        if first:
            mostFollowers = api.get_user(user_id=i)
            first = False
            pass
        user = api.get_user(user_id=i)
        if user.followers_count > mostFollowers.followers_count:
            mostFollowers = user
            print("New Most Popular User")
    except tweepy.errors.TooManyRequests:
        print("Waiting for rate limit to refresh")
        time.sleep(15 * 60)
        print("Starting up again")

# Most Popular follower of WUSTLPoliSci
mostFollowers.screen_name
# 'mariapaularomo'
mostFollowers.followers_count
# 357007 Followers

# Testing pagination, since the second part of the homework will
# probably need this
test = api.get_follower_ids(screen_name="@JoeBiden", cursor=-1)
len(test[0])
api.get_user(user_id=wustlFollowers[0]).followers_count
