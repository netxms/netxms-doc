.. _application-monitoring:

======================
Application monitoring
======================

Process monitoring
==================

Platform subagents support process monitoring. Process metrics have "Process.*" format.
Metrics differ between different OS. Detailed description of each metric can be found
in :ref:`list-of-supported-metrics`.

.. _dbquery:

Application Database Monitoring
===============================

For application database monitoring can be used database monitoring subagents or
database query subagents. Information about database monitoring subagents can be
found :ref:`there<database-monitoring>`. In this chapter will be described only
DBQuery subagents usage and configuration. This subagent supports all databases that
are supported by |product_name| server :ref:`link to supported database list<supported-db-list>`.

This type of Metrics provide DBQuery subagent. This subagent has 2 types of Metrics:
one that periodically executes SQL queries and returns results and error
codes as Metric parameters and second execute queries by Metric request (synchronously).
SQL queries are specified in the agent configuration. Background query can be also
executed per request. Synchronously executed query can have parameters that are
passes to it by DCI configuration.

.. versionadded:: 2.5
   Synchronously executed queries

For time consuming SQL requests it is highly recommended to use background execution.
Heavy SQL can cause request timeout for synchronous execution.

Metrics
-------

When loaded, DBQuery subagent adds the following metrics to agent:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Metric                                 | Description                                                                                                |
+========================================+============================================================================================================+
| DB.Query(*dbid*,\ *query*)             | Result of immediate execution of the query *query* in database identified by *dbid*. Database with given   |
|                                        | name must be defined in configuration file.                                                                |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| DB.QueryResult(*name*)                 | Last result of execution of the query *name*. Query with given name must be defined in configuration file. |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| DB.QueryStatus(*name*)                 | Status of last execution of the query *name*. Query with given name must be defined in configuration file. |
|                                        | Value returned is native SQL error code.                                                                   |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| DB.QueryStatusText(*name*)             | Status of last execution of the query *name* as a text. Query with given name must be defined              |
|                                        | in configuration file.                                                                                     |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| *queryName*                            | Result of immediate execution of query defined in agent config file with name *queryName*.                 |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| *queryName*\ (\ *param1*, *param2*...) | Result of immediate execution of query defined in agent config file with name *queryName* like             |
|                                        | ConfigurableQuery metric. Where *param1*, *param2*... are parameters to bind into defined query.           |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+


Tables
------

When loaded, DBQuery subagent adds the following tables to agent:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Table                                  | Description                                                                                                |
+========================================+============================================================================================================+
| DB.Query(*dbid*,\ *query*)             | Result of immediate execution of the query *query* in database identified by *dbid*. Database with given   |
|                                        | name must be defined in configuration file.                                                                |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| DB.QueryResult(*name*)                 | Last result of execution of the query *name*. Query with given name must be defined in configuration file. |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| *queryName*                            | Result of immediate execution of query defined in agent config file with name *queryName*.                 |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| *queryName*\ (\ *param1*, *param2*...) | Result of immediate execution of query defined in agent config file with name *queryName* like             |
|                                        | ConfigurableQuery metric. Where *param1*, *param2*... are parameters to bind into defined query.           |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+

Configuration file
------------------

All configuration parameters related to DBQuery subagent should be placed into **\*DBQUERY** section of agent's configuration file.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 25 50 200

   * - Parameter
     - Format
     - Description
   * - Database
     - semicolon separated option list
     - Define new database connection (See database connection options section below).
   * - Query
     - *name*:*dbid*:*interval*:*query*
     - Define new query. This parameter can be specified multiple times to define multiple queries.
       Fields in query definition have the following meaning:

        - *name*     Query name which will be used in parameters to retrieve collected data.
        - *dbid*     Database ID (defined by Database parameter)
        - *interval* Polling interval in seconds.
        - *query*    SQL query to be executed.
   * - ConfigurableQuery
     - *name*:*dbid*:*description*:*query*
     - Define new query. This parameter can be specified multiple times to define
       multiple queries. Fields in query definition have the following meaning:

        - *name*        Query name which will be used in parameters to retrieve collected data.
        - *dbid*        Database ID (defined by Database parameter)
        - *description* Description that will be shown in agents parameter description.
        - *query*       SQL query to be executed.


Database connection options
---------------------------

+-----------------------+-----------+--------------------------------------------------+
| Name                  | Status    | Description                                      |
+=======================+===========+==================================================+
| **dbname**            | optional  | Database name.                                   |
+-----------------------+-----------+--------------------------------------------------+
| **driver**            | mandatory | Database driver name. Available drivers are:     |
|                       |           | - db2.ddr                                        |
|                       |           | - informix.ddr                                   |
|                       |           | - mssql.ddr                                      |
|                       |           | - mysql.ddr                                      |
|                       |           | - odbc.ddr                                       |
|                       |           | - oracle.ddr                                     |
|                       |           | - pgsql.ddr                                      |
|                       |           | - sqlite.ddr                                     |
+-----------------------+-----------+--------------------------------------------------+
| **encryptedPassword** | optional  | Database password in encrypted form (use         |
|                       |           | :ref:`nxencpasswd-tools-label` command line tool |
|                       |           | to encrypt passwords). This option takes         |
|                       |           | precedence over **password** option.             |
+-----------------------+-----------+--------------------------------------------------+
| **id**                | mandatory | Database connection ID which will be used to     |
|                       |           | identify this connection in configuration and    |
|                       |           | parameters.                                      |
+-----------------------+-----------+--------------------------------------------------+
| **login**             | optional  | Login name.                                      |
+-----------------------+-----------+--------------------------------------------------+
| **password**          | optional  | Database password in clear text form.            |
+-----------------------+-----------+--------------------------------------------------+
| **server**            | optional  | Database server name or IP address.              |
+-----------------------+-----------+--------------------------------------------------+


Configuration Example
---------------------

.. code-block:: cfg

   # This sample nxagentd.conf instructs agent to:
   #   1. load DBQuery subagent
   #   2. Define two databases - db1 (Oracle) and db2 (MySQL).
   #   3. Execute query "SELECT f1 FROM table1" in database db1 every 60 seconds
   #   4. Execute query "SELECT f1 FROM table2 WHERE f2 LIKE ':%'" on DSN2 every 15 seconds

   MasterServers = netxms.demo
   SubAgent = dbquery.nsm

   *DBQUERY
   Database = id=db1;driver=oracle.ddr;server=10.0.0.2;login=netxms;encryptedPassword=H02kxYckADXCpgp+8SvHuMKmCn7xK8e4wqYKfvErx7g=
   Database = id=db2;driver=mysql.ddr;server=10.0.0.4;dbname=test_db;login=netxms;password=netxms1
   Query = query1:db1:60:SELECT f1 FROM table1
   Query = query2:db2:15:SELECT f1 FROM table2 WHERE f2 LIKE ':%'
   ConfigurableQuery = query3:db2:Comment in param:SELECT name FROM images WHERE name like ?



Log monitoring
==============

Application logs can be added to monitoring. For log monitoring configuration refer to
:ref:`log-monitoring` chapter.

External Metrics
================

It is possible to define External metrics that will get metric data from the script that
is executed on the agent. This option can be used to get status from some command line
tools or from self made scripts. Information about options and configuration is
available in :ref:`agent-external-parameter` chapter.
