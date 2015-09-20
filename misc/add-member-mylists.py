#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
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
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

"""
Add one or more usernames to a list of script owner.
"""

cred = twitter.verify_credentials()
l = len(sys.argv)

if l == 1:
    username = input("Enter the username or user ID to add to lists: ")
    targetx = input("Enter slug or ID of lists to add the user to (separate by spaces): ")
elif l == 2:
    username = sys.argv[1]
    targetx = input("Enter slug or ID of lists to add the user to (separate by spaces): ")
elif l >= 3:
    username = sys.argv[1]
    targetx = " ".join(sys.argv[2:l])


if username.isnumeric is True:
    user1 = int(username)
    user2 = str(username)
else:
    user1 = str(username)
    user2 = None

if user2 is None:
    userid = user1
else:
    try:
        u1a = twitter.show_user(user_id=user1)
        userid = u1a["screen_name"]
    except:
        userid = user2


owner = cred["screen_name"]
targets = targetx.split()
lt = len(targets)


for i in range(lt):
    if targets[i].isnumeric is True:
        target1 = int(targets[i])
        target2 = str(targets[i])
    else:
        target1 = str(targets[i])
        target2 = None
        
    if target2 is None:
        target = target1
    else:
        try:
            t1a = twitter.show_user(user_id=target1)
            target = t1a["screen_name"]
        except:
            target = target2


try:
    data = twitter.add_user_member(slug=userid, owner_screen_name=owner,
                                   screen_name=target)
except TwythonError as e:
    print(e)
    data = ""

if len(data) > 0:
    print("""{0} added to https://twitter.com{1} which now has {2} members.
    """.format(target, data['uri'], data['member_count']))
else:
    print("User not added to any lists.")
