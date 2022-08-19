# Homework 3
import tweepy
import os
import importlib

# Set the right directory
os.chdir("/Users/peter/Code/python_summer2022/HW")

# Set up API
twitter = importlib.import_module("start_twitter")
# Doing it this way so the LSP will show avaliable functions.
api = tweepy.API(twitter.auth, wait_on_rate_limit=True)

wustl = api.get_user(screen_name="@WUSTLPoliSci")
wustlFollowers = api.get_follower_ids(screen_name="@WUSTLPoliSci")
wustlFriends = api.get_friend_ids(screen_name="@WUSTLPoliSci")

# FOLLOWERS OF WUSTL --------------------------------------------------------
mostTweets = 0
mostFollowers = 0
first = True

for i in wustlFollowers:
    try:
        if first:
            mostFollowers = api.get_user(user_id=i)
            mostTweets = api.get_user(user_id=i)
            first = False
            pass
        user = api.get_user(user_id=i)
        # Check for most followers
        if user.followers_count > mostFollowers.followers_count:
            mostFollowers = user
            print("New Most Popular User: %s" % mostFollowers.screen_name)
        # Check for most tweets
        if user.statuses_count > mostTweets.statuses_count:
            mostTweets = user
            print("New Most Active User: %s" % mostTweets.screen_name)
    # If the above checks do not capture an error, this is here as a backup
    except tweepy.TweepyException:
        print("Skipping Twitter user due to some issue")

# Most Popular follower of WUSTLPoliSci
mostFollowers.screen_name
# 'mariapaularomo'
mostFollowers.followers_count
# 357007 Followers

# Most Active follower of WUSTLPoliSci
mostTweets.screen_name
# 'TheNjoroge'
mostTweets.statuses_count
# 171067 tweets

# FRIENDS OF WUSTL ----------------------------------------------------------
# Layman < 100
# Expert >= 100 & < 1000
# Celebrity >= 1000
friends = {}

for i in wustlFriends:

    user = api.get_user(user_id=i)

    # Test based on if the user is a layman, expert, or celebrity
    if user.followers_count < 100:
        try:
            if user.statuses_count > friends["layman"].statuses_count:
                friends["layman"] = user
                print("New Most Active Layman: %s" % user.screen_name)
        # If it's the first time, make them the entry in the dictionary
        except KeyError:
            friends["layman"] = user
    elif user.followers_count >= 100 and user.followers_count < 1000:
        try:
            if user.statuses_count > friends["expert"].statuses_count:
                friends["expert"] = user
                print("New Most Active Expert: %s" % user.screen_name)
        except KeyError:
            friends["expert"] = user
    else:
        try:
            if user.statuses_count > friends["celebrity"].statuses_count:
                friends["celebrity"] = user
                print("New Most Active Celebrity: %s" % user.screen_name)
        except KeyError:
            friends["celebrity"] = user

    # Find most active user
    try:
        if user.followers_count > friends["most active"].followers_count:
            friends["most popular"] = user
            print("New Most Popular Friend: %s" % user.screen_name)
    except KeyError:
        friends["most popular"] = user


# Most Popular
friends["most popular"].screen_name
# BarackObama
friends["most popular"].followers_count
# 132597681

# Most Active Layman
friends["layman"].screen_name
# usmanfalalu1
friends["layman"].statuses_count
# 1440

# Most Active Expert
friends["expert"].screen_name
# prof_nokken
friends["expert"].statuses_count
# 20362

# Most Active Celebrity
friends["celebrity"].screen_name
# nytimes
friends["celebrity"].statuses_count
# 481564

# FOLLOWERS OF FOLLOWERS ----------------------------------------------------

# FRIENDS OF FRIENDS --------------------------------------------------------

# Testing pagination, since the second part of the homework will
# probably need this
test = api.get_follower_ids(screen_name="@JoeBiden", cursor=-1)
len(test[0])
api.get_user(user_id=wustlFollowers[0]).followers_count
