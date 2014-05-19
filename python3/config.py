from authinfo import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from authinfo import client_args

# If on Linux, BSD, OS X or other UNIX system, change the homedir
# value to the home directory for your user account.  This is usually
# /home/username, but on OS X it is /Users/username instead.
#
# If on Windows, comment out the first five variables and uncomment
# the four lines which follow.  This should be the default location
# for the GPG directory and settings.  Windows users using portable
# implementations of GPG (e.g. GPG4USB) will need to modify the
# homedir and possibly the gpg_home lines accordingly.

homedir = ""  # must be specified, usually /home/username
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
