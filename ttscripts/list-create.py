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
    name = input("Enter the name (slug) of the new list: ")
    mode = input("Public or private: ")
    desc = input("Description (optional, 100 characters): ")
elif l == 2:
    name = sys.argv[1]
    mode = input("Public or private: ")
    desc = input("Description (optional, 100 characters): ")
elif l == 3:
    name = sys.argv[1]
    if sys.argv[2].lower() == "public" or "private" or "pub" or "priv":
        mode = sys.argv[2].lower()
        desc = input("Description (optional, 100 characters): ")
    else:
        mode = "public"
        desc = sys.argv[2]
elif l == 4:
    name = sys.argv[1]
    if sys.argv[2].lower() == "public" or "private" or "pub" or "priv":
        mode = sys.argv[2].lower()
        desc = sys.argv[3]
    else:
        mode = "public"
        desc = sys.argv[2:]
elif l > 4:
    name = sys.argv[1]
    if sys.argv[2].lower() == "public" or "private" or "pub" or "priv":
        mode = sys.argv[2].lower()
        desc = sys.argv[3:]
    else:
        mode = "public"
        desc = sys.argv[2:]
else:
    name = input("Enter the name (slug) of the new list: ")
    mode = input("Public or private: ")
    desc = input("Description (optional, 100 characters): ")


try:
    new = twitter.create_list(name=name, mode=mode, description=desc)
except TwythonError as e:
    print(e)

