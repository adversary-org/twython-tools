#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import sys
#from twython import Twython, exceptions
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    target1 = sys.argv[1]
else:
    target1 = input("User to show: ")

try:
    target = int(target1)
except:
    target = target1

if isinstance(target, str) is True:
    try:
        data = twitter.show_user(screen_name=target)
    except TwythonError as e:
        print(e)
        data =""
elif isinstance(target, int) is True:
    try:
        data = twitter.show_user(user_id=target)
    except TwythonError as e:
        print(e)
        data = ""
elif isinstance(int(target), int) is True:
    try:
        data = twitter.show_user(user_id=target)
    except TwythonError as e:
        print(e)
        data = ""

if len(data) >= 1:
    print("""
Name:     %s
About:    %s

Username: %s
User ID:  %s
Created:  %s

Tweets:   %s

Following:  %s
Followers:  %s
""" % (data["name"], data["description"], data["screen_name"], data["id_str"], data["created_at"], data["statuses_count"], data["friends_count"], data["followers_count"]))
else:
    pass
