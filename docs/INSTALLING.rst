==========
Installing
==========

Okay, there isn't much to it, but since this might be of interest to
non-geeks I should include something here.

------------------------------------------------------
Quick and Dirty Instructions for Geeks and Power Users
------------------------------------------------------

For the geeks, make sure you've got Python 3.4 or higher installed on
your system, then use pip to install the following:

* Twython
* GPG
* GPGME 1.8.0 or higher with the Python bindings.
* A GPG key capable of encrypting (i.e. with an encryption subkey).

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
operating system and the package.  You need Python 3.4 or higher.

GNU/Linux users may already have Python 3 installed, depending on
distribution.  Mac users will only have Python 2.7 installed by
default and can install 3.4 without any problems.  Mac users may also
choose to install with Homebrew or MacPorts.  Windows users will not
have any version installed by default and can install either or both
branches.  For this software we only care about Python 3.

GPG and GPGME are available from the `GNU Privacy Guard
<https://www.gnupg.org>`_ website.  It is best to install both from
this site, but Windows users are likely to need to use the `GPG4Win
<https://www.gpg4win.org`_ version and many OS X users favour the
`GPGTools <https://www.gpgtools.org>`_ version.  If GPGME is installed
with the Python bindings, the command below to install with pip3 is
not needed for that component.

Once that is installed, open a terminal (or Terminal.app for OS X or
run cmd.exe on Windows) and run the following commands:

    pip3 install twython
    pip3 install gpg

Mac OS X users, Ubuntu users and some other GNU/Linux distribution
users will need (or want) to use sudo with those commands:

    sudo pip3 install twython
    sudo pip3 install gpg


-------------
Configuration
-------------

First check the config.py and make sure the default settings are
correct for your platform.  You will probably only need to change
things by commenting out and uncommenting lines if you're on Windows.

Then decide whether or not you want the scripts to ask about
connecting to or checking for Tor each time or to just go ahead and do
that without interaction.  If the latter then comment out the line
which says `from cargs import dynamic` and uncomment the line saying
`from cargs import dynamic`.

Then make sure you've got your Twitter App Key, App Secret, OAuth
Token and Oauth Secret from the `Twitter App management page <https://twitter.com/settings/applications>`__.

Then run gen-auth.py and enter those details in the prompts.  Enter
the key ID for your GPG key in the prompt.

That's it.  The authorisation codes will be securely protected by GPG
and unlocking them will be handled by gpg-agent.  All that remains is
to use the scripts.

