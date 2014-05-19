#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.verify_credentials()

user = raw_input("Enter Twitter handle to get followers of: ")
followids = twitter.get_followers_ids(screen_name=user)
for x in followids["ids"]:
    data = twitter.show_user(user_id=x)
    print(data["screen_name"])

