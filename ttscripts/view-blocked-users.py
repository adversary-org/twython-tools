#!/usr/bin/env python3

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# 
#
#
# Requirements:
#
# * Python 3.4 or later.
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

import time
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
    blocked = twitter.list_blocks(skip_status=1, cursor=-1)
    busr = blocked["users"]
    bnum = len(busr)
    print(" ")
    for i in range(bnum):
        print("{0}: {1}".format(busr[i]["screen_name"], busr[i]["name"]))
    print(" ")
    print("Number of users blocked: {0}".format(bnum))
    print(" ")
except TwythonError as e:
    print(e)
