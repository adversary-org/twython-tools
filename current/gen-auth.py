#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.4
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
# * Converted from scripts initially developed with Python 2.7.x.
# * A current version of PyCrypto.
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
__version__ = "0.0.4"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import base64
import getpass
import hashlib

from simplecrypt import encrypt, decrypt

print("""
The passphrase set with this script must be used with the authinfo.py
script or added to that script (the latter is *much* less secure).

The password or passphrase is encrypted with 256-bit AES utiliing as
SHA-256 hash implemented with PyCrypto and SimpleCrypt.  SimpleCrypt
is included with this software, but you must install PyCrypto
separately (i.e. with pip).

""")

files = ["oauth1.txt.asc", "oauth2.txt.asc", "oauth3.txt.asc", "oauth4.txt.asc"]

data = []

data.append(input("Enter Consumer Key (APP_KEY): "))
data.append(input("Enter Consumer Secret (APP_SECRET): "))
data.append(input("Enter Access Token (OAUTH_TOKEN): "))
data.append(input("Enter Access Token Secret (OAUTH_TOKEN_SECRET): "))

password = getpass.getpass("Enter the passphrase to secure Twitter access: ")
phrase = hashlib.sha256(password.encode("utf-8")).hexdigest()
del password

for i in range(4):
    afile = open(files[i], "w")
    afile.write(base64.b64encode(encrypt(phrase, data[i].encode("utf-8"))))
    afile.close()

del phrase
del data

