#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import division

##
# Copyright (C) Benjamin D. McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# 
#
#
# Requirements:
#
# * Python 3.4 or later.
# * Converted from scripts initially developed with Python 2.7.x.
#
# Options and notes:
#
# Usage:  
#
##

from license import __author__
from license import __copyright__
from license import __copyrighta__
from license import __license__
__version__ = "0.0.1"
from license import __bitcoin__

# import datetime
import time
import os
import os.path
import shutil
import subprocess
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
cred = twitter.verify_credentials()

ls = os.listdir
op = os.path
ow = os.walk
s = subprocess
tt = time.time

pandoc = op.expanduser("~/Library/Haskell/bin/pandoc")
# pandoc = "/usr/local/bin/pandoc"
wkhtmltoimage = "/usr/local/bin/wkhtmltoimage"

mfid = []
l = len(sys.argv)

print("""
A variation on tweet-full.py specifically for posting text in a single
image; either as a standard status update or in reply to someone else.

Enter the message, filenames of any images to upload and the status ID
of a tweet if you are replying to it.

Media filenames need to include either full or relative paths.  Up to
4 images (GIF, JPG or PNG), or 1 animated GIF, or 1 short video (MP4).

If a text/md/rst/etc. file is specified instead of an image then that
file will be converted to a single image and uploaded.

A single file may be referred to on the command line, use the prompts
if more than 1 is to be used.

If replying to a Tweet then the status ID of the tweet must be entered
at the relevant prompt.  It can accept the URL of the tweet if the
status ID numbe is the last part of the URL.  The username of the
person being replied to, including the at symbol must be included in
any reply, otherwise it is merely another tweet.

If no content is entered for the tweet, but it is in reply to a tweet,
the script will use the status ID to assemble a string of usernames
and hashtags to reply to.

Filenames can be entered on the command line, but both the reply ID
(twid) and tweet can only be entered at the prompts.  These are the
fields which can be skipped just by hitting enter.  So the quickest
post is images on the command line followed by enter three times.

usage: tweet-long.py [filename.txt] [css file]
""")


if l == 2:
    media_fn = sys.argv[1]
    css0 = input("Enter the style sheet for the file conversion process: ")
    reply_id = input("If replying to someone, enter the status ID of that message: ")
    message = input("Enter your Tweet: ")
elif l == 3:
    media_fn = sys.argv[1]
    css0 = sys.argv[2]
    reply_id = input("If replying to someone, enter the status ID of that message: ")
    message = input("Enter your Tweet: ")
elif l == 4:
    media_fn = sys.argv[1]
    css0 = sys.argv[2]
    reply_id = sys.argv[3]
    message = input("Enter your Tweet: ")
elif l >= 5:
    media_fn = sys.argv[1]
    css0 = sys.argv[2]
    reply_id = sys.argv[3]
    message = " ".join(sys.argv[4:])
else:
    media_fn = input("If uploading images, enter the filename(s), separated by spaces (max. 4): ")
    css0 = input("Enter the style sheet for the file conversion process: ")
    reply_id = input("If replying to someone, enter the status ID of that message: ")
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

mfiles = media_fn.split()
lm = len(mfiles)  # should usually be 1

if len(css0) > 0:
    try:
        css = op.realpath(css0)
    except:
        css = "Resources/style.css"
else:
    css = "Resources/style.css"

if lm == 0 and len(message) == 0:
    print("Content is mandatory.")
    sys.exit()
elif lm == 0 and len(message) > 0:
    ts = int(tt())
    st = str(ts)
    nf = "Drafts/tweet-{0}.md".format(st)
    afile = open(nf, "wb")
    afile.write(message.encode("utf-8"))
    afile.close()
    mfiles.append(nf)

for i in range(lm):
    if os.path.isfile(os.path.realpath(mfiles[i])) is True:
        mediaf = os.path.realpath(mfiles[i])
    elif os.path.isfile(os.path.realpath("InputFiles/{0}".format(mfiles[i]))) is True:
        mediaf = os.path.realpath("InputFiles/{0}".format(mfiles[i]))
    else:
        mediaf = os.path.relpath(mfiles[i])

    mfl = mediaf.lower()
    mfle = mfl.endswith
    fp, fe = op.splitext(mediaf)
    fn = fp.split("/")[-1]
    fm = "Drafts/{0}_orig.html".format(fn)
    fo = "Drafts/{0}.html".format(fn)
    fi = "InputFiles/{0}{1}".format(fn, fe)
    fz = "InputFiles/{0}.{1}".format(fn, fe.lower())
    fxp = "InputFiles/{0}.png".format(fn)
    fxj = "InputFiles/{0}.jpg".format(fn)
    fxg = "InputFiles/{0}.gif".format(fn)
    fxm = "InputFiles/{0}.mp4".format(fn)
    if mfle(".png") or mfle(".gif") or mfle(".jpg") or mfle(".jpeg") or mfle(".mp4") is True:
        if mediaf == fi:
            print("File ready for upload.")
        else:
            shutil(mediaf, )
        mf = open(mediaf, "rb")
        response = twitter.upload_media(media=mf)
        mfid.append(response["media_id"])
    elif mfle(".md") or mfle(".txt") or mfle(".text") is True:
        s.call([pandoc, "-f", "markdown", "-t", "html5", "-s", "-o", fo,
                mediaf])  # , stdout=pipe).communicate()
    elif mfle(".rst") or mfle(".rest") is True:
        s.call([pandoc, "-f", "rst", "-t", "html5", "-s", "-o", fo, mediaf])
    elif mfle(".org") is True:
        s.call([pandoc, "-f", "org", "-t", "html5", "-s", "-o", fo, mediaf])
    elif mfle(".htm") or mfle(".xhtml") or mfle(".htmlx") is True:
        s.call([pandoc, "-f", "html", "-t", "html5", "-s", "-o", fo, mediaf])
    elif mfle(".html") is True:
        if mediaf == fo:
            shutil.move(mediaf, fm)
            s.call([pandoc, "-f", "html", "-t", "html5", "-s", "-o", fo, fm])
        else:
            s.call([pandoc, "-f", "html", "-t", "html5", "-s", "-o", fo,
                    mediaf])
    
    s.call([wkhtmltoimage, "--width", "600", "--user-style-sheet", css, fo,
            fxp])

    mf = open(fxp, "rb")
    response = twitter.upload_media(media=mf)
    mfid.append(response["media_id"])


if len(message) < 1 and twid is None:
    mesg = "."
elif len(message) < 1 and twid is not None:
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


if mesg is not None and twid is None and mfid is not None:
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
        twitter.update_status(status=".", media_ids=mfid)
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
