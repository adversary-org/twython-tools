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

import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)

if l == 1:
    user = input("Enter username or user ID of user: ")
elif l >= 2:
    user = sys.argv[1]

if isinstance(user, str) is True:
    data = twitter.get_list_memberships(screen_name=user)
elif isinstance(user, int) is True:
    data = twitter.get_list_memberships(user_id=user)

for i in range(len(data["lists"])):
    print("""          Source:  %s
            Name:  %s
             URL:  %s
List description:  %s
""" % (data["lists"][i]["user"]["screen_name"], data["lists"][i]["user"]["name"], "https://twitter.com"+data["lists"][i]["uri"], data["lists"][i]["description"]))
