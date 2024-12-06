.. _application-monitoring:

======================
Application monitoring
======================

Process monitoring
==================

Platform subagents support process monitoring. Process metrics have "Process.*"
format. Metrics differ between different OS. Detailed description of each metric
can be found in :ref:`list-of-supported-metrics`.

.. _dbquery:

Application Database Monitoring
===============================

For application database monitoring you can use database monitoring subagents or
database query subagents. Information about database monitoring subagents can be
found in :ref:`database-monitoring`. This chapter discusses only DBQuery
subagents configuration and usage. 

DBQuery subagent has 2 types of query execution: background - that periodically
executes SQL query and provides result and error code as metrics and
synchronous, when query is executed by request. Background query, however, can
be also executed per request. Synchronously executed query can have parameters
that are supplied along with requested metric. SQL queries are specified in the
agent configuration or a full query can be supplied via ``DB.Query()`` metric. 

For time consuming SQL requests it is highly recommended to use background
execution. Heavy SQL can cause request timeout for synchronous execution.


Configuration file
------------------

General configuration parameters related to DBQuery subagent are set in
**[DBQUERY]** section of agent's configuration file. The following parameters
are supported:

.. list-table::
   :header-rows: 1
   :widths: 42 52 100

   * - Parameter
     - Format
     - Description
   * - AllowEmptyResultSet
     - yes or no
     - If set to ``yes`` (default), agent returns empty metric value if database
       returns empty result. If set to ``no``, agents returns error in case if
       query returns empty result. 
   * - Database
     - Semicolon-separated option list
     - Database connection information. **Deprecated, specify database
       connection parameters in [DBQUERY/Databases/id] sections**
   * - Query
     - *name*:*dbid*:*interval*:*query*
     - Define query scheduled for background execution. Can be specified
       multiple times to define multiple queries. Fields in query definition
       have the following meaning:

        - *name* - Query name which will be used in metrics to retrieve
          collected data.
        - *dbid* - Database connection ID
        - *interval* - Polling interval in seconds.
        - *query* - SQL query to be executed.
   * - ConfigurableQuery
     - *name*:*dbid*:*description*:*query*
     - Define query for synchronous execution. Can be specified multiple times
       to define multiple queries. Fields in query definition have the following
       meaning:

        - *name* - Query name which will be used in metrics to retrieve
          collected data.
        - *dbid* - Database connection ID
        - *description* - Description that will be shown in agents parameter
          description.
        - *query* - SQL query to be executed. Bind variables are supported,
          question mark (``?``) placeholders in the query will be substituted
          with parameters supplied along with requested metric. 


Database connection parameters are set in separate sections named
**[DBQUERY/Databases/id]** where ``id`` is database connection id used to
identify this connection in configuration parameters and agent metrics. The
following parameters are supported:


.. list-table::
   :header-rows: 1
   :widths: 40 25 100

   * - Name
     - Status
     - Description
   * - **name** 
     - optional
     - Database name
   * - **DBDriverOptions**
     - optional
     - Additional driver-specific parameters
   * - **driver** 
     - mandatory
     - Database driver name. Available drivers are: 

        - db2
        - informix
        - mssql
        - mysql
        - odbc
        - oracle
        - pgsql
        - sqlite        
   * - **encryptedPassword**
     - optional
     - Database password in encrypted form (use :ref:`nxencpasswd-tools-label`
       command line tool to encrypt passwords). This option takes precedence
       over **password** option
   * - **login** 
     - optional
     - Login name
   * - **password**
     - optional
     - Database password. Remember to enclose password in double quotes
       ("password") if it contains # character. This parameter automatically
       detects and accepts password encrypted with
       :ref:`nxencpasswd-tools-label` tool.
   * - **server**
     - optional
     - Database server name or IP address.


Configuration Example
---------------------

.. code-block:: sh

   MasterServers = netxms.demo
   SubAgent = dbquery.nsm

   [DBQUERY]
   # Query1 will be executed every 60 seconds (be can be also executed on-demand via metric "query1"):
   Query = query1:db1:60:SELECT f1 FROM table1

   # Query2 will be executed on demand, one parameter should be supplied along with the metric
   ConfigurableQuery = query2:db1:This query requires one parameter:SELECT f1 FROM table2 WHERE f2 LIKE ?
   
   [DBQUERY/Databases/db1]
   driver=pgsql
   server=10.0.0.4
   login=netxms
   password=netxms1
   name=test_db


Metrics
-------

When loaded, DBQuery subagent adds the following metrics to agent:

.. list-table::
   :header-rows: 1
   :widths: 50 100

   * - Metric
     - Description
   * - DB.Query(*dbid*,\ *query*)
     - Result of immediate execution of the query *query* in database identified
       by *dbid*. Database with given name must be defined in configuration
       file.
   * - DB.QueryExecutionTime(*name*) 
     - Last execution duration in milliseconds of the query *name*. Query with
       given name must be defined in configuration file.

       .. versionadded:: 4.4.3
        
   * - DB.QueryResult(*name*) 
     - Last result of execution of the query *name*. Query with given name must
       be defined in configuration file.
   * - DB.QueryStatus(*name*) 
     - Status of last execution of the query *name*. Query with given name must
       be defined in configuration file. Value returned is native SQL error
       code. 
   * - DB.QueryStatusText(*name*)
     - Status of last execution of the query *name* as a text. Query with given
       name must be defined in configuration file.
   * - *queryName*  
     - Result of immediate execution of query *queryName* defined in agent
       config file with ``Query=...``.
   * - *queryName*\ (\ *param1*, *param2*...)
     - Result of immediate execution of query *queryName* defined in agent
       config file with ``ConfigurableQuery=...``. Optional parameters *param1*,
       *param2*... will be used as bind variables in the query. 
     

Tables
------

When loaded, DBQuery subagent adds the following tables to agent:

.. list-table::
   :header-rows: 1
   :widths: 50 100

   * - Table
     - Description
   * - DB.Query(*dbid*,\ *query*)
     - Result of immediate execution of the query *query* in database identified
       by *dbid*. Database with given name must be defined in configuration
       file
   * - DB.QueryResult(*name*)
     - Last result of execution of the query *name*. Query with given name must
       be defined in configuration file
   * - *queryName*
     - Result of immediate execution of query *queryName* defined in agent
       config file with ``Query=...``.
   * - *queryName*\ (\ *param1*, *param2*...)
     - Result of immediate execution of query *queryName* defined in agent
       config file with ``ConfigurableQuery=...``. Optional parameters *param1*,
       *param2*... will be used as bind variables in the query. 




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
