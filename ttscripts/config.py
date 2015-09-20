# -*- coding: utf-8 -*-

# You can set permanent proxy and header settings in cargs.permanent,
# then swap the two options around (it may be preferable to delete the
# dynamic class if the permanent one is set):

# from cargs import permanent
from cargs import dynamic
from authinfo import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
import os.path
expandusr = os.path.expanduser
fpath = os.path.abspath
rpath = os.path.realpath

homedir = expandusr("~")
curdir = fpath(".")
inputdir = "{0}/InputFiles".format(curdir)
indir = rpath(inputdir)
outputdir = "{0}/OutputFiles".format(curdir)
outdir = rpath(outputdir)
#homedir = "C:\Documents and Settings\Administrator\Application Data"
#homebin = ""  # set this if you move foad.py to another location
#              # (e.g. homedir+"/bin/" or "/usr/local/bin/"
#foad = homebin+"foad.py"
foad = "foad.py"  # Add foad.py to this directory or add to path.
