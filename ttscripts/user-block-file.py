#!/usr/bin/env python3

##
# Copyright (C) Benjamin D. McGinnes, 2013-2020
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
__version__ = "0.0.2"
from license import __bitcoin__

import os.path
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l >=2:
    userfile = sys.argv[1]
else:
    userfile = input("Path to file of users to block: ")

uf = os.path.expanduser(userfile)
with open(uf, "r") as f:
    users = f.readlines()

for user in users:
    try:
        target = int(user.strip())
    except:
        target = user.strip()

    if isinstance(target, str) is True:
        try:
            twitter.create_block(screen_name=target)
        except TwythonError as e:
            print(e)
    elif isinstance(target, int) is True:
        try:
            twitter.create_block(user_id=target)
        except TwythonError as e:
            print(e)

