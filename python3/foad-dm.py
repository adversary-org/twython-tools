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
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import subprocess
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)
p = subprocess.check_output

if l == 1:
    wtf = input("* Type of fuck to give: ")
    target = input("* Twitter username: ")
    name = input("Name to use (optional): ")
elif l == 2:
    wtf = sys.argv[1]
    target = input("* Twitter username: ")
    name = input("Name to use (optional): ")
elif l == 3:
    wtf = sys.argv[1]
    target = sys.argv[2]
    name = input("Name to use (optional): ")
elif l >= 4:
    wtf = sys.argv[1]
    target = sys.argv[2]
    nm = []
    for i in range(l - 3):
        nm.append(str(sys.argv[i + 3]))
    name = " ".join(nm)
else:
    wtf = input("* Type of fuck to give: ")
    target = input("* Twitter username: ")
    name = input("Name to use (optional): ")

if len(name) == 0:
    name = target

mesg = p(foad +" "+ wtf +" "+ name, shell=True).strip()
print(mesg.decode("utf-8", "strict"))

try:
    twitter.send_direct_message(screen_name=target, text=mesg)
except TwythonError as e:
    print(e)
