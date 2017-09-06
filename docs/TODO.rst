=====
To Do
=====

---------------
Local Databases
---------------

Currently output or records resulting from the scripts and API calls
are stored as text or JSON data in the OutputFiles directory.  This is
fine for static content, usually saved as a timestamped snapshot of
the time the script was run.  It is not, however, fine for datasets
which may need to be updated in a form beyond simply appending new
data, as may be the case with Twitter lists.  For data of this type a
database is a better option.

Since these scripts are intended to be lightweight and only accessed
by the local user maintaining the scripts, a full SQL database like
Postgres, Oracle or SQL Server is definitely **overkill**.  As is the
use of SQL-like databses such as MySQL and MariaDB.  A local file is
enough for updating by and reference of these scripts, as a
consequence the most appropriate solution is to use one or more SQLite
database files.

Support for SQLite is included in the Python 3 DB-API 2.0 interface
and does not result in additional software requirements.  Python
documentation for the `sqlite3 module is available here
<https://docs.python.org/3.6/library/sqlite3.html>`_.


---------------
List Management
---------------

Existing scripts to create lists, add and remove list membership and
so on should be updated to create and maintain a local databse of
current data.  Though users will generally use screen names for
recording this data, the Twitter user ID will always be recorded and
used as the authoritive reference point as that is the one constant
identifier with Twitter accounts.

It may also be possible or preferred to maintain a local historical
record of these updates.  This is particularly relevant for
maintaining a record of blocklists, mute lists and a record of prior
filtering or listing of users who may utilise blocking to circumvent
the use of Twitter lists to classify them.  Thus it will be possible
to record a local reason for a private filter, mute or block that
cannot be lost, even if that user subsequently utilises a block on
Twitter to remove themselves from any private Twitter lists which may
be used.


List Conversion
---------------

Currently the `view-lists.py` amd `view-list-info.py` scripts will
write text output of the total number of lists created andthe current
membership and subscriber data for those lists.  It should be possible
to use these scripts (most likely new scripts based on them) to write
all relevant data to a databse file containing the list membership,
maybe the subscribers (though that may fluctuate a great deal and may
not be that useful) and possibly additional notes about either the
member or the reason for adding them.

Subsequent additions to and substractions from lists can then continue
with the relevant other scripts modified to access local list based
database files.  It will therefore be necessary to maintain list based
database files with a consistent naming convention which matches lists
to the list owner's username or user ID number and the list's slug
name.  There may be problems if an existing list slug name is changed
in the future.


Local Files
-----------

It is highly likely that it will be preferred to maintain different
database types in separate subdirectories of the `Data/` directory to
separate list specific databse files from other databse files.

It will also be possible to use local files to make a locally filtered
stream of tweets from list member accounts in the same way as
Twitter's lists are currently used, but without the need to have a
list saved with Twitter, either public or private.  Since Twitter
lists already provide this function, this is not a priority.  The
preference is to simply maintain a local database of current list data
which may subsequently be used to restore a list if Twitter decides to
delete lists in the future.  This situation has already occurred and
has been reported by `Asher Wolf<https://twitter.com/Asher_Wolf>`_,
following an update of at least one Twitter app.

Rather than creating a dynamic stream from local data, the preferred
use of a local database for creating filtered timelines is to either
restore a list which may have been deleted or to create a temporary
private list with the relevant membership data and then delete that
list when the stream is no longer required.


Shared Data
-----------

Some Twitter accounts are organisational accounts used by multiple
individuals and consequently they are maintained from multiple
locations.  These scripts cannot necessarily provide synchronised data
sets for those types of accounts.  Nevertheless it should still be
possible to maintain relevant offsite records of such accounts.  One
option is to convert to a full SQL server (but that's even less of a
priority than creating timeline streams from local databases).
Alternatively creating a SQL dump file of the account's database files
and sharing those amongst the account managers will do the job.

This type of manual manipulation of database content may be best
served by the use of third party tools.  Though it is a proprietary
and paid product, I've generally found Navicat's database tools to be
incredibly useful when playing with a whole bunch of database types;
usually Postgres, MySQ, MariaDB and SQLite).

