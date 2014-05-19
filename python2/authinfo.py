#!/usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import gnupg

gpg_home = "~/.gnupg"
gpg = gnupg.GPG(gnupghome=gpg_home)

# For most users the passphrase should be handled by gpg-agent.  This
# is especially the case if encrypting to one's own key on the command
# line for the four files instead of using gen-key.py.

phrase = raw_input("Enter the passphrase to authorise access to Twitter: ")
#phrase = "" # optionally insert passphrase directly here (a bad idea).

afile = open("oauth1.txt.asc", "rb")
doauth1 = gpg.decrypt_file(afile, passphrase=phrase)
afile.close()

bfile = open("oauth2.txt.asc", "rb")
doauth2 = gpg.decrypt_file(bfile, passphrase=phrase)
bfile.close()

cfile = open("oauth3.txt.asc", "rb")
doauth3 = gpg.decrypt_file(cfile, passphrase=phrase)
cfile.close()

dfile = open("oauth4.txt.asc", "rb")
doauth4 = gpg.decrypt_file(dfile, passphrase=phrase)
dfile.close()

APP_KEY = doauth1.data.strip()
APP_SECRET = doauth2.data.strip()
OAUTH_TOKEN = doauth3.data.strip()
OAUTH_TOKEN_SECRET = doauth4.data.strip()

