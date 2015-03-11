.. _snmp:

####
SNMP
####


MIB browser
===========



Drivers
=======


Setting default SNMP credentials
================================


MIB Explorer
============

MIB browser shows all loaded MIB configurations, and allows to run :term:`SNMP` 
walk on a selected node :term:`nodes <Node>`. Node can be selected in browser 
by selecting :guilabel:`Set node object...` option in view menu. 

To run walk user should select line of tree from were will be requested all data. 
By walk will be requested all subtree OIDs. 

After walk is done it's results will shown in the table below.

.. todo::
  add immage and describe posibility to show line in mib configuration by value and
  add dci by value

Using ifTable and ifXTable
==========================

Configure SNMP Proxy
====================


Configure SNMP Trap Proxy
=========================

It is possible to proxy SNMP traps. 

In this case as a destination of traps should be set the proxy node.

Agent configuration
-------------------

To enable trap proxy "EnableSNMPTrapProxy" parameter should be set to "yes".

Optionally can be configured also "SNMPTrapListenAddress" and "SNMPTrapPort". 
Default values can be checked there: :ref:`master-configuration-file-label`

Server configuration
--------------------

By default traps are accepted only from known nodes. To accept all traps
set "LogAllSNMPTraps" server configuration variable to 1. 

To correctly send response for SNMPv3, it should be also configured 
the proxy node for the sender node. It is done in sender node 
properties in "Communications" tab, SNMP section. 

Import MIB
==========

MIB files (MIBs) describe structure of information transferred via SNMP. 
Every device can support multiple MIBs, some of them are standard and 
public, other can be proprietary and vendor specific. NetXMS uses compiled 
MIBs to allow you to select OID and see its description (for example when 
selecting SNMP data for DCI collection). You do not need to compile new 
MIBs if you are OK with direct input of OID.

Compiling MIBs
--------------

 - Change suffix of your new MIB file to .txt
 - Copy your MIB file to /usr/share/netxms/mibs
 - Use nxmibc binary to create a new compiled MIB file from all MIBs in directory. 
   Add parameter -z for compressed output file.
   
.. codeblock::

  nxmibc -d /usr/share/netxms/mibs -o /usr/share/netxms/mibs/netxms.mib
  
Parameters recognized by nxmibc:

.. codeblock::

  nxmibc [options] source1 ... sourceN

  Valid options:
    -d <dir>  : Include all MIB files from given directory to compilation
    -o <file> : Set output file name (default is netxms.mib)
    -P        : Pause before exit
    -s        : Strip descriptions from MIB objects
    -z        : Compress output file
    
Troubleshooting
---------------

If nxmibc fails, it may be caused by syntax or import errors in your MIB. 
Try to check it with smilint (part of net-snmp package) and correct any 
errors on level 3.
