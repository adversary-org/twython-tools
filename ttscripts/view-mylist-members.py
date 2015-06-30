#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright © Ben McGinnes, 2013-2015
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
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2015"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

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
        data = twitter.get_list_members(slug=listid, owner_screen_name=me,
                                        count=5000)
    except TwythonError as e:
        print(e)
elif isinstance(listid, int) is True:
    try:
        data = twitter.get_list_members(list_id=listid, owner_screen_name=me,
                                        count=5000)
    except TwythonError as e:
        print(e)

tstr = str(round(now.timestamp()))
path = os.path.realpath(outdir)
members = []

nf1 = "{0}/{1}-{2}-alldata.txt".format(path, listid, tstr)
nf2 = "{0}/{1}-{2}-usernames.txt".format(path, listid, tstr)
nf3 = "{0}/{1}-{2}-summary.txt".format(path, listid, tstr)

ld = len(data["users"])

afile = open(nf1, "w")
afile.write(now.isoformat())
afile.write("\n")
afile.write("Total number of users in list:  {0}".format(ld))
afile.write("\n")
afile.write("\n")
for i in range(ld):
    dstr = str(data["users"][i])
    afile.write(dstr)
    afile.write("\n")
    afile.write("\n")
afile.write("\n")
afile.write(now.isoformat())
afile.write("\n")
afile.write("Total number of users in list:  {0}".format(ld))
afile.write("\n")
afile.close()

bfile = open(nf2, "w")
for i in range(ld):
    user = data["users"][i]["screen_name"]
    members.append(user)
    bfile.write(user)
    bfile.write("\n")
bfile.close()

resp = """
Data accurate as of:    {0} UTC
Total number of users:  {1}

Data saved to:

{2}
{3}
{4}
""".format(now.isoformat(), ld, nf1, nf2, nf3)

cfile = open(nf3, "w")
cfile.write(resp)
cfile.close()

print(resp)
