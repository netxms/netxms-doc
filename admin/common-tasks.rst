.. _getting-things-monitored:

##############################################
Common monitoring tasks (rename this chapter!)
##############################################


Operating System
================


File meta information
=====================

.. todo::

  size, mtime, hash

.. _log-monitoring:
  
Log monitoring
==============

With NetXMS you can monitor changes in text log files, Windows Event Log, and
built-in syslog server. All log monitoring done by agents, except for built-in
syslog server. In general, log processing goes as following:

#. When new line added to log file, it is passed to appropriate log parser
#. If line matched one of the patterns, event associated with this pattern sent
   to server
#. Server receives event and passes to event processing policy as usual, with
   event source set to node from which event was received.


Agent Configuration for Log Monitoring
--------------------------------------

To be able to monitor logs with NetXMS agent, you should load ``LOGWATCH``
subagent and define parser configuration for each log file you wish to monitor.
Example of agent configuration file:

.. code-block:: cfg

   SubAgent = logwatch.nsm
 
   # Below is log parsers definitions
   *LOGWATCH
   Parser = C:\NetXMS\parser1.xml
   Parser = C:\NetXMS\parser2.xml


Syslog Monitoring
-----------------

NetXMS has built-in syslog server, which can be used to receive logs from
network devices and servers. It is also possible to parse incoming syslog
messages in a way similar to Windows Event Log monitoring. To parse syslog
messages, ``LOGWATCH`` subagent is not required – parsing is done by the server
itself. You only need to define monitoring rules in
:menuselection:`Configuration --> Syslog Parser`


Parser Definition File
----------------------

Parser definition file is an XML document with the following structure:

.. code-block:: xml

    <parser>
        <file>file name</file>
        <macros>
            <macro name="name">macro body</macro>
            <!-- more <macro> tags can follow -->
        </macros>
        <rules>
            <rule>
                <match>regexp</match>
                <id>event id</id>
                <level>severity level</level>
                <source>event source</source>
                <event>event</event>
                <context>context</context>
            </rule>
            <!-- more <rule> tags can follow -->
        </rules>
    </parser>


Entire ``<macros>`` section can be omitted, and inside ``<rule>`` tag only ``<match>`` is mandatory.

Global Parser Options
---------------------

In the ``<parser>`` tag you can specify the following options:

+------------+------------------------------------------------------+---------------+
| Option     | Description                                          | Default value |
+============+======================================================+===============+
| processAll | If this option set to ``1``, parser will always pass | 0             |
|            | log record through all rules. If this option set to  |               |
|            | ``0``, processing will stop after first match.       |               |
+------------+------------------------------------------------------+---------------+
| trace      | Trace level                                          | 0             |
+------------+------------------------------------------------------+---------------+


<file> Tag
----------

In the ``<file>`` tag you should specify log file to apply this parser to. To specify Windows Event Log, prepend it's name with asterisk (``*``), for example ``*System``.


.. _log-monitoring-macros:

Macros
------

In the ``<macros>`` section you can define macros for use in matching rules. For example, it can be useful to define macro for a timestamp preceding each log record and use it in matching rules instead of actual regular expression. You can define as many macros as you wish, each within it's own ``<macro>`` tag. Each macro should have unique name, defined in ``name`` attribute, and can be used in matching rules in form ``@{name}``.

Example: you need to parse log file where each line starts with timestamp in
format ``dd/mm/yy HH:MM:SS``. You can define the following macro:

.. code-block:: xml

    <rules>
        <rule>
            <match>@{timestamp}.*([A-Za-z]+) failed.*</match>
            <event>12345</event>
        </rule>
        <rule>
            <match>@{timestamp}.*error.*</match>
            <event>45678</event>
        </rule>
    </rules>

Please note that ``<macros>`` section always should be located before
``<rules>`` section in parser definition file.


Matching rules
--------------

In the ``<rules>`` section you define matching rules for log records. Each rule
placed inside it's own ``<rule>`` tag. Each rule can have additional options:

.. list-table::
   :widths: 15 70 15
   :header-rows: 1

   * - Option
     - Description
     - Default value
   * - break
     - If this option set to ``1`` and curent line match to regular expression
       in the rule, parser will stop processing of current line, even if global
       parser option ``processAll`` was set to ``1``. If this option set to
       ``0`` (which is default), processing will stop according to
       ``processAll`` option settings.
     - 0
   * - context
     - Name of the context this rule belongs to. If this option is set, rule will be processed only if given context was already activated with <context> tag in one of the rules processed earlier (it can be either same line or one of the previous lines).
     - *empty*

Inside the ``<rule>`` section there are the following additional tags:
``<match>``, ``<description>``, ``<event>``, and ``<context>``. Only
``<match>`` section is mandatory – it specifies regular expression against
which log record should be matched. All other tags are optional and define
parser behavior if a record matches the regular expression.


<match> Tag
~~~~~~~~~~~

Tag ``<match>`` contains a POSIX regular expression that is used to match log
records. Parts enclosed in parenthesis can be extracted from log record and
passed as arguments of generated event. You can use macros defined in
:ref:`log-monitoring-macros` section. Also, it is possible to define inverted
match rules (rules when log record considered matching if it does not match
regular expression). Inverted match can be set by setting attribute ``invert``
to ``1``.

Some examples:

.. code-block:: xml

    <match>^Error: (.*)</match>

This regular expression will match any line starting with word ``Error:``, and
everything after this word will be extracted from the log record for use with
an event.

.. code-block:: xml

    <match>[0-9]{3}</match>

This regular expression will match any line containing at least 3 consecutive digits.

.. code-block:: xml

    <match invert="1">abc</match>

This regular expression will match any line not containing character sequence ``abc``.


<id> Tag
~~~~~~~~

Tag ``<id>`` can be used to filter records from Windows Event Log by event ID.
You can specify either single event ID or ID range (by using two numbers
separated with minus sign). For example:


.. code-block:: xml

    <id>7</id>

will match records with event ID equal 7, and

.. code-block:: xml

    <id>10-20</id>

will match records with ID in range from 10 to 20 (inclusive).  This tag has no
effect for text log files, and can be used as a synonym for ``<facility>`` tag
for syslog monitoring.


<source> Tag
~~~~~~~~~~~~

Tag ``<source>`` can be used to filter records from Windows Event Log by event
source. You can specify exact event source name or pattern with ``*`` and ``?``
meta characters.

Some examples:

.. code-block:: xml

    <source>Tcpip</source>

will match records with event source ``"Tcpip`` (case-insensitive), and

.. code-block:: xml

    <source>X*</source>

will match records with event source started from letter ``X``.  This tag has
no effect for text log files, and can be used as a synonym for ``<tag>`` tag
for syslog monitoring.


<level> Tag
~~~~~~~~~~~

Tag ``<level>`` can be used to filter records from Windows Event log by event
severity level (also called :guilabel:`event type` in older Windows versions).
Each severity level has it's own code, and to filter by multiple severity
levels you should specify sum of appropriate codes. Severity level codes are
following:


+------+---------------+
| Code |  Severity     |
+======+===============+
| 1    | Error         |
+------+---------------+
| 2    | Warning       |
+------+---------------+
| 4    | Information   |
+------+---------------+
| 8    | Audit Success |
+------+---------------+
| 16   | Audit Failure |
+------+---------------+


Some examples:

.. code-block:: xml

    <level>1</level>

will match all records with severity level :guilabel:`Error`, and

.. code-block:: xml

    <level>6</level>

will match all records with severity level :guilabel:`Warning` or
:guilabel:`Information`.  This tag has no effect for text log files, and can be
used as a synonym for ``<severity>`` tag for syslog monitoring.


<facility> Tag
~~~~~~~~~~~~~~

Tag ``<facility>`` can be used to filter syslog records (received by NetXMS
built-in syslog server) by facility code. The following facility codes can be
used:

+--------+------------------------------------------+
|   Code |     Facility                             |
+========+==========================================+
|  0     | kernel messages                          |
+--------+------------------------------------------+
|  1     | user-level messages                      |
+--------+------------------------------------------+
|  2     | mail system                              |
+--------+------------------------------------------+
|  3     | system daemons                           |
+--------+------------------------------------------+
|  4     | security/authorization messages          |
+--------+------------------------------------------+
|  5     | messages generated internally by syslogd |
+--------+------------------------------------------+
|  6     | line printer subsystem                   |
+--------+------------------------------------------+
|  7     | network news subsystem                   |
+--------+------------------------------------------+
|  8     | UUCP subsystem                           |
+--------+------------------------------------------+
|  9     | clock daemon                             |
+--------+------------------------------------------+
|  10    | security/authorization messages          |
+--------+------------------------------------------+
|  11    | FTP daemon                               |
+--------+------------------------------------------+
|  12    | NTP subsystem                            |
+--------+------------------------------------------+
|  13    | log audit                                |
+--------+------------------------------------------+
|  14    | log alert                                |
+--------+------------------------------------------+
|  15    | clock daemon                             |
+--------+------------------------------------------+
|  16    | local use 0 (local0)                     |
+--------+------------------------------------------+
|  17    | local use 1 (local1)                     |
+--------+------------------------------------------+
|  18    | local use 2 (local2)                     |
+--------+------------------------------------------+
|  19    | local use 3 (local3)                     |
+--------+------------------------------------------+
|  20    | local use 4 (local4)                     |
+--------+------------------------------------------+
|  21    | local use 5 (local5)                     |
+--------+------------------------------------------+
|  22    | local use 6 (local6)                     |
+--------+------------------------------------------+
|  23    | local use 7 (local7)                     |
+--------+------------------------------------------+


You can specify either single facility code or facility code range (by using
two numbers separated by minus sign). For example:

.. code-block:: xml

   <facility>7</facility>

will match records with facility code equal 7, and

.. code-block:: xml

   <facility>10-20</facility>

will match records with facility code in range from 10 to 20 (inclusive).  This
tag has no effect for text log files, and can be used as a synonym for ``<id>``
tag for Windows Event Log monitoring.


<tag> Tag
~~~~~~~~~

Tag ``<tag>`` can be used to filter syslog records (received by NetXMS built-in
syslog server) by content of ``tag`` field. You can specify exact value or
pattern with ``*`` and ``?`` meta characters.

Some examples:

.. code-block:: xml

    <tag>httpd</tag>

will match records with tag "httpd" (case-insensetive), and

.. code-block:: xml

    <tag>X*</tag>

will match records with tag started from letter ``X``.  This tag has no effect
for text log files, and can be used as a synonym for ``<source>`` tag for
Windows Event Log monitoring.


<severity> Tag
~~~~~~~~~~~~~~

Tag ``<severity>`` can be used to filter syslog records (received by NetXMS
built-in syslog server) by severity level. Each severity level has it's own
code, and to filter by multiple severity levels you should specify sum of
appropriate codes. Severity level codes are following:


+------+---------------+
| Code |  Severity     |
+======+===============+
| 1    | Emergency     |
+------+---------------+
| 2    | Alert         |
+------+---------------+
| 4    | Critical      |
+------+---------------+
| 8    | Error         |
+------+---------------+
| 16   | Warning       |
+------+---------------+
| 32   | Notice        |
+------+---------------+
| 64   | Informational |
+------+---------------+
| 128  | Debug         |
+------+---------------+


Some examples:

.. code-block:: xml

    <severity>1</severity>

will match all records with severity level :guilabel:`Emergency`, and

.. code-block:: xml

    <severity>6</severity>

will match all records with severity level :guilabel:`Alert` or
:guilabel:`Critical`. This tag has no effect for text log files, and can be
used as a synonym for ``<level>`` tag for Windows Event Log monitoring.


<description> Tag
~~~~~~~~~~~~~~~~~

Tag ``<description>`` contains textual description of the rule, which will be shown in parser trace.


<event> Tag
~~~~~~~~~~~

Tag ``<event>`` defines event to be generated if current log record match to
regular expression defined in ``<match>`` tag. Inside ``<event>`` tag you
should specify event code to be generated (or event name if you configure
server-side syslog parsing). If you wish to pass parts of log record text
extracted with regular expression as event's parameters, you should specify
correct number of parameters in ``params`` attribute.


<context> Tag
~~~~~~~~~~~~~

Tag ``<context>`` defines activation or deactivation of contexts. It has the
following format:

.. code-block:: xml

   <context action="action" reset="reset mode">context name</context>

Possible actions are:

+--------+----------------------------------------------------+
| Action | Description                                        |
+========+====================================================+
| clear  | Deactivate (clear "active" flag of) given context. |
+--------+----------------------------------------------------+
| set    | Activate (set "active" flag of) given context.     |
+--------+----------------------------------------------------+

Reset mode determines how context will be deactivated (reset). Possible values for reset mode are:

+------------+-------------------------------------------------------+
| Reset mode | Description                                           |
+============+=======================================================+
| auto       | Deactivate context automatically after first match    |
|            | in context (match rule with ``context`` attribute set |
|            | to given context).                                    |
+------------+-------------------------------------------------------+
| manual     | Context can be deactivated only by explicit           |
|            | ``<context action="clear">`` statement.               |
+------------+-------------------------------------------------------+

Both ``action`` and ``reset`` attributes can be omitted; default value for
``action`` is ``set``, and default value for ``reset`` is ``auto``.


Examples of Parser Definition File
----------------------------------

Generate event with code ``100000`` if line in the log file /var/log/messages
contains word error:

.. code-block:: xml

    <parser>
        <file>/var/log/messages</file>
        <rules>
            <rule>
                <match>error</match>
                <event>100000</event>
            </rule>
        </rules>
    </parser>

Generate event with code ``200000`` if line in the log file ``C:\demo.log``
contains word ``process:`` and is immediately following line containing text
``process startup failed``; everything after word ``process:`` will be sent as
event's parameter:

.. code-block:: xml

    <parser>
        <file>C:\demo.log</file>
        <rules>
            <rule>
                <match>process startup failed</match>
                <context action="set" reset="auto">STARTUP_FAILED</context>
            </rule>
            <rule context="STARTUP_FAILED">
                <match>process:(.*)</match>
                <event params="1">200000</event>
            </rule>
        </rules>
    </parser>

.. _service-monitoring:
    
Service monitoring
==================

There are two options to add service monitoring: the first one is to add it through 
menu option :guilabel:`Create Network Service...` as an object with the status 
that will be propagated on a node, and the second one is to add it's monitoring as 
DCI. 

Network Service
---------------

Object representing network service running on a node (like http or
ssh), which is accessible online (via TCP IP). Network Service objects 
are always created manually. Currently, the system works with the following 
protocols - HTTP, POP3, SMTP, Telnet, SSH and Custom protocol type. For Custom
protocol, a user should define the TCP port number and the system will be
checking whether that port is available. For the predefined standard services
the system will also check whether an appropriate response is returned. In case
of SMTP, the system will send a test mail, in case of POP3 – try to log in with
a certain user, in case of HTTP – check whether the contents of a desired web
page correspond to a certain given template. As soon as the Network Service
object is created, it will be automatically included into the status poll. Each
time when the status poll for the particular node is carried out, all Network
Service objects are polled for a reply. If an object's reply corresponds to a
certain condition, its status is set as NORMAL. If an object is not responding,
its status will be hanged to CRITICAL. Wile network service creation there can be 
also created :term:`DCI` that will collect service status. 

.. figure:: _images/create_network_service.png

In default configuration request is done 
with help of Port Check subagent on the server node. If it should be done through 
different node is should be changed in it's properties after service creation by 
selecting Poller node. There is also possibility to set quantity of polls that is 
required to be sure that state have changed. 

.. figure:: _images/network_service_properties.png

Service monitoring using DCI
----------------------------

Second option is to use :term:`DCI` to monitor service. There are 2 subagents that 
provide service monitoring metrics: PortCheck and NetSVC. It is recommended to use 
NetSVC for all curl supported protocols. As it can check not only availability, but 
also response. For unsupported protocols can be used Custom check of PortCheck 
subagent.


PortCheck configuration
~~~~~~~~~~~~~~~~~~~~~~~

This subagent can be used to check TCP ports and specifically implements checks for 
common services. It is highly recommended to use netsvc subagent especially for 
HTTP and HTTPS monitoring. 

When loaded, PORTCHECK subagent adds the following Metrics to node Metric list:

.. list-table:: 
   :widths: 50 100
   :header-rows: 1
   
   * - Parameter 
     - Description 
   * - ServiceCheck.Custom(\ *target*\ ,\ *port*\ [,\ *timeout*\ ]) 
     - Check that TCP *port* is open on *target*. Optional argument *timeout* specifies timeout in milliseconds.  This is a very simple test that does nothing more than check the port is open.
   * - ServiceCheck.HTTP(\ *target*\ ,[\ *port*\ ],\ *URI*\ ,\ *hostHeader*\ [,\ *regex*\ [,\ *timeout*\ ]])
     - Check that HTTP service is running on *target*.  Optional argument *port* specifies the port to connect with, otherwise 80 will be used.  The *URI* is NOT a URL it is the host header request URI.  As an example to test URL http://www.netxms.org/index.html enter www.netxms.org:/index.html. *hostHeader* is currently not used, but may be the Host option at some point in the request made.  Optional argument *regex* is the regular expression to check returned from the request, otherwise "^HTTP/1.[01] 200 .*" will be used.  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.POP3(\ *target*\ ,\ *username*\ ,\ *password*\ [,\ *timeout*\ )
     - Check that POP3 service is running on *target* and that we are able to login using the supplied *username* and *password*.  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.SMTP(\ *target*\ ,\ *toAddress*\ [,\ *timeout*\ ])
     - Check that SMTP service is running on *target* and that it will accept an e-mail to *toAddress*.  The e-mail will be from noreply@\ *DomainName* using the *DomainName* option in the config file or its default value (see below).  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.SSH(\ *target*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that SSH service is running on *target*.  Optional argument *port* specifies the port to connect with, otherwise 22 will be used.  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.Telnet(\ *target*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that Telnet service is running on *target*.  Optional argument *port* specifies the port to connect with, otherwise 23 will be used.  Optional argument *timeout* specifies timeout in milliseconds.
     
.. note:
  Parameters in [ ] are optional, when optional parameters are used they should 
  be used without [ ]. 
     
     
All of the ServiceCheck.* parameters return the following values:

.. list-table:: 
   :widths: 15 50
   :header-rows: 1
   
   * - Value
     - Description
   * - 0
     - Success, *target* was connected to an returned expected response.
   * - 1
     - Invalid arguments were passed.
   * - 2
     - Cannot connect to *target*.
   * - 3
     - Invalid / Unexpected response from *target*.
     
All configuration parameters related to PORTCHECK subagent should be placed into 
***PORTCHECK** section of agent's configuration file. The following configuration parameters 
are supported:

.. list-table:: 
   :widths: 20 20 100 20
   :header-rows: 1
   
   * - Parameter
     - Format
     - Description
     - Default value
   * - DomainName
     - *string*
     - Set default domain name for processing. Currently this is only used by SMTP check to set the from e-mail address.
     - netxms.org
   * - Timeout
     - *milliseconds*
     - Set response timeout to *milliseconds*.
     - 3000
  
Configuration example:
  
.. code-block:: cfg

   # This sample nxagentd.conf instructs agent to:
   #   1. Load PORTCHECK subagent
   #   2. Set domain name for from e-mail to netxms.demo
   #   3. Default timeout for commands set to 5 seconds (5000 milliseconds)

   MasterServers = netxms.demo
   SubAgent = /usr/lib/libnsm_portcheck.so

   *portCheck
   DomainName = netxms.demo
   Timeout = 5000


NetSVC configuration
~~~~~~~~~~~~~~~~~~~~

This subagent can be used to check network services supported by libcurl. More about 
syntaxes can be found there: http://curl.haxx.se/docs/manpage.html.

This subagent will add this Metrics to node Metric list:

.. list-table:: 
   :widths: 50 100
   :header-rows: 1
   
   * - Parameter 
     - Description 
   * - Service.Check(,) ServiceCheck.Custom(\ *target*\ ,\ *port*\ [,\ *timeout*\ ]) 
     - Check that TCP *port* is open on *target*. Optional argument *timeout* specifies timeout in milliseconds.  This is a very simple test that does nothing more than check the port is open.


HTTP check example: 

.. code-block:: cfg

   Service.Check(https://inside.test.ru/,^HTTP/1\.[01] 200.*)
   
"^HTTP/1\.[01] 200.*" - this is default value and may be missed in expression. 

.. note::
  If agent is build from sources, then libcurl-dev should be installed to 
  build netsvc subagent. 

.. _database-monitoring:

Database monitoring
===================



Oracle
------


DB2
---


MongoDB
-------

Application monitoring
======================

Process monitoring
------------------

Platform subagents support process monitoring. Process metrics have "Process.*" format. 
Metrics differ between different OS. Detailed description of each metric can be found 
in :ref:`list-of-supported-metrics`.

Application Database Monitoring
-------------------------------

For application database monitoring can be used database monitoring subagents or 
database query subagents. Information about database monitoring subagents can be 
found :ref:`there<database-monitoring>`. In this chapter will be described only 
query subagents configuration. 

This type of Metrics provide DBQuery subagent. This subagent has 2 types of Metrics:
one that periodically executes SQL queries and returns results and error
codes as Metric parameters and second execute queries by Metric request(synchronously). 
SQL queries are specified in the agent configuration. Background query can be also 
executed per request. Synchronously executed query can have parameters that are 
passes to it by DCI configuration. 

.. versionadded:: 2.5
   Synchronously executed queries

For time consuming SQL requests it is highly recommended to use background execution. 
Heavy SQL can cause request timeout for synchronous execution. 

Parameters
~~~~~~~~~~

When loaded, DBQuery subagent adds the following parameters to agent:

+----------------------------------------+------------------------------------------------------------------------------------------------------------+
| Parameter                              | Description                                                                                                |
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
|                                        | ConfigurableQuery parameter. Where *param1*, *param2*... are parameters to bind into defined query.        |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+


Tables
~~~~~~

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
|                                        | ConfigurableQuery parameter. Where *param1*, *param2*... are parameters to bind into defined query.        |
+----------------------------------------+------------------------------------------------------------------------------------------------------------+

Configuration file
~~~~~~~~~~~~~~~~~~

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
     - Define new query. This parameter can be specified multiple times to define multiple queries. Fields in query definition have the following meaning:
        - *name*        Query name which will be used in parameters to retrieve collected data.
        - *dbid*        Database ID (defined by Database parameter)
        - *description* Description that will be shown in agents parameter description.
        - *query*       SQL query to be executed.

         
Database connection options
~~~~~~~~~~~~~~~~~~~~~~~~~~~
         
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
~~~~~~~~~~~~~~~~~~~~~

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
--------------

Application logs can be added to monitoring. For log monitoring configuration refer to 
:ref:`log-monitoring` chapter. 

External Metrics
----------------

It is possible to define External metrics that will get metric data from the script that 
is executed on the agent. This option can be used to get status from some command line 
tools or from self made scripts. Information about options and configuration is 
available in :ref:`agent-external-parameter` chapter. 


Monitoring hardware (lm-sensors)
================================


UPS monitoring
==============


Cluster monitoring
==================

.. _monitoring-mobile-device:

Monitoring mobile devices
=========================


