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
directly from |product_name| management console, based on pending alarms. In this
situation |product_name| and external helpdesk system will have synchronized
issue workflow.

For now integration is done only with JIRA.

JIRA Module
-----------

This module provide integration between |product_name| and JIRA.

Required |product_name| configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For |product_name| is required to configure server parameters(they should be created by user)
and restart the server.

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Parameter name
     - Description
   * - HelpDeskLink
     - For JIRA integration should be set to “jira.hdlink” (without quotes)
   * - JiraIssueType
     - Name of the JIRA issue type, which will be used by |product_name|.
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
  4. Modify transitions to call plugin’s post-function and change related alarm in
     |product_name|

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
  1. Right click on alarm in |product_name| and select “Create ticket in helpdesk system”:

     .. figure:: _images/jira_create_ticket.png

  2. In a moment, issue will be created and Helpdesk ID will be show in corresponding
     column:

     .. figure:: _images/jira_helpdesk_ID.png

  3. Right click on the alarm and select “Show helpdesk ticket in web browser” to
     navigate to the issue in JIRA:

     .. figure:: _images/jira_ticket_show.png



Hooks
=====

Sometimes it is required to add some additional functionality after poll, object
creation or other action - for this purpose hooks were created.
Hook is manually created script in :guilabel:`Script Library` that is executed
at a special condition like end of the poll or interface creation.

More about poll types and purposes can be found :ref:`there <concepts_polling>`
and about script creation :ref:`there <scripting>`.

To be recognized as a hook script should have special name. It should be named
according to convention: Hook\:\:\ `hook_name`.

Example: Hook\:\:ConfigurationPoll

Full list of hooks:

.. list-table::
   :header-rows: 1
   :widths: 70 70 70 70

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
     - Hook that is executed on a new node add. This script should return 1 if
       node should be added. In case if script returns nothing or something other
       than 1 - node will not be added.
     - $ipAddr - IP address of the node being processed

       $ipNetMask - netmask of the node being processed

       $macAddr - MAC address of the node being processed

       $zoneId - zone ID of the node being processed
     - true/false - boolean - whether node should be created
   * - Hook\:\:DiscoveryPoll
     - Hook that is executed at the ens of discovery poll
     - $node - current node, object of 'Node' type
     - none
   * - Hook\:\:PostObjectCreate
     - Hook that is executed after object is created
     - $object - current object, one of 'NetObj' subclasses

       $node - current object if it is 'Node' class
     - none
   * - Hook\:\:CreateSubnet
     - Hook that is executed after creation of a subnet
     - $node - current node, object of 'Node' class

       $1 - current subnet, object of 'Subnet' class
     - true/false - boolean - whether subnet should be created
   * - Hook\:\:UpdateInterface
     - Hook that is executed at the ens of interface update
     - $node - current node, object of 'Node' type

       $interface - current interface, object of 'Interface' type
     - none
   * - Hook\:\:EventProcessor
     - Hook that is executed for each event prior to it's processing by Event Processing Policies. 
       
     - $object - event source object, one of 'NetObj' subclasses

       $node - event source object if it is 'Node' class

       $event - event being processed (object of 'Event' class)
     - none
   * - Hook\:\:AlarmStateChange
     - Hook that is executed on alarm state change (alarm gets acknowledged, resolved or terminated)
     - $alarm - alarm being processed (object of 'Alarm' class)
     - none
   * - Hook\:\:UnboundTunnelOpened
     - Hook that is executed when tunnel connection is established, but not bound to a node. 
     - $tunnel - incoming tunnel information (object of 'Tunnel' class)
     - none     
   * - Hook\:\:BoundTunnelOpened
     - Hook that is executed when tunnel connection bound to a node is established. 
     - $node - node this tunnel was bound to (object of 'Node' class)
     
       $tunnel - incoming tunnel information (object of 'Tunnel' class)
     - none     

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
:menuselection:`Tools --> Server Console` menu in management console. Once in
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

Autologin for Management Console
================================

.. versionadded:: 1.2.9

Starting from version 1.2.4, it is possible to connect management console (nxmc)
or web management console to server automatically without login dialog. This chapter
describes additional command line options and URL parameters for that.

Desktop Console
---------------

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

For example, to connect management console to server 10.0.0.2 as user guest with empty password, use command

.. code-block:: abap

    nxmc -auto -server=10.0.0.2 -login=guest

Web Console
-----------

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

.. code-block:: abap

    http://server/nxmc?auto&server=10.0.0.2&login=guest&dashboard=SystemOverview


|product_name| data usage in external products
==============================================

|product_name| provides next options to use data in other applications:

    * Use :ref:`autologin <autologin>` and dashboard name in URL to add dashboard to your company
      documentation(where URL usage is possible).
    * Use :ref:`Grafana <grafana-integration>` for graph creation and further usage
    * Get data through :ref:`Web API <rest-api>`

.. _rest-api:

Web API/Rest API
================

The |product_name| WebAPI is being developed to support larger integration possibilities for the |product_name|
server and is based on the RESTful philosophy. API calls are REST-like (although not purely RESTful)
and uses JSON for data exchange. The API currently supports Grafana integration and
some additional parameters for integration. The |product_name| WebAPI is currently in very early development!

Information about Grafana configuration can be found :ref:`here <grafana-integration>`.

Requirements
------------

   * A running instance of the |product_name| server.
   * Access to a web server.

Setup
-----

1. Download netxms-websvc-VERSION.war (example: netxms-websvc-2.2.15.war) file from http://www.netxms.org/download page.
2. Copy the downloaded .war file to your web server.
3. Create a :file:`nxapisrv.properties` file and place it in the property file location of your
   web server and specify the |product_name| Server address with the property.

Localhost address will be used if no address was set. Server configuration example:

   .. code-block:: cfg

        netxms.server.address=sever.office.radensolutions.com

If the server is running on a non-standard port, specify it with the following property:

  .. code-block:: cfg

    netxms.server.port=

Implemented functionality
-------------------------

Authentication
~~~~~~~~~~~~~~

Login
^^^^^

Any user account configured in NetXMX can be used to authenticate to Rest API, however
this user should have access right to objects that will be requested through the API.

There are 3 implemented options of authentication:

   1. Basic authentication for Rest API session creation, more information can be found on :wikipedia:`Wikipedia <Basic access authentication>`
   2. Through POST request for Rest API session creation
   3. Through POST request to allow external software user authentication using |product_name| user accounts.
      To be able to login using this authentication type, user account should have "External tool integration account" access right set.

Creating Rest API session:
%%%%%%%%%%%%%%%%%%%%%%%%%%

Request type: **POST**

JSON data:

.. code-block:: json

    {"login":"admin","password":"netxms"}

Request path: *API_HOME*/sessions

Return data:

    On success server will set cookie session_handle and json with session GUID and server version.
    When performing subsequent requests, session GUID should be provided in `Session-Id:` field of request's header
    or the cookie should be passed.

Performing external authentication:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Request type: **POST**

JSON data:

.. code-block:: json

    {"login":"admin","password":"netxms"}

Request path: *API_HOME*/authenticate

Return data:

    The API will return a 200 response if the credentials are correct, a 400 response if
    either login or password is not provided or 401 if the provided credentials are incorrect.

Authentication used to gain Rest API session.

Logout
^^^^^^

To log out request with given session ID.

Request type: **DELETE**

Request path: *API_HOME*/sessions/**{sid}**

Return data:

    The API will return a 200 response if log out succeed.

Objects
~~~~~~~

Get multiple objects with filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request to get all objects available to this user or to get objects that fulfill
filter requirements and are available to this user.

Request type: **GET**

Request path: *API_HOME*/objects

Filter options:

    * area=\ *geographical area*
    * class=\ *comma-separated class list*
    * name=\ *pattern or regex, if useRegex=true*
    * parent=\ *parent object id*
    * topLevelOnly=\ *boolean - select top level objects only. false by default*
    * useRegex=\ *boolean - treat name and custom attribute value as regex. false by default*
    * zone=\ *comma-separated list of zone UINs*
    * @custom_attribute_name=\ *pattern or regex, if useRegex=true*

Return data:

    Will return filtered objects or all objects available to user.

Get object by id
^^^^^^^^^^^^^^^^

Request to get exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**

Return data:

    Object information identified by provided ID or GUID.

Create object
^^^^^^^^^^^^^

Request to create new object.

Request type: **POST**

JSON data:

  JSON object can contain fields form 2 filed entities: 

    * :ref:`creation-fields`
    * :ref:`modification-fields`

  Minimal JSON for node creation under "Infrastructure Services" object:

  .. code-block:: json

      {"objectType": 2, "name":"testNode", "parentId": 2, "primaryName":"10.5.0.12" }

  Minimal JSON for container creation under "Infrastructure Services" object:

  .. code-block:: json

      {"objectType": 5, "name":"New container", "parentId": 2}

Request path: *API_HOME*/objects

Return data:

    New object ID.

  .. code-block:: json

    { "id": 15130 }

Update object
^^^^^^^^^^^^^

Request to update object.

Request type: **PATCH**

Request path: *API_HOME*/objects/**{object-id}**

JSON data:

  JSON object can contain :ref:`modification-fields`.

  Fields that are not set will not be updated. Array elements will be replaced fully (if new array does not contain old elements - they will be deleted).

  Json to update object's custom attributes (json should contain all custom attributes, attributes that are not part of JSON will be deleted):

  .. code-block:: json

    {
      "customAttributes": {
          "test attr2": {
              "value": "new value"
          },
          "test attr": {
              "value": "new value"
          }
      }
    }


Get object by id
^^^^^^^^^^^^^^^^

Request to delete object.

Request type: **DELETE**

Request path: *API_HOME*/objects/**{object-id}**

Return data:

    Object information identified by provided ID or GUID.

.. _creation-fields:

Creation fields
^^^^^^^^^^^^^^^
This list represents all fields that are object creation fields. Note that this is common list for any type of object.

.. list-table::
   :widths: 21 21 34
   :header-rows: 1

   * - Field name
     - Type
     - Comment
   * - objectType
     - Ingeger
     - Possible options:
  
       * SUBNET: 1
       * NODE: 2
       * INTERFACE: 3
       * NETWORK: 4
       * CONTAINER: 5
       * ZONE: 6
       * SERVICEROOT: 7
       * TEMPLATE: 8
       * TEMPLATEGROUP: 9
       * TEMPLATEROOT: 10
       * NETWORKSERVICE: 11
       * VPNCONNECTOR: 12
       * CONDITION: 13
       * CLUSTER: 14
       * OBJECT_BUSINESSSERVICE_PROTOTYPE: 15
       * NETWORKMAPROOT: 19
       * NETWORKMAPGROUP: 20
       * NETWORKMAP: 21
       * DASHBOARDROOT: 22
       * DASHBOARD: 23
       * BUSINESSSERVICEROOT: 27
       * BUSINESSSERVICE: 28
       * NODELINK: 29
       * SLMCHECK: 30
       * MOBILEDEVICE: 31
       * RACK: 32
       * ACCESSPOINT: 33
       * CHASSIS: 35
       * DASHBOARDGROUP: 36
       * SENSOR: 37  
   * - name
     - String
     - Object name
   * - parentId
     - Long
     - Parent object id this object to be created under
   * - comments
     - String
     - Object comment
   * - creationFlags
     - Ingeger
     - Bit flags for object creation. Possible options:

       * DISABLE ICMP: 0x0001
       * DISABLE NXCP: 0x0002
       * DISABLE SNMP: 0x0004
       * CREATE UNMANAGED: 0x0008
       * ENTER MAINTENANCE: 0x0010
       * AS ZONE PROXY: 0x0020
       * DISABLE ETHERNET IP: 0x0040
       * SNMP SETTINGS LOCKED: 0x0080
       * EXTERNAL GATEWAY: 0x0100
   * - primaryName
     - String
     - Node primary name (IP address or dns name)
   * - agentPort
     - Ingeger
     - Node agent port
   * - snmpPort
     - Ingeger
     - Node SNMP port
   * - etherNetIpPort
     - Ingeger
     - Node ethernetIP port
   * - sshPort
     - Ingeger
     - Node ssh port
   * - ipAddress
     - String
     - Interface IP address
   * - agentProxyId
     - Long
     - Node agent proxy id
   * - snmpProxyId
     - Long
     - Node SNMP proxy id
   * - etherNetIpProxyId
     - Long
     - Node ethernetIP proxy id
   * - icmpProxyId
     - Long
     - Node ICMP proxy id
   * - sshProxyId
     - Long
     - Node ssh proxy id
   * - mapType
     - Ingeger
     - Network map type
   * - seedObjectIds
     - Long[]
     - Network map seed objects
   * - zoneUIN
     - Ingeger
     - Subnet/Node/Zone zone UIN
   * - serviceType
     - Ingeger
     - Network service types: 
      
       * CUSTOM: 0
       * SSH: 1
       * POP3: 2
       * SMTP: 3
       * FTP: 4
       * HTTP: 5
       * HTTPS: 6
       * TELNET: 7
   * - ipPort
     - Ingeger
     - Network Service IP port
   * - request
     - String
     - Network Service request
   * - response
     - String
     - Network Service response
   * - linkedNodeId
     - Long
     - Linked object for Node Link object
   * - template
     - Boolean
     - If service check object is template 
   * - macAddress
     - String
     - Interface or sensor MAC address
   * - ifIndex
     - Ingeger
     - Interface index
   * - ifType
     - Ingeger
     - Interface type
   * - module
     - Ingeger
     - Interface module number
   * - port
     - Ingeger
     - Interface port
   * - physicalPort
     - Boolean
     - IF interface has physical port
   * - createStatusDci
     - Boolean
     - IF status DCI should be created for network service
   * - deviceId
     - String
     - Mobile device ID
   * - height
     - Ingeger
     - Rack height
   * - controllerId
     - Long
     - Chassis controller node id
   * - sshLogin
     - String
     - Node ssh login
   * - sshPassword
     - String
     - Node password
   * - deviceClass
     - Ingeger
     - Sensor device class
   * - vendor
     - String
     - Sensor vendor
   * - commProtocol
     - Ingeger
     - Sensor communication protocol
   * - xmlConfig
     - String
     - Sensor XML config
   * - xmlRegConfig
     - String
     - Sensor XML registration config
   * - serialNumber
     - String
     - Sensor serial number
   * - deviceAddress
     - String
     - Sensor device address
   * - metaType
     - String
     - Sensor meta type
   * - description
     - String
     - Sensor description
   * - sensorProxy
     - Long
     - Sensor proxy node id
   * - instanceDiscoveryMethod
     - Business service instance discovery method     
     - Possible values:
      
        * IDM_AGENT_LIST - 1
        * IDM_AGENT_TABLE - 2
        * IDM_SCRIPT - 5


.. _modification-fields:

Modification fields
^^^^^^^^^^^^^^^^^^^

.. note::

  Starting from version 4 isAutoBindEnabled and isAutoUnbindEnabled replaced by autoBindFlags

.. list-table::
   :widths: 21 21 34
   :header-rows: 1

   * - Field name
     - Type
     - Comment
   * - name
     - String
     -
   * - primaryName
     - String
     -
   * - alias
     - String
     -
   * - nameOnMap
     - String
     -
   * - acl
     - :ref:`AccessListElement <access-list-element-fields>`\ []
     -
   * - inheritAccessRights
     - Boolean
     -
   * - customAttributes 
     - JSON object {String: :ref:`CustomAttribute<custom-attribute-element-fields>`}
     - Object name is custom attribute name and value is in :ref:`CustomAttribute<custom-attribute-element-fields>` object
   * - autoBindFilter
     - String
     -
   * - version
     - Integer
     -
   * - description
     - String
     -
   * - agentPort
     - Integer
     -
   * - agentSecret
     - String
     -
   * - agentProxy
     - Long
     -
   * - snmpPort
     - Integer
     -
   * - snmpVersion
     - String
     - Node SNMP version:
      
       * V1
       * V2C
       * V3
       * DEFAULT
   * - snmpAuthMethod
     - Integer
     -
   * - snmpPrivMethod
     - Integer
     -
   * - snmpAuthName
     - String
     -
   * - snmpAuthPassword
     - String
     -
   * - snmpPrivPassword
     - String
     -
   * - snmpProxy
     - Long
     -
   * - icmpProxy
     - Long
     -
   * - trustedNodes
     - Long[]
     -
   * - geolocation
     - :ref:`Geolocation <geolocation-fields>`
     -
   * - mapBackground
     - String
     - UUID
   * - mapBackgroundLocation
     - :ref:`Geolocation <geolocation-fields>`
     -
   * - mapBackgroundZoom
     - Integer
     -
   * - mapBackgroundColor
     - Integer
     -
   * - mapImage
     - String
     - UUID
   * - columnCount
     - Integer
     -
   * - script
     - String
     -
   * - activationEvent
     - Integer
     -
   * - deactivationEvent
     - Integer
     -
   * - sourceObject
     - Long
     -
   * - activeStatus
     - Integer
     -
   * - inactiveStatus
     - Integer
     -
   * - drillDownObjectId
     - Long
     -
   * - pollerNode
     - Long
     -
   * - requiredPolls
     - Integer
     -
   * - serviceType
     - Integer
     -
   * - ipProtocol
     - Integer
     -
   * - ipPort
     - Integer
     -
   * - ipAddress
     - String
     - Network service IP address
   * - request
     - String
     - Network service IP request
   * - response
     - String
     - Network service IP response
   * - objectFlags
     - Integer
     - Object flags specific for each object. Possible values can be found in NXSL documentation under each object. (Example: `Node flags <https://www.netxms.org/documentation/nxsl-latest/#_constants_6>`_)
   * - ifXTablePolicy
     - Integer
     -
   * - reportDefinition
     - String
     -
   * - networkList
     - String[]
     - IP address list
   * - statusCalculationMethod
     - Integer
     -
   * - statusPropagationMethod
     - Integer
     -
   * - fixedPropagatedStatus
     - String
     - Object status: 
      
       * NORMAL
       * WARNING
       * MINOR
       * MAJOR
       * CRITICAL
       * UNKNOWN
       * UNMANAGED
       * DISABLED
       * TESTING
   * - statusShift
     - Integer
     -
   * - statusTransformation
     - ObjectStatus[]
     - Object status mapping list. Possible values:
      
       * NORMAL
       * WARNING
       * MINOR
       * MAJOR
       * CRITICAL
       * UNKNOWN
       * UNMANAGED
       * DISABLED
       * TESTING
   * - statusSingleThreshold
     - Integer
     -
   * - statusThresholds
     - Integer[]
     -
   * - expectedState
     - Integer
     -
   * - linkColor
     - Integer
     -
   * - connectionRouting
     - Integer
     -
   * - discoveryRadius
     - Integer
     -
   * - height
     - Integer
     -
   * - filter
     - String
     -
   * - peerGatewayId
     - Long
     -
   * - localNetworks
     - String[]
     - VPN networks IP adress 
   * - remoteNetworks
     - String[]
     - VPN networks IP adress 
   * - postalAddress
     - :ref:`PostalAddress<postal-address-fields>`
     -
   * - agentCacheMode
     - String
     - Possible values:
      
        * DEFAULT
        * ON
        * OFF
   * - agentCompressionMode
     - String
     - Possible values:
      
        * DEFAULT
        * ENABLED
        * DISABLED
   * - mapObjectDisplayMode
     - String
     - Possible values:
      
        * ICON
        * SMALL_LABEL
        * LARGE_LABEL
        * STATUS
        * FLOOR_PLAN
   * - physicalContainerObjectId
     - Long
     -
   * - rackImageFront
     - String
     - UUID
   * - rackImageRear
     - String
     - UUID
   * - rackPosition
     - Short
     -
   * - rackHeight
     - Short
     -
   * - rackOrientation
     - String
     - Possible values:
      
        * FILL
        * FRONT
        * REAR
   * - dashboards
     - Long[]
     -
   * - rackNumberingTopBottom
     - Boolean
     -
   * - controllerId
     - Long
     -
   * - chassisId
     - Long
     -
   * - sshProxy
     - Long
     -
   * - sshLogin
     - String
     -
   * - sshPassword
     - String
     -
   * - sshPort
     - Integer
     -
   * - sshKeyId
     - Integer
     -
   * - zoneProxies
     - Long[]
     -
   * - urls
     - ObjectUrl[]
     -
   * - seedObjectIds
     - Long[]
     -
   * - macAddress
     - String
     - Sensor mac address
   * - deviceClass
     - Integer
     -
   * - vendor
     - String
     -
   * - serialNumber
     - String
     -
   * - deviceAddress
     - String
     -
   * - metaType
     - String
     -
   * - sensorProxy
     - Long
     -
   * - xmlConfig
     - String
     -
   * - snmpPorts
     - String[]
     -
   * - responsibleUsers
     - Long[]
     -
   * - icmpStatCollectionMode
     - String
     - Possible values:
      
        * DEFAULT
        * ON
        * OFF
   * - icmpTargets
     - String[]
     - ICMP ping targets IP addresses 
   * - chassisPlacement
     - String
     -
   * - etherNetIPPort
     - Integer
     -
   * - etherNetIPProxy
     - Long
     -
   * - certificateMappingMethod
     - String
     - Possible values:
      
        * SUBJECT
        * PUBLIC_KEY
        * COMMON_NAME
        * TEMPLATE_ID
   * - certificateMappingData
     - String
     -
   * - categoryId
     - Integer
     -
   * - geoLocationControlMode
     - GeoLocationControlMode
     - Possible values:
      
        * NO_CONTROL
        * RESTRICTED_AREAS
        * ALLOWED_AREAS
   * - geoAreas
     - long[]
     -
   * - instanceDiscoveryMethod
     - Business service instance discovery method     
     - Possible values:
      
        * IDM_AGENT_LIST - 1
        * IDM_AGENT_TABLE - 2
        * IDM_SCRIPT - 5
   * - instanceDiscoveryData
     - Business service instance discovery data     
     - 
   * - instanceDiscoveryFilter
     - Business service instance discovery data filtering script     
     - 
   * - autoBindFilter2
     - Second binding script used for DCI binding. Urrently used in business service     
     - 
   * - autoBindFlags
     - Auto bind bit flags     
     - Firs script is currently used for object bind/unbind, second for dci bind/unbind. Possible values:
      
        * First script for auto bind is enabeled - 0x0001
        * First script for auto unbind is enabeled - 0x0002
        * Second script for auto bind is enabeled - 0x0004
        * Second script for auto unbind is enabeled - 0x0008
   * - objectStatusThreshold
     - Business service default threshold for auto created object checks    
     - Possible values:
      
        * Default - 0
        * Warning - 1 
        * Minor - 2 
        * Major - 3 
        * Critical - 4 
   * - dciStatusThreshold
     - Business service default threshold for auto created DCI checks    
     - Possible values:
      
        * Default - 0
        * Warning - 1 
        * Minor - 2 
        * Major - 3 
        * Critical - 4 
   * - sourceNode
     - Id of source node for business service instance discovery methods    
     - 

.. _geolocation-fields:

GeoLocation fields
^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - type
    - Integer
    - Available options:
     
      * UNSET: 0
      * MANUAL: 1
      * GPS: 2
      * NETWORK: 3
  * - latitude
    - Double
    -
  * - longitude
    - Double
    -
  * - accuracy
    - int
    -	Location accuracy in meters
  * - timestamp
    - Integer
    - UNIX timestamp

.. _access-list-element-fields:

AccessListElement fields
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - userId
    - Long
    -
  * - accessRights
    - Integer
    - Bit flag field. Available options:
     
      * OBJECT ACCESS READ: 0x00000001
      * OBJECT ACCESS MODIFY: 0x00000002
      * OBJECT ACCESS CREATE: 0x00000004
      * OBJECT ACCESS DELETE: 0x00000008
      * OBJECT ACCESS READ ALARMS: 0x00000010
      * OBJECT ACCESS ACL: 0x00000020
      * OBJECT ACCESS UPDATE ALARMS: 0x00000040
      * OBJECT ACCESS SEND EVENTS: 0x00000080
      * OBJECT ACCESS CONTROL: 0x00000100
      * OBJECT ACCESS TERM ALARMS: 0x00000200
      * OBJECT ACCESS PUSH DATA: 0x00000400
      * OBJECT ACCESS CREATE ISSUE: 0x00000800
      * OBJECT ACCESS DOWNLOAD: 0x00001000
      * OBJECT ACCESS UPLOAD: 0x00002000
      * OBJECT ACCESS MANAGE FILES: 0x00004000
      * OBJECT ACCESS MAINTENANCE: 0x00008000
      * OBJECT ACCESS READ AGENT: 0x00010000
      * OBJECT ACCESS READ SNMP: 0x00020000
      * OBJECT ACCESS SCREENSHOT: 0x00040000

.. _custom-attribute-element-fields:

CustomAttribute fields
^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - value
    - String
    - Attribute value
  * - flags
    - Long
    - Available options:
     
      * INHERITABLE: 1

.. _postal-address-fields:

PostalAddress fields
^^^^^^^^^^^^^^^^^^^^

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - country
    - String
    -
  * - city
    - String
    -
  * - streetAddress
    - String
    -
  * - postcode
    - String
    - 

Bind node
^^^^^^^^^

Request to bind object to container.

Request type: **POST**

JSON data:

  Bind object to object in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/bind


Bindto node
^^^^^^^^^^^

Request to bind object under container.

Request type: **POST**

JSON data:

  Bind object in URL to "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/bindTo

Unbind node
^^^^^^^^^^^

Request to unbind object from container.

Request type: **POST**

JSON data:

  Unbind object from container in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/unbind


UnbindFrom node
^^^^^^^^^^^^^^^

Request to unbind object from container.

Request type: **POST**

JSON data:

  Unbind object in URL from "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/unbindFrom


Poll object
^^^^^^^^^^^

Create object poll request

Request type: **POST**

JSON data:

  .. code-block:: json

      {"type": "status"}

One of the following poll types:

  * configuration full
  * configuration
  * discovery
  * interface
  * status
  * topology

Request path: *API_HOME*/objects/**{object-id}**/polls

Return data:

    Will return UUID of request, that should be used to get request output and request type.

  .. code-block:: json

    { "id": 15130,
      "type": "status" }

Get object poll data
^^^^^^^^^^^^^^^^^^^^

Get object poll request data 

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/polls/output/**{request-UUID}**

Return data:

    Will return request output data.

  .. code-block:: json

    { "streamId": 0,
      "completed": false,
      "message": "Poll request accepted..." }

Business Services
~~~~~~~~~~~~~~~~~

Get checks
^^^^^^^^^^

Request all business service checks

Request type: **GET**

Request path: *API_HOME*/**{object-id}**/checks

Create new check
^^^^^^^^^^^^^^^^

Create new business service check

Request type: **POST**

Request path: *API_HOME*/**{object-id}**/checks

JSON data:

  Create new script business service check:

  .. code-block:: json

      {
          "checkType": "SCRIPT",
          "description": "Web created script",
          "script": "return OK;",
          "objectId": 0,
          "dciId": 0,
          "threshold": 0
       }


Update existing check
^^^^^^^^^^^^^^^^^^^^^

Update existing business service check

Request type: **PUT**

Request path: *API_HOME*/**{object-id}**/checks/**check-id**

JSON data:

  Update existing business service check to object check with object ID "166":

  .. code-block:: json

      {
          "checkType": "OBJECT",
          "description": "Web created script",
          "script": "return OK;",
          "objectId": 166,
          "dciId": 0,
          "threshold": 0
      }


Update existing check
^^^^^^^^^^^^^^^^^^^^^

Delete existing business service check

Request type: **DELETE**

Request path: *API_HOME*/**{object-id}**/checks/**check-id**


Get tickets
^^^^^^^^^^^

Get ticket list for given time range. 

Request type: **GET**

Request path: *API_HOME*/**{object-id}**/tickets

Time range can be requested in 2 ways.

First option is back from now with given parameters:

    * timeUnit=\ *Type of time range. Possible values: MINUTE, HOUR, DAY*
    * timeRage=\ *Range in given units*

Second option is fixe time range:

    * start=\ *UNIX timestamp*
    * end=\ *UNIX timestamp*


Get uptime
^^^^^^^^^^

Get uptime for given time range. 

Request type: **GET**

Request path: *API_HOME*/**{object-id}**/uptime

Time range can be requested in 2 ways.

First option is back from now with given parameters:

    * timeUnit=\ *Type of time range. Possible values: MINUTE, HOUR, DAY*
    * timeRage=\ *Range in given units*

Second option is fixe time range:

    * start=\ *UNIX timestamp*
    * end=\ *UNIX timestamp*

Alarms
~~~~~~

Full scope of currently active alarms can be obtained or object specific list.

Get multiple alarms with filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Request to get all active alarms available to this user or to get active alarms that fulfill
filter requirements and are available to this user.

Request type: **GET**

Request path: *API_HOME*/alarms

Filter options:

    * alarm=\ *list of alarm states. Possible values: outstanding, acknowledged, resolved*
    * createdBefore=\ *UNIX timestamp*
    * createdAfter=\ *UNIX timestamp*
    * objectId=\ *ID or related object*
    * objectGuid=\ *GUID or related object*
    * includeChildObjects=\ *boolean. Set to true to get alarms of container child objects*
    * resolveReferences=\ *resolve IDs into human readable data*
    * updatedBefore=\ *UNIX timestamp*
    * updatedAfter=\ *UNIX timestamp*

Return data:

    Will return filtered active alarms or all active alarms available to user.

Alarm by id
^^^^^^^^^^^

Request to get an alarm by it's ID.

Request type: **GET**

Request path: *API_HOME*/alarms/**{alarm-id}**

Return data:

    Will return alarm specified by ID.

DCI Data
~~~~~~~~

There are 2 options to get DCI last values. First is to get last values for one DCI and the second one is to create adhoc summary table with required values for all nodes under container.

DCI last values
^^^^^^^^^^^^^^^

Request to get last values of DCI identified by ID for exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/datacollection/**{dci-id}**/values

Filter options:

    * from=\ *requested period start time as unix timestamp*
    * to=\ *requested period end time as unix timestamp*
    * timeInterval=\ *requested time interval in seconds*
    * itemCount=\ *number of items to be returned*

Return data:

    Will return last values for requested node and DCI limited by filters.

Adhoc summary table
^^^^^^^^^^^^^^^^^^^

Option to get last values for multiple nodes(for all nodes under provided container) for the same DCIs. Required DCIs and container are provided in request.

Request type: **POST**

Request path: *API_HOME*/summaryTable/adHoc

POST request JSON

.. code-block:: json

    {
        "baseObject":"ContainerName",
        "columns": [
            {
            "columnName":"Free form name that will be used in return table for this column",
            "dciName":"Name of DCI, that will be used for filtering"
            },
            {
            "columnName":"Name2",
            "dciName":"DCIName2"
            }
        ]
    }

Return data:

    Will return adhoc summary table configured accordingly to request json.

Find Object
===========

Management console has an option to filter objects by defined by user criteria. Filter can be access by :menuselection:`Tools->Find Object`\ .
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

LEEF server module provides functionality to send audit log to IBM Security QRadar. 
The Log Event Extended Format (LEEF) is a customized event format for IBM Security QRadar. More about it can be found 
`there <https://www.ibm.com/docs/en/dsm?topic=leef-overview>`_.

LEEF server module should be enabled in server configuraiton file by adding "Module=leef.nxm" line to :file:`netxmsd.conf` file.

Additionaly to module configuration "LEEF" section should be added with required configurations.

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
    - LEEF separator character as a char or in numeric format: "xHH", where HH is hexdecimal digit

Additional fields can be configured in ExtraData sub section in the same key=value format.
  

Example:

.. code-block:: cfg

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

