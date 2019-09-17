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
Console, Web Interface or Management Console for Android. Rich and Web console 
have almost the same functionality and the same user interface. 

.. only:: html

  .. figure:: _images/architecture_scheme.png

.. only:: latex

  .. figure:: _images/architecture_scheme.png
     :scale: 60

.. _concept_object:

Objects
=======

All network infrastructure monitored by |product_name| inside monitoring system
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
|product_name| API.

|product_name| has eight top level objects – ``Entire Network``, ``Service Root``,
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
   * - Entire Network
     - Abstract object representing root of IP topology tree. All zone and
       subnet objects located under it. System can have only one object of this
       class.
     - - Zone (if zoning enabled)
       - Subnet (if zoning disabled)
   * - Zone
     - Object representing group of (usually interconnected) IP networks
       without overlapping addresses. Contains appropriate subnet objects.
     - - Subnet
   * - Subnet
     - Object representing IP subnet. Typically objects of this class created
       automatically by the system to reflect system's knowledge of IP
       topology. The system places Node objects inside an appropriate Subnet
       object based on an interface configuration. Subnet objects have only one
       editable attribute - :guilabel:`Name`.
     - - Node
   * - Node
     - Object representing physical host or network device(such as routers and switches).
       These objects can be created either manually by administrator or automatically during
       network discovery process. They have a lot of attributes controlling all aspects
       of interaction between |product_name| server and managed node. For example, the attributes
       specify what data must be collected, how node status must be checked, which protocol
       versions to use etc. Node objects contain one or more interface objects. The system
       creates interface objects automatically during configuration polls.
     - - Interface
       - Network Service
       - VPN Connector
   * - Cluster
     - Object representing cluster consisted of two or more hosts.
     - - Node
   * - Interface
     - Interface objects represent network interfaces of managed computers and
       devices. These objects created automatically by the system during
       configuration polls or can be created manually by user.
     -
   * - Network Service
     - Object representing network service running on a node (like http or
       ssh), which is accessible online (via TCP IP). Network Service objects
       are always created manually. Currently, the system works with the following
       protocols - HTTP, POP3, SMTP, Telnet, SSH and Custom protocol type.
     -
   * - VPN Connector
     - Object representing VPN tunnel endpoint. Such objects can be created to
       add VPN tunnels to network topology known y |product_name| server. VPN Connector
       objects are created manually. In case if there is a VPN
       connection linking two different networks open between two firewalls that are
       added to the system as objects, a user can create a VPN Connector object on
       each of the firewall objects and link one to another. The network topology will
       now show that those two networks are connected and the system will take this
       condition into account during problem analysis and event correlation.
     -
   * - Service Root
     - Abstract object representing root of your infrastructure service tree.
       System can have only one object of this class.
     - - Cluster
       - Condition
       - Container
       - Mobile Device
       - Node
       - Subnet
       - Rack
   * - Container
     - Grouping object which can contain nodes, subnets, clusters, conditions,
       or other containers. With help of container objects you can build
       object's tree which represents logical hierarchy of IT services in your
       organization.
     - - Cluster
       - Condition
       - Container
       - Mobile Device
       - Node
       - Subnet
       - Rack
   * - Condition
     - Object representing complicated condition – like "cpu on node1 is
       overloaded and node2 is down for more than 10 minutes". Conditions may
       represent more complicated status checks because each condition can have
       a script attached. Interval for evaluation of condition status is
       configured in Server Configuration Variables as ConditionPollingInterval
       with default value 60 seconds.
     -
   * - Template Root
     - Abstract object representing root of your template tree.
     - - Template
       - Template Group
   * - Template Group
     - Grouping object which can contain templates or other template groups.
     - - Template
       - Template Group
   * - Template
     - Data collection template. See Data Collection section for more
       information about templates.
     - - Mobile Device
       - Node
   * - Network Map Root
     - Abstract object representing root of your network map tree.
     - - Network Map
       - Network Map Group
   * - Network Map Group
     - Grouping object which can contain network maps or other network map
       groups.
     - - Network Map
       - Network Map Group
   * - Network Map
     - Network map.
     -
   * - Dashboard Root
     - Abstract object representing root of your dashboard tree.
     - - Dashboard
   * - Dashboard
     - Dashboard. Can contain other dashboards.
     - - Dashboard
   * - Business Service Root
     - Abstract object representing root of your business service tree. System
       can have only one object of this class.
     - - Business Service
   * - Business Service
     - Object representing single business service. Can contain other business
       services, node links, or service checks.
     - - Business Service
       - Node Link
       - Service Check
   * - Node Link
     - Link between node object and business service. Used to simplify creation
       of node-related service checks.
     - - Service Check
   * - Service Check
     - Object used to check business service state. One business service can
       contain multiple checks.
     -
   * - Rack
     - Object representing rack(works like container)
     - - Node

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

Unmanaged status
----------------

Objects can be unmanaged. In this status object is not polled, DCIs are not collected,
no data is updated about object. This status can be used to store data about object
that temporary or at permanently unavailable or not managed.

.. _maintenance_mode:

Maintenance mode
------------------

This is special status, because it is not included in usual status lit. This
status prevents event processing for special node. While this status node is
still polled and DCI data is still collected, but no event is generated.

Event Processing
================

|product_name| is event based monitoring system. Events can come from different sources
(polling processes (status, configuration, discovery, and data collection), :term:`SNMP`
traps, and directly from external applications via client library.)
and all are forwarded to |product_name| Event Queue. All events are processed by |product_name|
Event Processor one-by-one, according to the processing rules defined in
:term:`Event Processing Policy<EPP>`. As a result of event processing, preconfigured
actions can be executed, and/or event can be shown up as :term:`alarm <Alarm>`.

Usually alarm represents something that needs attention of network administrators
or network control center operators, for example low free disk space on a server.
|product_name| provides one centralized location, the Alarm Browser, where the alarms are
visible. It can be configured which events should be considered
important enough to show up as alarm.

.. figure:: _images/event_flow.png

   Event flow inside the monitoring system

.. _concepts_polling:

Polling
=======

For some type of objects |product_name| server start gathering status and configuration information
as soon as they are added to the system. These object types are: nodes, conditions,
clusters, business services. This process called *polling*. There are multiple polling
types, usually performed with different intervals:

+--------------------+----------------------------------------------------------------------------------------------+
| Type               | Purpose                                                                                      |
+====================+==============================================================================================+
| Status             | Determine current status of an object                                                        |
+--------------------+----------------------------------------------------------------------------------------------+
| Configuration      | Determine current configuration of an object (list of interfaces, supported protocols, etc.) |
+--------------------+----------------------------------------------------------------------------------------------+
| Topology           | Gather information related to network topology                                               |
+--------------------+----------------------------------------------------------------------------------------------+
| Discovery          | Find potential new nodes during network discovery cycles                                     |
+--------------------+----------------------------------------------------------------------------------------------+
| Routing            | Gather information about IP routing                                                          |
+--------------------+----------------------------------------------------------------------------------------------+
| Instance Discovery | Verify all DCIs created by instance discovery process                                        |
+--------------------+----------------------------------------------------------------------------------------------+
| Network Discovery  | Searches for new nodes                                                                       |
+--------------------+----------------------------------------------------------------------------------------------+

.. _basic-concepts-dci:

Data Collection
===============

From each node |product_name| can collect one or more :term:`metrics <Metric>` which
can be either single-value ("CPU.Usage"), or table ("FileSystem.Volumes").
When new data sample is collected, it's value is checked against configured
thresholds. This documentation use term :term:`Data Collection Item <DCI>`
to describe configuration of metric collection schedule, retention, and thresholds.

Metrics can be collected from multiple data sources:

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Source
     - Description
   * - Internal
     - Metrics internal to the server (server statistics, etc.)
   * - |product_name| Agent
     - Data is collected from |product_name| agent, which should be installed
       on target node. Server collect data from agent based on schedule.
   * - SNMP
     - SNMP transport will be used. Server collect data based on schedule.
   * - Push
     - Values are pushed by external system (using `nxpush` or API).
   * - SM-CLP
     -
   * - Windows Performance counters
     -
   * - Check Point SNMP
     -
   * - Script
     - Value is generated by NXSL script. Script should be stored in
       :guilabel:`Script Library`.


Discovery
=========

Network discovery
-----------------

|product_name| can detect new devices and servers on the network and automatically
create node objects for them. Two modes are available – passive and active.

In passive mode server will use only non-intrusive methods by querying ATP and
routing tables from known devices. Tables from the server running |product_name| are
used as seed for passive discovery.

In active mode server will periodically scan configured address ranges using
ICMP echo requests in addition to passive scan methods.

Instance discovery
------------------

|product_name| can create parameters for :term:`Data Collection Item <DCI>` automatically.
Instance discovery collects information about node instances like disk mountpoints,
device list, etc. and automatically creates or removes :term:`DCIs <DCI>` with
obtained data.


Security
========

All communications are encrypted using either AES-256, AES-128, or Blowfish and
authenticated. As additional security measure, administrator can restrict list
of allowed ciphers.

Agent authenticate incoming connections using IP white list and optional
preshared key.

User passwords (if internal database is used) as hashed with salt with SHA-256.

All shared secrets and passwords stored in the system can be obfuscated
to prevent snooping.
