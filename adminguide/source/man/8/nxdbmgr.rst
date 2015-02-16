:orphan:

nxdbmgr
=======

Synopsis
--------

**nxdbmgr** [*options*] {
[check] | [unlock] | [upgrade] | [reindex] |
[init *file*] | [batch *file*] | [export *file*] | [import *file*] |
[get *name*] | [set *name* *value*]
}

Description
-----------

:program:`nxdbmgr` is a tool for ...

Unless the ``-h``, or ``--help`` option is given, one of the commands bellow
must be present.

check
    Check database consistency

unlock
    Unlock database instance after server crash / unclean shutdown

upgrade
    Upgrade existing database schema and data to latest version

reindex
    Rebuild index on tables with collected data

init *file*
    Description

batch *file*
    Description

export *file*
    Description

import *file*
    Description

get *name*
    Description

set *name *value*
    Description

Options
-------

-c <file>       Use alternate configuration file. Default is {search}
-d              Check collected data (may take very long time).
-f              Force repair - do not ask for confirmation.
-h              Display help and exit.
-I              Create new tables with TYPE=InnoDB (MySQL specific).
-M              Create new tables with TYPE=MyISAM (MySQL specific).
-N              Do not replace existing configuration value (specific to "set"
                command).
-q              Quiet mode (don't show startup banner).
-t              Enable trace mode (show executed SQL queries).
-v              Display version and exit.
-X              Ignore SQL errors when upgrading (**USE WITH CAUTION!**)

Examples
--------

nxdbmgr init /usr/share/netxms/sql/netxms/sql/dbinit_pgsql.sql
    Description

nxdbmgr upgrade
    Description

nxdbmgr get EnableZoning
    Get current value for option ``EnableZoning``

nxdbmgr set EnableZoning 1
    Set option ``EnableZoning`` to "1"

Files
-----

/etc/netxmsd.conf
    Default configuration file

Exit Status
-----------

0
    Success

1
    Invalid command line arguments

2
    Configuration file malformed or cannot be loaded

3
    Unable to load and initialize database driver (as specified by ``DBDriver``
    parameter in configuration file)

4
    Unable to connect to database

5
    Unable to determine current database version.

See Also
--------

:manpage:`netxmsd.conf(5)`

