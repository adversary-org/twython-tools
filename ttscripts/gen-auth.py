#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.1.1
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
#
# Requirements:
#
# * Python 3.4 or later (developed with Python 3.5.x)
# * GPG, GPGME and PyME (the latter is included with GPGME)
# ** The PyME module has been renamed as gpg.
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
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2017"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2017"
from license import __license__
__version__ = "0.1.1"
from license import __bitcoin__


import os
from gpg import core, errors

print("""
This script encrypts the OAuth data in an importable format with the
OpenPGP (GPG) key specified by the user.

Due to python-gnupg not keeping up with changes to GPG 2.1, this
script is being migrated to use PyME and GPGME.

Encryption method shamelessly nicked from simple.py in the PyME
examples directory (but adapted to write to a file instead of stdout).
The original code is dual licensed under the same terms as both GPGME
and PyME (i.e. the GPL version 2.0 and LGPL version 2.1).

""")

core.check_version(None)

data = []

data.append(input("Enter Consumer Key (APP_KEY): "))
data.append(input("Enter Consumer Secret (APP_SECRET): "))
data.append(input("Enter Access Token (OAUTH_TOKEN): "))
data.append(input("Enter Access Token Secret (OAUTH_TOKEN_SECRET): "))

rkey = input("Enter the key ID to encrypt to: ")
# rkey = ""

authdata = """class oauth:
    APP_KEY = \"{0}\"
    APP_SECRET = \"{1}\"
    OAUTH_TOKEN = \"{2}\"
    OAUTH_TOKEN_SECRET = \"{3}\"
""".format(data[0], data[1], data[2], data[3])
del data

plain = core.Data(authdata)
cipher = core.Data()
c = core.Context()
c.set_armor(1)

c.op_keylist_start(rkey, 0)
r = c.op_keylist_next()

del authdata

if r == None:
    print("""The key for user "{0}" was not found""".format(rkey))
else:
    try:
        c.op_encrypt([r], 1, plain, cipher)
        cipher.seek(0, os.SEEK_SET)
        afile = open("oauth.py.asc", "wb")
        afile.write(cipher.read())
        afile.close()
    except errors.GPGMEError as ex:
        print(ex.getstring())

