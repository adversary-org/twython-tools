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
# 
#
#
# Requirements:
#
# * Python 3.4 or later.
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
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

"""
Add one or more usernames to a list of script owner.
"""

cred = twitter.verify_credentials()
l = len(sys.argv)

if l == 1:
    listname = input("Enter the ID or name (slug) of the list: ")
    targetx = input("Enter usernames or IDs to add (separate by spaces): ")
elif l == 2:
    listname = sys.argv[1]
    targetx = input("Enter usernames or IDs to add (separate by spaces): ")
elif l >= 3:
    listname = sys.argv[1]
    targetx = " ".join(sys.argv[2:l])

try:
    listid = int(listname)
except:
    listid = str(listname)


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

datachecklist = []

if lt == 1:
    try:
        data = twitter.add_list_member(slug=listid, owner_screen_name=owner,
                                       screen_name=target)
    except TwythonError as e:
        print(e)
        data = None
    if data is not None:
        datacheck = True
    else:
        datacheck = False
elif lt >= 2 and lt <= 100:
    targets = ", ".join(targety)
    try:
        data = twitter.create_list_members(slug=listid,
                                           owner_screen_name=owner,
                                           user_id=targets)
    except TwythonError as e:
        print(e)
        data = None
    if data is not None:
        datacheck = True
    else:
        datacheck = False
elif lt > 100:
    t0 = lt / 100
    t1 = math.floor(t0)
    t2 = t1 * 100
    t3 = lt - t2
    for i in range(t1):
        targets = ", ".join(targety[(i * 100):((i + 1) * 100)])
        try:
            data = twitter.create_list_members(slug=listid,
                                               owner_screen_name=owner,
                                               user_id=targets)
        except TwythonError as e:
            print(e)
            data = None
        if data is not None:
            datachecklist.append(targets)
        else:
            pass
    for i in range(t2, t3):
        targets = ", ".join(targety[(i * 100):((i + 1) * 100)])
        try:
            data = twitter.create_list_members(slug=listid,
                                               owner_screen_name=owner,
                                               user_id=targets)
        except TwythonError as e:
            print(e)
            data = None
        if data is not None:
            datachecklist.append(targets)
        else:
            pass
    if len(datachecklist) > 0:
        datacheck = True
    else:
        datacheck = False


targeted = ", ".join(targety)

if datacheck is True:
    print("""{0} added to https://twitter.com{1} which now has {2} members.
    """.format(targeted, data['uri'], data['member_count']))
else:
    print("No users added to any list.")
