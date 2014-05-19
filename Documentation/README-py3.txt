Requirements

* Python 3.2 or above
* GNU Privacy Guard (GPG) 1.4 or 2.0
* Python Requests 2.1.0 or above
* Twython 3.1.0 or above
* Python GnuPG 0.3.5 or above

* A Twitter account
* Twitter API/App keys/tokens
* Internet connectivity

==========

The config.py script will need to be edited before the scripts can be
used at all.  Most settings are already present, but the homedir will
need to be specified for Linux and OS X users.  Then the gen-auth.py
script needs to be run to set the GPG encrypted authentication codes
obtained from twitter.com.

==========

Unless otherwise specified, DO NOT include the @ symbol in a Twitter
username, the scripts usually add these if they are required.  Rare
exceptions include replies and basic tweets.

==========

