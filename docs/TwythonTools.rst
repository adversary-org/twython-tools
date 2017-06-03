Requirements
============

* Python 3.4 or above
* Python Requests 2.1.0 or above
* Twython 3.3.0 or above
* GPG current version, ideally on the 2.1 branch
* GPGME 1.8.0 or above
* A GPG Key with encryption subkey.
* foad.py (optional)
* A Twitter account
* Twitter API/App keys/tokens
* Internet connectivity


The ``config.py`` script may need to be edited before some of the
scripts can be used at all.  Most settings are already present, but
the correct path will need to be set if ``foad.py`` is added.  Then
the ``gen-auth.py`` script needs to be run to set the GPG encrypted
authentication codes obtained from twitter.com.


Unless otherwise specified, **DO NOT** include the @ symbol in a
Twitter username, the scripts usually add these if they are required.
Rare exceptions include replies and basic tweets.  So if using the
foad.py script with ``tweet-basic.py`` via a grave accented call (see
below) the @ symbol should be used with the foad.py -n or -r flags.


All foad-* and froad-* scripts use the format of:

::

    f[r]oad-script.py <type> <target>

In some cases (replies) with additional fields for status IDs or other
fields are added.

This format matches the old usage of the IRC/text script (``foad.py``)
rather than most of the other Twitter scripts:

::
   
    foad.py <type> [<target>]

In the case of the IRC/text script it is still quite possible the
script will be used without a target, which is why the target field
comes after the type.

Of the Twitter scripts, only the foad-tweet.py script might be used
without a target specified.  All the others require a target or they
fail to work.

Both the ``foad-tweet.py`` and ``foad-dm.py`` scripts can be used in
conjunction with an alternate name (e.g. a full name).  That variable
is set last so that it can be included on the command line without
requiring the use of quotation marks.

As the original ``foad.py`` has been updated to take advantage of
argparse, in time these scripts will be updated to match it.

Note that the foad and froad scripts have been archived in their own
branch and the recommended method of using this script is now to use
the secondary method described below by embedding a foad command in
grave accents.

A second method of using the ``foad.py`` script (or any other
script/command which produces text output) is to call it with the
standard ``tweet-basic.py`` or ``tweet-dm.py`` scripts and the script
called within grave accents (i.e. \` the character on the same key as
the tilde character).  For example:

::
   
    tweet-basic.py \`foad.py -f fascinating -n "George Brandis"\`

Would send a tweet which said:

::
   
    Fascinating story, George Brandis, in what chapter do you shut the fuck up?

To insert any other text before or after that output it needs to be
called through the foad.py script, it cannot be included outside the
command line.  This includes appending hashtags to the comment.

The result should be the same as using
``subprocess.check_output('foad.py -f fascinating -n "George Brandis"', shell=True).decode("utf-8").strip()`` within a script.  Obviously there
is no additional danger to using shell=True in a situation where the
user already has shell access.
