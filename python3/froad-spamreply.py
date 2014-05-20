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

if l == 2:
    wtf = sys.argv[1]
    victim = input("* Recipient: ")
    stat = input("* Twitter ID for status being replied to: ")
elif l == 3:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    stat = input("* Twitter ID for status being replied to: ")
elif l >= 4:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    stat = sys.argv[3]
elif l < 2:
    wtf = input("* Type of fuck to give: ")
    victim = input("* Recipient: ")
    stat = input("* Twitter ID for status being replied to: ")
    tags = input("Append hashtags (optional, enter as they appear): ")
else:
    wtf = input("* Type of fuck to give: ")
    victim = input("* Recipient: ")
    stat = input("* Twitter ID for status being replied to: ")
    tags = input("Append hashtags (optional, enter as they appear): ")

target = "@" + victim
mesg = p(foad +" "+ wtf +" "+ target, shell=True).strip()

print(mesg.decode("utf-8", "strict"))

try:
    twitter.update_status(status=mesg, in_reply_to_status_id=stat)
    twitter.report_spam(screen_name=victim)
except TwythonError as e:
    print(e)
