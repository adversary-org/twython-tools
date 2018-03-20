#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Benjamin D. McGinnes, 2013-2018
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.1.2
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# 
#
# Requirements:
#
# * Python 3.4 or later.
# * GPGME 1.10.0 or later with Python bindings.
#
# Options and notes:
#
# The config.py file must be customised prior to running either
# gen-auth.py or authinfo.py in order to set the correct path for the
# GPG configuration and adjust other settings.
#
# No longer requires PyCrypto, SimpleCrypt, python-gnupg or gconfig.py.
# Instead requires GPG and GPGME with Python bindings.
# Passphrase handled by gpg-agent.
#
# Python requirements raised due to GPGME requirements.
# May also work with Python 2.7, but untested.
#
##

from license import __author__
from license import __copyright__
from license import __copyrighta__
from license import __license__
from license import __bitcoin__
__version__ = "0.1.2"

import os
import os.path
import gpg

if os.path.exists("oauth.py.gpg") is True:
    oauthy = "oauth.py.gpg"
elif os.path.exists("oauth.py.asc") is True:
    oauthy = "oauth.py.asc"
else:
    oauthy = None

if oauthy is not None:
    with open(oauthy, "rb") as afile:
        authdata = gpg.Context().decrypt(afile)
    exec(authdata[0].decode("utf-8"))
else:
    print("""
    You must run gen-auth.py first.
""")

APP_KEY = oauth.APP_KEY
APP_SECRET = oauth.APP_SECRET
OAUTH_TOKEN = oauth.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = oauth.OAUTH_TOKEN_SECRET
