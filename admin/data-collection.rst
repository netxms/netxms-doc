.. _data-collection:


###############
Data collection
###############

.. _how_data_collection:

How data collection works
=========================

Every node can have many data collection items configured (see
:ref:`basic-concepts-dci` for detailed description). NetXMS server has a set of
threads dedicated to data collection, called `Data Collectors`, used to gather
information from the nodes according to :term:`DCI` configuration. You can
control how many data collectors will run simultaneously, by changing server
configuration parameter ``NumberOfDataCollectors``.

All configured DCIs are checked for polling requirement every two seconds and
if DCI needs to be polled, appropriate polling request is placed into internal
data polling queue. First available data collector will pick up the request and
gather information from the node according to DCI configuration. If a new value
was received successfully, it's being stored in the database, and thresholds
are checked. After threshold checking, data collector is ready for processing
new request. Processing of a newly received parameter value is outlined on the
figure below.

.. figure:: _images/dci_param_proc.png

   Newly received parameter processing

It is also possibility to push data to server. If DCI source is set to
:guilabel:`Push`, server just waits for new values instead of polling himself
data source.

.. versionadded:: 2.0-M5
    Offline data collection. 
    
By default DCI data is not collected while connection between server and agent is 
broken as poll request could not get till agent. There is special configuration 
that allows to collect data and store it on agent till connection with server is 
restored and collected data is pushed to the server. This option is available for 
metrics, table metrics and proxy SNMP metrics. Not implemented for proxy SNMP table 
metrics. In case of this configuration agent stores DCI configuration locally and does 
all metric collection and dispatch by himself. DCI configuration is synchronized on 
connect, DCI configuration change or SNMP proxy server change. Information about 
configuration options can be found there: :ref:`offline-data-collection`.

.. _dci-configuration:

DCI configuration
=================

Basic configuration
-------------------

Data collection for a node can be configured using management console. To open
data collection configuration window, right-click on node object in
:guilabel:`Object Browser` or on a :guilabel:`Network Map`, and click
:guilabel:`Data Collection Configuration`. You will see the list of configured data
collection items. From here, you can add new or change existing parameters to
monitor. Right click on the item will open pop-up menu with all possible
actions.

.. todo: 
  Add description of each action in DCI object menu. Separate each field description 
  by property pages. 

Each DCI have multiple attributes which affects the way data is collected.
Detailed information about each attribute is given below.


Description
~~~~~~~~~~~

Description is a free-form text string describing DCI. It is not used by the
server and is intended for better information understanding by operators. If
you use the :guilabel:`Select` button to choose a parameter from the list,
description field will be filled automatically.


Parameter
~~~~~~~~~

Name of the parameter of interest, used for making a request to target node.
For NetXMS agent and internal parameters it will be parameter name, and for
SNMP agent it will be an SNMP OID. You can use the :guilabel:`Select` button
for easier selection of required parameter name.


Origin
~~~~~~

Origin of data (method of obtaining data). Possible origins are:

- :guilabel:`NetXMS agent`
- :guilabel:`SNMP agent`
- :guilabel:`CheckPoint SNMP agent`
- :guilabel:`Windows Performance Counter`
- :guilabel:`Internal` (data generated inside NetXMS server process)
- :guilabel:`Push Agent`
- :guilabel:`Script` (from script library, can be used instead of internal dummy)
  

:guilabel:`Push Agent` origin is very different from all others, because it
represents DCIs whose values are pushed to server by external program (usually
via :ref:`nxapush-label` or :ref:`nxpush-label` command line tool) instead of being
polled by the server based on the schedule.


Data Type
~~~~~~~~~

Data type for the parameter. Can be one of the following: :guilabel:`Integer`,
:guilabel:`Unsigned Integer`, :guilabel:`64-bit Integer`, :guilabel:`64-bit
Unsigned Integer`, :guilabel:`Float` (floating point number), or
:guilabel:`String`. Selected data type affects collected data processing - for
example, you cannot use operations like ``less than`` or ``greater than`` on
strings. If you select parameter from the list using the :guilabel:`Select`
button, correct data type will be set automatically.


Polling Interval
~~~~~~~~~~~~~~~~

An interval between consecutive polls, in seconds. If you select the
:guilabel:`Use advanced scheduling` option, this field has no meaning and will
be disabled.


Advanced Schedule
~~~~~~~~~~~~~~~~~

If you turn on this flag, NetXMS server will use custom schedule for collecting
DCI values instead of fixed intervals. This schedule can be configured on the
:guilabel:`Schedule` page. Advanced schedule consists of one or more records;
each representing desired data collection time in cron-style format.
Record has five fields, separated by spaces: minute, hour, day of month, month,
and day of week.

Optionally, the sixth field can be specified for resolution in seconds (this is
a non-standard extension which is not compatible with a regular cron format).
Moreover, the sixth field (but not others) supports additional stepping syntax
with a percent sign (``%``), which means that the step in seconds calculated in
absolute seconds since the Unix epoch (00:00:00 UTC, 1st of January, 1970).
It's not recommended to use seconds in custom schedules as your main data
collection strategy though. Use seconds only if it is absolutely necessary.

Allowed values for each filed are:

+--------------------+---------------------------+
| Field              | Value                     |
+====================+===========================+
| minute             | 0 - 59                    |
+--------------------+---------------------------+
| hour               | 0 - 23                    |
+--------------------+---------------------------+
| day of month       | 1 - 31                    |
+--------------------+---------------------------+
| month              | 1 - 12                    |
+--------------------+---------------------------+
| day of week        | 0 - 7 (0 and 7 is Sunday) |
+--------------------+---------------------------+
| seconds (optional) | 0 - 59                    |
+--------------------+---------------------------+

A field may be an asterisk (``*``), which always stands for "any".

Examples
""""""""

Run five minutes after midnight, every day:
  
  ``5 0 * * *``
  
Run at 14:15 on the first day of every month:

  ``15 14 1 * *``


Run every 5 minutes:

  ``*/5 * * *``

Run every minute on 10th second:

  ``* * * * * 10``

Run twice a minute (on seconds 0 and 45):

  ``* * * * * */45``

Run every 45 seconds:

  ``* * * * * *%45``
  

Associate with cluster resource
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this field you can specify cluster resource associated with DCI. Data
collection and processing will occur only if node you configured DCI for is
current owner of this resource. This field is valid only for cluster member
nodes.


Retention Time
~~~~~~~~~~~~~~

This attribute specifies how long the collected data should be kept in
database, in days. Minimum retention time is 1 day and maximum is not limited.
However, keeping too many collected values for too long will lead to
significant increase of your database size and possible performance
degradation.


Status
~~~~~~

:term:`DCI` status can be one of the following: :guilabel:`Active`,
:guilabel:`Disabled`, :guilabel:`Not Supported`. Server will collect data only
if the status is :guilabel:`Active`. If you wish to stop data collection
without removing :term:`DCI` configuration and collected data, the
:guilabel:`Disabled` status can be set manually. If requested parameter is not
supported by target node, the :guilabel:`Not Supported` status is set by the
server.

Other Options
~~~~~~~~~~~~~
  1. There is option to show last DCI value in object tooltip on a map. 
     (Other Options -> Show last value in object tooltip)
  2. DCI can be used to calculate object status. Such kind of DCI should 
     return integer number from 0 till 4 representing object status. To 
     use DCI for status calculation, there should be selected this option 
     in it's properties (Other Options -> Use this DCI for node status 
     calculation).

Data Transformations
--------------------

In simplest case, NetXMS server collects values of specified parameters and
stores them in the database. However, you can also specify various
transformations for original value. For example, you may be interested in a
delta value, not in a raw value of some parameter. Or, you may want to have
parameter value converted from bytes to kilobytes. All transformations will
take place after receiving new value and before threshold processing.

Data transformation consists of two steps. On the first step, delta calculation
is performed. You can choose four types of delta calculation:

=================== ===========================================================
Function            Description
=================== ===========================================================
None                No delta calculation performed. This is the default
                    setting for newly created DCI.
Simple              Resulting value will be calculated as a difference
                    between current raw value and previous raw value.
                    By raw value is meant the parameter value
                    originally received from host.
Average per second  Resulting value will be calculated as a difference
                    between current raw value and previous raw value,
                    divided by number of seconds passed between current
                    and previous polls.
Average per minute  Resulting value will be calculated as a difference
                    between current raw value and previous raw value,
                    divided by number of minutes passed between current
                    and previous polls.
=================== ===========================================================


On the second step, custom transformation script is executed (if presented). By
default, newly created DCI does not have a transformation script. If
transformation script is presented, the resulting value of the first step is
passed to the transformation script as a parameter; and a result of script
execution is a final DCI value. Transformation script gets original value as
first argument (available via special variable ``$1``), and also has two
predefined global variables: ``$node`` (reference to current node object), and
``$dci`` (reference to current DCI object). For more information about NetXMS
scripting language, please consult :ref:`scripting` chapter in this manual.

.. _dci-push-parameters-label:

Push parameters
---------------

NetXMS gives you ability to push DCI values when you need it instead of polling
them on specific time intervals. To be able to push data to the server, you
should take the following steps:

#. Set your DCI's origin to Push Agent and configure other properties as usual,
   excluding polling interval which is meaningless in case of pushed data.
#. Create separate user account or pick an existing one and give "Push Data"
   access right on the DCI owning node to that user.
#. Use :ref:`nxapush-label` or :ref:`nxpush-label` utility or client API for pushing data.


List DCIs
---------

Usually DCIs have scalar values. A list DCI is a special DCI which returns a
list of values. List DCIs are mostly used by NetXMS internally (to get the list
of network interfaces during the configuration poll, for example) but can also
be utilized by user in some occasions. NetXMS Management Console does not
support list DCIs directly but their names are used as input parameters for
Instance Discovery methods. List DCI values can be also obtained with
:command:`nxget` command line utility (e.g. for use in scripts).


Table DCIs
----------

Table DCI collects and stores data in table format(multi row, column). 


.. _offline-data-collection:

Offline data collection
=======================

Offilne data collection allow metric data to be obtained while connection between 
server and agent have been broken. This option is available for metrics, table 
metrics and proxy SNMP metrics. Not implemented for proxy SNMP table metrics. 
While break data is stored on agent, and on connect it is send to server. Detailed 
description can be found there: :ref:`how_data_collection`.

Agent side cache is configurable globally, on node level, and on DCI level. By 
default it's off.

All collected data goes throught all transfarmations and thresholds only when it comes to server. 
To prevent generation of old events it can be set :guilabel:`OffileDataRelivanceTime` configuration variable to time period in seconds within which received offline data still relevant for threshold validation. By dafault it is set to 1 day. 

.. versionadded:: 2.0-M5
    Offline data collection. 

Configuration
-------------

It can be enabled:
  - globally - set configuration parameter :guilabel:`DefaultAgentCacheMode` to 1.
  - on node level - change :guilabel:`Agent cache mode` :guilabel:`on` in node properties on :guilabel:`Polling` page
  - on DCI level - change :guilabel:`Agent cache mode` :guilabel:`on in DCI properties on :guilabel:`General` page

  
.. _last-values:

Last DCI values View
====================

.. todo:
  Add description of this view with all menu items. 

Thresholds
==========

Overview
--------

For every DCI you can define one or more thresholds. Each threshold there is a
pair of condition and event - if condition becomes true, associated event is
generated. To configure thresholds, open the data collection editor for node or
template, right-click on the DCI record and select :guilabel:`Edit` from the
pop-up menu, then select the :guilabel:`Thresholds` page. You can add, modify
and delete thresholds using buttons below the threshold list. If you need to
change the threshold order, select one threshold and use arrow buttons located
on the right to move the selected threshold up or down.


Instance
--------

Each DCI has an :guilabel:`Instance` attribute, which is a free-form text
string, passed as a 6th parameter to events associated with thresholds. You can
use this parameter to distinguish between similar events related to different
instances of the same entity. For example, if you have an event generated when
file system was low on free space, you can set the :guilabel:`Instance`
attribute to file system mount point.


Threshold Processing
--------------------

.. figure:: _images/threshold_processing_algorithm.png
   
   Threshold processing algorithm

As you can see from this flowchart, threshold order is very important. Let's
consider the following example: you have DCI representing CPU utilization on
the node, and you wish two different events to be generated - one when CPU
utilization exceeds 50%, and another one when it exceeds 90%. What happens when
you place threshold ``> 50`` first, and ``> 90`` second? The following table
shows values received from host and actions taken by monitoring system
(assuming that all thresholds initially unarmed):

====== ========================================================================
Value    Action
====== ========================================================================
10     Nothing will happen.
55     When checking first threshold (``> 50``), the system will find
       that it's not active, but condition evaluates to true. So, the system
       will set threshold state to "active" and generate event
       associated with it.
70     When checking first threshold (``> 50``), the system will find
       that it's already active, and condition evaluates to true.
       So, the system will stop threshold checking and
       will not take any actions.
95     When checking first threshold (``> 50``), the system will find
       that it's already active, and condition evaluates to true.
       So, the system will stop threshold checking and will not
       take any actions.
====== ========================================================================

Please note that second threshold actually is not working, because it's
masked by the first threshold. To achieve desired results, you should place
threshold ``> 90`` first, and threshold ``> 50`` second.

You can disable threshold ordering by checking :guilabel:`Always process all
thresholds` checkbox. If it is marked, system will always process all
thresholds.


Threshold Configuration
-----------------------

When adding or modifying a threshold, you will see the following dialog:

.. figure:: _images/threshold_configuration_dialog.png


First, you have to select what value will be checked:

======================== ======================================================
Last polled value        Last value will be used. If number of polls set to
                         more then ``1``, then condition will evaluate to true
                         only if it's true for each individual value of
                         last ``N`` polls.
Average value            An average value for last ``N`` polls will be used
                         (you have to configure a desired number of polls).
Mean deviation           A mean absolute deviation for last ``N`` polls will be
                         used (you have to configure a desired number of
                         polls). Additional information on how mean absolute
                         deviation calculated can be found `here 
                         <http://en.wikipedia.org/wiki/Mean_deviation>`_.
Diff with previous value A delta between last and previous values will be
                         used. If DCI data type is string, system will use
                         ``0``, if last and previous values match; and ``1``,
                         if they don't.
Data collection error    An indicator of data collection error. Instead of
                         DCI's value, system will use ``0`` if data collection
                         was successful, and ``1`` if there was a data
                         collection error. You can use this type of
                         thresholds to catch situations when DCI's value
                         cannot be retrieved from agent.
======================== ======================================================

Second, you have to select comparison function. Please note that not all
functions can be used for all data types. Below is a compatibility table:

================ ======= ======== ======= ===== ============== ===== ======
Type/Function    Integer Unsigned Integer Int64 Unsigned Int64 Float String
================ ======= ======== ======= ===== ============== ===== ======
Less             X       X        X       X     X              X
Less or equal    X       X        X       X     X              X
Equal            X       X        X       X     X              X     X
Greater or equal X       X        X       X     X              X
Greater          X       X        X       X     X              X
Not equal        X       X        X       X     X              X     X
Like                                                                 X
Not like                                                             X
================ ======= ======== ======= ===== ============== ===== ======

Third, you have to set a value to check against. If you use ``like`` or ``not
like`` functions, value is a pattern string where you can use meta characters:
asterisk (``*``), which means "any number of any characters", and question mark
(``?``), which means "any character".

Fourth, you have to select events to be generated when the condition becomes
true or returns to false. By default, system uses ``SYS_THRESHOLD_REACHED`` and
``SYS_THRESHOLD_REARMED`` events, but in most cases you will change it to your
custom events.

You can also configure threshold to resend activation event if threshold's
condition remain true for specific period of time. You have three options -
default, which will use server-wide settings, never, which will disable
resending of events, or specify interval in seconds between repeated events.


Thresholds and Events
---------------------

You can choose any event to be generated when threshold becomes active or
returns to inactive state. However, you should avoid using predefined system
events (their names usually start with ``SYS_`` or ``SNMP_``). For example, you
set event ``SYS_NODE_CRITICAL`` to be generated when CPU utilization exceeds
80%. System will generate this event, but it will also generate the same event
when node status will change to ::guilabel::`CRITICAL`. In your event
processing configuration, you will be unable to determine actual reason for
that event generation, and probably will get some unexpected results. If you
need custom processing for specific threshold, you should create your own event
first, and use this event in the threshold configuration. NetXMS has some
preconfigured events that are intended to be used with thresholds. Their names
start with ``DC_``.

The system will pass the following six parameters to all events generated as a
reaction to threshold violation:

#. Parameter name (DCI's name attribute)
#. DCI description
#. Threshold value
#. Actual value
#. Unique DCI identifier
#. Instance (DCI's instance attribute)

For example, if you are creating a custom event that is intended to be
generated when file system is low on free space, and wish to include file
system name, actual free space, and threshold's value into event's message
text, you can use message template like this:

  ``File system %6 has only %4 bytes of free space (threshold: %3 bytes)``

For events generated on threshold's return to inactive state (default event is
``SYS_THRESHOLD_REARMED``), parameter list is different:

#. Parameter name (DCI's name attribute)
#. DCI description
#. Unique DCI identifier
#. Instance (DCI's instance attribute)


.. _data-collection-templates:

Templates
=========

What is template
----------------

Often you have a situation when you need to collect same parameters from
different nodes. Such configuration making may easily fall into repeating one
action many times. Things may became even worse when you need to change
something in already configured DCIs on all nodes - for example, increase
threshold for CPU utilization. To avoid these problems, you can use data
collection templates. Data collection template (or just template for short) is
a special object, which can have configured DCIs similar to nodes.

When you create template and configure DCIs for it, nothing happens - no data
collection will occur. Then, you can apply this template to one or multiple
nodes - and as soon as you do this, all DCIs configured in the template object
will appear in the target node objects, and server will start data collection
for these DCIs. If you then change something in the template data collection
settings - add new DCI, change DCI's configuration, or remove DCI - all changes
will be reflected immediately in all nodes associated with the template. You
can also choose to remove template from a node. In this case, you will have two
options to deal with DCIs configured on the node through the template - remove
all such DCIs or leave them, but remove relation to the template. If you delete
template object itself, all DCIs created on nodes from this template will be
deleted as well.

Please note that you can apply an unlimited number of templates to a node - so
you can create individual templates for each group of parameters (for example,
generic performance parameters, MySQL parameters, network counters, etc.) and
combine them, as you need.


Creating template
-----------------

To create a template, right-click on :guilabel:`Template Root` or
:guilabel:`Template Group` object in the :guilabel:`Object Browser`, and click
:menuselection:`Create --> Template`. Enter a name for a new template and click
:guilabel:`OK`.


Configuring templates
---------------------

To configure DCIs in the template, right-click on :guilabel:`Template` object
in the :guilabel:`Object Browser`, and select :guilabel:`Data Collection` from
the pop-up menu. Data collection editor window will open. Now you can configure
DCIs in the same way as the node objects.


Applying template to node
-------------------------

To apply a template to one or more nodes, right-click on template object in
:guilabel:`Object Browser` and select :guilabel:`Apply` from pop-up menu. Node
selection dialog will open. Select the nodes that you wish to apply template
to, and click :guilabel:`OK` (you can select multiple nodes in the list by
holding :kbd:`Control` key). Please note that if data collection editor is open
for any of the target nodes, either by you or another administrator, template
applying will be delayed until data collection editor for that node will be
closed.


Removing template from node
---------------------------

To remove a link between template and node, right-click on :guilabel:`Template`
object in the :guilabel:`Object Browser` and select :guilabel:`Unbind` from
pop-up menu. Node selection dialog will open. Select one or more nodes you wish
to unbind from template, and click :guilabel:`OK`. The system will ask you how
to deal with DCIs configured on node and associated with template:

.. figure:: _images/remove_template.png

If you select Unbind DCIs from template, all DCIs related to template will
remain configured on a node, but association between the DCIs and template will
be removed. Any further changes to the template will not be reflected in these
DCIs. If you later reapply the template to the node, you will have two copies
of each DCI - one standalone (remaining from unbind operation) and one related
to template (from new apply operation). Selecting Remove DCIs from node will
remove all DCIs associated with the template. After you click OK, node will be
unbound from template.


Macros in template items
------------------------

You can use various macros in name, description, and instance fields of
template DCI. These macros will be expanded when template applies to node.
Macro started with ``%{`` character combination and ends with ``}`` character.
The following macros are currently available:

.. tabularcolumns:: |p{0.3 \textwidth}|p{0.6 \textwidth}|

================= =============================================================
Macro             Expands to
================= =============================================================
node_id           Node unique id
node_name         Node name
node_primary_ip   Node primary IP address
script:name       String returned by script name. Script should be stored in
                  script library (accessible via
                  :menuselection:`Configuration --> Script Library`).
                  Inside the script, you can access current node's properties
                  via $node variable.
================= =============================================================

For example, if you wish to insert node's IP address into DCI description, you
can enter the following in the description field of template DCI:

  ``My IP address is %{node_primary_ip}``

When applying to node with primary IP address 10.0.0.1, on the node will be
created DCI with the following description:

  ``My IP address is 10.0.0.1``

Please note that if you change something in the node, name for example, these
changes will not be reflected automatically in DCI texts generated from macros.
However, they will be updated if you reapply template to the node.


Instance Discovery
==================

Sometimes you may need to monitor multiple instances of some entity, with exact
names and number of instances not known or different from node to node. Typical
example is file systems or network interfaces. To automate creation of DCIs for
each instance you can use instance discovery mechanism. First you have to
create "master" DCI. Create DCI as usual, but in places where normally you
would put instance name, use the special macro {instance}. Then, go to
:guilabel:`Instance Discovery` tab in DCI properties, and configure instance
discovery method and optionally filter script.


Discovery Methods
-----------------

There are four different methods for instance discovery:


================== ========== =================================================
Method             Input Data Description
================== ========== =================================================
Agent List         List name  Read list from agent and use it's values as
                              instance names.
Agent Table        Table name Read table from agent and use it's instance
                              column values as instance names.
SNMP Walk - Values Base OID   Do SNMP walk starting from given OID and use
                              values of returned varbinds as instance names.
SNMP Walk - OIDs   Base OID   Do SNMP walk starting from given OID and use IDs
                              of returned varbinds as instance names.
================== ========== =================================================


Instance Filter
---------------

You can optionally filter out unneeded instances and transform instance names
using filtering script written in NXSL. Script will be called for each instance
and can return ``TRUE`` (to accept instance), ``FALSE`` (to reject instance),
and array of two elements - first is ``TRUE`` and second is new value for
instance name.


Working with collected data
===========================

Once you setup DCI, data starts collecting in the database. You can access this
data and work with it in different ways. Data can be visualized in three ways:
in graphical form, as a historical view(textual format) and as DCI summary table, 
this layout types can be combined in Dashboards.
More detailed description about visualization and layout can be found there:
:ref:`visualisation`.


