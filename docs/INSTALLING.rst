==========
Installing
==========

Okay, there isn't much to it, but since this might be of interest to
non-geeks I should include something here.

------------------------------------------------------
Quick and Dirty Instructions for Geeks and Power Users
------------------------------------------------------

For the geeks, make sure you've got Python 3.2 or higher installed on
your system, then use pip to install the following:

* Twython
* PyCrypto

Everything else is optional or included.  Then dump the ttscripts
directory somewhere in your path.  If you're including FOAD, put
foad.py somewhere in your path (and optionally symlink foad to
foad.py) too.


---------------------
Detailed Instructions
---------------------

This is for those of you with near zero experience at anything even
vaguely geeky (but are willing to run scripts in a terminal, shell or
dos-style prompt).

The first thing you need is Python 3, so pop over to the `Python
website <https://www.python.org>`_ and download the latest version of
Python 3 (ignore the Python 2 on offer), the site should detect your
operating system and the package.  You need Python 3.3 or higher and
as of 2015 the current version is 3.4.2.

GNU/Linux users may already have Python 3 installed, depending on
distribution.  Mac users will only have Python 2.7 installed by
default and can install 3.4 without any problems.  Mac users may also
choose to install with Homebrew or MacPorts.  Windows users will not
have any version installed by default and can install either or both
branches.  For this software we only care about Python 3.

Once that is installed, open a terminal (or Terminal.app for OS X or
run cmd.exe on Windows) and run the following commands:

    pip3 install twython
    pip3 install pycrypto

Mac OS X users, Ubuntu users and some other GNU/Linux distribution
users will need (or want) to use sudo with those commands:

    sudo pip3 install twython
    sudo pip3 install pycrypto


