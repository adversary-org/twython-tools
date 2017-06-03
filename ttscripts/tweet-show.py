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

from license import __author__
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2015"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2015"
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import requests
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    twid0 = sys.argv[1]
elif l < 2:
    twid0 = input("ID number or URL of status to fetch: ")
else:
    twid0 = input("ID number of tweet to fetch: ")

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
