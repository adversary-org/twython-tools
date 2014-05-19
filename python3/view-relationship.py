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
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

l = len(sys.argv)

if l == 1:
    user1 = input("Enter username or user ID of first user: ")
    user2 = input("Enter username or user ID of second user: ")
elif l == 2:
    user1 = sys.argv[1]
    user2 = input("Enter username or user ID of second user: ")
elif l >= 3:
    user1 = sys.argv[1]
    user2 = sys.argv[2]
else:
    user1 = "benmcginnes"
    user2 = input("Enter username or user ID of second user: ")

if isinstance(user1, str) is True and isinstance(user2, str) is True:
    data1 = twitter.show_friendship(source_screen_name=user1, target_screen_name=user2)
    data2 = twitter.show_friendship(source_screen_name=user2, target_screen_name=user1)
elif isinstance(user1, str) is True and isinstance(user2, int) is True:
    data1 = twitter.show_friendship(source_screen_name=user1, target_id=user2)
    data2 = twitter.show_friendship(source_id=user2, target_screen_name=user1)
elif isinstance(user1, int) is True and isinstance(user2, str) is True:
    data1 = twitter.show_friendship(source_id=user1, target_screen_name=user2)
    data2 = twitter.show_friendship(source_screen_name=user2, target_id=user1)
elif isinstance(user1, int) is True and isinstance(user2, int) is True:
    data1 = twitter.show_friendship(source_id=user1, target_id=user2)
    data2 = twitter.show_friendship(source_id=user2, target_id=user1)
else:
    print("Something went wrong!")

d1 = data1["relationship"]
d1s = d1["source"]
d1ss = d1s["screen_name"]
su1 = twitter.show_user(screen_name=d1ss)
d1sfx = d1s["following"]
if d1sfx is True:
    d1sf = "Yes"
elif d1sfx is False:
    d1sf = "No"
else:
    d1sf = "unknown"
    
d1sbx = d1s["blocking"]
if d1sbx is True:
    d1sb = "Yes"
elif d1sbx is False:
    d1sb = "No"
else:
    d1sb = "unknown"

d1sdx = d1s["can_dm"]
if d1sdx is True:
    d1sd = "Yes"
elif d1sdx is False:
    d1sd = "No"
else:
    d1sd = "unknown"

d1t = d1["target"]
d1tf = d1t["following"]
d1ts = d1t["screen_name"]
d1tfx = d1t["following"]
if d1tfx is True:
    d1tf = "Yes"
elif d1tfx is False:
    d1tf = "No"
else:
    d1tf = "unknown"

results1 = """    Name:     %s
    About:    %s

    Source:   %s        Target:  %s
    Username: %s        User ID:  %s
    Created:  %s

    Tweets:   %s
    Following:  %s      Followers:  %s

    %s following %s:  %s
    %s following %s:  %s

    %s able to DM %s:   %s
    Is %s blocking %s:  %s
""" % (su1["name"], su1["description"], d1ss, d1ts, su1["screen_name"], su1["id_str"], su1["created_at"], su1["statuses_count"], su1["friends_count"], su1["followers_count"], d1ss, d1ts, d1sf, d1ts, d1ss, d1tf, d1ss, d1ts, d1sd, d1ss, d1ts, d1sb)


d2 = data2["relationship"]
d2s = d2["source"]
d2ss = d2s["screen_name"]
su2 = twitter.show_user(screen_name=d2ss)
d2sfx = d2s["following"]
if d2sfx is True:
    d2sf = "Yes"
elif d2sfx is False:
    d2sf = "No"
else:
    d2sf = "unknown"
    
d2sbx = d2s["blocking"]
if d2sbx is True:
    d2sb = "Yes"
elif d2sbx is False:
    d2sb = "No"
else:
    d2sb = "unknown"

d2sdx = d2s["can_dm"]
if d2sdx is True:
    d2sd = "Yes"
elif d2sdx is False:
    d2sd = "No"
else:
    d2sd = "unknown"

d2t = d2["target"]
d2tf = d2t["following"]
d2ts = d2t["screen_name"]
d2tfx = d2t["following"]
if d2tfx is True:
    d2tf = "Yes"
elif d2tfx is False:
    d2tf = "No"
else:
    d2tf = "unknown"

results2 = """    Name:     %s
    About:    %s

    Source:   %s        Target:  %s
    Username: %s        User ID:  %s
    Created:  %s

    Tweets:   %s
    Following:  %s      Followers:  %s

    %s following %s:  %s
    %s following %s:  %s

    %s able to DM %s:   %s
    Is %s blocking %s:  %s
""" % (su2["name"], su2["description"], d2ss, d2ts, su2["screen_name"], su2["id_str"], su2["created_at"], su2["statuses_count"], su2["friends_count"], su2["followers_count"], d2ss, d2ts, d2sf, d2ts, d2ss, d2tf, d2ss, d2ts, d2sd, d2ss, d2ts, d2sb)


print(results1)
print("")
print(results2)
