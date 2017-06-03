#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright © Ben McGinnes, 2013-2017
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
#
# Options and notes:
#
# Usage:  
#
##

from license import __author__
from license import __copyright__
from license import __license__
__version__ = "0.0.2"
from license import __bitcoin__

import datetime
import os.path
import pprint
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()
dd = datetime.datetime
pp = pprint.pprint
l = len(sys.argv)

if l == 1:
    limits = input("Enter the resources to check (separated by spaces): ")
elif l == 2:
    limits = sys.argv[1]
elif l > 2:
    limits = sys.argv[1:]
else:
    limits = input("Enter the resources to check (separated by spaces): ")


if limits.lower() == "all":
    limited = "application,favorites,followers,friends,lists,search,statuses,users,help"
else:
    limit = limits.split()
    limited = ",".join(limit)


num = len(limits)
now = dd.utcnow()

try:
    ltd = twitter.get_application_rate_limit_status(resources=limited)
except TwythonError as e:
    print(e)
    pass

pp(ltd)
print("Valid at:  {0} UTC".format(now.isoformat()))
