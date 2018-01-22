.. _icmp-ping:

=========
ICMP ping
=========

This subagent can be used to measure ICMP ping response times from one location to another. 
There are two types of metrics: offline collected and offline collected. 
Oflline collected metrics:
    * ICMP.AvgPingTime 
    * ICMP.LastPingTime
    * ICMP.PacketLoss
    * ICMP.PingStdDev
    
Online metric:
    * Icmp.Ping
    
Offline metric targets can be configured in agent configuration file or agent will create new 
target automatically on first request. Automatically created targets will return 0 as a result 
on the firs request.

.. versionadded:: 2.2.2
    Automatic target configuration in PING subagent

Metrics
=======

When loaded, PING subagent adds the following parameters to agent:

+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Parameter                             | Description                                                                                         |
+=======================================+=====================================================================================================+
| Icmp.AvgPingTime(*target*)            | Average ICMP ping response time from *target* for last minute. Argument *target* can be either      |
|                                       | IP address or name specified in Target configuration record (see below).                            |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.LastPingTime(*target*)           | Last ICMP ping response time from *target*. Argument *target* can be either IP address or name      |
|                                       | specified in Target configuration record (see below).                                               |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.PacketLoss(*target*)             | ICMP ping packet loss (in percents) for *target*. Argument *target* can be either IP address or     |
|                                       | name specified in Target configuration record (see below).                                          |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.Ping(*target*,*timeout*,*psize*) | ICMP ping response time from *target*. Agent will send echo request as soon as it receives          |
|                                       | request for paramter's value, and will return response time for that particular request. Argument   |
|                                       | *target* should be an IP address. Optional argument *timeout* specifies timeout in milliseconds.    |
|                                       | Default timeout is 1 second. Optional argument *psize* specifies packet size in bytes, including    |
|                                       | IP header. If this argument is omitted, value from DefaultPacketSize configuration parameter        |
|                                       | will be used.                                                                                       |
|                                       | Please note that other parameters just returns result of background ping process, while this        |
|                                       | parameter waits for actual ping completion and then returns the result. Because of this behavior,   |
|                                       | it is not recommended to use **Icmp.Ping** parameter for instant monitoring, only for               |
|                                       | occasional tests. For instant monitoring, you should configure targets for background ping and use  |
|                                       | **Icmp.AvgPingTime** or **Icmp.LastPingTime** parameters to retrieve results.                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.PingStdDev(*target*)             | [http://en.wikipedia.org/wiki/Standard_deviation Standard deviation] of ICMP ping response time for |
|                                       | *target*. Argument *target* can be either IP address or name specified in Target configuration      |
|                                       | record (see below).                                                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+


Metric Tables
=============

+-----------------+---------------------------------------------+
| Table           | Description                                 |
+=================+=============================================+
| Icmp.Targets    | Table of configured ping targets. Contains: |
|                 | * IP address                                |
|                 | * Last response time (milliseconds)         |
|                 | * Average response time (milliseconds)      |
|                 | * Packet loss (percents)                    |
|                 | * Configured packet size                    |
|                 | * Name                                      |
|                 | * DNS name                                  |
|                 | * Automatic                                 |
+-----------------+---------------------------------------------+

Metric Lists
============

+-----------------+---------------------------------------+
| List            | Description                           |
+=================+=======================================+
| Icmp.Targets    | List of configured ping target names. |
+-----------------+---------------------------------------+

Configuration file
==================  

All configuration parameters related to PING subagent should be placed into **\*PING** section of agent's configuration file.
The following configuration parameters are supported:

+-------------------+---------------------+----------------------------------------------------------------------------------------+---------------+
| Parameter         | Format              | Description                                                                            | Default value |
+===================+=====================+========================================================================================+===============+
| DefaultPacketSize | *bytes*             | Set default packet size to *bytes*.                                                    | 46            |
+-------------------+---------------------+----------------------------------------------------------------------------------------+---------------+
| PacketRate        | *packets*           | Set ping packet rate per minute.  Allowed values are from 1 to 60 and values below or  | 4             |
|                   |                     | above will be adjusted automatically.                                                  |               |
+-------------------+---------------------+----------------------------------------------------------------------------------------+---------------+
| Target            | *ip*:*name*:*psize* | Add target with IP address *ip* to background ping target list and assign an optional  | *none*        |
|                   |                     | name *name* to it. Target will be pinged using packets of *psize* bytes size. Name     |               |
|                   |                     | and packet size fields are optional and can be omitted. This parameter can be given    |               |
|                   |                     | multiple times to add multiple targets.                                                |               |
+-------------------+---------------------+----------------------------------------------------------------------------------------+---------------+
| Timeout           | *milliseconds*      | Set response timeout to *milliseconds*. Allowed values are from 500 to 5000 and values | 3000          |
|                   |                     | below or above will be adjusted automatically.                                         |               |
+-------------------+---------------------+----------------------------------------------------------------------------------------+---------------+


Configuration example:

.. code-block:: cfg

   # This sample nxagentd.conf instructs agent to:
   #   1. load PING subagent
   #   2. Ping target 10.0.0.1 with default size (46 bytes) packets and 10.0.0.2 with 1000 bytes packets
   #   3. Timeout for ping set to 1 second and pings are sent 12 times per minute (each 5 seconds)

   MasterServers = netxms.demo
   SubAgent = ping.nsm

   *PING
   Timeout = 1000
   PacketRate = 12
   Target = 10.0.0.1:target_1
   Target = 10.0.0.2:target_2:1000

.. note::
  PING subagent uses value of 10000 to indicate timed out requests.
