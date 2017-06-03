#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
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
# __name__ <list-slug> user1 user2 user3 etc.
#
##

from license import __author__
from license import __copyright__
from license import __license__
__version__ = "0.0.1"
from license import __bitcoin__

import math
import sys
import time
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

"""
Add one or more usernames to a list of script owner.
"""

cred = twitter.verify_credentials()
l = len(sys.argv)

if l == 1:
    username = input("Enter the ID or username to add to lists: ")
    targetx = input("Enter lists/slugs (separate by spaces): ")
elif l == 2:
    username = sys.argv[1]
    targetx = input("Enter lists/slugs (separate by spaces): ")
elif l >= 3:
    username = sys.argv[1]
    targetx = " ".join(sys.argv[2:l])

try:
    userid = int(username)
except:
    userid = str(username)


owner = cred["screen_name"]
targetz = targetx.split()
targety = []
lt = len(targetz)

for i in range(lt):
    if targetz[i].isnumeric is True:
        target1 = int(targetz[i])
        target2 = str(targetz[i])
    else:
        target1 = str(targetz[i])
        target2 = None

    if target2 is None:
        target = target1
    else:
        try:
            t1a = twitter.show_user(user_id=target1)
            target = t1a["screen_name"]
        except:
            target = target2

    targety.append(target)

dcl = []
tl = len(targety)

for i in range(tl):
    try:
        if tl < 15:
            data = twitter.add_list_member(slug=targety[i],
                                           owner_screen_name=owner,
                                           screen_name=userid)
        else:
            data = twitter.add_list_member(slug=targety[i],
                                           owner_screen_name=owner,
                                           screen_name=userid)
            time.sleep(62)
    except TwythonError as e:
        print(e)
        data = None
    if data is not None:
        dcl.append(data)
    else:
        pass


if len(dcl) > 0:
    for i in range(len(dcl)):
        print("""{0} added to https://twitter.com{1} which now has {2} members.
        """.format(userid, dcl[i]['uri'], dcl[i]['member_count']))
else:
    print("No users added to any list.")
