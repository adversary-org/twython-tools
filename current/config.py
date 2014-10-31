# -*- coding: utf-8 -*-

from authinfo import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from authinfo import client_args
from os.path import expanduser

homedir = expanduser("~")
#homedir = "C:\Documents and Settings\Administrator\Application Data"
#homebin = ""  # set this if you move foad.py to another location
#              # (e.g. homedir+"/bin/" or "/usr/local/bin/"
#foad = homebin+"foad.py"
foad = "foad.py"  # Add foad.py to this directory or add to path.
