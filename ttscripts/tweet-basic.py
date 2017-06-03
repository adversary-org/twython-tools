#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
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

# __author__ = "Ben McGinnes <ben@adversary.org>"
# __copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2017"
# __copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2017"
from license import __author__
from license import __copyright__
from license import __copyrighta__
from license import __copyright2__
from license import __copyright2a__
from license import __license__
from license import __bitcoin__

__version__ = "0.0.2"

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >= 2:
    msg = []
    for i in range(l - 1):
        msg.append(str(sys.argv[i + 1]))
    mesg = " ".join(msg)
elif l < 2:
    mesg = input("Tweet (140 characters max): ")
else:
    mesg = input("Tweet (140 characters max): ")

try:
    twitter.update_status(status=mesg)
except TwythonError as e:
    print(e)
