Requirements

* Python 2.6 or 2.7
* GNU Privacy Guard 1.4 or 2.0
* Python Requests 2.0.0 or higher
* Twython 3.1.0 or higher
* Python GnuPG 0.3.5 or higher

* A Twitter account
* Twitter API/App keys/tokens
* Internet connectivity

==========

All foad-* and froad-* scripts use the format of:

f[r]oad-script.py $target $type

With the exception of the foad-tweet.py script which uses:

foad-tweet.py $type $target

This is generally different from the IRC/text script (foad.py) called
by these scripts.

In part this is to keep the Twitter scripts in line with the other
inoffensive scripts on which these ones are based.  The type is there
instead of the normally entered text.  In the case of the IRC/text
script it is still quite possible the script will be used without a
target, which is why the target field comes after the type.

Of the Twitter scripts, only the foad-tweet.py script might be used
without a target specified, hence the different order.  All the others
require a target or they fail to work.

Both the foad-tweet.py and foad-dm.py scripts can be used in
conjunction with an alternate name (e.g. a full name).  That variable
is set last so that it can be included on the command line without
requiring the use of quotation marks.
