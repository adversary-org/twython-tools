#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright © Ben McGinnes, 2013-2017
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
from license import __copyright__
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import datetime
import math
import os.path
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()
dd = datetime.datetime

l = len(sys.argv)

if l >= 2:
    user = sys.argv[1]
else:
    user = cred["screen_name"]
    #user = input("Enter Twitter handle to get lists of: ")

suser = twitter.show_owned_lists(screen_name=user, count=1000)
fnum = 1000
lnum = float(len(suser["lists"]))
pnum = int(math.ceil(lnum / 1000))

thelists = []

pages = []
for i in range(pnum):
    pages.append("p"+str(i+1))

oldpages = []
for i in range(pnum):
    oldpages.append("p"+str(i))

p0 = { "next_cursor": -1 }  # So the following exec() call doesn't fail.
now = dd.utcnow()

for i in range(pnum):
    try:
        exec(pages[i]+" = twitter.show_owned_lists(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")
    except(exceptions.TwythonRateLimitError):
        pass

for p in range(pnum):
    try:
        exec("for i in range(fnum): thelists.append(suser['lists'][i]['slug'])")
    except(IndexError):
        pass

ln = len(thelists)
tstr = str(round(now.timestamp()))
path = os.path.realpath(outdir)
nf = "{0}/{1}-lists-{2}.txt".format(path, user, tstr)

afile = open(nf, "w")
for i in range(ln):
    afile.write(thelists[i])
    afile.write("\n")
    print("{0}".format(thelists[i]))
afile.close()

print("Number of lists:  {0}".format(ln))
