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

if l == 1:
    target = raw_input("* Twitter username: ")
    wtf = raw_input("* Type of fuck to give: ")
    name = raw_input("Name to use (optional): ")
elif l == 2:
    target = sys.argv[1]
    wtf = raw_input("* Type of fuck to give: ")
    name = raw_input("Name to use (optional): ")
elif l == 3:
    target = sys.argv[1]
    wtf = sys.argv[2]
    name = raw_input("Name to use (optional): ")
elif l >= 4:
    target = sys.argv[1]
    wtf = sys.argv[2]
    nm = []
    for i in range(l - 3):
        nm.append(str(sys.argv[i + 3]))
    name = " ".join(nm)
else:
    target = raw_input("* Twitter username: ")
    wtf = raw_input("* Type of fuck to give: ")
    name = raw_input("Name to use (optional): ")

if len(name) == 0:
    name = target

mesg = p(foad +" "+ wtf +" "+ name, shell=True).strip()

print(mesg)

twitter.send_direct_message(screen_name=target, text=mesg)
