.. _concepts:

########
Concepts
########

Architecture overview
=====================

The system has three-tier architecture: the information is collected by 
monitoring agents (either our own high-performance agents or SNMP agents) 
and delivered to monitoring server for processing and storage. Network 
administrator can access collected data using cross-platform Management 
Console, Web Interface or Management Console for Android. 

.. only:: html
  .. figure:: _images/architecture_scheme.png

.. only:: latex
  .. figure:: _images/architecture_scheme.png
     :scale: 60

Architecture scheme

NetXMS server is daemon or service. It collects, process and stores data, 
does network discovery. Server is modular and can be extended with additional 
functionality. By it selves server can collect only some simple 
information about nodes or can use :term:`SNMP` agent to collect data from 
SNMP-capable devices. NetXMS has special drivers for different types of SNMP 
devices that collect data like VLANs, interfaces and other default collected 
information. 

NetXMS server does not support horizontal scaling. For now it is possible 
only event exchange between servers. 

NetXMS agent is daemon or service that is installed on nodes to provide
additional monitoring options and can be used like :term:`SNMP` agent or 
NetXMS agent proxy. Agent implements communication with server and work with 
configuration. Agent functionality is extended with subagents. Server uses 
4701 port to communicate with agents.

There are default OS subagents and manually loaded like file manager, 
ping or others. There are different types of subagents. It can be just 
a library that is loaded by NetXMS agent or it can be application that 
uses NetXMS subagent library to provide required subagent interface. 
Library type of subagents can be run as one process with agent or as a 
separate process. It can be used when it is necessary to run them under 
different user privileges. 
Agent uses 4700 port to communicate with server.

Subagent can be also run as a separate application. 

NetXMS also provides some command line tools like nxdbmgr(work with NetXMS 
database), nxencpasswd(password encryption) and others. Information about this 
tools can be found in :ref:`command_line_tools` chapter.

In further chapters will be described main NetXMS objects and concepts. 

.. _concept_object:

Objects
=======

All network infrastructure monitored by NetXMS inside monitoring system 
represented as a set of :term:`objects <Object>`. Each object
represents one physical or logical entity (like host or network interface), 
or group of them. Objects are organized into hierarchical structure. 
Each object has it's own access rights. Access rights are applied 
hierarchically on all children of object. For example if it grant :guilabel:`Read`
access right for user on a :guilabel:`Container`, than user have :guilabel:`Read` 
right on all objects that contains this :guilabel:`Container`. 
Every object has set of attributes; some of them are common 
(like :guilabel:`id` and :guilabel:`name` or :guilabel:`status`),  while other 
depends on object class – for example, only :guilabel:`Node` objects have 
attribute :guilabel:`SNMP community string`. There are default attributes 
and custom attributes defined either by user or integrated application via 
NetXMS API.

NetXMS has eight top level objects – ``Entire Network``, ``Service Root``,
``Template Root``, ``Policy Root``, ``Network Map Root``, ``Dashboard Root``,
``Report Root``, and ``Business Service Root``. These objects served as an
abstract root for appropriate object tree. All top level objects has only one
editable attribute – name.

.. tabularcolumns:: |p{0.2 \textwidth}|p{0.5 \textwidth}|p{0.3 \textwidth}|

.. list-table::
   :widths: 20 50 30
   :header-rows: 1
   :class: longtable

   * - Object Class
     - Description
     - Valid Child Objects
   * - |ENTIRE_NETWORK| Entire Network
     - Abstract object representing root of IP topology tree. All zone and
       subnet objects located under it. System can have only one object of this
       class.
     - - |ZONE| Zone (if zoning enabled)
       - |SUBNET| Subnet (if zoning disabled)
   * - |ZONE| Zone
     - Object representing group of (usually interconnected) IP networks
       without overlapping addresses. Contains appropriate subnet objects.
     - - |SUBNET| Subnet
   * - |SUBNET| Subnet
     - Object representing IP subnet. Typically objects of this class created
       automatically by the system to reflect system's knowledge of IP
       topology. The system places Node objects inside an appropriate Subnet
       object based on an interface configuration. Subnet objects have only one
       editable attribute - :guilabel:`Name`.
     - - |NODE| Node
   * - |NODE| Node
     - Object representing physical host or network device(such as routers and switches). 
       These objects can be created either manually by administrator or automatically during
       network discovery process. They have a lot of attributes controlling all aspects 
       of interaction between NetXMS server and managed node. For example, the attributes 
       specify what data must be collected, how node status must be checked, which protocol 
       versions to use etc. Node objects contain one or more interface objects. The system 
       creates interface objects automatically during configuration polls.
     - - |INTERFACE| Interface
       - |NETWORK_SERVICE| Network Service
       - |VPN| VPN Connector
   * - |CLUSTER| Cluster
     - Object representing cluster consisted of two or more hosts.
     - - |NODE| Node
   * - |INTERFACE| Interface
     - Interface objects represent network interfaces of managed computers and
       devices. These objects created automatically by the system during 
       configuration polls or can be created manually by user.
     -
   * - |NETWORK_SERVICE| Network Service
     - Object representing network service running on a node (like http or
       ssh), which is accessible online (via TCP IP). Network Service objects 
       are always created manually. Currently, the system works with the following 
       protocols - HTTP, POP3, SMTP, Telnet, SSH and Custom protocol type. 
     -
   * - |VPN| VPN Connector
     - Object representing VPN tunnel endpoint. Such objects can be created to
       add VPN tunnels to network topology known y NetXMS server. VPN Connector 
       objects are created manually. In case if there is a VPN
       connection linking two different networks open between two firewalls that are
       added to the system as objects, a user can create a VPN Connector object on
       each of the firewall objects and link one to another. The network topology will
       now show that those two networks are connected and the system will take this
       condition into account during problem analysis and event correlation.
     -
   * - |SERVICE_ROOT| Service Root
     - Abstract object representing root of your infrastructure service tree.
       System can have only one object of this class.
     - - |CLUSTER| Cluster
       - |CONDITION| Condition
       - |CONTAINER| Container
       - |MOBILE_DEVICE| Mobile Device
       - |NODE| Node
       - |SUBNET| Subnet
   * - |CONTAINER| Container
     - Grouping object which can contain nodes, subnets, clusters, conditions,
       or other containers. With help of container objects you can build
       object's tree which represents logical hierarchy of IT services in your
       organization.
     - - |CLUSTER| Cluster
       - |CONDITION| Condition
       - |CONTAINER| Container
       - |MOBILE_DEVICE| Mobile Device
       - |NODE| Node
       - |SUBNET| Subnet
   * - |CONDITION| Condition
     - Object representing complicated condition – like "cpu on node1 is
       overloaded and node2 is down for more than 10 minutes". Conditions may 
       represent more complicated status checks because each condition can have 
       a script attached. Interval for evaluation of condition status is 
       configured in Server Configuration Variables as ConditionPollingInterval 
       with default value 60 seconds.
     -
   * - |TEMPLATE_ROOT| Template Root
     - Abstract object representing root of your template tree.
     - - |TEMPLATE| Template
       - |TEMPLATE_GROUP| Template Group
   * - |TEMPLATE_GROUP| Template Group
     - Grouping object which can contain templates or other template groups.
     - - |TEMPLATE| Template
       - |TEMPLATE_GROUP| Template Group
   * - |TEMPLATE| Template
     - Data collection template. See Data Collection section for more
       information about templates.
     - - |MOBILE_DEVICE| Mobile Device
       - |NODE| Node
   * - |NETWORK_MAP_ROOT| Network Map Root
     - Abstract object representing root of your network map tree.
     - - |NETWORK_MAP| Network Map
       - |NETWORK_MAP_GROUP| Network Map Group
   * - |NETWORK_MAP_GROUP| Network Map Group
     - Grouping object which can contain network maps or other network map
       groups.
     - - |NETWORK_MAP| Network Map
       - |NETWORK_MAP_GROUP| Network Map Group
   * - |NETWORK_MAP| Network Map
     - Network map.
     -
   * - |DASHBOARD_ROOT| Dashboard Root
     - Abstract object representing root of your dashboard tree.
     - - |DASHBOARD| Dashboard
   * - |DASHBOARD| Dashboard
     - Dashboard. Can contain other dashboards.
     - - |DASHBOARD| Dashboard
   * - |BSERV_ROOT| Business Service Root
     - Abstract object representing root of your business service tree. System
       can have only one object of this class.
     - - |BSERV| Business Service
   * - |BSERV| Business Service
     - Object representing single business service. Can contain other business
       services, node links, or service checks.
     - - |BSERV| Business Service
       - |NODE_LINK| Node Link
       - |SERVICE_CHECK| Service Check
   * - |NODE_LINK| Node Link
     - Link between node object and business service. Used to simplify creation
       of node-related service checks.
     - - |SERVICE_CHECK| Service Check
   * - |SERVICE_CHECK| Service Check
     - Object used to check business service state. One business service can
       contain multiple checks. 
     -

.. |BSERV_ROOT| image:: _images/icons/business_services.png
.. |BSERV| image:: _images/icons/business_service.png
.. |SERVICE_CHECK| image:: _images/icons/service_check.png
.. |CLUSTER| image:: _images/icons/cluster.png
.. |CONDITION| image:: _images/icons/condition.png
.. |CONTAINER| image:: _images/icons/container.png
.. |DASHBOARD_ROOT| image:: _images/icons/dashboards.png
.. |DASHBOARD| image:: _images/icons/dashboard.png
.. |ENTIRE_NETWORK| image:: _images/icons/entire_network.png
.. |INTERFACE| image:: _images/icons/interface.png
.. |MOBILE_DEVICE| image:: _images/icons/mobile_device.png
.. |NETWORK_MAP_GROUP| image:: _images/icons/network_map_group.png
.. |NETWORK_MAP_ROOT| image:: _images/icons/network_maps.png
.. |NETWORK_MAP| image:: _images/icons/network_map.png
.. |NETWORK_SERVICE| image:: _images/icons/network_service.png
.. |NODE_LINK| image:: _images/icons/node_link.png
.. |NODE| image:: _images/icons/node.png
.. |REPORT_GROUP| image:: _images/icons/report_group.png
.. |REPORT_ROOT| image:: _images/icons/reports.png
.. |REPORT| image:: _images/icons/report.png
.. |SERVICE_ROOT| image:: _images/icons/infrastructure_services.png
.. |SUBNET| image:: _images/icons/subnet.png
.. |TEMPLATE_GROUP| image:: _images/icons/template_group.png
.. |TEMPLATE_ROOT| image:: _images/icons/templates.png
.. |TEMPLATE| image:: _images/icons/template.png
.. |VPN| image:: _images/icons/interface.png
.. |ZONE| image:: _images/icons/zone.png


Object status
-------------

Each object has a status. Status of the object calculated based on polling results, 
status of underlying objects, associated alarms and status :term:`DCIs<DCI>`. For some object classes, 
like Report or :term:`Template`, status is irrelevant. Status for such objects is always :guilabel:`Normal`. 
Object's status can be one of the following:


.. list-table::
   :widths: 10 30 70
   :header-rows: 1

   * - Nr.
     - Status
     - Description
   * - 0
     - |NORMAL| Normal
     - Object is in normal state.
   * - 1
     - |WARNING| Warning
     - Warning(s) exist for the object.
   * - 2
     - |MINOR| Minor
     - Minor problem(s) exist for the object.
   * - 3
     - |MAJOR| Major
     - Major problem(s) exist for the object.
   * - 4
     - |CRITICAL| Critical
     - Critical problem(s) exist for the object.
   * - 5
     - |UNKNOWN| Unknown
     - Object's status is unknown to the management server.
   * - 6
     - |UNMANAGED| Unmanaged
     - Object is set to "unmanaged" state.
   * - 7
     - |DISABLED| Disabled
     - Object is administratively disabled (only applicable to interface objects).
   * - 8
     - |TESTING| Testing
     - Object is in testing state (only applicable to interface objects).

.. |NORMAL| image:: _images/icons/status/normal.png
.. |WARNING| image:: _images/icons/status/warning.png
.. |MINOR| image:: _images/icons/status/minor.png
.. |MAJOR| image:: _images/icons/status/major.png
.. |CRITICAL| image:: _images/icons/status/critical.png
.. |UNKNOWN| image:: _images/icons/status/unknown.png
.. |UNMANAGED| image:: _images/icons/status/unmanaged.png
.. |DISABLED| image:: _images/icons/status/disabled.png
.. |TESTING| image:: _images/icons/status/testing.png

Event Processing
================

NetXMS is event based monitoring system. Events can come from different sources 
(polling processes (status, configuration, discovery, and data collection), :term:`SNMP` 
traps, and directly from external applications via client library.)
and all are forwarded to NetXMS Event Queue. All events are processed by NetXMS 
Event Processor one-by-one, according to the processing rules defined in 
:term:`Event Processing Policy<EPP>`. As a result of event processing, preconfigured 
actions can be executed, and/or event can be shown up as :term:`alarm <Alarm>`.  

Usually alarm represents something that needs attention of network administrators 
or network control center operators, for example low free disk space on a server.
NetXMS provides one centralized location, the Alarm Browser, where the alarms are 
visible. It can be configured which events should be considered 
important enough to show up as alarm.

.. figure:: _images/event_flow.png

   Event flow inside the monitoring system

.. _concepts_polling:
   
Polling
=======

For some type of objects NetXMS server start gathering status and configuration information
as soon as they are added to the system. These object types are: nodes, conditions,
clusters, business services. This process called *polling*. There are multiple polling
types, usually performed with different intervals:

+---------------+----------------------------------------------------------------------------------------------+
| Type          | Purpose                                                                                      |
+===============+==============================================================================================+
| Status        | Determine current status of an object                                                        |
+---------------+----------------------------------------------------------------------------------------------+
| Configuration | Determine current configuration of an object (list of interfaces, supported protocols, etc.) |
+---------------+----------------------------------------------------------------------------------------------+
| Topology      | Gather information related to network topology                                               |
+---------------+----------------------------------------------------------------------------------------------+
| Discovery     | Find potential new nodes during network discovery cycles                                     |
+---------------+----------------------------------------------------------------------------------------------+
| Routing       | Gather information about IP routing                                                          |
+---------------+----------------------------------------------------------------------------------------------+
   
Data Collection
===============

One of NetXMS important parts is Data Collection. Every :term:`Node` can have many :term:`metrics <Metric>`, 
like “CPU utilization”, “amount of free memory” or “disk space usage”. NetXMS server can collect these parameters, 
check them for threshold violations and store them in the database. Configuration for metric collection is 
called :term:`Data Collection Item <DCI>`. There can be different sources for metrics. Table bellow 
lists possible sources and gives some simple description about them. 

.. list-table::
   :widths: 30 70
   :header-rows: 1
    
   * - Source
     - Description
   * - Internal
     - This type of source does not require any node configuration. It is collected by server.
   * - NetXMS Agent
     - This type of source required NetXMS agent installation on a node. This list can be 
       supplemented with subagents. Metrics are requested by server.
   * - SNMP
     - This type of source requires :term:`SNMP` configuration on device and server.
   * - Push
     - This type of source requires installation of nxpush command line tool and script creation
       that will run this tool in requested intervals and will provide to server metric data.
   * - SM-CLP
     - 
   * - Windows Performance counters
     - 
   * - Check Point SNMP
     -  
   * - Script
     - This type of source requires creation of script in :guilabel:`Script Library` that will 
       be executed according to schedule to gent next value. 

Collected data can be analyzed manually by viewing it with help of :guilabel:`History` table, graph,
displayed on :guilabel:`Dashboard` or on :guilabel:`Network Map`. 

Other option to use collected data is to configure threshold. Each threshold is executed on a new 
coming data and generates user predefined event if data meets threshold rules. Generated event will 
be processed with other events. 


Discovery
=========


Network discovery
-----------------

NetXMS is capable of discovering your network automatically. Network discovery module can operate in 
two modes - passive and active. In passive mode, information about new hosts and devices obtained from 
ARP tables and routing tables of already known devices. NetXMS starts with it’s own ARP cache and 
routing table. In active discovery mode, NetXMS server will send an ICMP echo requests to all IP 
addresses in given range, and consider each responding address for adding to database. For each new 
device found NetXMS server tries to gather additional information using SNMP and NetXMS agent, and then 
adds it to database. By default NetXMS server will add all discovered devices to database, but you can 
limit it by using discovery filters.

Service discovery
-----------------

TBD (not implemented yet)


Security 
========

There are described some concepts of NetXMS that are connected
with data protection. 

Messages between NetXMS agent and NetXMS server can be encrypted, 
encryption between them can be forced by NetXMS configuration. There 
can be also added :guilabel:`Shared Secret` that is checked on agent-server
connection and in case server does not know secret of an agent, connection 
will not be established. Another possibility to control access to the agent 
is cosing the correct server access level in agent configuration properties. 

When it is required to write password or :guilabel:`Shared Secret` in agent
configuration file, there is possibility to encrypt it. All passwords can 
be encrypted with help of nxencpasswd command line tool and added in configuration 
in encrypted way. 
