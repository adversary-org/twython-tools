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
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

# import datetime
# import time
import os
import os.path
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()

l = len(sys.argv)

print("""
Enter the message, filenames of any images to upload and the status ID
of a tweet if you are replying to it.

Media filenames need to include either full or relative paths.  Up to
4 images (GIF, JPG or PNG), or 1 animated GIF, or 1 short video (MP4).

If replying to a Tweet then the status ID of the tweet must be entered
at the relevant prompt.  It can accept the URL of the tweet if the
status ID numbe is the last part of the URL.  The username of the
person being replied to, including the at symbol must be included in
any reply, otherwise it is merely another tweet.

Will always prompt for the reply status ID and the media filenames,
but the tweet can be entered with the command like with tweet-basic.py
or at a prompt.  The latter method is recommended when used with some
non-ASCII characters, but the former may be more conducive to
combining with foad.py and similar types of scripts.
""")


reply_id = input("If replying to someone, enter the status ID of that message: ")
media_fn = input("If uploading images, enter the filename(s),separated by spaces (max. 4): ")


if l >= 2:
    msg = []
    for i in range(l - 1):
        msg.append(str(sys.argv[i + 1]))
    message = " ".join(msg)
else:
    message = input("Enter your Tweet: ")

if len(reply_id) > 0:
    twid0 = reply_id.split("/")
    twid1 = twid0[-1]
    try:
        twid = int(twid1)
    except:
        twid = None
else:
    twid = None

if len(media_fn) > 0:
    mfiles = media_fn.split()
    lm = len(mfiles)
    mfid = []
    for i in range(lm):
        if os.path.isfile(os.path.realpath(mfiles[i])) is True:
            mediaf = os.path.realpath(mfiles[i])
        elif os.path.isfile(os.path.realpath("InputFiles/{0}".format(mfiles[i]))) is True:
            mediaf = os.path.realpath("InputFiles/{0}".format(mfiles[i]))
        else:
            mediaf = None

        if mediaf is None:
            mfid.append(mediaf)
        else:
            mf = open(mediaf, "rb")
            response = twitter.upload_media(media=mf)
            mfid.append(response["media_id"])
else:
    mfid = None


if len(message) < 1 and twid is None and mfid is None:
    mesg = None
elif len(message) < 1 and twid is None and mfid is not None:
    mesg = "."
elif len(message) < 1 and twid is not None and mfid is not None:
    users = []
    hashtags = []
    try:
        tweet = twitter.show_status(id=twid)
        user1 = "@"+tweet["user"]["screen_name"]
        users.append(user1)
        rtweet = tweet["text"]
        rtword = rtweet.split()
        for i in range(len(rtword)):
            if rtword[i].startswith("@") is True:
                users.append(rtword[i])
            elif rtword[i].startswith("#") is True:
                hashtags.append(rtword[i])
            else:
                pass
        ustr = " ".join(users)
        hstr = " ".join(hashtags)
        mesg = "{0} {1}".format(ustr, hstr)
    except TwythonError as e:
        print(e)
        mesg = "."
else:
    mesg = message

    
if mesg is not None and twid is None and mfid is None:
    try:
        twitter.update_status(status=mesg)
    except TwythonError as e:
        print(e)
elif mesg is not None and twid is not None and mfid is None:
    try:
        twitter.update_status(status=mesg, in_reply_to_status_id=twid)
    except TwythonError as e:
        print(e)
elif mesg is not None and twid is None and mfid is not None:
    try:
        twitter.update_status(status=mesg, media_ids=mfid)
    except TwythonError as e:
        print(e)
elif mesg is not None and twid is not None and mfid is not None:
    try:
        twitter.update_status(status=mesg, media_ids=mfid,
                              in_reply_to_status_id=twid)
    except TwythonError as e:
        print(e)
elif mesg is None and twid is None and mfid is not None:
    try:
        twitter.update_status(status="", media_ids=mfid)
    except TwythonError as e:
        print(e)
elif mesg is None and twid is not None and mfid is not None:
    try:
        twitter.update_status(status="", media_ids=mfid,
                              in_reply_to_status_id=twid)
    except TwythonError as e:
        print(e)
else:
    print("""
As with all things in this world, you get out of it what you put in
and you put in nothing.
""")
