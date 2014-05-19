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
from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#twitter.verify_credentials()

l = len(sys.argv)
p = subprocess.check_output

if l == 2:
    wtf = sys.argv[1]
    victim = input("* Recipient: ")
    stat = input("* Twitter ID for status being replied to: ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 3:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    stat = input("* Twitter ID for status being replied to: ")
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l == 4:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    stat = sys.argv[3]
    tags = input("Append hashtags (optional, enter as they appear): ")
elif l >= 5:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    stat = sys.argv[3]
    tag = []
    for i in range(l - 4):
        tag.append(str(sys.argv[i + 4]))
    tags = " ".join(tag)
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
msg = p(foad +" "+ wtf +" "+ target, shell=True).strip()

if target in msg:
    message = msg
elif target not in msg:
    message = target + ", " + msg[0:4].lower() + msg[4:len(msg)]

if len(message) + len(tags) <= 135:
    mesg = message +" "+tags
elif len(message) + len(tag[0]) <= 135:
    mesg = message +" "+tag[0]
else:
    mesg = message

print(mesg.decode("utf-8", "strict"))

twitter.update_status(status=message, in_reply_to_status_id=stat)
twitter.create_block(screen_name=victim)
