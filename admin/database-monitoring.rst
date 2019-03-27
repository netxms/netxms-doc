.. _database-monitoring:

===================
Database monitoring
===================


There are created few specialized monitoring subagents: Oracle, DB2, MongoDB. Further
will be described how to configure and use this subagents. Besides this there is
opportunity to monitor also other types of databases supported by |product_name|
server(:ref:`link to supported database list<supported-db-list>`) using database query
suabgent as this databases support receiving performance parameters using queries.
This subagent details are described in :ref:`dbquery` chapter.

Oracle
======

|product_name| subagent for Oracle DBMS monitoring (further referred to as Oracle subagent) monitors
one or more instances of Oracle databases and reports various database-related parameters.

All parameters available from Oracle subagent gathered or calculated once per minute thus it's
recommended to set DCI poll interval for these items to 60 seconds or more. All parameters are
obtained or derived from the data available in Oracle's data dictionary tables and views through
regular select queries. Oracle subagent does not monitor any of the metrics related to lower level
database layers, such as database processes. Monitoring of such parameters can be achieved through
the standard |product_name| functionality.

Pre-requisites
--------------

An Oracle user with the role **select_catalog_role** assigned.

Required rights can be assigned to user with the following query:

.. code-block:: sql

   grant select_catalog_role to user;

Where *user* is the user configured in Oracle subagent for database access.


Configuration file
------------------

Oracle subagent can be configured using XML configuration file (usually created
as separate file in configuration include directory), or in simplified INI format,
usually in main agent configuration file.

XML configuration:

You can specify multiple databases in the **oracle** section. Each database description
must be surrounded by database tags with the **id** attribute. It can be any unique integer
and instructs the Oracle subagent about the order in which database sections will be processed.

Each database definition supports the following parameters:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Parameter                              | Description                                                                                                |
+========================================+============================================================================================================+
| Id                                     | Database identifier. It will be used to address this database in parameters.                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Name                                   | Database TNS name or connection string.                                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Username                               | User name for connecting to database.                                                                      |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Password                               | Database user password.                                                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| EncryptedPassword                      | Database user password encrypted with :ref:`nxencpasswd-tools-label` tool.                                 |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+

Sample Oracle subagent configuration file in XML format:

.. code-block:: xml

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

INI configuration:

You can specify only one database when using INI configuration format. If you need
to monitor multiple databases from same agent, you should use configuration file in XML format.

**ORACLE** section can contain the following parameters:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Parameter                              | Description                                                                                                |
+========================================+============================================================================================================+
| Id                                     | Database identifier. It will be used to address this database in parameters.                               |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Name                                   | Database TNS name or connection string.                                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Username                               | User name for connecting to database.                                                                      |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Password                               | Database user password.                                                                                    |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| EncryptedPassword                      | Database user password encrypted with nxencpasswd.                                                         |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+

Sample Oracle subagent configuration file in INI format:

.. code-block:: cfg

   [ORACLE]
   ID = DB1
   TNSName = TEST
   Username = NXMONITOR
   Password = NXMONITOR

Parameters
----------

When loaded, Oracle subagent adds the following parameters to agent (all parameters requires database ID as first argument):

+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Parameter                                               | Description                                                                       |
+=========================================================+===================================================================================+
| Oracle.CriticalStats.AutoArchivingOff(*dbid*)           | Archive logs enabled but auto archiving off (YES/NO)                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.DatafilesNeedMediaRecovery(*dbid*) | Number of datafiles that need media recovery                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.DFOffCount(*dbid*)                 | Number of offline datafiles                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.FailedJobs(*dbid*)                 | Number of failed jobs                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.FullSegmentsCount(*dbid*)          | Number of segments that cannot extend                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.RBSegsNotOnlineCount(*dbid*)       | Number of rollback segments not online                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.CriticalStats.TSOffCount(*dbid*)                 | Number of offline tablespaces                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Cursors.Count(*dbid*)                            | Current number of opened cursors system-wide                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.AvgIoTime(*dbid*, *datafile*)           | Average time spent on single I/O operation for *datafile* in milliseconds         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.Blocks(*dbid*, *datafile*)              | *datafile* size in blocks                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.BlockSize(*dbid*, *datafile*)           | *datafile* block size                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.Bytes(*dbid*, *datafile*)               | *datafile* size in bytes                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.FullName(*dbid*, *datafile*)            | *datafile* full name                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.MaxIoReadTime(*dbid*, *datafile*)       | Maximum time spent on a single read for *datafile* in milliseconds                |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.MaxIoWriteTime(*dbid*, *datafile*)      | Maximum time spent on a single write for *datafile* in milliseconds               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.MinIoTime(*dbid*, *datafile*)           | Minimum time spent on a single I/O operation for *datafile* in milliseconds       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.PhysicalReads(*dbid*, *datafile*)       | Total number of physical reads from *datafile*                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.PhysicalWrites(*dbid*, *datafile*)      | Total number of physical writes to *datafile*                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.ReadTime(*dbid*, *datafile*)            | Total read time for *datafile* in milliseconds                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.Status(*dbid*, *datafile*)              | *datafile* status                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.Tablespace(*dbid*, *datafile*)          | *datafile* tablespace                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DataFile.WriteTime(*dbid*, *datafile*)           | Total write time for *datafile* in milliseconds                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.CreateDate(*dbid*)                        | Database creation date                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.IsReachable(*dbid*)                       | Database is reachable (YES/NO)                                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.LogMode(*dbid*)                           | Database log mode                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.Name(*dbid*)                              | Database name                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.OpenMode(*dbid*)                          | Database open mode                                                                |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.DBInfo.Version(*dbid*)                           | Database version                                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Dual.ExcessRows(*dbid*)                          | Excessive rows in DUAL table                                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Instance.ArchiverStatus(*dbid*)                  | Archiver status                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Instance.Status(*dbid*)                          | Database instance status                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Instance.ShutdownPending(*dbid*)                 | Is shutdown pending (YES/NO)                                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Instance.Version(*dbid*)                         | DBMS Version                                                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Objects.InvalidCount(*dbid*)                     | Number of invalid objects in DB                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.CacheHitRatio(*dbid*)                | Data buffer cache hit ratio                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.DictCacheHitRatio(*dbid*)            | Dictionary cache hit ratio                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.DispatcherWorkload(*dbid*)           | Dispatcher workload (percentage)                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.FreeSharedPool(*dbid*)               | Free space in shared pool (bytes)                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.Locks(*dbid*)                        | Number of locks                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.LogicalReads(*dbid*)                 | Number of logical reads                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.LibCacheHitRatio(*dbid*)             | Library cache hit ratio                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.MemorySortRatio(*dbid*)              | PGA memory sort ratio                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.PhysicalReads(*dbid*)                | Number of physical reads                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.PhysicalWrites(*dbid*)               | Number of physical writes                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Performance.RollbackWaitRatio(*dbid*)            | Ratio of waits for requests to rollback segments                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Sessions.Count(*dbid*)                           | Number of sessions opened                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Sessions.CountByProgram(*dbid*, *program*)       | Number of sessions opened by specific program                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Sessions.CountBySchema(*dbid*, *schema*)         | Number of sessions opened with specific schema                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.Sessions.CountByUser(*dbid*, *user*)             | Number of sessions opened with specific Oracle user                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.BlockSize(*dbid*, *tablespace*)       | *tablespace* block size                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.DataFiles(*dbid*, *tablespace*)       | Number of datafiles in *tablespace*                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.FreeBytes(*dbid*, *tablespace*)       | Free bytes in *tablespace*                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.FreePct(*dbid*, *tablespace*)         | Free space percentage in *tablespace*                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.Logging(*dbid*, *tablespace*)         | *tablespace* logging mode                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.Status(*dbid*, *tablespace*)          | *tablespace* status                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.TotalBytes(*dbid*, *tablespace*)      | Total size in bytes of *tablespace*                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.Type(*dbid*, *tablespace*)            | *tablespace* type                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.UsedBytes(*dbid*, *tablespace*)       | Used bytes in *tablespace*                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+
| Oracle.TableSpace.UsedPct(*dbid*, *tablespace*)         | Used space percentage in *tablespace*                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------+


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


DB2
===

|product_name| subagent for DB2 monitoring is designed to provide a way to extract various parameters
known as Data Collection Items (DCI) from an instance or several instances of DB2 database.

Configuration
-------------

DB2 subagent can be configured in two ways. The first one would be a simple INI file and the
second one would be an XML configuration file. Please note that to use the XML configuration,
you first need to declare the XML file in the DB2 section of the INI configuration file. The
details are below.

The configuration section in INI file looks like the following:

.. code-block:: cfg

   SubAgent          = db2.nsm

   [DB2]
   DBName            = dbname
   DBAlias           = dbalias
   UserName          = dbuser
   Password          = mypass123
   QueryInterval     = 60
   ReconnectInterval = 30

Parameters:

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
     - The password for the database to connect to
     -
   * - EncryptedPassword
     - string
     - The encrypted password for the database to connect to (use nxencpasswd for encryption)
     -
   * - QueryInterval
     - milliseconds
     - The interval to perform queries with
     - 60
   * - ReconnectInterval
     - milliseconds
     - The interval to try to reconnect to the database if the connection was lost or could not be established
     - 30

XML configuration allows the monitoring of several database instances.

To be able to use the XML configuration file, you first need to specify the file to use in the
DB2 section of the INI file. The syntax is as follows:

.. code-block:: cfg

   SubAgent          = db2.nsm

   [DB2]
   ConfigFile        = /myhome/configs/db2.xml

.. note:
  Note that all other entries in the DB2 will be ignored.

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

.. code-block:: xml

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

As you can see, the parameters are the same as the ones from the INI configuration. Each database
declaration must be placed in the ``db2sub`` tag and enclosed in the ``db2`` tag. The ``db2`` tag
must have a numerical id which has to be a positive integer greater than 0.

Provided parameters
~~~~~~~~~~~~~~~~~~~

To get a DCI from the subagent, you need to specify the id from the ``db2`` entry in the XML
configuration file (in case of INI configuration, the id will be **1**). To specify the id, you
need to add it enclosed in brackets to the name of the parameter that is being requested (e.g.,
``db2.parameter.to.request(**1**)``). In the example, the parameter ``db2.parameter.to.request``
from the database with the id **1** will be returned.

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
     - The number of tables that use large row Ids but not all indexes have been rebuilt yet
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
     - The number of tables that use large slots but there has not yet been an offline table reorganization or table truncation operation
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
     - The number of times that a group buffer pool (GBP) page is requested from the GBP
   * - DB2.Table.Data.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) page is read into the local buffer pool (LBP)
   * - DB2.Table.Data.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) page is requested from the GBP when the version stored in the local buffer pool (LBP) is invalid
   * - DB2.Table.Data.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a data page is present in the local buffer pool (LBP)
   * - DB2.Table.Data.Lbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of group buffer pool (GBP) independent pages found in a local buffer pool (LBP)
   * - DB2.Table.Xda.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages for XML storage objects (XDA) that are logically read from the buffer pool
   * - DB2.Table.Xda.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of data pages for XML storage objects (XDA) that are physically read
   * - DB2.Table.Xda.Gbp.LogicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a data page for an XML storage object (XDA) is requested from the group buffer pool (GBP)
   * - DB2.Table.Xda.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a group buffer pool (GBP) dependent data page for an XML storage object (XDA) is read into the local buffer pool (LBP)
   * - DB2.Table.Xda.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that a page for an XML storage objects (XDA) is requested from the group buffer pool (GBP) because the version in the local buffer pool (LBP) is invalid
   * - DB2.Table.Xda.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of times that an XML storage objects (XDA) page is present in the local buffer pool (LBP)
   * - DB2.Table.Xda.Gbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT64
     - The number of group buffer pool (GBP) independent XML storage object (XDA) pages found in the local buffer pool (LBP)
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
     - The number of column-organized pages that are logically read from the buffer pool
   * - DB2.Table.Col.PhysicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of column-organized pages that are physically read
   * - DB2.Table.Col.Gbp.LogicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a group buffer pool (GBP) dependent column-organized page is requested from the GBP
   * - DB2.Table.Col.Gbp.PhysicalReads(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a group buffer pool (GBP) dependent column-organized page is read into the local buffer pool (LBP) from disk
   * - DB2.Table.Col.Gbp.InvalidPages(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a column-organized page is requested from the group buffer pool (GBP) when the page in the local buffer pool (LBP) is invalid
   * - DB2.Table.Col.Lbp.PagesFound(*)
     - Database id
     - DCI_DT_INT
     - The number of times that a column-organized page is present in the local buffer pool (LBP)
   * - DB2.Table.Col.Gbp.IndepPagesFound(*)
     - Database id
     - DCI_DT_INT
     - The number of group buffer pool (GBP) independent column-organized pages found in the local buffer pool (LBP)
   * - DB2.Table.ColsReferenced(*)
     - Database id
     - DCI_DT_INT
     - The number of columns referenced during the execution of a section for an SQL statement
   * - DB2.Table.SectionExecutions(*)
     - Database id
     - DCI_DT_INT
     - The number of section executions that referenced columns in tables using a scan


MongoDB
=======

.. versionadded:: 2.0-M3

|product_name| subagent for MongoDB monitoring. Monitors one or more instances of MongoDB databases and
reports various database-related parameters.

All parameters available from MongoDB subagent gathered or calculated once per minute thus it's
recommended to set DCI poll interval for these items to 60 seconds or more. It is supposed that
by one agent will be monitored databases with same version.

Building mongodb subagent
-------------------------

Use "--with-mongodb=/path/to/mongoc driver" parameter to include MongoDB subagent in build. Was tested with
mongo-c-driver-1.1.0.

Agent Start
-----------

While start of subagent at least one database should be up and running. Otherwise subagent will not start.
On start subagent requests serverStatus to get list of possible DCI. This list may vary from version to version
of MongoDB.

Configuration file
------------------

.. todo:
  Add description of configuration string for connection to database.

Parameters
----------

There are 2 types of parameters: serverStatus parameters, that are generated form response on a subagent start
and predefined for database status.

Description of serverStatus parameters can be found there: `serverStatus <http://docs.mongodb.org/manual/reference/command/serverStatus/>`_.
In this type of DCI should be given id of server from where parameter should be taken.

Description of database status parameters can be found there: `dbStats <http://docs.mongodb.org/master/reference/command/dbStats/>`_.

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Parameter
     - Description
   * - MongoDB.collectionsNum(*id*,\ *databaseName*)
     - Contains a count of the number of collections in that database.
   * - MongoDB.objectsNum(*id*,\ *databaseName*)
     - Contains a count of the number of objects (i.e. documents) in the database across all collections.
   * - MongoDB.avgObjSize(*id*,\ *databaseName*)
     - The average size of each document in bytes.
   * - MongoDB.dataSize(*id*,\ *databaseName*)
     - The total size in bytes of the data held in this database including the padding factor.
   * - MongoDB.storageSize(*id*,\ *databaseName*)
     - The total amount of space in bytes allocated to collections in this database for document storage.
   * - MongoDB.numExtents(*id*,\ *databaseName*)
     - Contains a count of the number of extents in the database across all collections.
   * - MongoDB.indexesNum(*id*,\ *databaseName*)
     - Contains a count of the total number of indexes across all collections in the database.
   * - MongoDB.indexSize(*id*,\ *databaseName*)
     - The total size in bytes of all indexes created on this database.
   * - MongoDB.fileSize(*id*,\ *databaseName*)
     - The total size in bytes of the data files that hold the database.
   * - MongoDB.nsSizeMB(*id*,\ *databaseName*)
     - The total size of the namespace files (i.e. that end with .ns) for this database.


List
----

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Parameter
     - Description
   * - MongoDB.ListDatabases(*id*)
     - Returns list of databases existing on this server

Informix
========

|product_name| subagent for Informix (further referred to as Informix subagent) monitors one or more Informix databases and reports database-related parameters.

All parameters available from Informix subagent gathered or calculated once per minute thus its recommended to set DCI poll interval for these items to 60 seconds or more. All parameters are obtained or derived from the data available in Informix system catalogs. Informix subagent does not monitor any of the metrics related to lower level database layers, such as database processes. Monitoring of such parameters can be achieved through the standard |product_name| functionality.

Pre-requisites
--------------

An database user must have rights to Informix system catalog tables.

Configuration
-------------

You can specify multiple databases in the informix section. Each database description must be surrounded by database tags with the id attribute. Id can be any unique integer, it instructs the Informix subagent about the order in which database sections will be processed.

Each database definition supports the following parameters:


.. list-table::
   :widths: 50 100
   :header-rows: 1
   
   * - Parameter
     - Description
   * - Id
     - Database identifier. It will be used to address this database in parameters.	
   * - Name
     - Database name. This is a name of Informix DSN.
   * - Server
     - Name of the Informix server.
   * - UserName
     - User name for connecting to database.
   * - Password
     - Database user password.
     
Configuration example:

.. code-block:: cfg

    Subagent=informix.nsm
    
    [informix]
    ID=db1
    DBName = instance1
    DBLogin = user
    DBPassword = password
    
Provided parameters
~~~~~~~~~~~~~~~~~~~

To get a DCI from the subagent, you need to specify the id from the ``informix`` entry in the XML
configuration file (in case of INI configuration, the id will be **1**). To specify the id, you
need to add it enclosed in brackets to the name of the parameter that is being requested (e.g.,
``informix.parameter.to.request(**1**)``). In the example, the parameter ``informix.parameter.to.request``
from the database with the id **1** will be returned.

.. list-table::
   :widths: 40 20 20 70
   :header-rows: 1

   * - Parameter
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
     

MySQL
=====

|product_name| subagent for MySQL monitoring. Monitors one or more instances of MySQL databases and
reports various database-related parameters.

MySQL subagent requires |product_name| the MySQL driver to be available in the system. 

Configuration
-------------

You can specify one or multiple databases in the MySQL section. In case of single database 
definition simply set all required parameters under ``[mysql]`` section. In multi database 
configuration define each database under ``mysql/databases/<name>`` section with unique 
``<name>`` for each database. If no id provided ``<name>`` of the section will be used as a 
database id. 


Each database definition supports the following parameters:

.. list-table::
   :widths: 50 200 200
   :header-rows: 1
   
   * - Parameter
     - Description
     - Default value
   * - Id
     - Database identifier. It will be used to address this database in parameters.	
     - localdb - for single DB definition; last part of section name - for multi database definition
   * - Name
     - Database name. This is a name of MySQL DSN.
     - information_schema
   * - Server
     - Name or IP of the MySQL server.
     - 127.0.0.1
   * - UserName
     - User name for connecting to database.
     - netxms
   * - Password
     - Database user password or encypred password. To encrypt password check :ref:`nxencpasswd-tools-label` tool.
     - 
     
Single database configuration example:

.. code-block:: cfg

    Subagent=mysql.nsm
    
    [mysql]
    ID=db1
    DBName = instance1
    DBLogin = user
    DBPassword = password
    

Multi database configuration example:

.. code-block:: cfg

    Subagent=mysql.nsm
    
    [mysql/databases/database#1]
    ID=db1
    DBName = instance1
    DBLogin = user
    DBPassword = password
    Server = netxms.demo
    
    
    [mysql/databases/local]
    DBName = information_schema
    DBLogin = user
    DBPassword = encPassword
    Server = 127.0.0.1

    
Provided parameters
-------------------

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Parameter
     - Description
   * - MySQL.Connections.Aborted(*id*)
     - MySQL: aborted connections
   * - ySQL.Connections.BytesReceived(*id*)
     - MySQL: bytes received from all clients
   * - ySQL.Connections.BytesSent(*id*)
     - MySQL: bytes sent to all clients
   * - ySQL.Connections.Current(*id*)
     - MySQL: number of active connections
   * - ySQL.Connections.CurrentPerc(*id*)
     - MySQL: connection pool usage (%)
   * - ySQL.Connections.Failed(*id*)
     - MySQL: failed connection attempts
   * - ySQL.Connections.Limit(*id*)
     - MySQL: maximum possible number of simultaneous connections
   * - ySQL.Connections.Max(*id*)
     - MySQL: maximum number of simultaneous connections
   * - ySQL.Connections.MaxPerc(*id*)
     - MySQL: maximum connection pool usage  (%)
   * - ySQL.Connections.Total(*id*)
     - MySQL: cumulative connection count
   * - ySQL.InnoDB.BufferPool.Dirty(*id*)
     - MySQL: InnoDB used buffer pool space in dirty pages
   * - ySQL.InnoDB.BufferPool.DirtyPerc(*id*)
     - MySQL: InnoDB used buffer pool space in dirty pages (%)
   * - ySQL.InnoDB.BufferPool.Free(*id*)
     - MySQL: InnoDB free buffer pool space
   * - ySQL.InnoDB.BufferPool.FreePerc(*id*)
     - MySQL: InnoDB free buffer pool space (%)
   * - ySQL.InnoDB.BufferPool.Size(*id*)
     - MySQL: InnoDB buffer pool size
   * - ySQL.InnoDB.BufferPool.Used(*id*)
     - MySQL: InnoDB used buffer pool space
   * - ySQL.InnoDB.BufferPool.UsedPerc(*id*)
     - MySQL: InnoDB used buffer pool space (%)
   * - ySQL.InnoDB.DiskReads(*id*)
     - MySQL: InnoDB disk reads
   * - ySQL.InnoDB.ReadCacheHitRatio(*id*)
     - MySQL: InnoDB read cache hit ratio (%)
   * - ySQL.InnoDB.ReadRequest(*id*)
     - MySQL: InnoDB read requests
   * - ySQL.InnoDB.WriteRequest(*id*)
     - MySQL: InnoDB write requests
   * - ySQL.IsReachable(*id*)
     - MySQL: is database reachable
   * - ySQL.MyISAM.KeyCacheFree(*id*)
     - MySQL: MyISAM key cache free space
   * - ySQL.MyISAM.KeyCacheFreePerc(*id*)
     - MySQL: MyISAM key cache free space (%)
   * - ySQL.MyISAM.KeyCacheReadHitRatio(*id*)
     - MySQL: MyISAM key cache read hit ratio (%)
   * - ySQL.MyISAM.KeyCacheSize(*id*)
     - MySQL: MyISAM key cache size
   * - ySQL.MyISAM.KeyCacheUsed(*id*)
     - MySQL: MyISAM key cache used space
   * - ySQL.MyISAM.KeyCacheUsedPerc(*id*)
     - MySQL: MyISAM key cache used space (%)
   * - ySQL.MyISAM.KeyCacheWriteHitRatio(*id*)
     - MySQL: MyISAM key cache write hit ratio (%)
   * - ySQL.MyISAM.KeyDiskReads(*id*)
     - MySQL: MyISAM key cache disk reads
   * - ySQL.MyISAM.KeyDiskWrites(*id*)
     - MySQL: MyISAM key cache disk writes
   * - ySQL.MyISAM.KeyReadRequests(*id*)
     - MySQL: MyISAM key cache read requests
   * - ySQL.MyISAM.KeyWriteRequests(*id*)
     - MySQL: MyISAM key cache write requests
   * - ySQL.OpenFiles.Current(*id*)
     - MySQL: open files
   * - ySQL.OpenFiles.CurrentPerc(*id*)
     - MySQL: open file pool usage (%)
   * - ySQL.OpenFiles.Limit(*id*)
     - MySQL: maximum possible number of open files
   * - ySQL.Queries.Cache.HitRatio(*id*)
     - MySQL: query cache hit ratio (%)
   * - ySQL.Queries.Cache.Hits(*id*)
     - MySQL: query cache hits
   * - ySQL.Queries.Cache.Size(*id*)
     - MySQL: query cache size
   * - ySQL.Queries.ClientsTotal(*id*)
     - MySQL: number of queries executed by clients
   * - ySQL.Queries.Delete(*id*)
     - MySQL: number of DELETE queries
   * - ySQL.Queries.DeleteMultiTable(*id*)
     - MySQL: number of multitable DELETE queries
   * - ySQL.Queries.Insert(*id*)
     - MySQL: number of INSERT queries
   * - ySQL.Queries.Select(*id*)
     - MySQL: number of SELECT queries
   * - ySQL.Queries.Slow(*id*)
     - MySQL: slow queries
   * - ySQL.Queries.SlowPerc(*id*)
     - MySQL: slow queries (%)
   * - ySQL.Queries.Total(*id*)
     - MySQL: number of queries
   * - ySQL.Queries.Update(*id*)
     - MySQL: number of UPDATE queries
   * - ySQL.Queries.UpdateMultiTable(*id*)
     - MySQL: number of multitable UPDATE queries
   * - ySQL.Server.Uptime(*id*)
     - MySQL: server uptime
   * - ySQL.Sort.MergePasses(*id*)
     - MySQL: sort merge passes
   * - ySQL.Sort.MergeRatio(*id*)
     - MySQL: sort merge ratio (%)
   * - ySQL.Sort.Range(*id*)
     - MySQL: number of sorts using ranges
   * - ySQL.Sort.Scan(*id*)
     - MySQL: number of sorts using table scans
   * - ySQL.Tables.Fragmented(*id*)
     - MySQL: fragmented tables
   * - ySQL.Tables.Open(*id*)
     - MySQL: open tables
   * - ySQL.Tables.OpenLimit(*id*)
     - MySQL: maximum possible number of open tables
   * - ySQL.Tables.OpenPerc(*id*)
     - MySQL: table open cache usage (%)
   * - ySQL.Tables.Opened(*id*)
     - MySQL: tables that have been opened
   * - ySQL.TempTables.Created(*id*)
     - MySQL: temporary tables created
   * - ySQL.TempTables.CreatedOnDisk(*id*)
     - MySQL: temporary tables created on disk
   * - ySQL.TempTables.CreatedOnDiskPerc(*id*)
     - MySQL: temporary tables created on disk (%)
   * - ySQL.Threads.CacheHitRatio(*id*)
     - MySQL: thread cache hit ratio (%)
   * - ySQL.Threads.CacheSize(*id*)
     - MySQL: thread cache size
   * - ySQL.Threads.Created(*id*)
     - MySQL: threads created
   * - ySQL.Threads.Running(*id*)
     - MySQL: threads running
