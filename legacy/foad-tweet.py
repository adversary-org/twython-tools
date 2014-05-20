#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2014
# ben@adversary.org
#
# It is best to use the input prompts for at least the names,
# especially if using the "firstname lastname" options.

import subprocess
import sys
from twython import Twython
from authinfo import *
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

l = len(sys.argv)
p = subprocess.check_output

if l == 1:
    wtf = raw_input("* Type of fuck to give: ")
    victim = raw_input("Twitter username (optional): ")
    name = raw_input("Name to use (optional): ")
elif l == 2:
    wtf = sys.argv[1]
    victim = raw_input("Twitter username (optional): ")
    name = raw_input("Name to use (optional): ")
elif l == 3:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    name = raw_input("Name to use (optional): ")
elif l >= 4:
    wtf = sys.argv[1]
    victim = sys.argv[2]
    nm = []
    for i in range(l - 3):
        nm.append(str(sys.argv[i + 3]))
    name = " ".join(nm)
else:
    wtf = raw_input("* Type of fuck to give: ")
    victim = raw_input("Twitter username (optional): ")
    name = raw_input("Name to use (optional): ")

if len(victim) == 0 and len(name) == 0:
    mesg = p(foad +" "+ wtf, shell=True).strip()
elif len(victim) == 0 and len(name) >= 1:
    target = name
    mesg = p(foad +" "+ wtf +" "+ target, shell=True).strip()
elif len(victim) >= 1 and len(name) == 0:
    target = "@" + victim
    mesg = p(foad +" "+ wtf +" "+ target, shell=True).strip()
elif len(victim) >= 1 and len(name) >= 1:
    target1 = "@" + victim
    target2 = name
    mesg = target1 + ": " + p(foad +" "+ wtf +" "+ target2, shell=True).strip()

print(mesg)
twitter.update_status(status=mesg)
