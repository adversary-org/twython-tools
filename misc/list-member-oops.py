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

l = len(sys.argv)

if l == 1:
    listname = input("Enter the ID or name (slug) of the list: ")
    ownerid = input("Enter the screen name of the list owner: ")
    targetx = input("Enter username or user ID of user to add: ")
    targets = []
    targets.append(targetx)
elif l == 2:
    listname = sys.argv[1]
    ownerid = input("Enter the screen name of the list owner: ")
    targetx = input("Enter username or user ID of user to add: ")
    targets = []
    targets.append(targetx)
elif l == 3:
    listname = sys.argv[1]
    ownerid = sys.argv[2]
    targetx = input("Enter username or user ID of user to add: ")
    targets = []
    targets.append(targetx)
elif l == 4:
    listname = sys.argv[1]
    ownerid = sys.argv[2]
    targetx = sys.argv[3]
    targets = []
    targets.append(targetx)
elif l >= 5:
    listname = sys.argv[1]
    ownerid = sys.argv[2]
    targets = sys.argv[3:l]
else:
    listname = input("Enter the ID or name (slug) of the list: ")
    ownerid = input("Enter the screen name of the list owner: ")
    targetx = input("Enter username or user ID of user to add: ")
    targets = []
    targets.append(targetx)

lt = len(targets)

try:
    listid = int(listname)
except:
    listid = listname

if isinstance(listid, str) is True:
    if len(ownerid) >= 1:
        owner = ownerid
    else:
        owner = input("Enter the screen name of the list owner: ")
elif isinstance(listid, int) is True:
    owner = ownerid
    

if lt < 1:
    target = None
elif lt == 1:
    target = targets[0]
else:
    for i in range(lt):
        target1 = targets[i]
        try:
            target2 = int(target1)
            data = twitter.show_user(user_id=target2)
            target = data["screen_name"]
        except:
            target = target1
        if isinstance(listid, int) is True:
            twitter.add_list_member(list_id=listid, screen_name=target)
        else:
            if isinstance(owner, 

    
