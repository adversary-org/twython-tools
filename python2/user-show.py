#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

from twython import Twython, exceptions
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

target = raw_input("User to show: ")

try:
    data = twitter.show_user(screen_name=target)
    print("""
Name:     %s

Username: %s
User ID:  %s
Created:  %s

Tweets:   %s

Following:  %s
Followers:  %s
""" % (data["name"], data["screen_name"], data["id_str"], data["created_at"], data["statuses_count"], data["friends_count"], data["followers_count"]))
except(exceptions.TwythonError):
    print("User "+target+" does not exist.")
