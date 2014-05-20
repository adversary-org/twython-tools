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
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 2:
    wtf = sys.argv[1]
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 3:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    name = input("Name to use (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l >= 4:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    nm = []
    for i in range(l - 3):
        nm.append(str(sys.argv[i + 3]))
    name = " ".join(nm)
    tags = input("Append hashtags (optional, enter as they appear): ")
else:
    wtf = input("* Type of fuck to give: ")
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")

if len(victim) == 0 and len(name) == 0:
    msg = p(foad +" "+ wtf, shell=True).strip()
elif len(victim) == 0 and len(name) >= 1:
    target = name
    msg = p(foad +" "+ wtf +" "+ target, shell=True).strip()
elif len(victim) >= 1 and len(name) == 0:
    target = "@" + victim
    msg = p(foad +" "+ wtf +" "+ target, shell=True).strip()
elif len(victim) >= 1 and len(name) >= 1:
    target1 = "@" + victim
    target2 = name
    msg = target1 + ": " + p(foad +" "+ wtf +" "+ target2, shell=True).strip()

if len(msg) + len(tags) <= 135:
    mesg = msg +" "+tags
elif len(msg) + len(tags.split()[0]) <= 135:
    mesg = msg +" "+tags.split()[0]
else:
    mesg = msg

print(mesg.decode("utf-8", "strict"))

try:
    twitter.update_status(status=mesg)
except TwythonError as e:
    print(e)
