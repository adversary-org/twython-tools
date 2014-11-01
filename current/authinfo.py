#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.7
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x).
# * Converted from scripts initially developed with Python 2.7.x.
# * PyCrypto 2.6.1 or later.
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
__version__ = "0.0.7"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import binascii
import getpass
import hashlib
import sys

from simplecrypt import encrypt, decrypt

try:
    password = getpass.getpass("Enter the passphrase to authorise access to Twitter: ")
except getpass.GetPassWarning:
    print("Your current terminal may display your password.  You will be prompted to continue or not.")
    cont = input("Do you wish to continue (yes/no): ")
    if cont.lower() == "yes" or "y":
        password = getpass.getpass("Enter the passphrase to authorise access to Twitter: ")
    else:
        print("You should use a normal xterm to run this program.")
        print("Exiting.")
        sys.exit()

phrase = hashlib.sha256(password.encode("utf-8")).hexdigest()
del password

files = ["oauth1.txt.asc", "oauth2.txt.asc", "oauth3.txt.asc", "oauth4.txt.asc"]
authdata = []

for i in range(4):
    afile = open(files[i], "r")
    crypted = afile.read()
    afile.close()
    ciphertext = binascii.unhexlify(crypted.encode("utf-8"))
    plaintext = decrypt(phrase, ciphertext)
    authsecret = plaintext.decode("utf-8").strip()
    authdata.append(authsecret)

APP_KEY = authdata[0]
APP_SECRET = authdata[1]
OAUTH_TOKEN = authdata[2]
OAUTH_TOKEN_SECRET = authdata[3]

del phrase

