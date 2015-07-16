#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.3
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
__version__ = "0.0.3"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import datetime
import time
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()

l = len(sys.argv)
lt = l - 1
me = cred["screen_name"]

if l == 2:
    targets = []
    targets.append(sys.argv[1])
elif l > 2:
    targets = sys.argv[1:l]
else:
    targetx = input("User(s) to show (separate with spaces): ")
    targets = targetx.split()

for i in range(len(targets)):
    target1 = targets[i]
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
        them = data["screen_name"]
        dnow = datetime.datetime.utcnow().isoformat()
        data1 = twitter.show_friendship(source_screen_name=me,
                                        target_screen_name=them)
        data2 = twitter.show_friendship(source_screen_name=them,
                                        target_screen_name=me)

        d1 = data1["relationship"]
        d1s = d1["source"]
        d1ss = d1s["screen_name"]
        d1sfx = d1s["following"]
        if d1sfx is True:
            d1sf = "You are following {0}.".format(them)
        elif d1sfx is False:
            d1sf = "You are not following {0}.".format(them)
        else:
            d1sf = "unknown"

        d1sbx = d1s["blocking"]
        if d1sbx is True:
            d1sb = "You are blocking {0}.".format(them)
        elif d1sbx is False:
            d1sb = "You are not blocking {0}.".format(them)
        else:
            d1sb = "unknown"

        d1sdx = d1s["can_dm"]
        if d1sdx is True:
            d1sd = "You can send direct messages to {0}.".format(them)
        elif d1sdx is False:
            d1sd = "You cannot send direct messages to {0}.".format(them)
        else:
            d1sd = "unknown"

        d2 = data2["relationship"]
        d2s = d2["source"]
        d2ss = d2s["screen_name"]
        d2sfx = d2s["following"]
        if d2sfx is True:
            d2sf = "{0} is following you.".format(them)
        elif d2sfx is False:
            d2sf = "{0} is not following you".format(them)
        else:
            d2sf = "unknown"

        d2sbx = d2s["blocking"]
        if d2sbx is True:
            d2sb = "{0} is blocking you.".format(them)
        elif d2sbx is False:
            d2sb = "{0} is not blocking you.".format(them)
        else:
            d2sb = "unknown"

        d2sdx = d2s["can_dm"]
        if d2sdx is True:
            d2sd = "{0} can send direct messages to you.".format(them)
        elif d2sdx is False:
            d2sd = "{0} cannot send direct messages to you.".format(them)
        else:
            d2sd = "unknown"

        tnow = time.time()
        print("""
    Name:     {0}
    About:    {1}
    
    Username: {2}
    User ID:  {3}
    Created:  {4}
    
    Tweets:   {5}
    
    Following:  {6}
    Followers:  {7}

    {8}
    {9}

    {10}
    {11}

    {12}
    {13}
    
    Data accurate at: {14}Z (UTC)

    Current time is:  {15} UTC
                      {16} local time
    """.format(data["name"], data["description"], them, data["id_str"],
               data["created_at"], data["statuses_count"],
               data["friends_count"], data["followers_count"], d1sf, d2sf,
               d1sb, d2sb, d1sd, d2sd, dnow, time.asctime(time.gmtime(tnow)),
               time.ctime(tnow)))
    else:
        pass




