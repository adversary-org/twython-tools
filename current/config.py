from authinfo import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from authinfo import client_args
from os.path import expanduser

homedir = expanduser("~")
gpg_home = homedir+"/.gnupg"
gpg_homeshort = "~/.gnupg" # optional
pub_ring = gpg_home+"/pubring.gpg"
sec_ring = gpg_home+"/secring.gpg"
#homedir = "C:\Documents and Settings\Administrator\Application Data"
#gpg_home = homedir+"\GnuPG"
#pub_ring = gpg_home+"\pubring.gpg"
#sec_ring = gpg_home+"\secring.gpg"
pring = []
sring = []
pring.append(pub_ring)
sring.append(sec_ring)
#homebin = ""  # set this if you move foad.py to another location
#              # (e.g. homedir+"/bin/" or "/usr/local/bin/"
#foad = homebin+"foad.py"
foad = "foad.py"  # Add foad.py to this directory or add to path.
