.. _database-monitoring:

===================
Database monitoring
===================

There are several :ref:`subagents <subagent_list>` for database monitoring: DB2,
Informix, Oracle, MySQL, MongoDB, PostgreSQL. Below we will describe how to
configure and use these subagents. Besides it's also possible to monitor other
types of databases supported by |product_name| server(:ref:`link to supported
database list<supported-db-list>`) using database query subagent as these
databases support receiving performance parameters using queries. This subagent
details are described in :ref:`dbquery` chapter.

.. _oracle-subagent:

Oracle
======

|product_name| subagent for Oracle DBMS monitoring (further referred to as
Oracle subagent) monitors one or more instances of Oracle databases and reports
various database-related metrics.

All metrics available from Oracle subagent are collected or calculated once per
minute thus it's recommended to set DCI poll interval for these items to 60
seconds or more. All metrics are obtained or derived from the data available in
Oracle's data dictionary tables and views through regular select queries. Oracle
subagent does not monitor any of the metrics related to lower level database
layers, such as database processes. Monitoring of such metrics can be achieved
through the standard |product_name| functionality.

Pre-requisites
--------------

An Oracle user with the role **select_catalog_role** assigned.

Required rights can be assigned to user with the following query:

.. code-block:: sh

   grant select_catalog_role to user;

Where *user* is the user configured in Oracle subagent for database access.


Configuration file
------------------

Oracle subagent can be configured using XML configuration file (usually created
as separate file in configuration include directory), or in simplified INI format,
in main agent configuration file (nxagentd.conf).

Database definition supports the following parameters:


.. list-table::
   :widths: 20 70 20
   :header-rows: 1

   * - Parameter
     - Description
     - Default value
   * - Id
     - Database identifier. It will be used to address this database in
       parameters.
     -
   * - TnsName
     - Database TNS name or connection string.
     -
   * - ConnectionTTL
     - Time in seconds. When this time gets elapsed, connection to the DB is
       closed and reopened again.
     - 3600
   * - Username
     - User name for connecting to database.
     -
   * - Password
     - Database user password. When using INI format, remember to enclose
       password in double quotes ("password") if it contains # character. This
       parameter automatically detects and accepts password encrypted with
       :ref:`nxencpasswd-tools-label` tool.
     -
   * - EncryptedPassword
     - Database user password encrypted with :ref:`nxencpasswd-tools-label`
       tool. DEPRECATED. Use Password instead.
     -


XML configuration allows to specify multiple databases in the **oracle**
section. Each database description must be surrounded by database tags with the
**id** attribute. It can be any unique integer and instructs the Oracle subagent
about the order in which database sections will be processed.

Sample Oracle subagent configuration file in XML format:

.. code-block:: sh

   <config>
       <agent>
           <subagent>oracle.nsm</subagent>
       </agent>
       <oracle>
           <databases>
               <database id="1">
                   <id>DB1</id>
                   <tnsname>TEST</tnsname>
                   <username>NXMONITOR</username>
                   <password>NXMONITOR</password>
               </database>
               <database id="2">
                   <id>DB2</id>
                   <tnsname>PROD</tnsname>
                   <username>NETXMS</username>
                   <password>PASSWORD</password>
               </database>
           </databases>
       </oracle>
   </config>


You can specify only one database when using INI configuration format. If you
need to monitor multiple databases from same agent, you should use configuration
file in XML format.

Sample Oracle subagent configuration file in INI format:

.. code-block:: sh

   [ORACLE]
   ID = DB1
   Name = TEST
   Username = dbuser
   Password = "mypass123"


Metrics
-------

When loaded, Oracle subagent adds the following metrics to agent (all metrics require database ID as first argument):

+---------------------------------------------------------+------------------------------------------------------------------------------+
| Metric                                                  | Description                                                                  |
+=========================================================+==============================================================================+
| Oracle.CriticalStats.AutoArchivingOff(*dbid*)           | Archive logs enabled but auto archiving off (YES/NO)                         |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.DatafilesNeedMediaRecovery(*dbid*) | Number of datafiles that need media recovery                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.DFOffCount(*dbid*)                 | Number of offline datafiles                                                  |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.FailedJobs(*dbid*)                 | Number of failed jobs                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.FullSegmentsCount(*dbid*)          | Number of segments that cannot extend                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.RBSegsNotOnlineCount(*dbid*)       | Number of rollback segments not online                                       |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.CriticalStats.TSOffCount(*dbid*)                 | Number of offline tablespaces                                                |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Cursors.Count(*dbid*)                            | Current number of opened cursors system-wide                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.AvgIoTime(*dbid*, *datafile*)           | Average time spent on single I/O operation for *datafile* in milliseconds    |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.Blocks(*dbid*, *datafile*)              | *datafile* size in blocks                                                    |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.BlockSize(*dbid*, *datafile*)           | *datafile* block size                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.Bytes(*dbid*, *datafile*)               | *datafile* size in bytes                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.FullName(*dbid*, *datafile*)            | *datafile* full name                                                         |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.MaxIoReadTime(*dbid*, *datafile*)       | Maximum time spent on a single read for *datafile* in milliseconds           |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.MaxIoWriteTime(*dbid*, *datafile*)      | Maximum time spent on a single write for *datafile* in milliseconds          |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.MinIoTime(*dbid*, *datafile*)           | Minimum time spent on a single I/O operation for *datafile* in milliseconds  |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.PhysicalReads(*dbid*, *datafile*)       | Total number of physical reads from *datafile*                               |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.PhysicalWrites(*dbid*, *datafile*)      | Total number of physical writes to *datafile*                                |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.ReadTime(*dbid*, *datafile*)            | Total read time for *datafile* in milliseconds                               |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.Status(*dbid*, *datafile*)              | *datafile* status                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.Tablespace(*dbid*, *datafile*)          | *datafile* tablespace                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DataFile.WriteTime(*dbid*, *datafile*)           | Total write time for *datafile* in milliseconds                              |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.CreateDate(*dbid*)                        | Database creation date                                                       |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.IsReachable(*dbid*)                       | Database is reachable (YES/NO)                                               |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.LogMode(*dbid*)                           | Database log mode                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.Name(*dbid*)                              | Database name                                                                |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.OpenMode(*dbid*)                          | Database open mode                                                           |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.DBInfo.Version(*dbid*)                           | Database version                                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Dual.ExcessRows(*dbid*)                          | Excessive rows in DUAL table                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Instance.ArchiverStatus(*dbid*)                  | Archiver status                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Instance.Status(*dbid*)                          | Database instance status                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Instance.ShutdownPending(*dbid*)                 | Is shutdown pending (YES/NO)                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Instance.Version(*dbid*)                         | DBMS Version                                                                 |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Objects.InvalidCount(*dbid*)                     | Number of invalid objects in DB                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.CacheHitRatio(*dbid*)                | Data buffer cache hit ratio                                                  |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.DictCacheHitRatio(*dbid*)            | Dictionary cache hit ratio                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.DispatcherWorkload(*dbid*)           | Dispatcher workload (percentage)                                             |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.FreeSharedPool(*dbid*)               | Free space in shared pool (bytes)                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.Locks(*dbid*)                        | Number of locks                                                              |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.LogicalReads(*dbid*)                 | Number of logical reads                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.LibCacheHitRatio(*dbid*)             | Library cache hit ratio                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.MemorySortRatio(*dbid*)              | PGA memory sort ratio                                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.PhysicalReads(*dbid*)                | Number of physical reads                                                     |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.PhysicalWrites(*dbid*)               | Number of physical writes                                                    |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Performance.RollbackWaitRatio(*dbid*)            | Ratio of waits for requests to rollback segments                             |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Sessions.Count(*dbid*)                           | Number of sessions opened                                                    |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Sessions.CountByProgram(*dbid*, *program*)       | Number of sessions opened by specific program                                |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Sessions.CountBySchema(*dbid*, *schema*)         | Number of sessions opened with specific schema                               |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.Sessions.CountByUser(*dbid*, *user*)             | Number of sessions opened with specific Oracle user                          |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.BlockSize(*dbid*, *tablespace*)       | *tablespace* block size                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.DataFiles(*dbid*, *tablespace*)       | Number of datafiles in *tablespace*                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.FreeBytes(*dbid*, *tablespace*)       | Free bytes in *tablespace*                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.FreePct(*dbid*, *tablespace*)         | Free space percentage in *tablespace*                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.Logging(*dbid*, *tablespace*)         | *tablespace* logging mode                                                    |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.Status(*dbid*, *tablespace*)          | *tablespace* status                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.TotalBytes(*dbid*, *tablespace*)      | Total size in bytes of *tablespace*                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.Type(*dbid*, *tablespace*)            | *tablespace* type                                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.UsedBytes(*dbid*, *tablespace*)       | Used bytes in *tablespace*                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------+
| Oracle.TableSpace.UsedPct(*dbid*, *tablespace*)         | Used space percentage in *tablespace*                                        |
+---------------------------------------------------------+------------------------------------------------------------------------------+


Lists
-----

When loaded, Oracle subagent adds the following lists to agent:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| List                                   | Description                                                                                                |
+========================================+============================================================================================================+
| Oracle.DataFiles(*dbid*)               | All known datafiles in database identified by *dbid*.                                                      |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Oracle.DataTags(*dbid*)                | All data tags for database identified by *dbid*. Used only for internal diagnostics.                       |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Oracle.TableSpaces(*dbid*)             | All known tablespaces in database identified by *dbid*.                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+


Tables
------

When loaded, Oracle subagent adds the following tables to agent:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Table                                  | Description                                                                                                |
+========================================+============================================================================================================+
| Oracle.DataFiles(*dbid*)               | Datafiles in database identified by *dbid*.                                                                |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Oracle.Sessions(*dbid*)                | Open sessions in database identified by *dbid*.                                                            |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Oracle.TableSpaces(*dbid*)             | Tablespaces in database identified by *dbid*.                                                              |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+


.. _db2-subagent:

DB2
===

|product_name| subagent for DB2 monitoring is designed to provide a way to extract various metrics
known as Data Collection Items (DCI) from an instance or several instances of DB2 database.

Configuration
-------------

DB2 subagent configuration is specified in agent configuration file
(nxagentd.conf). Configuration can be done in two ways, the first one would be a
simple INI file and the second one would be an XML configuration file. Please
note that to use the XML configuration, you first need to declare the XML file
in the DB2 section of the INI configuration file. The details are below.


Database definition supports the following parameters:

.. list-table::
   :widths: 20 20 70 20
   :header-rows: 1

   * - Parameter
     - Format
     - Description
     - Default value
   * - DBName
     - string
     - The name of the database to connect to
     -
   * - DBAlias
     - string
     - The alias of the database to connect to
     -
   * - UserName
     - string
     - The name of the user for the database to connect to
     -
   * - Password
     - string
     - The password for the database to connect to. When using INI format,
       remember to enclose password in double quotes ("password") if it contains
       # character. This parameter automatically detects and accepts password
       encrypted with :ref:`nxencpasswd-tools-label` tool.
     -
   * - EncryptedPassword
     - string
     - Database user password encrypted with :ref:`nxencpasswd-tools-label`
       tool. DEPRECATED. Use Password instead.
     -
   * - QueryInterval
     - seconds
     - The interval to perform queries with
     - 60
   * - ReconnectInterval
     - seconds
     - The interval to try to reconnect to the database if the connection was
       lost or could not be established
     - 30


Sample DB2 subagent configuration file in INI format:

.. code-block:: sh

   SubAgent          = db2.nsm

   [DB2]
   DBName            = dbname
   DBAlias           = dbalias
   UserName          = dbuser
   Password          = "mypass123"
   QueryInterval     = 60
   ReconnectInterval = 30


XML configuration allows the monitoring of several database instances.

To be able to use the XML configuration file, you first need to specify the file
to use in the DB2 section of the INI file. The syntax is as follows:

.. code-block:: sh

   SubAgent          = db2.nsm

   [DB2]
   ConfigFile        = /myhome/configs/db2.xml

.. note:
  Note that all other entries in the DB2 section will be ignored.

.. list-table::
   :widths: 20 20 70 20
   :header-rows: 1

   * - Parameter
     - Format
     - Description
     - Default value
   * - ConfigFile
     - string
     - The path to the XML configuration file
     -

The XML configuration file itself should look like this:

.. code-block:: sh

   <config>
       <db2sub>
           <db2 id="1">
               <dbname>dbname</dbname>
               <dbalias>dbalias</dbalias>
               <username>dbuser</username>
               <password>mypass123</password>
               <queryinterval>60</queryinterval>
               <reconnectinterval>30</reconnectinterval>
           </db2>
           <db2 id="2">
               <dbname>dbname1</dbname>
               <dbalias>dbalias1</dbalias>
               <username>dbuser1</username>
               <password>mypass456</password>
               <queryinterval>60</queryinterval>
               <reconnectinterval>30</reconnectinterval>
           </db2>
       </db2sub>
   </config>

As you can see, the parameters are the same as the ones from the INI
configuration. Each database declaration must be placed under the ``db2sub`` tag
and enclosed in the ``db2`` tag. The ``db2`` tag must have a numerical id which
has to be a positive integer greater than 0.

Provided metrics
~~~~~~~~~~~~~~~~

To get a DCI from the subagent, you need to specify the id from the ``db2``
entry in the XML configuration file (in case of INI configuration, the id will
be **1**). To specify the id, you need to add it enclosed in brackets to the
name of the metric that is being requested (e.g.,
``db2.metric.to.request(**1**)``). In the example, the metric
``db2.metric.to.request`` from the database with the id **1** will be returned.

.. list-table::
   :widths: 40 20 20 70
   :header-rows: 1

   * - Parameter
     - Arguments
     - Return type
     - Description
   * - DB2.Instance.Version(*)
     - Database id
     - DCI_DT_STRING
     - DBMS version
   * - DB2.Table.Available(*)
     - Database id
     - DCI_DT_INT
     - The number of available tables
   * - DB2.Table.Unavailable(*)
     - Database id
     - DCI_DT_INT
     - The number of unavailable tables
   * - DB2.Table.Data.LogicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Data object logical size in kilobytes
   * - DB2.Table.Data.PhysicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Data object physical size in kilobytes
   * - DB2.Table.Index.LogicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Index object logical size in kilobytes
   * - DB2.Table.Index.PhysicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Index object physical size in kilobytes
   * - DB2.Table.Long.LogicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Long object logical size in kilobytes
   * - DB2.Table.Long.PhysicalSize(*)
     - Database id
     - DCI_DT_INT64
     - Long object physical size in kilobytes
   * - DB2.Table.Lob.LogicalSize(*)
     - Database id
     - DCI_DT_INT64
     - LOB object logical size in kilobytes
   * - DB2.Table.Lob.PhysicalSize(*)
     - Database id
     - DCI_DT_INT64
     - LOB object physical size in kilobytes
   * - DB2.Table.Xml.LogicalSize(*)
     - Database id
     - DCI_DT_INT64
     - XML object logical size in kilobytes
   * - DB2.Table.Xml.PhysicalSize(*)
     - Database id
     - DCI_DT_INT64
     - XML object physical size in kilobytes
   * - DB2.Table.Index.Type1(*)
     - Database id
     - DCI_DT_INT
     - The number of tables using type-1 indexes
   * - DB2.Table.Index.Type2(*)
     - Database id
     - DCI_DT_INT
     - The number of tables using type-2 indexes
   * - DB2.Table.Reorg.Pending(*)
     - Database id
     - DCI_DT_INT
     - The number of tables pending reorganization
   * - DB2.Table.Reorg.Aborted(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in aborted reorganization state
   * - DB2.Table.Reorg.Executing(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in executing reorganization state
   * - DB2.Table.Reorg.Null(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in null reorganization state
   * - DB2.Table.Reorg.Paused(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in paused reorganization state
   * - DB2.Table.Reorg.Alters(*)
     - Database id
     - DCI_DT_INT
     - The number of reorg recommend alter operations
   * - DB2.Table.Load.InProgress(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with load in progress status
   * - DB2.Table.Load.Pending(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with load pending status
   * - DB2.Table.Load.Null(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with load status neither in progress nor pending
   * - DB2.Table.Readonly(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in Read Access Only state
   * - DB2.Table.NoLoadRestart(*)
     - Database id
     - DCI_DT_INT
     - The number of tables in a state that won't allow a load restart
   * - DB2.Table.Index.Rebuild(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with indexes that require rebuild
   * - DB2.Table.Rid.Large(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that use large row IDs
   * - DB2.Table.Rid.Usual(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that don't use large row IDs
   * - DB2.Table.Rid.Pending(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that use large row Ids but not all indexes have been
       rebuilt yet
   * - DB2.Table.Slot.Large(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that use large slots
   * - DB2.Table.Slot.Usual(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that don't use large slots
   * - DB2.Table.Slot.Pending(*)
     - Database id
     - DCI_DT_INT
     - The number of tables that use large slots but there has not yet been an
       offline table reorganization or table truncation operation
   * - DB2.Table.DictSize(*
     - Database id
     - DCI_DT_INT64
     - Size of the dictionary in bytes
   * - DB2.Table.Scans(*)
     - Database id
     - DCI_DT_INT64
     - The number of scans on all tables
   * - DB2.Table.Row.Read(*)
     - Database id
     - DCI_DT_INT64
     - The number of reads on all tables
   * - DB2.Table.Row.Inserted(*)
     - Database id
     - DCI_DT_INT64
     - The number of insertions attempted on all tables
   * - DB2.Table.Row.Updated(*)
     - Database id
     - DCI_DT_INT64
     - The number of updates attempted on all tables
   * - DB2.Table.Row.Deleted(*)
     - Database id
     - DCI_DT_INT64
     - The number of deletes attempted on all tables
   * - DB2.Table.Overflow.Accesses(*)
     - Database id
     - DCI_DT_INT64
     - The number of r/w operations on overflowed rows of all tables
   * - DB2.Table.Overflow.Creates(*)
     - Database id
     - DCI_DT_INT64
     - The number of overflowed rows created on all tables
   * - DB2.Table.Reorg.Page(*)
     - Database id
     - DCI_DT_INT64
     - The number of page reorganizations executed for all tables
   * - DB2.Table.Data.LogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by data
   * - DB2.Table.Lob.LogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by LOBs
   * - DB2.Table.Long.LogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by long data
   * - DB2.Table.Index.LogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by indexes
   * - DB2.Table.Xda.LogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by XDA (XML storage object)
   * - DB2.Table.Row.NoChange(*)
     - Database id
     - DCI_DT_INT64
     - The number of row updates that yielded no changes
   * - DB2.Table.Lock.WaitTime(*)
     - Database id
     - DCI_DT_INT64
     - The total elapsed time spent waiting for locks (ms)
   * - DB2.Table.Lock.WaitTimeGlob(*)
     - Database id
     - DCI_DT_INT64
     - The total elapsed time spent on global lock waits (ms)
   * - DB2.Table.Lock.Waits(*)
     - Database id
     - DCI_DT_INT64
     - The total amount of locks occurred
   * - DB2.Table.Lock.WaitsGlob(*)
     - Database id
     - DCI_DT_INT64
     - The total amount of global locks occurred
   * - DB2.Table.Lock.EscalsGlob(*)
     - Database id
     - DCI_DT_INT64
     - The number of lock escalations on a global lock
   * - DB2.Table.Data.Sharing.Shared(*)
     - Database id
     - DCI_DT_INT
     - The number of fully shared tables
   * - DB2.Table.Data.Sharing.BecomingShared(*)
     - Database id
     - DCI_DT_INT
     - The number of tables being in the process of becoming shared
   * - DB2.Table.Data.Sharing.NotShared(*)
     - Database id
     - DCI_DT_INT
     - The number of tables not being shared
   * - DB2.Table.Data.Sharing.BecomingNotShared(*)
     - Database id
     - DCI_DT_INT
     - The number of tables being in the process of becoming not shared
   * - DB2.Table.Data.Sharing.RemoteLockWaitCount(*)
     - Database id
     - DCI_DT_INT64
     - The number of exits from the NOT_SHARED data sharing state
   * - DB2.Table.Data.Sharing.RemoteLockWaitTime(*)
     - Database id
     - DCI_DT_INT64
     - The time spent on waiting for a table to become shared
   * - DB2.Table.DirectWrites(*)
     - Database id
     - DCI_DT_INT64
     - The number of write operations that don't use the buffer pool
   * - DB2.Table.DirectWriteReqs(*)
     - Database id
     - DCI_DT_INT64
     - The number of request to perform a direct write operation
   * - DB2.Table.DirectRead(*)
     - Database id
     - DCI_DT_INT64
     - The number of read operations that don't use the buffer pool
   * - DB2.Table.DirectReadReqs(*)
     - Database id
     - DCI_DT_INT64
     - The number of request to perform a direct read operation
   * - DB2.Table.Data.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages that are logically read from the buffer pool
   * - DB2.Table.Data.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages that are physically read
   * - DB2.Table.Data.Gbp.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) page is requested from
       the GBP
   * - DB2.Table.Data.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) page is read into the
       local buffer pool (LBP)
   * - DB2.Table.Data.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) page is requested from
       the GBP when the version stored in the local buffer pool (LBP) is invalid
   * - DB2.Table.Data.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a data page is present in the local buffer pool
       (LBP)
   * - DB2.Table.Data.Lbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of group buffer pool (GBP) independent pages found in a local
       buffer pool (LBP)
   * - DB2.Table.Xda.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages for XML storage objects (XDA) that are logically
       read from the buffer pool
   * - DB2.Table.Xda.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages for XML storage objects (XDA) that are
       physically read
   * - DB2.Table.Xda.Gbp.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a data page for an XML storage object (XDA) is
       requested from the group buffer pool (GBP)
   * - DB2.Table.Xda.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) dependent data page
       for an XML storage object (XDA) is read into the local buffer pool (LBP)
   * - DB2.Table.Xda.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a page for an XML storage objects (XDA) is
       requested from the group buffer pool (GBP) because the version in the
       local buffer pool (LBP) is invalid
   * - DB2.Table.Xda.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that an XML storage objects (XDA) page is present in
       the local buffer pool (LBP)
   * - DB2.Table.Xda.Gbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of group buffer pool (GBP) independent XML storage object
       (XDA) pages found in the local buffer pool (LBP)
   * - DB2.Table.DictNum(*)
     - Database id
     - DCI_DT_INT64
     - The number of page-level compression dictionaries created or recreated
   * - DB2.Table.StatsRowsModified(*)
     - Database id
     - DCI_DT_INT64
     - The number of rows modified since the last RUNSTATS
   * - DB2.Table.ColObjectLogicalPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of logical pages used on disk by column-organized data
   * - DB2.Table.Organization.Rows(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with row-organized data
   * - DB2.Table.Organization.Cols(*)
     - Database id
     - DCI_DT_INT
     - The number of tables with column-organized data
   * - DB2.Table.Col.LogicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of column-organized pages that are logically read from the
       buffer pool
   * - DB2.Table.Col.PhysicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of column-organized pages that are physically read
   * - DB2.Table.Col.Gbp.LogicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a group buffer pool (GBP) dependent
       column-organized page is requested from the GBP
   * - DB2.Table.Col.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a group buffer pool (GBP) dependent
       column-organized page is read into the local buffer pool (LBP) from disk
   * - DB2.Table.Col.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a column-organized page is requested from the
       group buffer pool (GBP) when the page in the local buffer pool (LBP) is
       invalid
   * - DB2.Table.Col.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a column-organized page is present in the local
       buffer pool (LBP)
   * - DB2.Table.Col.Gbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT
     - The number of group buffer pool (GBP) independent column-organized pages
       found in the local buffer pool (LBP)
   * - DB2.Table.ColsReferenced(*)
     - Database id
     - DCI_DT_INT
     - The number of columns referenced during the execution of a section for an
       SQL statement
   * - DB2.Table.SectionExecutions(*)
     - Database id
     - DCI_DT_INT
     - The number of section executions that referenced columns in tables using a scan


.. _mongodb-subagent:

MongoDB
=======

|product_name| subagent for MongoDB monitoring. Monitors one or more instances
of MongoDB databases and reports various database-related metrics.

All metrics available from MongoDB subagent gathered or calculated once per
minute thus it's recommended to set DCI poll interval for these items to 60
seconds or more. It is supposed that only databases with same version are
monitored by one agent.

Building mongodb subagent
-------------------------

Use ``--with-mongodb=/path/to/mongoc driver`` parameter to include MongoDB
subagent in build. Was tested with mongo-c-driver-1.1.0.

Agent Start
-----------

While start of subagent at least one database should be up and running.
Otherwise subagent will not start. On start subagent requests serverStatus to
get list of possible DCI. This list may vary from version to version of MongoDB.

Configuration file
------------------

.. todo:
  Add description of configuration string for connection to database.

Metrics
-------

There are 2 types of metrics: serverStatus metrics, that are generated from
response on a subagent start and predefined for database status.

Description of serverStatus metrics can be found there: `serverStatus
<http://docs.mongodb.org/manual/reference/command/serverStatus/>`_. In this type
of DCI should be given id of server from where the metric should be taken.

Description of database status metrics can be found there: `dbStats
<http://docs.mongodb.org/master/reference/command/dbStats/>`_.

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Metric
     - Description
   * - MongoDB.collectionsNum(*id*,\ *databaseName*)
     - Contains a count of the number of collections in that database.
   * - MongoDB.objectsNum(*id*,\ *databaseName*)
     - Contains a count of the number of objects (i.e. documents) in the
       database across all collections.
   * - MongoDB.avgObjSize(*id*,\ *databaseName*)
     - The average size of each document in bytes.
   * - MongoDB.dataSize(*id*,\ *databaseName*)
     - The total size in bytes of the data held in this database including the
       padding factor.
   * - MongoDB.storageSize(*id*,\ *databaseName*)
     - The total amount of space in bytes allocated to collections in this
       database for document storage.
   * - MongoDB.numExtents(*id*,\ *databaseName*)
     - Contains a count of the number of extents in the database across all
       collections.
   * - MongoDB.indexesNum(*id*,\ *databaseName*)
     - Contains a count of the total number of indexes across all collections in
       the database.
   * - MongoDB.indexSize(*id*,\ *databaseName*)
     - The total size in bytes of all indexes created on this database.
   * - MongoDB.fileSize(*id*,\ *databaseName*)
     - The total size in bytes of the data files that hold the database.
   * - MongoDB.nsSizeMB(*id*,\ *databaseName*)
     - The total size of the namespace files (i.e. that end with .ns) for this
       database.


List
----

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Metric
     - Description
   * - MongoDB.ListDatabases(*id*)
     - Returns list of databases existing on this server


.. _informix-subagent:

Informix
========

|product_name| subagent for Informix (further referred to as Informix subagent)
monitors one or more Informix databases and reports database-related metrics.

All metrics available from Informix subagent are collected or calculated once
per minute, thus its recommended to set DCI poll interval for these items to 60
seconds or more. All metrics are obtained or derived from the data available
in Informix system catalogs. Informix subagent does not monitor any of the metrics
related to lower level database layers, such as database processes. Monitoring of
such metrics can be achieved through the standard |product_name| functionality.

Pre-requisites
--------------

A database user must have access rights to Informix system catalog tables.

Configuration
-------------

You can specify multiple databases in the [informix] section of agent
configuration file. Each database description must be surrounded by database
tags with the id attribute. Id can be any unique integer, it instructs the
Informix subagent about the order in which database sections will be processed.

Each database definition supports the following parameters:


.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Parameter
     - Description
   * - Id
     - Database identifier. It will be used to address this database in parameters.
   * - DBName
     - Database name. This is a name of Informix DSN.
   * - DBServer
     - Name of the Informix server.
   * - DBLogin
     - User name for connecting to database.
   * - DBPassword
     - The password for the database to connect to. When using INI format,
       remember to enclose password in double quotes ("password") if it contains
       # character. This parameter automatically detects and accepts password
       encrypted with :ref:`nxencpasswd-tools-label` tool.


Configuration example in INI format:

.. code-block:: sh

    Subagent=informix.nsm

    [informix]
    ID=db1
    DBName = instance1
    DBLogin = user
    DBPassword = "password"


Configuration example in XML format:

.. code-block:: sh

   <config>
       <agent>
           <subagent>informix.nsm</subagent>
       </agent>
       <informix>
           <databases>
               <database id="1">
                   <id>DB1</id>
                   <DBName>TEST</DBName>
                   <DBLogin>NXMONITOR</DBLogin>
                   <DBPassword>NXMONITOR</DBPassword>
               </database>
               <database id="2">
                   <id>DB2</id>
                   <DBName>PROD</DBName>
                   <DBLogin>NETXMS</DBLogin>
                   <DBPassword>PASSWORD</DBPassword>
               </database>
           </databases>
       </informix>
   </config>


Provided metrics
~~~~~~~~~~~~~~~~

To get a metric from the subagent, you need to specify the id from the
``informix`` entry in configuration file. To specify the id, you need to add it
enclosed in brackets to the name of the metric that is being requested (e.g.,
``informix.metric.to.request(**1**)``). In the example, the metric
``informix.metric.to.request`` from the database with the id **1** will be
returned.

.. list-table::
   :widths: 40 20 20 70
   :header-rows: 1

   * - Metric
     - Arguments
     - Return type
     - Description
   * - Informix.Session.Count(*)
     - Database id
     - DCI_DT_INT
     - Number of sessions opened
   * - Informix.Database.Owner(*)
     - Database id
     - DCI_DT_STRING
     - The database creation date
   * - Informix.Database.Logged(*)
     - Database id
     - DCI_DT_INT
     - Returns 1 if the database is logged, 0 - otherwise
   * - Informix.Dbspace.Pages.PageSize(*)
     - Database id
     - DCI_DT_INT
     - A size of a dbspace page in bytes
   * - Informix.Dbspace.Pages.PageSize(*)
     - Database id
     - DCI_DT_INT
     - A number of pages used in the dbspace
   * - Informix.Dbspace.Pages.Free(*)
     - Database id
     - DCI_DT_INT
     - A number of free pages in the dbspace
   * - Informix.Dbspace.Pages.FreePerc(*)
     - Database id
     - DCI_DT_INT
     - Percentage of free space in the dbspace


.. _mysql-subagent:

MySQL
=====

|product_name| subagent for MySQL monitoring. Monitors one or more instances of
MySQL databases and reports various database-related metrics.

MySQL subagent requires MySQL driver to be available in the system.

Configuration
-------------

Configuration of MySQL subagent is done in agent configuration file
(nxagentd.conf). One or multiple MySQL server instances can be specified. In
case of single database definition simply set all required parameters under
``[mysql]`` section. In multi database configuration define each database under
``mysql/databases/<name>`` section with unique ``<name>`` for each database. If
no id provided ``<name>`` of the section will be used as a database id.


Each database definition supports the following parameters:

.. list-table::
   :widths: 50 200 200
   :header-rows: 1

   * - Parameter
     - Description
     - Default value
   * - Id
     - Database identifier. It will be used to address this database in parameters.
     - localdb - for single DB definition; last part of section name - for multi
       database definition
   * - Database
     - Database name. This is a name of MySQL DSN.
     - information_schema
   * - Server
     - Name or IP of the MySQL server.
     - 127.0.0.1
   * - ConnectionTTL
     - Time in seconds. When this time gets elapsed, connection to the DB is
       closed and reopened again.
     - 3600
   * - Login
     - User name for connecting to database.
     - netxms
   * - Password
     - Database user password. When using INI format, remember to enclose
       password in double quotes ("password") if it contains # character. This
       parameter automatically detects and accepts password encrypted with
       :ref:`nxencpasswd-tools-label` tool.
     -


Single database configuration example:

.. code-block:: sh

    Subagent=mysql.nsm

    [mysql]
    Id=db1
    Database = instance1
    Login = user
    Password = password


Multi database configuration example:

.. code-block:: sh

    Subagent=mysql.nsm

    [mysql/databases/somedatabase]
    Database = instance1
    Login = user
    Password = password
    Server = netxms.demo


    [mysql/databases/local]
    Database = information_schema
    Login = user
    Password = encPassword
    Server = 127.0.0.1


Provided metrics
----------------

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Metric
     - Description
   * - MySQL.Connections.Aborted(*id*)
     - aborted connections
   * - MySQL.Connections.BytesReceived(*id*)
     - bytes received from all clients
   * - MySQL.Connections.BytesSent(*id*)
     - bytes sent to all clients
   * - MySQL.Connections.Current(*id*)
     - number of active connections
   * - MySQL.Connections.CurrentPerc(*id*)
     - connection pool usage (%)
   * - MySQL.Connections.Failed(*id*)
     - failed connection attempts
   * - MySQL.Connections.Limit(*id*)
     - maximum possible number of simultaneous connections
   * - MySQL.Connections.Max(*id*)
     - maximum number of simultaneous connections
   * - MySQL.Connections.MaxPerc(*id*)
     - maximum connection pool usage  (%)
   * - MySQL.Connections.Total(*id*)
     - cumulative connection count
   * - MySQL.InnoDB.BufferPool.Dirty(*id*)
     - InnoDB used buffer pool space in dirty pages
   * - MySQL.InnoDB.BufferPool.DirtyPerc(*id*)
     - InnoDB used buffer pool space in dirty pages (%)
   * - MySQL.InnoDB.BufferPool.Free(*id*)
     - InnoDB free buffer pool space
   * - MySQL.InnoDB.BufferPool.FreePerc(*id*)
     - InnoDB free buffer pool space (%)
   * - MySQL.InnoDB.BufferPool.Size(*id*)
     - InnoDB buffer pool size
   * - MySQL.InnoDB.BufferPool.Used(*id*)
     - InnoDB used buffer pool space
   * - MySQL.InnoDB.BufferPool.UsedPerc(*id*)
     - InnoDB used buffer pool space (%)
   * - MySQL.InnoDB.DiskReads(*id*)
     - InnoDB disk reads
   * - MySQL.InnoDB.ReadCacheHitRatio(*id*)
     - InnoDB read cache hit ratio (%)
   * - MySQL.InnoDB.ReadRequest(*id*)
     - InnoDB read requests
   * - MySQL.InnoDB.WriteRequest(*id*)
     - InnoDB write requests
   * - MySQL.IsReachable(*id*)
     - is database reachable
   * - MySQL.MyISAM.KeyCacheFree(*id*)
     - MyISAM key cache free space
   * - MySQL.MyISAM.KeyCacheFreePerc(*id*)
     - MyISAM key cache free space (%)
   * - MySQL.MyISAM.KeyCacheReadHitRatio(*id*)
     - MyISAM key cache read hit ratio (%)
   * - MySQL.MyISAM.KeyCacheSize(*id*)
     - MyISAM key cache size
   * - MySQL.MyISAM.KeyCacheUsed(*id*)
     - MyISAM key cache used space
   * - MySQL.MyISAM.KeyCacheUsedPerc(*id*)
     - MyISAM key cache used space (%)
   * - MySQL.MyISAM.KeyCacheWriteHitRatio(*id*)
     - MyISAM key cache write hit ratio (%)
   * - MySQL.MyISAM.KeyDiskReads(*id*)
     - MyISAM key cache disk reads
   * - MySQL.MyISAM.KeyDiskWrites(*id*)
     - MyISAM key cache disk writes
   * - MySQL.MyISAM.KeyReadRequests(*id*)
     - MyISAM key cache read requests
   * - MySQL.MyISAM.KeyWriteRequests(*id*)
     - MyISAM key cache write requests
   * - MySQL.OpenFiles.Current(*id*)
     - open files
   * - MySQL.OpenFiles.CurrentPerc(*id*)
     - open file pool usage (%)
   * - MySQL.OpenFiles.Limit(*id*)
     - maximum possible number of open files
   * - MySQL.Queries.Cache.HitRatio(*id*)
     - query cache hit ratio (%)
   * - MySQL.Queries.Cache.Hits(*id*)
     - query cache hits
   * - MySQL.Queries.Cache.Size(*id*)
     - query cache size
   * - MySQL.Queries.ClientsTotal(*id*)
     - number of queries executed by clients
   * - MySQL.Queries.Delete(*id*)
     - number of DELETE queries
   * - MySQL.Queries.DeleteMultiTable(*id*)
     - number of multitable DELETE queries
   * - MySQL.Queries.Insert(*id*)
     - number of INSERT queries
   * - MySQL.Queries.Select(*id*)
     - number of SELECT queries
   * - MySQL.Queries.Slow(*id*)
     - slow queries
   * - MySQL.Queries.SlowPerc(*id*)
     - slow queries (%)
   * - MySQL.Queries.Total(*id*)
     - number of queries
   * - MySQL.Queries.Update(*id*)
     - number of UPDATE queries
   * - MySQL.Queries.UpdateMultiTable(*id*)
     - number of multitable UPDATE queries
   * - MySQL.Server.Uptime(*id*)
     - server uptime
   * - MySQL.Sort.MergePasses(*id*)
     - sort merge passes
   * - MySQL.Sort.MergeRatio(*id*)
     - sort merge ratio (%)
   * - MySQL.Sort.Range(*id*)
     - number of sorts using ranges
   * - MySQL.Sort.Scan(*id*)
     - number of sorts using table scans
   * - MySQL.Tables.Fragmented(*id*)
     - fragmented tables
   * - MySQL.Tables.Open(*id*)
     - open tables
   * - MySQL.Tables.OpenLimit(*id*)
     - maximum possible number of open tables
   * - MySQL.Tables.OpenPerc(*id*)
     - table open cache usage (%)
   * - MySQL.Tables.Opened(*id*)
     - tables that have been opened
   * - MySQL.TempTables.Created(*id*)
     - temporary tables created
   * - MySQL.TempTables.CreatedOnDisk(*id*)
     - temporary tables created on disk
   * - MySQL.TempTables.CreatedOnDiskPerc(*id*)
     - temporary tables created on disk (%)
   * - MySQL.Threads.CacheHitRatio(*id*)
     - thread cache hit ratio (%)
   * - MySQL.Threads.CacheSize(*id*)
     - thread cache size
   * - MySQL.Threads.Created(*id*)
     - threads created
   * - MySQL.Threads.Running(*id*)
     - threads running


.. _pgsql-subagent:

PostgreSQL
==========

|product_name| subagent for PostgreSQL monitoring. Monitors one or more
instances of PostgeSQL servers and reports various database-related metrics.

PostgreSQL subagent requires PostgreSQL driver to be available in the system.

Pre-requisites
--------------

A PostgreSQL user with **CONNECT** right to at least one database on the server.

If the **PostgreSQL.DatabaseSize** metric should be monitored the user must have
the **CONNECT** right to other databases on the server too.


Starting from the PostgreSQL version 10, the user must have the the role
**pg_monitor** assigned. Required role can be assigned to user with the
following query:

.. code-block:: sh

    GRANT  pg_monitor TO user;

Where *user* is the user configured in PostgreSQL subagent for database access.


Configuration
-------------

Configuration of PostgreSQL subagent is done in agent configuration file
(nxagentd.conf). One or multiple PostgreSQL server instances can be specified.
In case of single server definition simply set all required parameters under
``[pgsql]`` section. In multi server configuration define each server instance
under ``pgsql/servers/<name>`` section with unique ``<name>`` for each server.
If no id provided ``<name>`` of the section will be used as a server id.

It is not necessary to configure connections to more than one database on the
same PostgreSQL server instance.

Each server definition supports the following parameters:

.. list-table::
   :widths: 50 200 200
   :header-rows: 1

   * - Parameter
     - Description
     - Default value
   * - Id
     - Server identifier. It will be used to address this server connection in
       parameters.
     - localdb - for single server definition

       last part of section name - for multi server definition
   * - Database
     - Maintenance database name. This is a name of the database on the server
       the subagent is connected to.
     - postgres
   * - Server
     - Name or IP of the PostgreSQL server.

       If the sever uses differnt than default port (5432) the *:port* must be
       added to the server name or IP.
     - 127.0.0.1
   * - ConnectionTTL
     - Time in seconds. When this time gets elapsed, connection to the DB is
       closed and reopened again.
     - 3600
   * - Login
     - User name for connecting to database.
     - netxms
   * - Password
     - Database user password.

       When using INI format, remember to enclose password in double quotes
       ("password") if it contains # character.

       This parameter automatically detects and accepts password encrypted with
       :ref:`nxencpasswd-tools-label` tool.
     -


Single server configuration example:

.. code-block:: sh

    Subagent=pgsql.nsm

    [pgsql]
    Id=production
    Server = 10.0.3.5
    Database = database1
    Login = user
    Password = password
    

Multi server configuration example:

.. code-block:: sh

    Subagent=pgsql.nsm

    [pgsql/servers/production]
    Server = 10.0.3.5
    Database = database1
    Login = user
    Password = password

    [pgsql/servers/testing]
    Server = 10.0.3.6
    Database = test_database
    Login = user
    Password = password


Provided Metrics 
----------------

When loaded, PostgreSQL subagent adds two types of metrics to the agent.

Database server metrics are common for all databases on the server. These
metrics require one argument which is server id from the configuration.

Database metrics are independent for each database on the server. These metrics
require two arguments. The first one is server id from the configuration the
second one is name of the database. If the second argument is missing the name
of the maintenance database from the configuration is used.

Alternatively, these two arguments can be specified as one argument in following
format: *datanase_name@server_id*. This format is returned by the
PostgreSQL.AllDatabases list.

Following table shows the database server metrics:

.. list-table::
   :widths: 50 20 100
   :header-rows: 1

   * - 	Metric
     - 	Type
     - 	Description
   * - 	PostgreSQL.IsReachable(*id*)
     - 	String
     - 	Is database server instance reachable
   * - 	PostgreSQL.Version(*id*)
     - 	String
     - 	Database server version
   * - 	PostgreSQL.Archiver.ArchivedCount(*id*)
     - 	Integer 64-bit
     - 	Number of WAL files that have been successfully archived
   * - 	PostgreSQL.Archiver.FailedCount(*id*)
     - 	Integer 64-bit
     - 	Number of failed attempts for archiving WAL files
   * - 	PostgreSQL.Archiver.IsArchiving(*id*)
     - 	String
     - 	Is archiving running
   * - 	PostgreSQL.Archiver.LastArchivedAge(*id*)
     - 	Integer
     - 	Age of the last successful archive operation
   * - 	PostgreSQL.Archiver.LastArchivedWAL(*id*)
     - 	String
     - 	Name of the last WAL file successfully archived
   * - 	PostgreSQL.Archiver.LastFailedAge(*id*)
     - 	Integer
     - 	Age of the last failed archival operation
   * - 	PostgreSQL.Archiver.LastFailedWAL(*id*)
     - 	String
     - 	Name of the WAL file of the last failed archival operation
   * - 	PostgreSQL.BGWriter.BuffersAlloc(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of buffers allocated
   * - 	PostgreSQL.BGWriter.BuffersBackend(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of buffers written directly by a backend
   * - 	PostgreSQL.BGWriter.BuffersBackendFsync(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of times a backend had to execute its own fsync call
   * - 	PostgreSQL.BGWriter.BuffersClean(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of buffers written by the background writer
   * - 	PostgreSQL.BGWriter.BuffersCheckpoint(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of buffers written during checkpoints
   * - 	PostgreSQL.BGWriter.CheckpointsReq(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of requested checkpoints that have been performed
   * - 	PostgreSQL.BGWriter.CheckpointsTimed(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of scheduled checkpoints that have been performed
   * - 	PostgreSQL.BGWriter.CheckpointSyncTime(*id*)
     - 	Float
     - 	Total amount of time that has been spent in the portion of checkpoint
       	processing where files are synchronized to disk, in milliseconds
   * - 	PostgreSQL.BGWriter.CheckpointWriteTime(*id*)
     - 	Float
     - 	Total amount of time that has been spent in the portion of checkpoint
       	processing where files are written to disk, in milliseconds
   * - 	PostgreSQL.BGWriter.MaxWrittenClean(*id*)
     - 	Integer 64-bit
     - 	Cumulative number of times the background writer stopped a cleaning scan
       	because it had written too many buffers
   * - 	PostgreSQL.GlobalConnections.AutovacuumMax(*id*)
     - 	Integer
     - 	Maximal number of autovacuum backends
   * - 	PostgreSQL.GlobalConnections.Total(*id*)
     - 	Integer
     - 	Total number of connections
   * - 	PostgreSQL.GlobalConnections.TotalMax(*id*)
     - 	Integer
     - 	Maximal number of connections
   * - 	PostgreSQL.GlobalConnections.TotalPct(*id*)
     - 	Integer
     - 	Used connections (%)
   * - 	PostgreSQL.Replication.InRecovery(*id*)
     - 	String
     - 	Is recovery in progress (from version 9.6.0)
   * - 	PostgreSQL.Replication.IsReceiver(*id*)
     - 	String
     - 	Is the server WAL receiver
   * - 	PostgreSQL.Replication.Lag(*id*)
     - 	Integer
     - 	Replication lag in seconds (from version 10.0)
   * - 	PostgreSQL.Replication.LagBytes(*id*)
     - 	Float
     - 	Replication lag in bytes (from version 10.0)
   * - 	PostgreSQL.Replication.WALSenders(*id*)
     - 	Integer 64-bit
     - 	Number of WAL senders
   * - 	PostgreSQL.Replication.WALFiles(*id*)
     - 	Integer 64-bit
     - 	Number of the WAL files  (from version 10.0)
   * - 	PostgreSQL.Replication.WALSize(*id*)
     - 	Float
     - 	Size of the WAL files (from version 10.0)

Following table shows the database metrics:

.. list-table::
   :widths: 50 20 100
   :header-rows: 1

   * - 	Metric
     - 	Type
     - 	Description
   * - 	PostgreSQL.DBConnections.Active(*id*[, *database*])
     - 	Integer
     - 	Number of backends for this database executing a query
   * - 	PostgreSQL.DBConnections.Autovacuum(*id*[, *database*])
     - 	Integer
     - 	Number of autovacuum backends for this database
   * - 	PostgreSQL.DBConnections.FastpathFunctionCall(*id*[, *database*])
     - 	Integer
     - 	Number of backends for this database executing a fast-path function
   * - 	PostgreSQL.DBConnections.Idle(*id*[, *database*])
     - 	Integer
     - 	Number of backends for this database waiting for a new client command
   * - 	PostgreSQL.DBConnections.IdleInTransaction(*id*[, *database*])
     - 	Integer
     - 	Number of backends for this database in a transaction, but is not
       	currently executing a query
   * - 	PostgreSQL.DBConnections.IdleInTransactionAborted(*id*[, *database*])
     - 	Integer
     - 	Number of backends for this database in a transaction, but is not
       	currently executing a query and one of the statements in the transaction
       	caused an error
   * - 	PostgreSQL.DBConnections.OldestXID(*id*[, *database*])
     - 	Integer
     - 	Age of the oldest XID
   * - 	PostgreSQL.DBConnections.Total(*id*[, *database*])
     - 	Integer
     - 	Total number of backends for connections to this database
   * - 	PostgreSQL.DBConnections.Waiting(*id*[, *database*])
     - 	Integer
     - 	Number of waiting backends for this database
   * - 	PostgreSQL.Locks.AccessExclusive(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of AccessExclusive locks for this database
   * - 	PostgreSQL.Locks.AccessShare(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of AccessShare locks for this database
   * - 	PostgreSQL.Locks.Exclusive(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of Exclusive locks for this database
   * - 	PostgreSQL.Locks.RowExclusive(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of RowExclusive locks for this database
   * - 	PostgreSQL.Locks.RowShare(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of RowShare locks for this database
   * - 	PostgreSQL.Locks.Share(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of Share locks for this database
   * - 	PostgreSQL.Locks.ShareRowExclusive(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of ShareRowExclusive locks for this database
   * - 	PostgreSQL.Locks.ShareUpdateExclusive(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of ShareUpdateExclusive locks for this database
   * - 	PostgreSQL.Locks.Total(*id*[, *database*])
     - 	Integer 64-bit
     - 	Total number of locks for this database
   * - 	PostgreSQL.Stats.BlkWriteTime(*id*[, *database*])
     - 	Float
     - 	Cumulative time spent writing data file blocks by backends in this
       	database, in milliseconds
   * - 	PostgreSQL.Stats.BlockReadTime(*id*[, *database*])
     - 	Float
     - 	Cumulative time spent reading data file blocks by backends in this
       	database, in milliseconds
   * - 	PostgreSQL.Stats.BlocksRead(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of disk blocks read in this database
   * - 	PostgreSQL.Stats.BloksHit(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of times disk blocks were found already in the buffer
       	cache
   * - 	PostgreSQL.Stats.CacheHitRatio(*id*[, *database*])
     - 	Float
     - 	Query cache hit ratio (%)
   * - 	PostgreSQL.Stats.Conflicts(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of queries canceled due to conflicts with recovery in
       	this database (stanby servers only)
   * - 	PostgreSQL.Stats.DatabaseSize(*id*[, *database*])
     - 	Integer 64-bit
     - 	Disk space used by the database
   * - 	PostgreSQL.Stats.Deadlocks(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of deadlocks detected in this database
   * - 	PostgreSQL.Stats.ChecksumFailures(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of data page checksum failures detected in this
       	database (from version 12.0)
   * - 	PostgreSQL.Stats.NumBackends(*id*[, *database*])
     - 	Integer
     - 	Number of backends currently connected to this database
   * - 	PostgreSQL.Stats.RowsDeleted(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of rows deleted by queries in this database
   * - 	PostgreSQL.Stats.RowsFetched(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of rows fetched by queries in this database
   * - 	PostgreSQL.Stats.RowsInserted(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of rows inserted by queries in this database
   * - 	PostgreSQL.Stats.RowsReturned(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of rows returned by queries in this database
   * - 	PostgreSQL.Stats.RowsUpdated(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of rows updated by queries in this database
   * - 	PostgreSQL.Stats.TempBytes(*id*[, *database*])
     - 	Integer 64-bit
     - 	Total amount of data written to temporary files by queries in this database
   * - 	PostgreSQL.Stats.TempFiles(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of temporary files created by queries in this database
   * - 	PostgreSQL.Stats.TransactionCommits(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of transactions in this database that have been committed
   * - 	PostgreSQL.Stats.TransactionRollbacks(*id*[, *database*])
     - 	Integer 64-bit
     - 	Cumulative number of transactions in this database that have been rolled back
   * - 	PostgreSQL.Transactions.Prepared(*id*[, *database*])
     - 	Integer 64-bit
     - 	Number of prepared transactions for this database

Lists
-----

When loaded, PostgreSQL subagent adds the following lists to agent:

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - 	List
     - 	Description
   * - 	PostgreSQL.DBServers
     - 	All configured servers (server ids).
   * - 	PostgreSQL.Databases(*id*)
     - 	All databases on server identified by *id*.
   * - 	PostgreSQL.AllDatabases
     - 	All databases on configured servers. The format of the list items is
       	*datanase_name@server_id*.
   * - 	PostgreSQL.DataTags(*id*)
     - 	All data tags for server identified by *id*. Used only for internal diagnostics.


Tables
------

When loaded, PostgreSQL subagent adds the following tables to agent:

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - 	Table
     - 	Description
   * - 	PostgreSQL.Backends(*id*)
     - 	Connection backends on server identified by *id*.
   * - 	PostgreSQL.Locks(*id*)
     - 	Locks on server identified by *id*.
   * - 	PostgreSQL.PreparedTransactions(*id*)
     - 	Prepared transactions on server identified by *id*.
