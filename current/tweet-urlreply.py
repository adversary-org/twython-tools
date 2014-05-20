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

import requests
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l == 1:
    url = input("Enter full URL of tweet: ")
elif l >= 2:
    url = sys.argv[1]

a = url.replace(sa1[0:20], "").replace("/status/", " ").split()
twid = int(a[1])

try:
    tweet = twitter.show_status(id=twid)
    name = tweet["user"]["name"]
    user = tweet["user"]["screen_name"]
    text = tweet["text"]
    show = name+" ("+user+"): "+text
    print(show)
except TwythonError as e:
    print(e)

tags = []
usr1 = []
usr2 = []
urls = []
tsep = text.split()

for x in tsep:
    if x.startswith("#") is True:
        tags.append(x)
    elif x.startswith("@") is True:
        usr1.append(x)
        usr2.append(x.replace("@", "")
    elif x.startswith("http:") is True:
        urls.append(x)
    elif x.startswith("https:") is True:
        urls.append(x)

for u in urls:
    r = requests.get(u, verify=False)
    print("%s forwards to %s" % (u, r.url))

# Reply to all:

char = 140 - (len(user) + 2) - (len(" ".join(tags)) + 1) - (len(" ".join(usr1)) + 1)
ques = "Enter the reply, not counting the username (%s characters max): " % char
msg = input(ques)
mesg = "@%s %s %s %s" % (user, msg, " ".join(usr1), " ".join(tags))

try:
    twitter.update_status(status=mesg, in_reply_to_status_id=twid)
except TwythonError as e:
    print(e)

## Reply to each individually:
#
#usrs = []
#usrs.append("@" + user)
#for y in usr1:
#    usrs.append(y)
#
#for z in usrs:
#    char = 140 - (len(z) + 1) - (len(" ".join(tags)) + 1)
#    ques = "Enter the reply, not counting the username (%s characters max): " % char
#    msg = input(ques)
#    mesg = "%s %s %s" % (z, msg, " ".join(tags))
#    try:
#        twitter.update_status(status=mesg, in_reply_to_status_id=twid)
#    except TwythonError as e:
#        print(e)
