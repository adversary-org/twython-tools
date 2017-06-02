#!/usr/bin/env python3

##
# Copyright (C) Benjamin D. McGinnes, 2013-2015
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

import argparse
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

parser = argparse.ArgumentParser(
    prog="twyt.py",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__title__, epilog=textwrap.dedent("""\
        You MUST place any parameter of more than one word in
        quotation marks.

        https://github.com/adversary-org/twython-tools

        Bitcoin:  {0}

    {1}
    {2}
    """.format(__bitcoin__, __version__, __copyright__)))
parser.add_argument("-c", "--command", help="The command or function to run. Default is tweet and options generally match the other arguments. Some user functions do not match flags, see documentation for details.", action="store", required=False)
parser.add_argument("-t", "--tweet", help="The tweet to post.", action="store", required=False)
parser.add_argument("-d", "--direct", help="The direct message to send.", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of target, more than one word must be in quotation marks. May or may not include the at symbol.", action="store", required=False)
parser.add_argument("-r", "--reply", help="The status ID of the tweet being replied to.", action="store", required=False)
parser.add_argument("-f", "--follow", help="The user to follow.  May or may not match --name.", action="store", required=False)
parser.add_argument("-F", "--unfollow", help="The user to stop following.  May or may not match --name.", action="store", required=False)
parser.add_argument("-b", "--block", help="The user to block.  May or may not match --name.", action="store", required=False)
parser.add_argument("-B", "--unblock", help="The user to unblock.  May or may not match --name.", action="store", required=False)
parser.add_argument("-m", "--mute", help="The user to mute.  May or may not match --name.", action="store", required=False)
parser.add_argument("-M", "--unmute", help="The user to unmute.  May or may not match --name.", action="store", required=False)
parser.add_argument("-s", "--spamblock", help="The user to block and report as a spammer.  May or may not match --name.", action="store", required=False)
parser.add_argument("-V", "--version", help="Print the version number.", action="store", required=False)

args = parser.parse_args()

if args.command is None:
    command = ""
else:
    cmd = args.command
    command = cmd.lower()

if args.tweet is None:
    tweet = ""
else:
    tweet = args.tweet

if args.direct is None:
    direct = ""
else:
    direct = args.direct

if args.name is None:
    name = ""
else:
    name = args.name

if args.reply is None:
    reply = ""
else:
    reply = args.reply
    try:
        replyid = int(reply)
    except:
        reply = ""

if args.block is None:
    block = ""
else:
    block = args.block

if args.unblock is None:
    unblock = ""
else:
    unblock = args.unblock

if args.follow is None:
    follow = ""
else:
    follow = args.follow

if args.unfollow is None:
    unfollow = ""
else:
    unfollow = args.unfollow

if args.mute is None:
    mute = ""
else:
    mute = args.mute

if args.unmute is None:
    unmute = ""
else:
    unmute = args.unmute

if command == "tweet" and len(tweet) == 0:
    tweet = input("Enter the tweet: ")
elif command == "reply" and isinstance(replyid, int) is False and len(tweet) == 0:
    tweet = input("Enter the tweet: ")
    reply = input("Enter the status ID of the tweet you are replying to: ")
    try:
        replyid = int(reply)
    except:
        print("You must enter a valid status ID number to reply to.")
elif command == "reply" and isinstance(replyid, int) is False and len(tweet) > 0:
    reply = input("Enter the status ID of the tweet you are replying to: ")
    try:
        replyid = int(reply)
    except:
        print("You must enter a valid status ID number to reply to.")
elif command == "reply" and isinstance(replyid, int) is True and len(tweet) == 0:
    tweet = input("Enter the tweet: ")
elif command == "follow" and len(follow) == 0 and len(name) == 0:
    target = input("Enter the username to be followed: ")
elif command == "follow" and len(follow) == 0 and len(name) > 0:
    target = name
elif command == "follow" and len(follow) > 0 and len(name) == 0:
    target = follow
elif command == "unfollow" and len(unfollow) == 0 and len(name) == 0:
    target = input("Enter the username to be unfollowed: ")
elif command == "unfollow" and len(unfollow) == 0 and len(name) > 0:
    target = name
elif command == "unfollow" and len(unfollow) > 0 and len(name) == 0:
    target = unfollow
