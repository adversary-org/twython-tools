#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2015
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
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2015"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2015"
__license__ = "BSD"
__version__ = "0.0.2"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import datetime
import math
import sys
import time
from twython import Twython, exceptions
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#creds = twitter.verify_credentials()

l = len(sys.argv)

if l >= 2:
    user = sys.argv[1]
else:
    user = input("Enter Twitter handle to get followers of: ")

suser = twitter.show_user(screen_name=user)
fnum = 200
pnum = int(math.ceil(float(suser["followers_count"]) / fnum))

pages = []
for i in range(pnum):
    pages.append("p"+str(i+1))

oldpages = []
for i in range(pnum):
    oldpages.append("p"+str(i))

p0 = { "next_cursor": -1 } # So the following exec() call doesn't fail.

for i in range(pnum):
    exec(pages[i]+" = twitter.get_followers_list(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")
    time.sleep(64)

followers = []

for p in range(pnum):
    try:
        exec("for i in range(fnum): followers.append("+pages[p]+"['users'][i])")
    except(IndexError):
        pass

lf = len(followers)
slf = str(lf)
ddtz = datetime.datetime.utcnow().isoformat()
ts = str(int(time.time()))
filename = "OutputFiles/"+user+"-followers-"+ts+".txt"

print(ddtz)
print(lf)

afile = open(filename, "ab")
afile.write(bytes("""Timestamp:  {0} UTC
Number of followers:  {1}
""".format(ddtz, slf), "utf-8"))
for x in followers:
    afile.write(bytes("""
    Name:  {0}
Username:  {1}
 User ID:  {2}

""".format(x["name"], x["screen_name"], x["id_str"]), "utf-8"))
afile.close()

print(datetime.datetime.utcnow().isoformat())
