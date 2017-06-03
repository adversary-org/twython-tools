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

if l >=2:
    target1 = sys.argv[1]
else:
    target1 = input("User to block: ")

try:
    target = int(target1)
except:
    target = target1

if isinstance(target, int) is True:
    try:
        twitter.create_block(user_id=target)
        twitter.report_spam(user_id=target)
    except TwythonError as e:
        print(e)
elif isinstance(target, str) is True:
    try:
        twitter.create_block(screen_name=target)
        twitter.report_spam(screen_name=target)
    except TwythonError as e:
        print(e)

