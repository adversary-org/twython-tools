#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.9
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
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
__version__ = "0.0.9"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import binascii
import getpass
import hashlib
import sys

from simplecrypt import encrypt, decrypt

print("""
The passphrase set with this script must be used with the authinfo.py
script or added to that script (the latter is *much* less secure).

The password or passphrase is encrypted with 256-bit AES utiliing as
SHA-256 hash implemented with PyCrypto and SimpleCrypt.  SimpleCrypt
is included with this software, but you must install PyCrypto
separately (i.e. with pip).

""")

data = []

data.append(input("Enter Consumer Key (APP_KEY): "))
data.append(input("Enter Consumer Secret (APP_SECRET): "))
data.append(input("Enter Access Token (OAUTH_TOKEN): "))
data.append(input("Enter Access Token Secret (OAUTH_TOKEN_SECRET): "))

try:
    password = getpass.getpass("Enter the passphrase to secure Twitter access: ")
except getpass.GetPassWarning:
    print("Your current terminal may display your password.  You will be prompted to continue or not.")
    cont = input("Do you wish to continue (yes/no): ")
    if cont.lower() == "yes" or "y":
        password = getpass.getpass("Enter the passphrase to secure Twitter access: ")
    else:
        print("You should use a normal xterm to run this program.")
        print("Exiting.")
        sys.exit()

phrase = hashlib.sha256(password.encode("utf-8")).hexdigest()
del password

authdata = """class oauth:
    APP_KEY = \"{0}\"
    APP_SECRET = \"{1}\"
    OAUTH_TOKEN = \"{2}\"
    OAUTH_TOKEN_SECRET = \"{3}\"
""".format(data[0], data[1], data[2], data[3])
del data
crypted = encrypt(phrase, authdata)
del phrase
del authdata
ciphertext = binascii.hexlify(crypted)
cryptfile = ciphertext.decode("utf-8")

afile = open("oauth.py.enc", "w")
afile.write(cryptfile)
afile.close()
