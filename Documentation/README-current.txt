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

All foad-* and froad-* scripts use the format of:

f[r]oad-script.py <type> <target>

In some cases (replies) with additional fields for status IDs.

This format matches the IRC/text script (foad.py) rather than most of
the other Twitter scripts:

foad.py <type> [<target>]

In the case of the IRC/text script it is still quite possible the
script will be used without a target, which is why the target field
comes after the type.

Of the Twitter scripts, only the foad-tweet.py script might be used
without a target specified.  All the others require a target or they
fail to work.

Both the foad-tweet.py and foad-dm.py scripts can be used in
conjunction with an alternate name (e.g. a full name).  That variable
is set last so that it can be included on the command line without
requiring the use of quotation marks.
