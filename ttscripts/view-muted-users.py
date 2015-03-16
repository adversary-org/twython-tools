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
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2015"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2015"
__license__ = "BSD"
__version__ = "0.0.2"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

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
    print("Number of users blocked: {0}".format(mnum))
    print(" ")
except TwythonError as e:
    print(e)
