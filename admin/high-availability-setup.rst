.. _high-availability-setup:

#######################
High Availability Setup
#######################

Infrastructure
==============


Production
----------

IP/hostname: netxms-prod

PostgreSQL version: 14.3

PostgreSQL systemd service name: postgresql-14.service

PostgreSQL data directory: /u0fs1/pg-data/14

PostgreSQL port: 5432

NetXMS installation prefix: /opt/netxms

NetXMS system service names: netxmsd.service, nxagentd.service, nxreportd.service


DR
--

IP/hostname: netxms-dr

PostgreSQL version: 14.2

PostgreSQL systemd service name: postgresql-14.service

PostgreSQL data directory: /u0fs1/pg-data/14

PostgreSQL port: 5432

NetXMS installation prefix: /opt/netxms

NetXMS system service names: netxmsd.service, nxagentd.service, nxreportd.service


Switchover procedure
====================

Switchover steps:

 #. Confirm which node is currently active

    #. The process “netxmsd” should be running only on active node (check with “ps” or “pgrep”)
    #. Run “pg_replica_state” to get the current state of the database on this server. The active node will be marked as “Sender / Primary”.

 #. Stop netxmsd on active node:

    #. Run “systemctl stop netxmsd”
    #. Make sure it is stopped (with “ps” or “pgrep”)

 #. Switch active database instance to standby (read-only) mode:

    #. Run “sudo -u postgres touch /u0fs1/pg-data/14/standby.signal”
    #. Run “systemctl restart postgresql-14”
    #. Check logs (`/u0fs1/pg-data/14/log/postgresql-*.log`), it should contain records:

       #. “starting PostgreSQL...”
       #. “consistent recovery state reached at...”
       #. “database system is ready to accept read only connections”

 #. Promote another node as new PostgreSQL sender node:

    #. On second node run `sudo -u postgres psql -c 'select pg_promote()'`
    #. Check log file for following records:

       #. “...received promote request”
       #. “selected new timeline ID: ...”
       #. “archive recovery complete”
       #. “database system is ready to accept connections” (non-readonly!)

 #. Start netxmsd on another node

The switchover procedure is identical when switching from PROD to DR and from DR to PROD.

Failover procedure
==================

Follow the switchover procedure from item 4 onwards.

Failover recovery
=================

Once a failed server (which was sender before the failover) is up and running, you need to
switch it to replica mode.

 #. Stop PostgreSQL (“systemctl stop postgresql-14”) on the failed node
 #. Run “sudo -u postgres touch /u0fs1/pg-data/14/standby.signal” to switch it to replica mode
 #. Unwind this DB instance to the state where it is in sync with the current sending server: 

    run `sudo -u postgres /usr/pgsql-14/bin/pg_rewind --target-pgdata=/u0fs1/pg-data/14 --source-server="host=ACTIVE_DB user=postgres password=PASSWORD"".`
    
    ACTIVE_DB should point to the current sender instance (netxms-prod or netxms-dr).
 #. Start PostgreSQL instance with “systemctl start postgresql-14”
 #. Check logs and make sure that the database is started and it is in read only
    mode. Once recovery is completed, a switchover procedure might be performed
