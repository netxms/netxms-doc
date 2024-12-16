.. _advanced:


###############
Advanced topics
###############

.. _zones:

Zones
=====

As |product_name| server keeps track of an IP topology, it is important to maintain the
configuration in which IP addresses do not overlap and that two IP addresses
from same subnet are really within one subnet. Sometimes, however, it is needed
to monitor multiple sites with overlapping IP address ranges. To correctly
handle such situation, zoning must be used. Zone in |product_name| is a group of IP
subnets which form non-overlapping IP address space. There is always zone 0
which contains subnets directly reachable by management server. For all other
zones server assumes that subnets within that zones are not reachable directly,
and proxy must be used.

Enable Zoning
-------------

Zoning support is off by default. To turn it on you must set server's
configuration variable ``EnableZoning`` to ``1`` and restart server. After
restart, server will create default zone with UIN (unique identification number)
``0`` and put all existing subnets into that zone. Subnet tree will looks like this:

.. figure:: _images/Zoning_enabled.png

Setting communication options for zones
---------------------------------------

Server have to know proxy nodes to be able to communicate with nodes in remote
zones. Default proxy settings for all nodes in the zone can be set on
Communications page in zone object properties:

.. figure:: _images/Zone_comm_settings.png

On this page you can set default proxy node for |product_name| agents, SNMP, and ICMP.
Note that proxy node must be in default zone and must have primary IP reachable
by |product_name| server.


Moving nodes between zones
--------------------------

To move existing node to another zone, select :guilabel:`Change zone` from
nodes context menu, then select target zone in zone selection dialog that will
appear. After move to another zone, server will immediately do configuration
poll on the node.


.. _helpdesk-integration:

Integration with external HelpDesk
----------------------------------

|product_name| provides possibility to create issues in external helpdesk system
directly from |product_name| management client, based on pending alarms. In this
situation |product_name| and external helpdesk system will have synchronized
issue workflow.

For now integration is done only with JIRA.

JIRA Module
-----------

This module provide integration between |product_name| and JIRA.

Required |product_name| configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For |product_name| is required to configure server parameters
and restart the server.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Parameter name
     - Description
   * - HelpDeskLink
     - For JIRA integration should be set to “jira.hdlink” (without quotes)
   * - Jira.IssueType
     - Name of the JIRA issue type, which will be used by |product_name|.
       Sample value: “Task” (without quotes)
   * - Jira.Login
     - Login of the JIRA user(This user should exist in JIRA system with with
       permissions to create issues in project(JiraProjectCode) and comment
       on own issues)
   * - Jira.Password
     - Password of the JIRA user
   * - Jira.ProjectCode
     - Project Key in JIRA. (Project should exist)
   * - Jira.ProjectComponent
     - Jira project component. (Project should exist)
   * - Jira.ResolvedStatus
     - Comma separated list of issue status codes indicating that issue is resolved. Default is “Done”.
   * - Jira.ServerURL
     - URL of JIRA installation. Example: “http://localhost:8080/jira”. Please note,
       that trailing slash (“/”) should be removed!
   * - Jira.Webhook.Path
     - Path part of Jira webhook URL (must start with /). Example: “/jira-webhook”. 
   * - Jira.Webhook.Port
     - Jira webhook listener port (0 to disable webhook). Default: “8008”. 

.. note::
    Starting from version 4.1.283 |product_name| version Webhook can be used for Jira to |product_name| integration. Not a jira plugin. 

If all configuration was successfully done after rester in console should be present:

::

  [25-Apr-2014 14:16:07.894] [INFO ] Helpdesk link module JIRA (version 1.2.14) loaded successfully

Required JIRA configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~
|product_name| JIRA plugin should be deployed to JIRA and configured. REST API should
be enabled in JIRA configuration (enabled in default configuration).

To access configuration page for the plugin, go to “System → Advanced” and select
“|product_name| Integration” tab:

.. figure:: _images/jira_netxms_plugin_configuration.png

Possible configuration options:

  1. “Plugin Enabled” — global on/off switch, plugin completely cease any activity
     when turned off (default).
  2. “Force Save” — by default, plugin will verify configuration before saving
     (connectivity to all servers, credentials). This checkbox allows to bypass
     this step completely and save configuration even if one of more |product_name|
     servers are rejecting provided credentials or do not respond at all)
  3. “Project Key” — Key of the project, where issues from |product_name| will be created.
     This key will be also used in workflow operations — plugin will process
     events related to this project:

      .. figure:: _images/jira_project_list.png

  4. “Servers” — addresses of up to a 3 |product_name| servers, can be either
     IP address or hostname.
  5. “Log In” — user login in |product_name| (User should exist in |product_name| with Read, View
     Alarms, Acknowledge Alarms, Terminate Alarms to all nodes)
  6. “Password” — user password in |product_name|

Plugin will verify configuration and provide feedback. If one or more
|product_name| servers are not responding (e.g. they are not configured yet), you can
select “Force Save” to overrule verification process and save configuration.


Workflow configuration
~~~~~~~~~~~~~~~~~~~~~~
Since JIRA workflow can be much more sophisticated than alarm states in |product_name|, JIRA
Administrator should decide which workflow transition should change |product_name| alarm
state.

|product_name| supports four alarm states:

  1. Outstanding — initial state, can’t be set from JIRA side
  2. Acknowledged — operator is aware of the problem and it’s in progress
     (“Acknowledge” action)
  3. Resolved — problem is resolved but alarm stays in the list until verified and
     terminated by supervisor (“Resolve” action)
  4. Terminated — problem is resolved and verified, alarm is removed from the list
     (“Terminate” action)

Sample workflow (JIRA default workflow):

.. figure:: _images/jira_workflow.png

Sample mapping:

.. list-table::
   :header-rows: 1
   :widths: 30 30

   * - Transition
     - |product_name| post-function action
   * - Start Progress
     - Acknowledge
   * - Resolve Issue
     - Resolve
   * - Close Issue
     - Terminate
   * - `All other transitions`
     - `Ignored`

Configure workflow in JIRA:

  1. Create new Workflow Schema if required
  2. Copy existing or create new Workflow
  3. Assign Workflow to the project, where |product_name| will create issues
  4. Modify transitions to call plugin’s post-function and change related alarm
     in |product_name|

    a. Click on a “cog” icon on a transition and select “View Post Functions”:

    .. figure:: _images/jira_post_function.png

    b. Click on “Add a new post function to the unconditional result of the
       transition”:

    .. figure:: _images/jira_post_function2.png

    c. Select “|product_name| Modify Alarm” and click “Add”:

    .. figure:: _images/jira_post_function3.png

    d. Select desired alarm action (Acknowledge / Resolve / Terminate) and click
       “Add”:

    .. figure:: _images/jira_post_function4.png

    e. Repeat for all required transitions

  5. Publish workflow changes


Ticket creation
~~~~~~~~~~~~~~~
Tickets are created from from alarms manually. To create ticket user should have
"Create helpdesk tickets" access for required objects.

Steps to create ticket:
  1. Right click on alarm in |product_name| and select “Create ticket in
     helpdesk system”:

     .. figure:: _images/jira_create_ticket.png

  2. In a moment, issue will be created and Helpdesk ID will be show in
     corresponding column:

     .. figure:: _images/jira_helpdesk_ID.png

  3. Right click on the alarm and select “Show helpdesk ticket in web browser”
     to navigate to the issue in JIRA:

     .. figure:: _images/jira_ticket_show.png



Hooks
=====

Sometimes it is required to add some additional functionality after poll, object
creation or other action - for this purpose hooks were created. Hook is manually
created script in :guilabel:`Script Library` that is executed at a special
condition like end of the poll or interface creation.

More about poll types and purposes can be found :ref:`there <concepts_polling>`
and about script creation :ref:`there <scripting>`.

To be recognized as a hook script should have special name. It should be named
according to convention: Hook\:\:\ `hook_name`.

Example: Hook\:\:ConfigurationPoll

Full list of hooks:


.. list-table::
   :header-rows: 1
   :widths: 30 30 30 20
   :class: longtable

   * - Hook name
     - Description
     - Parameters
     - Return value
   * - Hook\:\:StatusPoll
     - Hook that is executed at the end of status poll
     - $object - current object, one of 'NetObj' subclasses

       $node - current object if it is 'Node' class
     - none
   * - Hook\:\:ConfigurationPoll
     - Hook that is executed at the end of configuration poll
     - $object - current object, one of 'NetObj' subclasses

       $node - current object if it is 'Node' class
     - none
   * - Hook\:\:InstancePoll
     - Hook that is executed after instance discovery poll.
     - $object - current object, one of 'NetObj' subclasses

       $node - current object if it is 'Node' class
     - none
   * - Hook\:\:TopologyPoll
     - Hook that is executed at the ens of topology poll
     - $node - current node, object of 'Node' type
     - none
   * - Hook\:\:CreateInterface
     - Hook that is executed after new interface is created.
     - $node - current node, object of 'Node' type

       $1 - current interface, object of 'Interface' type
     - true/false - boolean - whether interface should be created
   * - Hook\:\:AcceptNewNode
     - This hook is executed by discovery process, after a new node is found and
       it's checked that no node with give IP address is present in the system
       and before any network discovery filters.
     - $ipAddr - IP address of the node being processed

       $ipNetMask - netmask of the node being processed

       $macAddr - MAC address of the node being processed

       $zoneUIN - zone UIN of the node being processed
     - true/false - boolean - whether node should be created
   * - Hook\:\:DiscoveryPoll
     - Hook that is executed at the end of discovery poll
     - $node - current node, object of 'Node' type
     - none
   * - Hook\:\:PostObjectCreate
     - Hook that is executed after object is created
     - $object - current object, one of 'NetObj' subclasses

       $node - current object if it is 'Node' class
     - none
   * - Hook\:\:CreateSubnet
     - Hook that is executed on subnet creation
     - $node - current node, object of 'Node' class

       $1 - current subnet, object of 'Subnet' class
     - true/false - boolean - whether subnet should be created
   * - Hook\:\:UpdateInterface
     - Hook that is executed at the end of interface update
     - $node - current node, object of 'Node' type

       $interface - current interface, object of 'Interface' type
     - none
   * - Hook\:\:EventProcessor
     - Hook that is executed for each event prior to it's processing by Event
       Processing Policies. 
       
     - $object - event source object, one of 'NetObj' subclasses

       $node - event source object if it is 'Node' class

       $event - event being processed (object of 'Event' class)
     - none
   * - Hook\:\:AlarmStateChange
     - Hook that is executed on alarm state change (alarm gets acknowledged,
       resolved or terminated)
     - $alarm - alarm being processed (object of 'Alarm' class)
     - none
   * - Hook\:\:UnboundTunnelOpened
     - Hook that is executed when tunnel connection is established, but not
       bound to a node. 
     - $tunnel - incoming tunnel information (object of 'Tunnel' class)
     - none     
   * - Hook\:\:BoundTunnelOpened
     - Hook that is executed when tunnel connection bound to a node is
       established. 
     - $node - node this tunnel was bound to (object of 'Node' class)
     
       $tunnel - incoming tunnel information (object of 'Tunnel' class)
     - none     
   * - Hook\:\:LDAPSynchronization
     - Hook executed for each LDAP record (user or group) during LDAP
       synchronization. 
     - $ldapObject - LDAP object being synchronized (object of 'LDAPObject'
       class)
     - true/false - boolean - whether processing of this LDAP record should
       continue
   * - Hook\:\:Login
     - Hook executed prior to user login
     - $user - user object (object of 'User' class)

       $session - session object (object of 'ClientSession' class)
     - true/false - boolean - whether login for this session should continue


Usually hooks are used for automatic actions that need to be done on node.
For example automatic remove change of expected state of interface depending
on some external parameters.


Troubleshooting
===============

.. _password-reset:

Resetting "system" user password
--------------------------------

.. warning::

   Server ("netxmsd") should be stopped while performing password reset operation!

Passwords in |product_name| are stored in hashed, not-reversible way, so there
are no way to recover it, but it can be reset. Use following procedure to reset
password and unlock account:

 1. stop netxmsd
 2. run "nxdbmgr reset-system-account" to unlock "system" account and change it's password to default ("netxms").
 3. start netxmsd
 4. login as "system" using password "netxms"
 5. In user manager change password for any admin user account
 6. login as admin user and disable "system" user account


Enable Crash Dump Generation
----------------------------

When running on Windows server is capable of creating crash dumps. To enable crash dump generation, add the following options to netxmsd.conf file:

.. code-block:: ini

   CreateCrashDumps = yes
   DumpDirectory = path

``DumpDirectory`` must point to directory writable by server process. After each crash server will create two files: info and mdmp. Info file contains basic information about crash, server version, and call stack of current thread. Mdmp file is a minidump which can be read and analyzed using debugger.

Force Crash Dump Creation
-------------------------

It is possible to force creation of crash dump. To do that you'll need access
to server debug console. You can access it using ``nxadm`` tool or via
:menuselection:`Tools --> Server Console` menu in management client. Once in
server debug console, you can run command ``dump`` or ``raise access``. First
command works only on Windows and will produce process dump without stopping
it. Second command will cause access violation exception which will lead to
process crash and crash dump generation.

SNMP Device not recognized as SNMP-capable
------------------------------------------

Common issues:

#. Invalid community string or credentials
#. Access control on the device or firewall prevent connections from |product_name|
   server
#. Device do not support ``System`` (.1.3.6.1.2.1.1) or ``Interfaces``
   (.1.3.6.1.2.1.2) MIBs, which are used to detect SNMP-capable devices. To
   override OIDs used for detection, set node's custom attribute
   ``snmp.testoid`` to any OID supported by device.

Automatic actions on a new node
===============================

On a new node creation is generated SYS_NODE_ADDED event. So any automatic
actions that should be done on a node can be done by creating :term:`EPP` rule
on on this event, that will run script. In such way can be done node bind to
container, template auto apply and other automatic actions.

.. _autologin:

Autologin for Management Client
===============================

It is possible to connect management client (nxmc) or web management client to
server automatically without login dialog. This chapter describes additional
command line options and URL parameters for that.

Desktop Management Client
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Command line option
     - Description
   * - -auto
     - Connect to server automatically without login dialog
   * - -dashboard=dashboard
     - Automatically open given dashboard after login (either dashboard object ID or name can be specified)
   * - -login=login
     - Set login name
   * - -password=password
     - Set password, default is empty
   * - -server=address
     - Set server name or IP address

For example, to connect management client to server 10.0.0.2 as user guest with empty password, use command

.. code-block:: sh

    nxmc -auto -server=10.0.0.2 -login=guest

Web Management Client
---------------------

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - URL parameters
     - Description
   * - auto
     - Connect to server automatically without login dialog
   * - dashboard=dashboard
     - Automatically open given dashboard after login (either dashboard object ID or name can be specified)
   * - login=login
     - Set login name
   * - password=password
     - Set password, default is empty
   * - server=address
     - Set server name or IP address

For example, to connect web management console to server 10.0.0.2 as user guest with empty password and
open dashboard called "SystemOverview", use URL

.. code-block:: ini

    http://server/nxmc?auto&server=10.0.0.2&login=guest&dashboard=SystemOverview


|product_name| data usage in external products
==============================================

|product_name| provides next options to use data in other applications:

    * Use :ref:`autologin <autologin>` and dashboard name in URL to add dashboard to your company
      documentation(where URL usage is possible).
    * Use :ref:`Grafana <grafana-integration>` for graph creation and further usage
    * Get data through :ref:`Web API <rest-api>`


Find Object
===========

Management client has an option to filter objects by defined by user criteria. Filter can be access by :menuselection:`Tools->Find Object`\ .
Filter can be used in two different modes: filter and query.

Filter
------

Filter will search object using class filter, zone filter, IP range and search string that will be checked for each object in all it's 
text fields (name, comments, custom attributes, Location, etc.). 

Query
-----

There can be written any script that will be executed on all objects and if stript returns true - object will be shown in the resulting 
table. There can be used the same syntax as for :ref:`dashboards-object-query` Dashboard element, but variables will not be added as 
additional columns for table in this case. 

Audit log forwarding
====================

Syslog
------

NetXMS allows to forward audit log to another syslog server to have all data in one place. 

Next configuration parameters should be set in order to forward audit log to external syslog server:

.. list-table::
  :widths: 21 21
  :header-rows: 1

  * - Name
    - Description
  * - ExternalAuditFacility
    - Syslog facility to be used in audit log records sent to external server.
  * - ExternalAuditPort
    - UDP port of external syslog server to send audit records to.
  * - ExternalAuditServer
    - External syslog server to send audit records to. If set to "none", external audit logging is disabled.
  * - ExternalAuditSeverity
    - Syslog severity to be used in audit log records sent to external server.
  * - ExternalAuditTag
    - Syslog tag to be used in audit log records sent to external server.

LEEF
----

LEEF server module provides functionality to send audit log to IBM Security
QRadar. The Log Event Extended Format (LEEF) is a customized event format for
IBM Security QRadar. More about it can be found `there
<https://www.ibm.com/docs/en/dsm?topic=leef-overview>`_.

LEEF server module should be enabled in server configuraiton file by adding
"Module=leef.nxm" line to :file:`netxmsd.conf` file.

Additionally to module configuration "LEEF" section should be added with
required configurations.

.. list-table::
  :widths: 21 21
  :header-rows: 1

  * - Name
    - Description
  * - Server
    - Server address
  * - Port
    - Server port
  * - EventCode
    - LEEF event code
  * - RFC5424Timestamp
    - "No" if RFC5424 Timestamp format should not be used (default value is Yes)
  * - Facility
    - Facility as facility in syslog
  * - Severity
    - Severity as severity in syslog
  * - Product
    - LEEF product field, by default will be "NetXMS"
  * - ProductVersion
    - LEEF product version field, by default will be server version
  * - Vendor
    - LEEF vendor field, default it "Raden Solutions"
  * - Separator
    - LEEF separator character as a char or in numeric format: "xHH", where HH
      is hexdecimal digit

Additional fields can be configured in ExtraData sub section in the same
key=value format.
  

Example:

.. code-block:: ini

   [LEEF]
   Server = 127.0.0.1
   Port = 514
   Facility = 13
   Severity = 5
   EventCode = 
   Separator = ^

   [LEEF/ExtraData]
   key = value
   key2 = value2


.. _custom-housekeeping-scripts:

Custom housekeeping scripts
===========================

To customize housekeeper operations it's possible to use custom scripts. Scripts
are executed in the end of housekeeping process. Due to security considerations
scrips are stored on server file system in ``<DataDirectory>/housekeeper``
folder, where ``<DataDirectory>`` is path to server data directory (see
``DataDirectory`` parameter in :ref:`server_configuration_file` for more
information). Multiple scripts can be present in the mentioned folder. 

Two types of scripts are supported: 
   * SQL (files with .sql extension) - file containing SQL queries. SQL query
     can take multiple lines, end of query is denoted with semicolon (``;``)
     character
   * NXSL (files with .nxsl extension) - file contains :term:`NXSL` script. In
     addition to all standard NXSL functionality, ``SQLQuery()`` NXSL function
     is supported, allowing SQL query execution to the database. 

To implement custom deletion of DCI and Table DCI data built-in deletion of this
data can be disabled by setting server configuration parameter
``Housekeeper.DisableCollectedDataCleanup``.


.. _fanout-drivers:

Fanout drivers
===============

|product_name| has concept of fanout driver, which enable collected data sending
to an additional database. 

InfluxDB
--------

To enable InfluxDB fanout driver, add ``PerfDataStorageDriver=influxdb`` to
:file:`netxmsd.conf` file. Driver configuration is specified in ``[InfluxDB]``
section.

.. list-table::
  :widths: 10 10
  :header-rows: 1

  * - Name
    - Description
  * - Bucket
    - Bucket name. 
  * - EnableUnsignedType
    - Enable (true) or disable (false) unsigned data type. Default: `false`.
  * - Database
    - Database name. Default value is `netxms`.
  * - Hostname
    - Hostname. Default is `localhost`.
  * - MaxCacheWaitTime
    - Maximum time in ms before cache being flushed.
      Default is `30000`.
  * - Password
    - Password. 
  * - Port
    - Network port number
  * - Protocol
    - Options are: `udp`, `api-v1` and `api-v2`. Default it `udp`.
  * - QueueFlushThreshold
    - Cache will be flushed when reaching this size (in bytes). Default: `32768`
  * - Queues
    - Number of queues for parallel operation. Default: `1`.
  * - QueueSizeLimit
    - Upper limit on queue size in bytes. If queue reaches this size, data will
      be dropped. Default: `4194304`.
  * - Token
    - Authentication token.
  * - ValidateValues ( from 5.1.2 )
    - If true, driver will validate values according to DCI data type, and drop invalid values (invalid numbers, out-of-range values). Default: false
  * - CorrectValues
    - If both ValidateValues and CorrectValues set to true, instead of dropping values that did not pass validation, correct values will be sent to InfluxDB instead. Unparsable numbers will be set to last parsable part (for example, 123abc will be sent as 123), out-of-range values will be sent as maximal or minimal possible value. Default: false
    


Configuration example:

.. code-block:: ini

   PerfDataStorageDriver=influxdb

   [InfluxDB]
   Protocol=api-v2
   Organization=netxms
   Bucket=netxms
   Token=MJzXfwcNm7uEu4mL31S-iVjZ-DJO9pPbCuDl90XotOS3TyY9VkVMoDr5o4u4w8opucyZ2-MwcrpfC2zymbcj2Q==


Details of operation
~~~~~~~~~~~~~~~~~~~~

Field key is made from DCI's metric name (except for SNMP and internal "Dummy"
DCIs where description is used). Space characters are removed, `:-.,#`
characters are replaced with `_`, `\\` is replaced with `/`.

Empty DCI values are not sent. 

If custom attribute named `ignore_influxdb` (with any value) exists on a node,
this node will be excluded from export. Also, if a DCI has Related Object set to
an interface and this interface has `ignore_influxdb` custom attribute, this
DCI will be ignored.

If there is custom attribute on the node or on related object with name starting
with `tag_`, it's name (excluding `tag_` part) and value will be used as tag.
There can be several such custom attributes.
