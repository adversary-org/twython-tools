#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright © Ben McGinnes, 2013-2015
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
#
# Options and notes:
#
# Usage:  
#
##

from license import __author__
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2015"
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import datetime
import os.path
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()
dd = datetime.datetime
l = len(sys.argv)

if l == 1:
    target = input("Enter slug name or ID of list: ")
elif l >= 2:
    target = sys.argv[1]

try:
    listid = int(target)
except:
    listid = target

me = cred["screen_name"]
now = dd.utcnow()

if isinstance(listid, str) is True:
    try:
        mdata = twitter.get_list_members(slug=listid, owner_screen_name=me,
                                        count=5000)
    except TwythonError as e:
        print(e)
elif isinstance(listid, int) is True:
    try:
        mdata = twitter.get_list_members(list_id=listid, owner_screen_name=me,
                                        count=5000)
    except TwythonError as e:
        print(e)

if isinstance(listid, str) is True:
    try:
        sdata = twitter.get_list_subscribers(slug=listid,
                                             owner_screen_name=me, count=5000)
    except TwythonError as e:
        print(e)
elif isinstance(listid, int) is True:
    try:
        sdata = twitter.get_list_subscribers(list_id=listid,
                                             owner_screen_name=me, count=5000)
    except TwythonError as e:
        print(e)


tstr = str(round(now.timestamp()))
path = os.path.realpath(outdir)
members = []
subscribers = []

# nf1 = "{0}/{1}-list-{2}-{3}-mem-alldata.txt".format(path, me, listid, tstr)
# nf2 = "{0}/{1}-list-{2}-{3}-mem-usernames.txt".format(path, me, listid, tstr)
# nf3 = "{0}/{1}-list-{2}-{3}-mem-summary.txt".format(path, me, listid, tstr)
# nf4 = "{0}/{1}-list-{2}-{3}-sub-alldata.txt".format(path, me, listid, tstr)
# nf5 = "{0}/{1}-list-{2}-{3}-sub-usernames.txt".format(path, me, listid, tstr)
# nf6 = "{0}/{1}-list-{2}-{3}-sub-summary.txt".format(path, me, listid, tstr)

nf1 = "{0}/{1}-list-{2}-{3}-mem-alldata.txt".format(path, me, listid, tstr)
nf2 = "{0}/{1}-list-{2}-{3}-mem-usernames.txt".format(path, me, listid, tstr)
nf3 = "{0}/{1}-list-{2}-{3}-sub-alldata.txt".format(path, me, listid, tstr)
nf4 = "{0}/{1}-list-{2}-{3}-sub-usernames.txt".format(path, me, listid, tstr)
nf5 = "{0}/{1}-list-{2}-{3}-summary.txt".format(path, me, listid, tstr)

lmd = len(mdata["users"])
lsd = len(sdata["users"])

afile = open(nf1, "w")
afile.write(now.isoformat())
afile.write("\n")
afile.write("Total number of users in list:  {0}".format(lmd))
afile.write("\n")
afile.write("\n")
for i in range(lmd):
    dstr = str(mdata["users"][i])
    afile.write(dstr)
    afile.write("\n")
    afile.write("\n")
afile.write("\n")
afile.write(now.isoformat())
afile.write("\n")
afile.write("Total number of users in list:  {0}".format(lmd))
afile.write("\n")
afile.close()

bfile = open(nf2, "w")
for i in range(lmd):
    user = mdata["users"][i]["screen_name"]
    members.append(user)
    bfile.write(user)
    bfile.write("\n")
bfile.close()

cfile = open(nf3, "w")
cfile.write(now.isoformat())
cfile.write("\n")
cfile.write("Total number of users in list:  {0}".format(lmd))
cfile.write("\n")
cfile.write("\n")
for i in range(lsd):
    dstr = str(sdata["users"][i])
    cfile.write(dstr)
    cfile.write("\n")
    cfile.write("\n")
cfile.write("\n")
cfile.write(now.isoformat())
cfile.write("\n")
cfile.write("Total number of users in list:  {0}".format(lmd))
cfile.write("\n")
cfile.close()

dfile = open(nf4, "w")
for i in range(lsd):
    user = sdata["users"][i]["screen_name"]
    subscribers.append(user)
    dfile.write(user)
    dfile.write("\n")
dfile.close()


resp = """
Data accurate as of:    {0}  UTC

Total number of members:      {1}
Total number of subscribers:  {2}

data saved to:

{3}
{4}
{5}
{6}
{7}
""".format(now.isoformat(), lmd, lsd, nf1, nf2, nf3, nf4, nf5)

efile = open(nf5, "w")
efile.write(resp)
efile.close()

print(resp)
