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

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    user = sys.argv[1]
else:
    user = input("User to block: ")

try:
    target = int(user)
except:
    target1 = user.split("/")
    target = target1[-1]
    
if isinstance(target, str) is True:
    try:
        twitter.destroy_block(screen_name=target, skip_status="true")
    except TwythonError as e:
        print(e)
elif isinstance(target, int) is True:
    try:
        twitter.destroy_block(user_id=target, skip_status="true")
    except TwythonError as e:
        print(e)
