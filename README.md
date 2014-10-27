Twython Tools
=============

Command line scripts and tools for implementing Twython functions.

Incorporates functions from other Python libraries and modules,
including twython, requests, python-gnupg and foad.py.

Also uses GPG and Tor.

The scripts in python2/ are legacy scripts and only present for
reference.

The scripts in python3/ are what I use and are actively maintained.

The foad.py script is [available here](https://github.com/adversary-org/foad).

Python version specific information is in the Documentation/
directory.


## Contacting me

My email address is in most of the scripts in this project as well as
included in my GPG key as the primary user ID.

A minimised copy of my GPG key is in the Documentation/ directory
(ben-key-min.asc), this version does not include all the current
signatures.  Refreshing that key from the key servers will restore
those signatures.

To get my key directly from the servers run:

    gpg --recv-keys 0x321E4E2373590E5D

To refresh my key if it is already in your keyring run:

    gpg --refresh-keys 0x321E4E2373590E5D

You can also visit my [website](http://www.adversary.org/) or [follow me on Twitter](https://twitter.com/benmcginnes).


## Using the Scripts

The scripts generally take their parameters on the command line, but
are also able to receive those parameters through interactive text
prompts.  Generally I recommend the latter at least until you are
familiar enough with the order to run them without those prompts.

