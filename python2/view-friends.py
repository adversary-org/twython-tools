#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import math
from twython import Twython
from config import *

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#creds = twitter.verify_credentials()

user = raw_input("Enter Twitter handle to get friends of: ")
suser = twitter.show_user(screen_name=user)
fnum = 200
pnum = int(math.ceil(float(suser["friends_count"]) / fnum))

pages = []
for i in range(pnum):
    pages.append("p"+str(i+1))

oldpages = []
for i in range(pnum):
    oldpages.append("p"+str(i))

p0 = { "next_cursor": -1 } # So the following exec() call doesn't fail.

for i in range(pnum):
    exec(pages[i]+" = twitter.get_friends_list(screen_name=user, count=fnum, skip_status=1, cursor="+oldpages[i]+"['next_cursor'])")

friends = []

for p in range(pnum):
    try:
        exec("for i in range(fnum): friends.append("+pages[p]+"['users'][i])")
    except(IndexError):
        pass

print(len(friends))

for x in friends:
    print("""Name:  %s
Username:  %s
""" % (x["name"], x["screen_name"]))
