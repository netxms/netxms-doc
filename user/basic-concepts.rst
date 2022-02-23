##############
Basic Concepts
##############

.. _concept_object:

Objects
=======

All monitored network infrastructure is represented as a set of :term:`objects <Object>`
in |product_name| monitoring system. Each object
represents one physical or logical entity (e.g. host or network interface),
or group of them (e.g. subnet, container). Objects are organized into hierarchical structure.
Each object has it's own access rights. Access rights are applied
hierarchically on all children of object. For example if :guilabel:`Read`
access right is granted to a user on a :guilabel:`Container`, then user has :guilabel:`Read`
right on all objects that this :guilabel:`Container` contains.
Every object has set of attributes; some of them exist for all objects
(like :guilabel:`id` and :guilabel:`name` or :guilabel:`status`),  while other
depend on object class – for example, only :guilabel:`Node` objects have
attribute :guilabel:`SNMP community string`. There are default attributes
and custom attributes defined either by user or external application via
|product_name| API.

|product_name| has six top level objects – ``Entire Network``,
``Service Root`` (named "Infrastructure Services" after system installation),
``Template Root``, ``Network Map Root``, ``Dashboard Root`` and
``Business Service Root``. These objects serve as an
abstract root for an appropriate object tree. All top level objects have only one
editable attribute – name.


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
     - Object representing IP subnet. Typically objects of this class are created
       automatically by the system to reflect system's knowledge of IP
       topology. The system places Node objects inside an appropriate Subnet
       object based on an interface configuration. Subnet objects have only one
       editable attribute - :guilabel:`Name`.
     - - Node
   * - Node
     - Object representing physical host or network device (such as a router or network switch).
       These objects can be created either manually by administrator or automatically during
       network discovery process. They have a lot of attributes controlling all aspects
       of interaction between |product_name| server and managed node. For example, the attributes
       specify what data must be collected, how node status must be checked, which protocol
       versions to use, etc. Node objects contain one or more interface objects. The system
       creates interface objects automatically during configuration polls.
     - - Interface
       - Access point
       - Network Service
       - VPN Connector
   * - Interface
     - Interface objects represent network interfaces of managed computers and
       devices. These objects created automatically by the system during
       configuration polls or can be created manually by user.
     -
   * - Access point
     - Object representing wireless network access point. A node can have
       several access points, e.g. 2.4Ghz and 5Ghz, or in case of thin wireless
       access points managed by a central controller. These objects are created
       automatically by the system.
     -
   * - Network Service
     - Object representing network service running on a node (like http or
       ssh), which is accessible online (via TCP IP). Network Service objects
       are always created manually. Currently, the system works with the following
       protocols - HTTP, POP3, SMTP, Telnet, SSH and Custom protocol type.
     -
   * - VPN Connector
     - Object representing VPN tunnel endpoint. Such objects can be created to
       add VPN tunnels to network topology known to |product_name| server. VPN Connector
       objects are created manually. In case if there is a VPN
       connection linking two different networks open between two firewalls that are
       added to the system as objects, a user can create a VPN Connector object on
       each of the firewall objects and link one to another. The network topology will
       now show that those two networks are connected and the system will take this
       condition into account during problem analysis and event correlation.
     -
   * - Service Root
     - Abstract object representing root of your infrastructure service tree.
       System can have only one object of this class. After system installation
       it is named "Infrastructure Services".
     - - Cluster
       - Chassis
       - Condition
       - Container
       - Node
       - Sensor
       - Subnet
       - Rack
   * - Container
     - Grouping object which can contain any type of objects that Service Root
       can contain. With help of container objects you can build
       object's tree which represents logical hierarchy of IT services in your
       organization.
     - - Cluster
       - Chassis
       - Condition
       - Container
       - Node
       - Sensor
       - Subnet
       - Rack
   * - Cluster
     - Object representing cluster consisting of two or more nodes. 
     - - Node
   * - Rack
     - Object representing a rack. It has the same purpose as container, but
       allows to configure visual representation of equipment installed in a rack.
     - - Node
       - Chassis
   * - Chassis
     - Object representing a chassis, e.g. a blade server enclosure. Chassis
       can be configured as a part of a rack.
     - - Node
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
     - Data collection template. 
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
       - Business Service Prototype
   * - Business Service
     - Object representing single business service. Can contain other business
       services or business service prototypes. 
     - - Business Service
       - Business Service Prototype
   * - Business Service Prototype
     - Prototype from which business service objects are automatically populated. 
     - 

Object status
-------------

Each object has a status. Status of an object calculated based on:

   * Polling results
   * Status of child objects (e.g. interfaces of node, nodes under container)
   * Active alarms, associated with the object (after an alarm is resolved or terminated, it no longer affects object status)
   * Value of status :term:`DCIs<DCI>` (DCI that has ``Use this DCI for node status calculation`` property enabled)

For some object classes, like Report or Template, status is irrelevant. Status for such objects is always :guilabel:`Normal`.
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
no data is updated about object. This status can be used to store data about an object
that is temporary or permanently unavailable or not managed.

.. _maintenance_mode:

Maintenance mode
------------------

This is special status, that's why it is not included in above status list. This
status prevents event processing for specific node. While this node in maintenance
mode is still polled and DCI data is still collected, but no event is generated.

Data Collection Items
=====================

Every node can have many parameters, such as CPU utilization, amount of free
memory or disk space usage. The management server can collect these parameters,
check them for threshold violations and store them in the database. In |product_name|,
parameters configured for collection are called Data Collection Items or DCI
for short. One DCI represents one node's parameter, and unlimited number of
DCIs can be configured for any node.

Thresholds
----------

Each threshold is a combination of a condition and event pair. If a condition
becomes true, associated "activation" event is generated, and when it becomes
false again, "deactivation" event generated. Thresholds let you take a
proactive approach to network management. Thresholds can be defined for any
data collection items that is monitored, more than one threshold for a single
DCI can be defined.

Events and Alarms
=================

Many services within |product_name| gather information and generate events that are
forwarded to |product_name| Event Queue. Events can also be emitted from agents on
managed nodes, or from management applications residing on the management
station or on specific network nodes. All events are processed by |product_name| Event
Processor one-by-one, according to the processing rules defined in Event
Processing Policy. As a result of event processing, some actions can be taken,
and event can be shown up as alarm, sent as e-mail and notifications
(SMS, instant messages). |product_name| provides one
centralized location - the Alarm Browser, where the alarms are visible to your
team. You can control which events should be considered important enough to
show up as alarms. You and your team can easily monitor the posted alarms and
take appropriate actions to preserve the health of your network.

Examples of alarms include:

- A router exceeded its threshold of traffic volume that you configured in Data
  Collection.
- The shell script that you wrote gathered the specific information you needed
  and posted it to the |product_name| as an event.
- One of your mission-critical servers switched to UPS battery power.
- An SNMP agent on a managed critical server forwarded a trap to |product_name| because
  it was overheating and about to fail.

Zones
=====

As |product_name| server keeps track of an IP topology, it is important to maintain the
configuration in which IP addresses do not overlap and that two IP addresses
from same subnet are really within one subnet. Sometimes, however, it is needed
to monitor multiple sites with overlapping IP address ranges. To correctly
handle such situation, zoning must be used. Zone in |product_name| is a group of IP
subnets which form non-overlapping IP address space. There is always zone 0 which
contains subnets directly reachable by management server. For all other zones
server assumes that subnets within that zones are not reachable directly, and
proxy must be used.
