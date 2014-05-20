#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
#

import subprocess
import sys
from twython import Twython
from authinfo import *
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

l = len(sys.argv)
p = subprocess.check_output

if l == 2:
    victim = sys.argv[1]
    wtf = raw_input("* Type of fuck to give: ")
elif l >= 3:
    victim = sys.argv[1]
    wtf = sys.argv[2]
elif l < 2:
    victim = raw_input("* Recipient: ")
    wtf = raw_input("* Type of fuck to give: ")
else:
    victim = raw_input("* Recipient: ")
    wtf = raw_input("* Type of fuck to give: ")

target = "@" + victim
mesg = p(foad +" "+ wtf +" "+ target, shell=True).strip()

if target in mesg:
    message = mesg
elif target not in mesg:
    message = target + ", " + mesg[0:4].lower() + mesg[4:len(mesg)]

print(message)

twitter.update_status(status=message)
twitter.create_block(screen_name=victim)
