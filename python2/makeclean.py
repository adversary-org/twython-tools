#! /usr/bin/env python

"""
Make Clean program directory (CLI)

Command line program to remove old files and pre-compiled bytecode.


Copyright (C) Benjamin D. McGinnes, 2006-2013

"""

__author__ = 'Ben McGinnes <ben@adversary.org>'
__copyright__ = 'Copyright (C) Benjamin D. McGinnes, 2006-2013'
__copyrightu__ = u'Copyright \xa9 Benjamin D. McGinnes, 2006-2013'.encode('UTF-8')
__copyrightl__ = u'Copyright \xa9 Benjamin D. McGinnes, 2006-2013'.encode('iso-8859-1')

import os

cleanUp = "rm -rf \~/ ; rm -f *.pyc ; rm -f *~ ; rm -f Documentation/*~ ; chmod 755 makeclean.py"
cleanWin = "del *.pyc"

a = os.name
b = "posix"
c = "nt"
d = "mac"
e = "os2"
f = "ce"
g = "java"
h = "riscos"

if a == b:
    os.system(cleanUp)
elif a == c:
    os.system(cleanWin)
elif a == d:
    os.system(cleanUp)
elif a == e:
    print("Nice, but your OS has gone the way of the Dodo.")
elif a == f:
    os.system(cleanWin)
elif a == g:
    print("That's not platform independent.")
elif a == h:
    print("You are not hardcore.")
else:
    os.system(cleanUp)
