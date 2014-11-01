#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.4
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
# Updated to take greater advantage of foad.py, which is now much
# better than it was when this was first written.
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.4"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import subprocess
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)
subpope = subprocess.Popen
subpipe = subprocess.PIPE
# foad = "foad.py"  # should already be set in config.py

# wtf should be the type of fuck (-f / --fuck)
# victim should be the foad.py relay (-r / --relay)
# name should be the foad.py target (-n / --name)
# sender should not be needed as it originates from a twitter account
# extra should be the foad.py extra data (may include tags)
# tags can also be separate from extra

if l == 1:
    wtf = input("* Type of fuck to give: ")
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 2:
    wtf = sys.argv[1]
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 3:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l >= 4:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    nm = []
    for i in range(l - 3):
        nm.append(str(sys.argv[i + 3]))
    name = " ".join(nm)
    extra = input("Extra comment (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")
else:
    wtf = input("* Type of fuck to give: ")
    victim = input("Twitter username (optional): ")
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
    tags = input("Append hashtags (optional, enter as they appear): ")

if len(victim) == 0 and len(name) == 0 and len(extra) == 0:
    msg = subpope([foad, "-f", wtf], stdout=subpipe).communicate()[0].strip()
elif len(victim) == 0 and len(name) == 0 and len(extra) > 0:
    msg = subpope([foad, "-f", wtf, "-e", extra], stdout=subpipe).communicate()[0].strip()
elif len(victim) == 0 and len(name) > 0 and len(extra) == 0:
    target = name
    msg = subpope([foad, "-f", wtf, "-n", target], stdout=subpipe).communicate()[0].strip()
elif len(victim) == 0 and len(name) > 0 and len(extra) > 0:
    target = name
    msg = subpope([foad, "-f", wtf, "-n", target, "-e", extra], stdout=subpipe).communicate()[0].strip()
elif len(victim) > 0 and len(name) == 0 and len(extra) == 0:
    target = "@" + victim
    msg = subpope([foad, "-f", wtf, "-n", target], stdout=subpipe).communicate()[0].strip()
elif len(victim) > 0 and len(name) == 0 and len(extra) > 0:
    target = "@" + victim
    msg = subpope([foad, "-f", wtf, "-n", target, "-e", extra], stdout=subpipe).communicate()[0].strip()
elif len(victim) > 0 and len(name) > 0 and len(extra) == 0:
    msg = subpope([foad, "-f", wtf, "-n", name, "-r", victim], stdout=subpipe).communicate()[0].strip()
elif len(victim) > 0 and len(name) > 0 and len(extra) > 0:
    msg = subpope([foad, "-f", wtf, "-n", name, "-r", victim, "-e", extra], stdout=subpipe).communicate()[0].strip()
            

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
