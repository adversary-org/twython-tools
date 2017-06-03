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
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()
l = len(sys.argv)

if l == 1:
    listx = input("Enter the name of the list to subscribe to: ")
    ownerx = input("Enter the owner of the list: ")
elif l == 2:
    listx = sys.argv[1]  # must be the url of the list
    ownerx = sys.argv[1]
elif l >= 3:
    listx = sys.argv[1]
    ownerx = sys.argv[2]
else:
    pass

if listx == ownerx:
    url = listx.split("/")
    name = url[-1]
    owner = url[-3]
else:
    name = listx
    owner = ownerx

try:
    sub = twitter.unsubscribe_from_list(slug=name, owner_screen_name=owner)
except TwythonError as e:
    print(e)
