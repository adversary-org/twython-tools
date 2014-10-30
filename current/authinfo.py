#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.3
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x).
# * Converted from scripts initially developed with Python 2.7.x.
# * python-gnupg 0.3.6 or later.
# * GNU Privacy Guard (GnuPG, GPG) 1.4.x or 2.0.x).
# * Tor service with SOCKS and proxy (optional).
#
# Options and notes:
#
# The config.py file must be customised prior to running either
# gen-auth.py or authinfo.py in order to set the correct path for the
# GPG configuration and adjust other settings.
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.3"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import getpass
import gnupg
from os.path import expanduser

userdir = expanduser("~")
gpg_home = userdir+"/.gnupg"
gpg = gnupg.GPG(gnupghome=gpg_home)

phrase = getpass.getpass("Enter the passphrase to authorise access to Twitter: ")
#phrase = "" # optionally insert passphrase directly here (a bad idea).
torcon = input("Will you be using Tor to access Twitter (Y/N): ")

afile = open("oauth1.txt.asc", "rb")
doauth1 = gpg.decrypt_file(afile, passphrase=phrase)
afile.close()

bfile = open("oauth2.txt.asc", "rb")
doauth2 = gpg.decrypt_file(bfile, passphrase=phrase)
bfile.close()

cfile = open("oauth3.txt.asc", "rb")
doauth3 = gpg.decrypt_file(cfile, passphrase=phrase)
cfile.close()

dfile = open("oauth4.txt.asc", "rb")
doauth4 = gpg.decrypt_file(dfile, passphrase=phrase)
dfile.close()

APP_KEY = doauth1.data.strip()
APP_SECRET = doauth2.data.strip()
OAUTH_TOKEN = doauth3.data.strip()
OAUTH_TOKEN_SECRET = doauth4.data.strip()

affirmative = ["Y", "yes", "y", "1", "true", "aye", 1, True]
negative = ["N", "no", "n", "0", "false", "nay", 0, False]

if torcon.lower() in negative:
    client_args = {
        "verify": False,
        "headers": {
            "User-Agent": "Twython"
            }
        }
elif torcon.lower() in affirmative:
    client_args = {
        "verify": False,
        "headers": {
            "User-Agent": "Twython Over Tor"
            },
        "proxies": {
            "http": "http://127.0.0.1:8118",
            "https": "https://127.0.0.1:8118",
            }
        }
else:
    client_args = {
        "verify": False,
        "headers": {
            "User-Agent": "Twython"
            }
        }
