#!/usr/bin/env python3

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD and/or Apache 2.0
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
##

from license import __author__
from license import __copyright__
from license import __copyrighta__
__license__ = "BSD, Apache 2.0"
__version__ = "0.0.1"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

"""
Remove one username to a list.
"""

l = len(sys.argv)

if l == 2:
    listname = sys.argv[1]
    ownerid = input("Enter the screen name of the list owner: ")
    targetx = input("Enter username or user ID of user to remove: ")
    targets = []
    targets.append(targetx)
elif l == 3:
    listname = sys.argv[1]
    ownerid = sys.argv[2]
    targetx = input("Enter username or user ID of user to remove: ")
    targets = []
    targets.append(targetx)
elif l >= 4:
    listname = sys.argv[1]
    ownerid = sys.argv[2]
    targetx = sys.argv[3]
    targets = []
    targets.append(targetx)
else:
    listname = input("Enter the ID or name (slug) of the list: ")
    ownerid = input("Enter the screen name of the list owner: ")
    targetx = input("Enter username or user ID of user to remove: ")
    targets = []
    targets.append(targetx)

try:
    listid = int(listname)
except:
    listid = str(listname)

try:
    owner0 = int(ownerid)
    owner1 = twitter.show_user(user_id=owner0)
    owner = owner1["screen_name"]
except:
    if len(ownerid.strip()) == 0:
        owner0 = input("Enter the screen name of the list owner: ")
        owner1 = owner0.strip()
    elif len(ownerid.strip()) > 0:
        owner = ownerid.strip()

try:
    target1 = int(targets[0])
    target2 = str(targets[0])
except:
    target1 = str(targets[0])
    target2 = None

if target2 is None:
    target = target1
else:
    t0 = twitter.show_user(user_id=target1)
    t1 = t0["screen_name"]
    t2 = target2
    tquery = input("Did you intend to remove {0} or {1} to the {2} list: ".
                   format(t1, t2, listid))
    if tquery == t1:
        target = t1
    elif tquery == t2:
        target = t2

try:
    data = twitter.delete_list_member(slug=listid, owner_screen_name=owner,
                                   screen_name=target)
except TwythonError as e:
    print(e)
    data = ""

if len(data) > 0:
    print("""{0} removed from https://twitter.com{1} which now has {2} members.
    """.format(target, data['uri'], data['member_count']))
else:
    print("No user removed from any list.")
