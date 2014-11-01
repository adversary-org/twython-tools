#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
# Script utilises argparse to perform all the functions of foad-* and
# froad-* scripts.  Will add the mute function too.
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__title__ = "Twython Tools"
__license__ = "BSD"
__version__ = "0.0.1"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import argparse
import subprocess
import sys
from twython import Twython, TwythonError
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

l = len(sys.argv)
subpope = subprocess.Popen
subpipe = subprocess.PIPE
# foad = "foad.py"  # should already be set in config.py

# wtf should be the type of fuck (-f / --fuck)
# relay should be the foad.py relay (-r / --relay)
# name should be the foad.py target (-n / --name)
# target should be the Twitter username, sometimes the name or the relay.
# sender should not be needed as it originates from a twitter account
# extra should be the foad.py extra data (may include tags)
# tags can also be separate from extra, these are appended after other
# rules are followed.

parser = argparse.ArgumentParser(
    prog="foader.py"
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=__title__, epilog=textwrap.dedent("""\
        You MUST place any parameter of more than one word in
        quotation marks.

        https://github.com/adversary-org/twython-tools

        Bitcoin:  {0}

    {1}
    {2}
    """.format(__bitcoin__, version, __copyright__)))
parser.add_argument("-f", "--fuck", help="One word, indicates type of fuck to give, run foad.py -f list_options to see possible flags.", action="store", required=False)
parser.add_argument("-u", "--user", help="Twitter username of recipient.", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of recipient, more than one word must be in quotation marks.", action="store", required=False)
parser.add_argument("-r", "--relay", help="Used to specify a third party to whom a message is to be delivered to by the target.", action="store", required=False)
parser.add_argument("-e", "--extra", help="Additional comment to append to output, more than one word must be in quotation marks.  Sometimes used to enhance an existing response rather than append text.", action="store", required=False)
parser.add_argument("-t", "--tags", help="Hashtags to append to a tweet, not normally used with DMs.", action="store", required=False)
parser.add_argument("-d", "--delivery", help="Used to specify a delivery method.  Delivery methods are: tweet, reply, \"open reply\" and dm.  The default is tweet.", action="store", required=False)
parser.add_argument("-b", "--block", help="Used to specify a type of user blocking (sometimes merely muting or unfollowing).  Block types are: block, spam, mute and unfollow.  The default is none, spam is report for spam and block.", action="store", required=False)
parser.add_argument("-s", "--status", help="Used to specify the status ID a tweet is in response to.  Only called in conjunction with the reply delivery method.", action="store", required=False)

args = parser.parse_args()

if args.fuck is None:
    wtf = ""
else:
    wtf = args.fuck.lower()

if args.user is None:
    target = ""
else:
    if args.user.startswith("@"):
        target = args.user
    else:
        target = "@" + args.user

if args.name is None:
    name = ""
else:
    name = args.name

if args.relay is None:
    relay = ""
else:
    relay = args.relay

if args.extra is None:
    extra = ""
else:
    extra = args.extra

if args.tags is None:
    tags = ""
else:
    tags = args.tags

if args.delivery is None:
    delivery = ""
else:
    delivery = args.delivery.lower()

if args.block is None:
    block = ""
else:
    block = args.block.lower()

if args.status is None:
    stat = ""
else:
    stat = args.status

# Sometimes users forget to include important data, prompt for that
# here:

if len(wtf) == 0:
    fuck = input("You must enter a type of fuck to give, enter it now: ")
    wtf = fuck.lower()

if delivery == "reply" or "open reply" or "public reply" and args.status is None and args.user is None and args.relay is not None:
    target = relay
    stat = input("Enter the status ID of the tweet being replied to: ")
elif delivery == "reply" or "open reply" or "public reply" and args.status is None and args.user is None and args.relay is None:
    target = input("Enter the username of the author of the tweet being replied to: ")
    stat = input("Enter the status ID of the tweet being replied to: ")
elif delivery == "reply" or "open reply" or "public reply" and args.status is None:
    stat = input("Enter the status ID of the tweet being replied to: ")

if block > 0 and args.user is None:
    target = input("You must specify the username of the account you wish to block or report: ")

# Now the rules (structure of messages and subprocess commands) for
# different types of foad messages to send (tags not included):

if delivery == "reply" or "open reply" or "public reply":
    if len(name) == 0 and len(target) > 0 and len(extra) == 0 and len(relay) == 0:
        m = subpope([foad, "-f", wtf, "-n", target], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target != name and len(extra) == 0 and len(relay) == 0:
        f = subpope([foad, "-f", wtf, "-n", name], stdout=subpipe).communicate()[0].strip()
        m = " ".join(target, f)
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) == 0 and len(target) > 0 and len(extra) > 0 and len(relay) == 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-e", extra], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) == 0 and len(target) > 0 and len(extra) == 0 and len(relay) > 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-r", relay], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) == 0 and len(target) > 0 and len(extra) > 0 and len(relay) > 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-e", extra, "-r", relay], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target == name and len(extra) > 0 and len(relay) == 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-e", extra], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target == name and len(extra) == 0 and len(relay) > 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-r", relay], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target == name and len(extra) > 0 and len(relay) > 0:
        m = subpope([foad, "-f", wtf, "-n", target, "-e", extra, "-r", relay], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target != name and len(extra) > 0 and len(relay) == 0:
        f = subpope([foad, "-f", wtf, "-n", name, "-e", extra], stdout=subpipe).communicate()[0].strip()
        m = " ".join(target, f)
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target != name and len(extra) == 0 and len(relay) > 0:
        f = subpope([foad, "-f", wtf, "-n", name, "-r", relay], stdout=subpipe).communicate()[0].strip()
        m = " ".join(target, f)
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and target != name and len(extra) > 0 and len(relay) > 0:
        f = subpope([foad, "-f", wtf, "-n", name, "-e", extra, "-r", relay], stdout=subpipe).communicate()[0].strip()
        m = " ".join(target, f)
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
    elif len(name) > 0 and len(relay) > 0 and target == relay and len(extra) == 0:
        m = subpope([foad, "-f", wtf, "-n", name, "-r", target], stdout=subpipe).communicate()[0].strip()
        if delivery == "open reply" or "public reply" and m.startswith("@"):
            msg = "." + m
        else:
            msg = m
elif delivery == "dm" or "direct":
    # Enter DM stuff here.
else:
    # Enter normal tweet rules here (the default).
    # Include something like open/public replies where necessary.
    # The latter is for picking fights.

if len(msg) + len(tags) <= 135:
    mesg = msg +" "+tags
elif len(msg) + len(tags.split()[0]) <= 135:
    mesg = msg +" "+tags.split()[0]
else:
    mesg = msg

message = mesg.decode("utf-8", "strict"))


# Block rules must come after messages prepared (last 3 rules are
# standard reply, dm and tweet):

if block == "block" and delivery == "dm" or "direct":
    try:
        twitter.send_direct_message(screen_name=target, text=message)
        twitter.create_block(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "spam" or "spammer" and delivery == "dm" or "direct":
    try:
        twitter.send_direct_message(screen_name=target, text=message)
        twitter.report_spam(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "unfollow" and delivery == "dm" or "direct":
    try:
        twitter.send_direct_message(screen_name=target, text=message)
        twitter.destroy_friendship(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "mute" and delivery == "dm" or "direct":
    try:
        twitter.send_direct_message(screen_name=target, text=message)
        #mute command
    except TwythonError as e:
        print(e)
elif block == "block" and delivery == "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message, in_reply_to_status_id=stat)
        twitter.create_block(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "spam" or "spammer" and delivery == "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message, in_reply_to_status_id=stat)
        twitter.report_spam(screen_name=victim)
    except TwythonError as e:
        print(e)
elif block == "unfollow" and delivery == "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message, in_reply_to_status_id=stat)
        twitter.destroy_friendship(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "mute" and delivery == "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message, in_reply_to_status_id=stat)
        #mute command
    except TwythonError as e:
        print(e)
elif block == "block" and delivery != "dm" or "direct" or "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message)
        twitter.create_block(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "spam" or "spammer" and delivery != "dm" or "direct" or "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message)
        twitter.report_spam(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "unfollow" and delivery != "dm" or "direct" or "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message)
        twitter.destroy_friendship(screen_name=target)
    except TwythonError as e:
        print(e)
elif block == "mute" and delivery != "dm" or "direct" or "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message)
        #mute command
    except TwythonError as e:
        print(e)
elif delivery == "dm" or "direct":
    try:
        twitter.send_direct_message(screen_name=target, text=message)
    except TwythonError as e:
        print(e)
elif delivery == "reply" or "open reply" or "public reply":
    try:
        twitter.update_status(status=message, in_reply_to_status_id=stat)
    except TwythonError as e:
        print(e)
else:
    try:
        twitter.update_status(status=message)
    except TwythonError as e:
        print(e)
