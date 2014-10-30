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
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.2"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import getpass
import gnupg
from os.path import expanduser

userdir = expanduser("~")
gpg_home = userdir+"/.gnupg"
gpg = gnupg.GPG(gnupghome=gpg_home)

print("""
The passphrase set with this script must be used with the authinfo.py
script or added to that script (the latter is *much* less secure).

Leaving the cipher option blank will use the default or preferred
symmetric cipher.  Otherwise enter the symmetric cipher you wish to
use (e.g. TWOFISH, AES256, CAMELLIA256, etc.).

See "gpg --version" output for available symmetric ciphers.
""")

data1 = input("Enter Consumer Key (APP_KEY): ")
data2 = input("Enter Consumer Secret (APP_SECRET): ")
data3 = input("Enter Access Token (OAUTH_TOKEN): ")
data4 = input("Enter Access Token Secret (OAUTH_TOKEN_SECRET): ")
phrase = getpass.getpass("Enter the passphrase to secure Twitter access: ")
cipheropt = input("Enter symmetric encryption algorithm to use: ")
file1 = "oauth1.txt.asc"
file2 = "oauth2.txt.asc"
file3 = "oauth3.txt.asc"
file4 = "oauth4.txt.asc"

if cipheropt == "":
    cipher = True
else:
    cipher = cipheropt.upper()

gpg.encrypt(data1, None, passphrase=phrase, symmetric=cipher, output=file1)
gpg.encrypt(data2, None, passphrase=phrase, symmetric=cipher, output=file2)
gpg.encrypt(data3, None, passphrase=phrase, symmetric=cipher, output=file3)
gpg.encrypt(data4, None, passphrase=phrase, symmetric=cipher, output=file4)
