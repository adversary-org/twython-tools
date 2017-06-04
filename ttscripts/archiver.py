#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import unicode_literals

import datetime
import os
import os.path
import shutil
import sys
import time

dt = datetime.time
dd = datetime.date
ddt = datetime.datetime
ls = os.listdir
op = os.path
expandusr = op.expanduser
fpath = op.abspath
rpath = op.realpath

#homedir = "C:\Documents and Settings\Administrator\Application Data"
#homebin = ""  # set this if you move foad.py to another location
#              # (e.g. homedir+"/bin/" or "/usr/local/bin/"
#foad = "foad.py"  # Add foad.py to this directory or add to path.
homedir = expandusr("~")
homebin = homedir+"/bin"
lindocs = homedir
macdocs = "{0}/Documents".format(homedir)
windocs = "{0}/My Documents".format(homedir)
curdir = fpath(op.curdir)
inputdir = "{0}/InputFiles".format(curdir)
indir = rpath(inputdir)
outputdir = "{0}/OutputFiles".format(curdir)
outdir = rpath(outputdir)
foad = homebin+"/foad.py"
arcdir = ""  # relative path to move files to

if sys.platform == "darwin":
    docdir = macdocs
elif sys.platform == "win32":
    docdir = windocs
else:
    docdir = lindocs

archive = docdir+arcdir
tmpmod = str(round(time.time()))
temparc = "{0}-temp-{1}".format(archive, tmpmod)

if op.exists(archive) is False:
    os.mkdir(archive)
elif op.exists(archive) is True and op.isdir(archive) is False:
    broken = archive
    os.mkdir(temparc)
    archive = temparc
elif op.exists(archive) is True and op.isdir(archive) is True:
    pass

# arcin = archive+"/data-input"
# arcout = archive+"/data-output"
arcin = "{0}/{1}_data-input".format(archive, dd.today().isoformat())
arcout = "{0}/{1}_data-output".format(archive, dd.today().isoformat())

if op.exists(arcin) is False:
    os.mkdir(arcin)
elif op.exists(arcin) is True and op.isdir(arcin) is False:
    shutil(arcin, "arcin-{0}".format(str(time.time())))
    os.mkdir(arcin)
else:
    pass

if op.exists(arcout) is False:
    os.mkdir(arcout)
elif op.exists(arcout) is True and op.isdir(arcout) is False:
    shutil(arcout, "arcout-{0}".format(str(time.time())))
    os.mkdir(arcout)
else:
    pass

infiles = []
outfiles = []
readin = "{0}/README.rst".format(indir)
readout = "{0}/README.rst".format(outdir)

for i in range(len(ls(outdir))):
    f = "{0}/{1}".format(outdir, ls(outdir)[i])
    if op.isfile(f) is True and f is not readout:
        outfiles.append(f)
    else:
        pass


for i in range(len(ls(indir))):
    f = "{0}/{1}".format(indir, ls(indir)[i])
    if op.isfile(f) is True and f is not readin:
        infiles.append(f)
    else:
        pass


lif = len(infiles)
lof = len(outfiles)

for i in range(lif):
    if infiles[i].endswith("README.rst"):
        infiles.remove(infiles[i])

for i in range(lof):
    if outfiles[i].endswith("README.rst"):
        outfiles.remove(outfiles[i])


li = len(infiles)
lo = len(outfiles)

if li > 0:
    for i in range(li):
        shutil.move(infiles[i], arcin)

if lo > 0:
    for i in range(lo):
        shutil.move(outfiles[i], arcout)


cleaner = "{0}/makeclean.py".format(curdir)

if op.isfile(cleaner) is True:
    import makeclean
else:
    pass
