# MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

# Register an app: https://dev.twitter.com/

# pip install tweepy
import tweepy

# Check the documentation page
# http://docs.tweepy.org/en/v3.2.0/

# Get access to API
# Copy/paste your keys here, move file out of github repo, import keys to public
# files.
auth = tweepy.OAuthHandler('aFhRPsV0AGvcpSCkkeSW6rx3k',
                           'ma9hCiW2YEizmXHoPEayfdncE7V0wxk50dPgo3UNlmZa1Fx7bw')
auth.set_access_token('1259646171665948673-thfO5qvXIE6SCJ0fO8BtqQcz5OYok5',
                      'jcVlW2VhGeCiIc5HLR2N0xUHIAIvB4UzhLer1A9F1B1Fb')
client = tweepy.API(auth)

# 3KdBTYPvIRiKEe7ekLyxIaaBl # API Key
# JX2dpQsj53EZZjk4KsmDYrVG2Twduy7y6oPMyG7hJXp3EhFipG # API Secret
# AAAAAAAAAAAAAAAAAAAAACT9fwEAAAAAWJiIw%2FUpkw7r5XSnKQ335MBbHX0%3DLhdo0aiaI21OKKTFC5qRsUI5rKU3bSpin5OX5RhTH93PTJHsU6 # Bearer Token
