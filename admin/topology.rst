.. _topology:


################
Network topology
################

Introduction
============

|product_name| server automatically creates and maintains network model on different
layers. All necessary information taken from ARP cache, routing tables, and
switch forwarding database of managed nodes. Topology data provided by CDP,
LLDP, and NDP (SONMP) protocols also used in building network model. Having
network model instantly available allows |product_name| users to perform various
network topology tasks much faster and easier.


How topology information is built
=================================


Find where node is connected
============================

It is possible to find switch port where any given node is connected (sometimes
called "connection point" in management console). To find out node's connection
point, right-click on node object, and select :guilabel:`Find switch port` in
pop-up menu. Message box with search results will pop up, and if port is found,
search results view will be opened (or updated if already open). Search results
view looks like this:

.. figure:: _images/Cp_search_results.png
   :scale: 70


Columns have the following meaning:

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Seq.
     - Search result sequence number
   * - Node
     - Name of end node object
   * - Interface
     - Name of node's interface object
   * - MAC
     - Interface's MAC address
   * - IP
     - Interface's IP address
   * - Switch
     - Name of switch node object
   * - Port
     - Name of interface object representing switch port
   * - Type
     - Connection type - direct or indirect. Direct connection type means that
       |product_name| server did not detect any other devices on same switch port, and
       most likely end node connected directly to the switch. Indirect means
       that some other devices was detected on same switch port. Virtual
       machines and virtual machine host will always be detected as indirect.


Find MAC address
================

It is possible to find location of any known MAC address in the network. To do
this, select :menuselection:`Tools --> Find MAC address`. Results of a search
will be displayed in the same results view. It is not necessary that node with
given MAC address be managed by |product_name| server, but if it is, appropriate
details will be displayed.


Find IP address
===============

It is possible to find location of any known IP address in the network. To do
this, select :menuselection:`Tools --> Find IP address`. Results of a search
will be displayed in the same results view. It is not necessary that node with
given IP address be managed by |product_name| server, but if it is, appropriate details
will be displayed.
