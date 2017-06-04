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
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

from license import __author__
from license import __copyright__
from license import __copyrighta__
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import datetime
import math
import sys
import time
from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#creds = twitter.verify_credentials()

l = len(sys.argv)

if l >= 2:
    user = sys.argv[1]
else:
    user = input("Enter Twitter handle to get friends of: ")

suser = twitter.show_user(screen_name=user)
fnum = 200
pnum = int(math.ceil(float(suser["friends_count"]) / fnum))

pages = []
for i in range(pnum):
    pages.append("p"+str(i+1))

oldpages = []
for i in range(pnum):
    oldpages.append("p"+str(i))

p0 = { "next_cursor": -1 } # So the following exec() call doesn't fail.

for i in range(pnum):
    exec(pages[i]+" = twitter.get_friends_list(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")

friends = []

for p in range(pnum):
    try:
        exec("for i in range(fnum): friends.append("+pages[p]+"['users'][i])")
    except(IndexError):
        pass

lf = len(friends)
slf = str(lf)
ddtz = datetime.datetime.utcnow().isoformat()
ts = str(int(time.time()))
# filename = "OutputFiles/{0}-friends-{1}.txt".format(user, ts)
filename = "OutputFiles/"+user+"-friends-"+ts+".txt"

print(ddtz)
print(lf)

afile = open(filename, "ab")
afile.write(bytes("""Timestamp:  {0} UTC
Number of friends:  {1}
""".format(ddtz, slf), "utf-8"))
for x in friends:
    afile.write(bytes("""
    Name:  {0}
Username:  {1}
 User ID:  {2}
""".format(x["name"], x["screen_name"], x["id_str"]), "utf-8"))
afile.close()

print(datetime.datetime.utcnow().isoformat())
