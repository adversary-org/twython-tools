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

        https://github.com/adversary-org/

        Bitcoin:  {0}

    {1}
    {2}
    """.format(__bitcoin__, __version__, __copyright__)))
parser.add_argument("-t", "--tweet", help="The tweet to post.", action="store", required=False)
parser.add_argument("-d", "--direct", help="The direct message to send.", action="store", required=False)
parser.add_argument("-n", "--name", help="Name of target, more than one word must be in quotation marks. May or may not include the at symbol.", action="store", required=False)
parser.add_argument("-r", "--reply", help="The status ID of the tweet being replied to.", action="store", required=False)
parser.add_argument("-b", "--block", help="The user to block.  May or may not match --name.", action="store", required=False)
parser.add_argument("-m", "--mute", help="The user to mute.  May or may not match --name.", action="store", required=False)
parser.add_argument("-s", "--spamblock", help="The user to block and report as a spammer.  May or may not match --name.", action="store", required=False)
parser.add_argument("-V", "--version", help="Print the version number.", action="store", required=False)

args = parser.parse_args()
    
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


try:
    twitter.update_status(status=tweet)
except TwythonError as e:
    print(e)
