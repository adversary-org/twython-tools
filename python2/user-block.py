#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

target = raw_input("User to block: ")

twitter.create_block(screen_name=target)
