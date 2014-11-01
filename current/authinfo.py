#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.8
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
__version__ = "0.0.8"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"


import binascii
import getpass
import hashlib
#import os
#import os.path
#import subprocess
import sys
#import tempfile

from simplecrypt import encrypt, decrypt

#if sys.platform == "darwin":
#    srm = "/usr/bin/srm"
#else:
#    if os.path.exists("/usr/bin/srm") is True:
#        srm = "/usr/bin/srm"
#    elif os.path.exists("/usr/local/bin/srm") is True:
#        srm = "/usr/local/bin/srm"
#    else:
#        srm = ""

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

afile = open("oauth.py.enc", "r")
crypted = afile.read()
afile.close()
ciphertext = binascii.unhexlify(crypted.encode("utf-8"))
plaintext = decrypt(phrase, ciphertext)
del phrase
authdata = plaintext.decode("utf-8")

exec(authdata)

#oauth = tempfile.mkstemp(suffix=".py", prefix="oauth", dir=".", text=True)
#
#for f in os.listdir("."):
#    if f.endswith(".py") and f.startswith("oauth"):
#        oauthc = f[0:len(f)-3]

#bfile = open(oauth[1], "w")
#bfile.write(authdata)
#bfile.close()

del authdata
from oauth import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET

#if len(srm) > 0 and sys.platform == "darwin":
#    secdel = subprocess.Popen([srm, "-fmzv", oauth[1]],
#                              stdout=subprocess.PIPE).communicate()
#    sdm = secdel[0].decode("utf-8")
#elif len(srm) > 0 and sys.platform == "linux" or "linux2":
#    secdel = subprocess.Popen([srm, "-fDv", oauth[1]],
#                              stdout=subprocess.PIPE).communicate()
#    sdm = secdel[0].decode("utf-8")
#elif len(srm) > 0 and sys.platform != "darwin" or "linux" or "linux2":
#    secdel = subprocess.Popen([srm, "-fv", oauth[1]],
#                              stdout=subprocess.PIPE).communicate()
#    sdm = secdel[0].decode("utf-8")
#elif len(srm) == 0 and sys.platform != "win32":
#    secdel = os.remove(oauth[1])
#    sdm = "Installing srm is recommended for this system, use your package manager."
#else:
#    secdel = os.remove(oauth[1])
#    sdm = "Using a system with access to srm is recommended."

# print(sdm)
