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
# Options and notes:
#
# It may be preferable to delete or comment out the class not being
# used.
#
# Usage:  
#
# This file and the classes in it are imported by config.py.
# The permanent class removes the need to answer questions about
# connecting through Tor and simply checks for the connection types,
# first for a custom installation of Tor, then for the Tor Browser
# Bundle and if neither are available it attempts a direct (ordinary)
# connection.
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright © Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__copyrightu__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__license__ = "BSD"
__version__ = "0.0.9"
__bitcoin__ = "1KvKMVnyYgLxU1HnLQmbWaMpDx3Dz15DVU"

import socket


class permanent:
    def checktor1():
        try:
            s = socket.socket()
            s.connect(("127.0.0.1", 9050))
            return True
        except socket.error, e:
            return False

    def checktor2():
        try:
            s = socket.socket()
            s.connect(("127.0.0.1", 9150))
            return True
        except socket.error, e:
            return False

    if checktor1() is True:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython Over Tor"
                },
            "proxies": {
                "http": "http://127.0.0.1:9050",
                "https": "https://127.0.0.1:9050",
                }
            }
        print("Tor configuration set on localhost and port 9050")
    elif checktor2() is True:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython Over Tor"
                },
            "proxies": {
                "http": "http://127.0.0.1:9150",
                "https": "https://127.0.0.1:9150",
                }
            }
        print("Tor configuration set on localhost and port 9150")
    else:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython"
                }
            }
        print("No Tor configuration set, direct connection enabled.")


class dynamic:
    torcon = input("Will you be using Tor to access Twitter (Y/N): ")
    affirmative = ["Y", "yes", "y", "1", "true", "aye", 1, True]
    negative = ["N", "no", "n", "0", "false", "nay", 0, False]

    if torcon.lower() in negative:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython"
                }
            }
        print("No Tor configuration set, direct connection enabled.")
    elif torcon.lower() in affirmative:
        tortype = input("Will you be using the Tor Browser Bundle: ")
        bundle = ["Y", "yes", "y", "1", "true", "aye", "bundle", 1, True]
        if tortype.lower() in bundle:
            client_args = {
                "verify": True,
                "headers": {
                    "User-Agent": "Twython Over Tor"
                    },
                "proxies": {
                    "http": "http://127.0.0.1:9150",
                    "https": "https://127.0.0.1:9150",
                    }
                }
            print("Tor configuration set on localhost and port 9150")
        else:
            client_args = {
                "verify": True,
                "headers": {
                    "User-Agent": "Twython Over Tor"
                    },
                "proxies": {
                    "http": "http://127.0.0.1:9050",
                    "https": "https://127.0.0.1:9050",
                    }
                }
            print("Tor configuration set on localhost and port 9050")
    else:
        client_args = {
            "verify": True,
            "headers": {
                "User-Agent": "Twython"
                }
            }
        print("No Tor configuration set, direct connection enabled.")
