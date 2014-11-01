#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.2
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
__version__ = "0.0.2"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import subprocess
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)
p = subprocess.check_output
subpope = subprocess.Popen
subpipe = subprocess.PIPE

if l == 1:
    wtf = input("* Type of fuck to give: ")
    target = input("* Twitter username: ")
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
elif l == 2:
    wtf = sys.argv[1]
    target = input("* Twitter username: ")
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
elif l == 3:
    wtf = sys.argv[1]
    target = sys.argv[2]
    name = input("Name to use (optional): ")
    extra = input("Extra comment (optional): ")
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
    extra = input("Extra comment (optional): ")

if len(name) == 0 and len(extra) == 0:
    mesg = subpope([foad, "-f", wtf], stdout=subpipe).communicate()[0].strip()
elif len(name) > 0 and len(extra) == 0:
    mesg = subpope([foad, "-f", wtf, "-n", name], stdout=subpipe).communicate()[0].strip()
elif len(name) == 0 and len(extra) > 0:
    mesg = subpope([foad, "-f", wtf, "-e", extra], stdout=subpipe).communicate()[0].strip()
elif len(name) > 0 and len(extra) > 0:
    mesg = subpope([foad, "-f", wtf, "-n", name, "-e", extra], stdout=subpipe).communicate()[0].strip()

msg = mesg.decode("utf-8", "strict")
print(msg)

try:
    twitter.send_direct_message(screen_name=target, text=msg)
except TwythonError as e:
    print(e)
