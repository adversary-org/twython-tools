#! /usr/bin/env python

# Copyright (C) Ben McGinnes, 2013
# ben@adversary.org
#

import gnupg

gpg_home = "~/.gnupg"
gpg = gnupg.GPG(gnupghome=gpg_home)

print("""
The passphrase set with this script must be used with the authinfo.py
script or added to that script (the latter is less secure).

Leaving the cipher option blank will use the default or preferred
symmetric cipher.  Otherwise enter the symmetric cipher you wish yo
use (e.g. TWOFISH, AES256, CAMELLIA256, etc.).

See "gpg --version" output for available symmetric ciphers.
""")

data1 = raw_input("Enter Consumer Key (APP_KEY): ")
data2 = raw_input("Enter Consumer Secret (APP_SECRET): ")
data3 = raw_input("Enter Access Token (OAUTH_TOKEN): ")
data4 = raw_input("Enter Access Token Secret (OAUTH_TOKEN_SECRET): ")
phrase = raw_input("Enter the passphrase to secure Twitter access: ")
cipheropt = raw_input("Enter symmetric encryption algorithm to use: ")
file1 = "oauth1.txt.asc"
file2 = "oauth2.txt.asc"
file3 = "oauth3.txt.asc"
file4 = "oauth4.txt.asc"
    
if cipheropt == "":
    cipher = True
else:
    cipher = cipheropt.upper()

gpg.encrypt(data1, None, passphrase=phrase, symmetric=cipher, output=file1)
gpg.encrypt(data2, None, passphrase=phrase, symmetric=cipher, output=file2)
gpg.encrypt(data3, None, passphrase=phrase, symmetric=cipher, output=file3)
gpg.encrypt(data4, None, passphrase=phrase, symmetric=cipher, output=file4)

# Anyone who wants to use their own keys can easily encrypt their
# OAuth data directly on the command line with something like this:
#
# echo "71da22d6fc88352d66f9c921e8c453" | gpg -ear 0xDEADBEEF -o oauth1.txt.asc
