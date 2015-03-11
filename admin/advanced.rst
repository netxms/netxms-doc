.. _advanced:


###############
Advanced topics
###############


Zones
=====

As NetXMS server keeps track of an IP topology, it is important to maintain the
configuration in which IP addresses do not overlap and that two IP addresses
from same subnet are really within one subnet. Sometimes, however, it is needed
to monitor multiple sites with overlapping IP address ranges. To correctly
handle such situation, zoning must be used. Zone in NetXMS is a group of IP
subnets which form non-overlapping IP address space. There is always zone 0
which contains subnets directly reachable by management server. For all other
zones server assumes that subnets within that zones are not reachable directly,
and proxy must be used.

Enable Zoning
-------------

Zoning support is off by default. To turn it on you must set server's
configuration variable ``EnableZoning`` to ``1`` and restart server. After
restart, server will create default zone with ID ``0`` and put all existing
subnets into that zone. Subnet tree will looks like this:

.. figure:: _images/Zoning_enabled.png

Setting communication options for zones
---------------------------------------

Server have to know proxy nodes to be able to communicate with nodes in remote
zones. Default proxy settings for all nodes in the zone can be set on
Communications page in zone object properties:

.. figure:: _images/Zone_comm_settings.png

On this page you can set default proxy node for NetXMS agents, SNMP, and ICMP.
Note that proxy node must be in default zone and must have primary IP reachable
by NetXMS server.


Moving nodes between zones
--------------------------

To move existing node to another zone, select :guilabel:`Change zone` from
nodes context menu, then select target zone in zone selection dialog that will
appear. After move to another zone, server will immediately do configuration
poll on the node.


.. _helpdesk-integration:

Integration with external HelpDesk
----------------------------------

NetXMS provides possibility to create issues in external helpdesk system 
directly from NetXMS management console, based on pending alarms. In this 
situation NetXMS and external helpdesk system will have synchronized 
issue workflow. 

For now integration is done only with JIRA. 

JIRA Module
-----------

This module provide integration between NetXMS and JIRA. 

Required NetXMS configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For NetXMS is required to configure server parameters(they should be created by user) 
and restart the server. 

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Parameter name
     - Description
   * - HelpDeskLink
     - For JIRA integration should be set to “jira.hdlink” (without quotes)
   * - JiraIssueType
     - Name of the JIRA issue type, which will be used by NetXMS. 
       Sample value: “Task” (without quotes)
   * - JiraLogin
     - Login of the JIRA user(This user should exist in JIRA system with with 
       permissions to create issues in project(JiraProjectCode) and comment 
       on own issues)
   * - JiraPassword
     - Password of the JIRA user
   * - JiraProjectCode
     - Project Key in JIRA. (Project should exist)
   * - JiraServerURL
     - URL of JIRA installation. Example: “http://localhost:8080/jira”. Please note,
       that trailing slash (“/”) should be removed!
       
If all configuration was successfully done after rester in console should be present:

::

  [25-Apr-2014 14:16:07.894] [INFO ] Helpdesk link module JIRA (version 1.2.14) loaded successfully

Required JIRA configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~
NetXMS JIRA plugin should be deployed to JIRA and configured. REST API should 
be enabled in JIRA configuration (enabled in default configuration).

To access configuration page for the plugin, go to “System → Advanced” and select
“NetXMS Integration” tab:

.. figure:: _images/jira_netxms_plugin_configuration.png

Possible configuration options:

  1. “Plugin Enabled” — global on/off switch, plugin completely cease any activity 
     when turned off (default).
  2. “Force Save” — by default, plugin will verify configuration before saving
     (connectivity to all servers, credentials). This checkbox allows to bypass 
     this step completely and save configuration even if one of more NetXMS 
     servers are rejecting provided credentials or do not respond at all)
  3. “Project Key” — Key of the project, where issues from NetXMS will be created. 
     This key will be also used in workflow operations — plugin will process 
     events related to this project:

      .. figure:: _images/jira_project_list.png

  4. “Servers” — addresses of up to a 3 NetXMS servers, can be either 
     IP address or hostname.
  5. “Log In” — user login in NetXMS (User should exist in NetXMS with Read, View 
     Alarms, Acknowledge Alarms, Terminate Alarms to all nodes)
  6. “Password” — user password in NetXMS 
  
Plugin will verify configuration and provide feedback. If one or more
NetXMS servers are not responding (e.g. they are not configured yet), you can
select “Force Save” to overrule verification process and save configuration.


Workflow configuration
~~~~~~~~~~~~~~~~~~~~~~
Since JIRA workflow can be much more sophisticated than alarm states in NetXMS, JIRA
Administrator should decide which workflow transition should change NetXMS alarm
state.

NetXMS supports four alarm states:

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
     - NetXMS post-function action
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
  3. Assign Workflow to the project, where NetXMS will create issues
  4. Modify transitions to call plugin’s post-function and change related alarm in
     NetXMS
     
    a. Click on a “cog” icon on a transition and select “View Post Functions”:

    .. figure:: _images/jira_post_function.png

    b. Click on “Add a new post function to the unconditional result of the
       transition”:

    .. figure:: _images/jira_post_function2.png

    c. Select “NetXMS Modify Alarm” and click “Add”:
    
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
  1. Right click on alarm in NetXMS and select “Create ticket in helpdesk system”:
  
     .. figure:: _images/jira_create_ticket.png 
     
  2. In a moment, issue will be created and Helpdesk ID will be show in corresponding
     column:
     
     .. figure:: _images/jira_helpdesk_ID.png
     
  3. Right click on the alarm and select “Show helpdesk ticket in web browser” to
     navigate to the issue in JIRA:
     
     .. figure:: _images/jira_ticket_show.png
    


Hooks (Pollers hooks)
=====================

NetXMS has 5 different poller types, sometimes it is required by user 
to add some additional functionality while this polls. For this purpose 
were created hooks. Hook is manually created script in 
:guilabel:`Script Library` that is executed at the very end of the poll.
More about poll types and purposes can be found :ref:`there <concepts_polling>` 
and about script creation :ref:`there <scripting>`. 

To be recognized as a hook script should have special name. It should be named 
according to convention: Hook\:\:\ `Pool_name`. 

Example: Hook\:\:ConfigurationPoll

Full list of hooks and 

  * - Hook name
    - Description 
    - Parameters
  * - Hook\:\:StatusPoll
    - Hook that is executed at the end of status poll
    - $node
  * - Hook\:\:ConfigurationPoll
    - Hook that is executed at the end of configuration poll
    - $node
  * - Hook\:\:InstancePoll
    - Hook that is executed after instance discovery poll.
    - $node
  * - Hook\:\:TopologyPoll
    - Hook that is executed at the ens of topology poll
    - $node
  * - Hook\:\:AcceptNewNode
    - Hook that is executed on a new node add. This script should return 1 if 
      node should be added. In case if script returns nothing or something other 
      than 1 - node will not be added. 
    - $ipAddr, $ipNetMask, $macAddr, $zoneId

Usually hooks are used for automatic actions that need to be done on node. 
For example automatic remove change of expected state of interface depending 
on some external parameters. 

Troubleshooting
===============

Reset password for user "admin"
-------------------------------

.. warning::

   Server ("netxmsd") should be stopped while performing this operation!

Passwords in NetXMS are stored in hashed, not-reversible way, so there are no way to recover it, but it can be reseted.

.. versionadded:: 1.2.9

Use following command to reset password and unlock account:

.. code-block:: sh

   nxdbmgr resetadmin

.. deprecated:: 1.2.9

To reset password to installation default ("netxms"):

#. Stop ``netxmsd``
#. Run ``nxdbmgr check`` to make sure that server is down and database is unlocked
#. Create temporary file "reset.sql" with following content:

   .. code-block:: sql

      UPDATE users SET
        password='3A445C0072CD69D9030CC6644020E5C4576051B1',
        flags=8,
        grace_logins=5,
        auth_method=0,
        auth_failures=0,
        disabled_until=0
      WHERE id=0;

#. Execute reset.sql:

   .. code-block:: sh

      nxdbmgr batch reset.sql

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
:menuselection:`Tools --> Server Console` menu in management console. Once in
server debug console, you can run command ``dump`` or ``raise access``. First
command works only on Windows and will produce process dump without stopping
it. Second command will cause access violation exception which will lead to
process crash and crash dump generation.

SNMP Device not recognised as SNMP-capable
------------------------------------------

Common issues:

#. Invalid community string or credentials
#. Access control on the device or firewall prevent connections from NetXMS
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
container, policy or template auto apply and other automatic actions. 
