#!/usr/bin/env python3

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
__version__ = "0.0.1"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    twids =[]
    for i in range(l - 1):
        twids.append(sys.argv[i + 1])
elif l < 2:
    twidz = input("ID numbers of tweets to fetch (separated by spaces): ")
    twids = twidz.split()
else:
    twidz = input("ID numbers of tweets to fetch (separated by spaces): ")
    twids = twidz.split()


for twid0 in twids:
    if twid0.startswith("http"):
        twid1 = twid0.split("/")
    else:
        try:
            twid = int(twid0)
            twid1 = None
        except:
            twid = twid0
            twid1 = None

    if twid1 is not None and twid1[2] == "t.co":
        try:
            r = requests.get(twid0, verify=True)
        except:
            r = requests.get(twid0, verify=False)
        twid2 = r.url
        twid3 = twid2.split("/")
        if twid3 == "twitter.com":
            if len(twid3) >= 6:
                if twid3[4] == "status":
                    try:
                        twid = int(twid3[5])
                    except:
                        twid = twid3[5]
                    else:
                        pass
                else:
                    twid = None
    elif twid1 is not None and twid1[2] == "twitter.com":
        if twid1[4] == "status":
            try:
                twid = int(twid1[5])
            except:
                twid = twid1[5]
            else:
                pass
        else:
            twid = None
    else:
        twid = None

    if twid is not None:
        try:
            tweet = twitter.show_status(id=twid)
            print(tweet["user"]["name"]+" ("+tweet["user"]["screen_name"]+"): "+tweet["text"])
        except TwythonError as e:
            print(e)
            # print(twid)
        else:
            pass
    else:
        print("You must enter a valid status ID.")
