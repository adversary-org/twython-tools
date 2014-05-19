#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter.verify_credentials()

filename = raw_input("File name of recipient list (text file): ")
mesg = raw_input("Direct message (140 characters max): ")

afile = open(filename, "r")
adata = afile.readlines()
afile.close()
for string in adata:
    target = string.strip()
    twitter.send_direct_message(screen_name=target, text=mesg)
