#!/usr/bin/env python

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
# Requirements:
#
# See Documentation/README-py2.txt
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import math
from twython import Twython, exceptions
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

user = raw_input("Enter Twitter handle to get followers of: ")
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
    try:
        exec(pages[i]+" = twitter.get_followers_list(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")
    except(exceptions.TwythonRateLimitError):
        pass

followers = []

for p in range(pnum):
    try:
        exec("for i in range(fnum): followers.append("+pages[p]+"['users'][i])")
    except(IndexError):
        pass

print(len(followers))

for x in followers:
    print("""Name:  %s
Username:  %s
""" % (x["name"], x["screen_name"]))
