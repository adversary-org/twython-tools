#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##
# Copyright (C) Ben McGinnes, 2013-2017
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.1.0
#
# BTC:  1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU
# License:  BSD
#
# Requirements:
#
# * Python 3.4 or later (developed with Python 3.4.x).
# * GPGME 1.8.0 or later with Python bindings.
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

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2017"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2017"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2017"
from license import __license__
__version__ = "0.1.0"
from license import __bitcoin__


import gpg

afile = open("oauth.py.asc", "rb")
authdata = gpg.Context().decrypt(afile)
afile.close()

exec(authdata[0].decode("utf-8"))
del authdata

APP_KEY = oauth.APP_KEY
APP_SECRET = oauth.APP_SECRET
OAUTH_TOKEN = oauth.OAUTH_TOKEN
OAUTH_TOKEN_SECRET = oauth.OAUTH_TOKEN_SECRET
