.. _log-monitoring:

==============
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
======================================

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
=================

NetXMS has built-in syslog server, which can be used to receive logs from
network devices and servers. It is also possible to parse incoming syslog
messages in a way similar to Windows Event Log monitoring. To parse syslog
messages, ``LOGWATCH`` subagent is not required – parsing is done by the server
itself. You only need to define monitoring rules in
:menuselection:`Configuration --> Syslog Parser`


Parser Definition File
======================

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
=====================

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
==========

In the ``<file>`` tag you should specify log file to apply this parser to. To specify Windows Event Log, prepend it's name with asterisk (``*``), for example ``*System``.

It is possible to specify the encoding of the log file by adding the ``encoding`` attribute. By default, the parser will attempt to detect the encoding by scaning the file`s BOM. 

File encodings that can be defined in the ``encoding`` attribute:
* ``ACP``
* ``UTF-8``
* ``UCS-2``
* ``UCS-2LE``
* ``UCS-2BE``
* ``UCS-4``
* ``UCS-4LE``
* ``UCS-4BE``

When using ``UCS-2`` or ``UCS-4`` values, the endianness of the system will be detected automatically.

.. _log-monitoring-macros:

Macros
======

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
==============

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
-----------

Tag ``<match>`` contains a POSIX regular expression that is used to match log
records. Parts enclosed in parenthesis can be extracted from log record and
passed as arguments of generated event. You can use macros defined in
:ref:`log-monitoring-macros` section. Also, it is possible to define inverted
match rules (rules when log record considered matching if it does not match
regular expression). Inverted match can be set by setting attribute ``invert``
to ``1``. Other possible option that can be configured is number of times that 
exptession should be matched to generate event. 

Some examples:

.. code-block:: xml

    <match>^Error: (.*)</match>

This regular expression will match any line starting with word ``Error:``, and
everything after this word will be extracted from the log record for use with
an event.

.. code-block:: xml

    <match repeatCount="3" repeatInterval="120" reset="false">[0-9]{3}</match>

This regular expression will match any line containing at least 3 consecutive digits. 
And event will be generated only if this regular expression will be matched 3 or 
more times in 2 minutes(120 seconds). Matched count wount be reset once mark will 
is reached, so if expresstion is matched more than 3 times in 2 minutes, event will 
be generated more than one time. 

.. code-block:: xml

    <match invert="1">abc</match>

This regular expression will match any line not containing character sequence ``abc``.

Possible attributes for tag ``<match>``:

+----------------+------------------------------------------------------+---------------+
| Option         | Description                                          | Default value |
+================+======================================================+===============+
| invert         | If this option set to ``true``, it will be matched   | false         |
|                | amy line that does not contain matching expression.  |               |
+----------------+------------------------------------------------------+---------------+
| repeatCount    | The number ot times expression should be matched to  | 0             |
|                | generate event. It this option set to ``0``, event   |               |
|                | will be generated immediately on expression match.   |               |
+----------------+------------------------------------------------------+---------------+
| repeatInterval | The time interval during which the expression should | 0             |
|                | be matched. It this option set to ``0``, event will  |               |
|                | be generated immediately on expression match.        |               |
+----------------+------------------------------------------------------+---------------+
| reset          | If this option set to ``true``, it will set to zero  | true          |
|                | match repeat count. So if while ``repeatInterval``   |               |
|                | expression have been matched ``repeatCount`` times+1 |               |
|                | it will not generate second event.                   |               |
+----------------+------------------------------------------------------+---------------+


<id> Tag
--------

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
------------

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
-----------

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
--------------

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
---------

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
--------------

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
-----------------

Tag ``<description>`` contains textual description of the rule, which will be shown in parser trace.


<event> Tag
-----------

Tag ``<event>`` defines event to be generated if current log record match to
regular expression defined in ``<match>`` tag. Inside ``<event>`` tag you
should specify event code to be generated (or event name if you configure
server-side syslog parsing). If you wish to pass parts of log record text
extracted with regular expression as event's parameters, you should specify
correct number of parameters in ``params`` attribute.


<context> Tag
-------------

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
==================================

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
    