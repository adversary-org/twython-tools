Requirements
============

* Python 3.2 or above
* Python Requests 2.1.0 or above
* Twython 3.1.0 or above
* PyCrypto 2.6.1 or above
* foad.py (optional)

* A Twitter account
* Twitter API/App keys/tokens
* Internet connectivity


The config.py script may need to be edited before some of the scripts
can be used at all.  Most settings are already present, but the
correct path will need to be set if foad.py is added.  Then the
gen-auth.py script needs to be run to set the GPG encrypted
authentication codes obtained from twitter.com.

If modifying the rounds or counter in SimpleCrypt, which is currently
set to 50,000 (and has a default of 10,000 with the module on PyPI),
the gen-auth.py script will need to be run again as changing that
parameter is enough to make the decryption process fail.


Unless otherwise specified, **DO NOT** include the @ symbol in a Twitter
username, the scripts usually add these if they are required.  Rare
exceptions include replies and basic tweets.


All foad-* and froad-* scripts use the format of:

f[r]oad-script.py <type> <target>

In some cases (replies) with additional fields for status IDs or other
fields are added.

This format matches the old usage of the IRC/text script (foad.py)
rather than most of the other Twitter scripts:

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

As the original foad.py has been updated to take advantage of
argparse, in time these scripts will be updated to match it.

