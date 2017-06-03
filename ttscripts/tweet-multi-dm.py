#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
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
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
from license import __license__
__version__ = "0.0.1"
from license import __bitcoin__

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l == 1:
    filename = input("File name of recipient list (text file): ")
    mesg = input("Direct message (140 characters max): ")
elif l == 2:
    filename = sys.argv[1]
    mesg = input("Direct message (140 characters max): ")
elif l >= 3:
    filename = sys.argv[1]
    msg = []
    for i in range(l - 2):
        msg.append(str(sys.argv[i + 2]))
    mesg = " ".join(msg)
else:
    filename = input("File name of recipient list (text file): ")
    mesg = input("Direct message (140 characters max): ")

afile = open(filename, "r")
adata = afile.readlines()
afile.close()
for string in adata:
    target = string.strip()
    try:
        twitter.send_direct_message(screen_name=target, text=mesg)
    except TwythonError as e:
        print(e)
