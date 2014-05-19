#!/usr/bin/env python3

##
# Copyright (C) Ben McGinnes, 2013-2014
# ben@adversary.org
# OpenPGP/GPG key:  0x321E4E2373590E5D
#
# Version:  0.0.1
#
# BTC:  19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk
# License:  GPLv3
#
# https://www.gnu.org/copyleft/gpl.html
#
# Requirements:
#
# * Python 3.2 or later (developed with Python 3.4.x)
#
# Options and notes:
#
# Usage:  
#
##

__author__ = "Ben McGinnes <ben@adversary.org>"
__copyright__ = "Copyright \u00a9 Benjamin D. McGinnes, 2013-2014"
__copyrighta__ = "Copyright (C) Benjamin D. McGinnes, 2013-2014"
__license__ = "GPLv3 or WTFNMFPL"
__version__ = "0.0.1"
__bitcoin__ = "19J2Dc5DTztWRWMPcLwshj96NAnXAxtCvk"


import sys

l = len(sys.argv)

if l == 2:
    filename = sys.argv[1]
    pattern = input("Enter the pattern to match and remove: ")
elif l >= 3:
    filename = sys.argv[1]
    logrus = []
    for i in range(l -2):
        logrus.append(str(sys.argv[i + 2]))
    pattern = " ".join(logrus)
else:
    filename = input("Enter the name of the file: ")
    pattern = input("Enter the pattern to match and remove: ")

f = open(filename, "r")
lines = f.readlines()
f.close()

f = open(filename, "w")
for line in lines:
    if line != pattern + "\n":
        f.write(line)
f.close()
