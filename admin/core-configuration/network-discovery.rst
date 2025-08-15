.. _network-discovery:

#################
Network discovery
#################

Introduction
============

|product_name| is capable of discovering your network automatically. The network discovery
module can operate in two modes: passive and active.

In passive mode
information about new hosts and devices are obtained from :term:`ARP` tables and
routing tables of already known devices. |product_name| starts with its own
:term:`ARP` cache and routing table.

In active discovery mode the |product_name| server will send an :term:`ICMP` echo
request to all IP addresses in the given range and consider each responding
address for adding to database. If zoning is used the server sends an echo request
only in zone 0. In other zones requests are sent by proxies. For each new device
the |product_name| server tries to gather additional information using the
:term:`SNMP` and |product_name| agent and then adds it to database. By default
the |product_name| server will add all discovered devices to database, but you can
limit it by using discovery filters. Default :term:`SNMP` credentials can be set
in :ref:`default_snmp`.

The default intervals are 2 hours for active discovery and 15 minutes for passive
discovery. These values can be changed in the Network Discovery configuration.
The number of discovery poller threads changes dynamically and is defined by the server
configuration parameters  ``ThreadPool.Discovery.BaseSize`` and
``ThreadPool.Discovery.MaxSize``. More information about server configuration
parameters can be found at :ref:`here <server_configuration_parameters>`.

Configuring Network Discovery
=============================

To change network discovery settings, go to the main menu of the management client and
choose :menuselection:`Configuration --> Network Discovery`. The configuration form
will open:

.. figure:: ../_images/network_discovery_config.png

General
-------

In this section, you can choose the network discovery mode and choose if the source node of
:term:`SNMP Trap` or syslog source address should be used for discovery.

Schedule
--------

For passive discovery the interval (in seconds) is selected.
For active discovery you cen choose either an interval (in seconds) or a cron
format schedule. See :ref:`here <cron_format>` for more details.

Filter
------

In this section, you can define a filter for adding new nodes to |product_name| database.
Available filtering options are:

**No filtering**

Any new device found will be added to the database. This is the default setting.

**Custom script**

You can choose a :term:`NXSL` script from the :guilabel:`Script Library` to work
as a discovery filter. This custom filtering script will get an object of class
``NewNode`` as its first parameter (special variable ``$1``), and should return
true to allow node inclusion into database.

**Automatically generated script**

This option can be used if you need only simple filtering. When selected,
additional options control what nodes will be added to database:

.. list-table::

   * - Accept node if it has |product_name| agent
     - If checked, only nodes with |product_name| agent detected will pass the filter.
   * - Accept node if it has SNMP agent
     - If checked, only nodes with SNMP agent detected will pass the filter.
   * - Accept node if it is within given range or subnet
     - Only accept nodes within given address range or subnet. Address ranges
       can be configured in :guilabel:`Address Filters` section.


Please note that the first two options (|product_name| agent presence and SNMP agent
presence) forms ``OR`` condition - if both are checked, any node with either
SNMP agent or |product_name| agent will pass. Whereas the address range check and the first two options
forms ``AND`` condition - so if a node does pass the agent presence check,
but is not in an allowed IP address range, it will not be accepted. In other
words, if all three options are checked, the condition for a new node to pass filter
can be written as following:

  **if** (node has |product_name| agent **or** node has SNMP agent) **and** node within given range **then** pass


Active Discovery Targets
------------------------

In this section you can define address ranges for active discovery. The |product_name|
server will periodically send ICMP echo requests to these addresses, and
consider every responding device for addition to the database. This list has no
effect if active discovery is off.


Address Filters
---------------

In this section you can define address ranges for the automatically generated
discovery filter. This list has no effect if discovery is off or the filter is not
set to :guilabel:`Automatically generated script`.
