#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright (C) Ben McGinnes, 2013-2015
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
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2015"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2015"
from license import __license__
__version__ = "0.0.1"
from license import __bitcoin__

import sys
import requests
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

if dir().count("permanent") > 0 or dir().count("dynamic") > 0:
    if permanent.checktor1() or dynamic.checktor1 is True:
        proxyval = True
        # proxies = { "http": "http://127.0.0.1:9050",
        #             "https": "https://127.0.0.1:9050", }
        proxies = { "http": "http://127.0.0.1:8118",
                    "https": "https://127.0.0.1:8118", }
    elif permanent.checktor2() or dynamic.checktor2() is True:
        proxyval = True
        # proxies = { "http": "http://127.0.0.1:9150",
        #             "https": "https://127.0.0.1:9150", }
        proxies = { "http": "http://127.0.0.1:8118",
                    "https": "https://127.0.0.1:8118", }
    elif permanent.checktor3() or dynamic.checktor2() is True:
        proxyval = True
        proxies = { "http": "http://127.0.0.1:8118",
                    "https": "https://127.0.0.1:8118", }
    else:
        proxyval = False
else:
    proxyval = False
    pass


headers = { "headers" : "Twython Tools", }
l = len(sys.argv)

if l >= 2:
    twid0 = sys.argv[1]
elif l < 2:
    twid0 = input("ID number of tweet to fetch: ")
else:
    twid0 = input("ID number of tweet to fetch: ")

try:
    twid = int(twid0)
except:
    twid1 = twid0.split("/")
    twid = twid1[-1]

try:
    tweet = twitter.show_status(id=twid)
    lt = len(tweet['extended_entities']['media'])
    for i in range(lt):
        purl = tweet['extended_entities']['media'][i]['media_url']
        plst = purl.split("/")
        pnom = "OutputFiles/{0}".format(plst[-1])
        if proxyval is True:
            try:
                r = requests.get(purl, headers=headers, proxies=proxies, verify=True)
            except:
                r = requests.get(purl, headers=headers, verify=True)
        else:
            r = requests.get(purl, headers=headers, verify=True)
        pfile = open(pnom, "wb")
        pfile.write(r.content)
        pfile.close()
        print("Media file downloaded to: {0}".format(pnom))
except TwythonError as e:
    print(e)
