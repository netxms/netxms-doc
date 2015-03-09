.. _snmp:

####
SNMP
####


MIB browser
===========


Drivers
=======


Setting default SNMP credentials
===================================

MIB Explorer
=============

Using ifTable and ifXTable
=============================

Configure SNMP trap Proxy
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