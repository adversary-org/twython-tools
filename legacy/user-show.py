#!/usr/bin/env python

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
# Requirements:
#
# See Documentation/README-py2.txt
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


from twython import Twython, exceptions
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

target = raw_input("User to show: ")

try:
    data = twitter.show_user(screen_name=target)
    print("""
Name:     %s

Username: %s
User ID:  %s
Created:  %s

Tweets:   %s

Following:  %s
Followers:  %s
""" % (data["name"], data["screen_name"], data["id_str"], data["created_at"], data["statuses_count"], data["friends_count"], data["followers_count"]))
except(exceptions.TwythonError):
    print("User "+target+" does not exist.")
