.. _windows_event_log_synchronization:

=================================
Windows Event Log Synchronization
=================================

|product_name| can collect and centrally store Windows event logs. Collection is
performed by |product_name| agents. It's possible to filter by log type, Source
and Event IDs at agent side to reduce network traffic consumption. 

Windows events received by |product_name| server are stored in the database and
can later be viewed in :menuselection:`View --> Windows event log`. Upon
reception event logs can be parsed according to rules and |product_name| events
can be generated.


Agent Configuration for Event Log Synchronization
=================================================

Agent configuration to enable Windows Event Log Synchronization can be done in
two ways:

#. In agent's configuration file
#. Using Agent Configuration policy. For more information see
   :ref:`agent-policies-label`.

Windows Event Log Synchronization subagent should be enabled in agent
configuration:

.. code-block:: cfg

   SubAgent=wineventsync.nsm


Logs that should be monitored (Application, Security, etc) are specified in
``WinEventSync`` section:

.. code-block:: cfg

   [WinEventSync]
   EventLog=Application
   EventLog=Security
   EventLog=System


With above configuration all records in the specified logs will be synchronized. 
It is possible to configure per-log settings to filter only part of records. 
Per-log configuration is specified in sections named according to log name, e.g.
``WinEventSync/System``. 

Filtering by Event IDs is done using parameters ``IncludeEvent`` and
``ExcludeEvent``. You can configure a range like 100-200. Comma separated lists
are not supported, you can however add multiple Include/ExcludeEvent lines.

By default, if no ``IncludeEvent`` or ``ExcludeEvent`` are given, all IDs in
that log will be synced. Explicit Includes override Excludes. So if you
configure an IncludeEvent=201 and an ExcludeEvent=200-300, you will receive all
Events except 200 and 202-300.

To exclude all Event IDs, use ``ExcludeEvent=0-65535``, then you can use
``IncludeEvent`` to select only the IDs you need. 

.. code-block:: cfg

   [WinEventSync/Security]
   IncludeEvent=4624-4625
   IncludeEvent=4800-4803
   ExcludeEvent=0-65535


Filtering by Source is done using parameters ``IncludeSource`` and
``ExcludeSource``. By default, if no ``IncludeSource`` are ``ExcludeSource`` are
given, all sources in that log will be synchronized. You can use
``ExcludeSource=*`` to exclude every source and speficy ``IncludeSource`` to
override the exclude for specific sources. 

.. code-block:: cfg

   [WinEventSync/System]
   IncludeSource=Microsoft-Windows-WindowsUpdateClient
   ExcludeSource=*

Filtering by severity level (also called :guilabel:`event type` in older Windows
versions) is done using parameter ``SeverityFilter``. Each severity level has
it's own numeric value, and to filter by multiple severity levels you should
specify sum of appropriate values (bitmask). Or alternatively you can specify
severity level names separated by commas. Below are level names and their
values:

.. list-table::
   :header-rows: 1
   :widths: 60 20 20

   * - Severity level name
     - Hexadecimal value
     - Decimal value
   * - Error 
     - 0x001
     - 1
   * - Warning
     - 0x002
     - 2
   * - Information
     - 0x004
     - 4
   * - AuditSuccess
     - 0x008
     - 8
   * - AuditFailure
     - 0x010
     - 16
   * - Critical
     - 0x100
     - 256

Below examples will have same result of filtering only Warning and Error records:

.. code-block:: cfg

   [WinEventSync/System]
   SeverityFilter = 0x012


.. code-block:: cfg

   [WinEventSync/System]
   SeverityFilter = 18


.. code-block:: cfg

   [WinEventSync/System]
   SeverityFilter = Warning,Error


Agent log mesages related to windows event log synchronization are written with
tag ``winsyncevent``. For debugging you can add ``DebugTags=winsyncevent:6`` to
agent configuration - this will set debug level 6 for that tag. 

Server Configuration for Event Log Synchronization
==================================================

Upon being received on server Windows events are parsed accoriding to rules
defined in :menuselection:`Configuration --> Windows event parser`. Rules can be
edites in two ways - using graphical editor or XML editor. When switching from
one editor to another all entered information is automatically converted. 

If :guilabel:`Process all` checkbox is not set, rules are processed until first
match. If it's set, all rules are always processed. 

In the :guilabel:`Macros` section you can define macros for use in matching
rules. For example, it can be useful to define macro for IP address and use it
in matching rules instead of actual regular expression. You can define as many
macros as you wish. Each macro should have unique name, and can be used in
matching rules in form ``@{name}``.

A rule can have multiple conditions - regular expression match, severity level,
Event ID, Source, log type.

:guilabel:`Matching regular expression` contains a PCRE compliant regular
expression that is used to match Windows event log records. Parts enclosed in
parenthesis are extracted from Windows event log record and passed as arguments
of generated |product_name| event. You can use macros defined in
:guilabel:`Macros` section. If :guilabel:`Invert` checkbox is set, Windows event
log record will be considered matching if it does not match regular expression.

:guilabel:`Level` can be used to filter records from Windows Event log by event
severity level (also called :guilabel:`event type` in older Windows versions).
Each severity level has it's own numeric value, and to filter by multiple
severity levels you should specify sum of appropriate values (bitmask). Severity
level numerical values are the following:


.. list-table::
   :header-rows: 1
   :widths: 80 20

   * - Severity level
     - Decimal value
   * - Error
     - 1
   * - Warning
     - 2
   * - Information
     - 4
   * - Audit Success
     - 8
   * - Audit Failure
     - 16
   * - Critical (only on Windows 7/Windows Server 2008 and higher) 
     - 256


:guilabel:`Id` can be used to filter records from Windows Event Log by event ID.
You can specify either single event ID (e.g. ``7``) or ID range by using two
numbers separated with minus sign (e.g. ``10-20`` will match records with ID in
range from 10 to 20 inclusive). 

:guilabel:`Source` can be used to filter records from Windows Event Log by event
source. You can specify exact event source name or pattern with ``*`` and ``?``
meta characters. E.g. ``Tcpip`` will match records with event source ``Tcpip``
(case-insensitive), and ``X*`` will match records with event source started from
letter ``X``. 

:guilabel:`Log name` allows to filter records by Windows Event Log name. You can
specify exact name or pattern with ``*`` and ``?`` meta characters. 

:guilabel:`Description` contains textual description of the rule. It is printed
in parser trace in the log file. 

When a rule is matched the following actions can be performed:

    * Generate |product_name| event. Event generation is optional - it could be
      useful to have rules that work as exclusion - 
      match specific conditions and do not perform any actions. 
    * Break. In this case the following rules will not be processed even if
      :guilabel:`Process all` is set. 
    * Do not save to database. If this is set,
      mached Windows Event Log record will not be saved to the database.


Passing parameters to events
============================

The log parser can send parameters to events.
All capture groups will be sent to the event as parameters. 

+----------+----------------------------------------------------+
| Number   | Description                                        |
+==========+====================================================+
| 1…n      | Capture groups                                     |
+----------+----------------------------------------------------+

