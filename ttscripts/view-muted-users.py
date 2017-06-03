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
    muted = twitter.list_mutes(skip_status=1, cursor=-1)
    musr = muted["users"]
    mnum = len(musr)
    print(" ")
    for i in range(mnum):
        print("{0}: {1}".format(musr[i]["screen_name"], musr[i]["name"]))
    print(" ")
    print("Number of users silenced: {0}".format(mnum))
    print(" ")
except TwythonError as e:
    print(e)
