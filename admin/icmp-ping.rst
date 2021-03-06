.. _icmp-ping:

=========
ICMP ping
=========

The following options exist to monitor systems using ICMP pings:

* ICMP response statistic collection
* Metrics provided by ping subagent


ICMP response statistic collection
==================================

|product_name| can periodically perform ICMP polls and calculate node
availability statistics. This functionality can be controlled globally via
server configuration parameter ``ICMP.CollectPollStatistics`` or locally on each
node. ICMP polling interval and statistic calculation period (expressed in
number of polls), timeout and ICMP packet size are configured via server
configuration parameters, see :ref:`server_configuration_parameters`.

ICMP requests are sent to node's primary IP address. Additional targets can be
specified in node's properties. It's also possible to set node's interfaces as
targets by enabling :guilabel:`Collect ICMP response statistic for this
interface` in properties of the interface (enabling this for interface that
corresponds to primary IP address will lead to pinging this address twice).

ICMP polling is performed from server, from a zone proxy if zoning is used or
from specific proxy if it's configured in node properties. Proxying agent should
have ``ping.nsm`` subagent enabled.

Results of ICMP response statistic collection for primary IP address are visible
in :guilabel:`Object Details -> Overview` and are available as internal
parameters:

* ICMP.ResponseTime.Average
* ICMP.PacketLoss
* ICMP.ResponseTime.Last
* ICMP.ResponseTime.Max
* ICMP.ResponseTime.Min

Results of ICMP response statistic collection for additional targets and
interfaces are available as internal parameters:

* ICMP.ResponseTime.Average(*)
* ICMP.PacketLoss(*)
* ICMP.ResponseTime.Last(*)
* ICMP.ResponseTime.Max(*)
* ICMP.ResponseTime.Min(*)

For example, ``ICMP.PacketLoss(8.8.8.8)`` parameter will provide packet loss for
target with IP address 8.8.8.8.

No historical data is stored by default. It's necessary to configure DCIs using
above mentioned internal parameters to store historical data.

Ping subagent
=============

This subagent can be used to measure ICMP ping response times from one location
to another. Measurements can be either scheduled by the agent itself or
requested by the server.

Metrics scheduled by the agent (based on "PacketRate" parameter):

* ICMP.AvgPingTime
* ICMP.LastPingTime
* ICMP.PacketLoss
* ICMP.PingStdDev

These metrics can be either defined in agent configuration file (using one or
more "Target" parameters), or registered automatically on first request from
server. If targets are registered automatically, default packet size is used.
First request to non-existing target will return "0" as a value. Automatically
registered targets are automatically removed after a timeout, if server stops
requesting metrics for that target.


Metrics available on demand:

* ICMP.Ping

Metrics
-------

When loaded, PING subagent adds the following parameters to agent:

+-----------------------------------------+-----------------------------------------------------------------------------------------------------+
| Parameter                               | Description                                                                                         |
+=========================================+=====================================================================================================+
| Icmp.AvgPingTime(*target*)              | Average ICMP ping response time from *target* for last minute. Argument *target* can be either      |
|                                         | IP address or name specified in Target configuration record (see below).                            |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.LastPingTime(*target*)             | Last ICMP ping response time from *target*. Argument *target* can be either IP address or name      |
|                                         | specified in Target configuration record (see below).                                               |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.PacketLoss(*target*)               | ICMP ping packet loss (in percents) for *target* for last minute. Argument *target* can be either   |
|                                         | IP address or name specified in Target configuration record (see below).                            |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.Ping(*target*, *timeout*, *psize*) | ICMP ping response time from *target*. Agent will send echo request as soon as it receives          |
|                                         | request for parameter's value, and will return response time for that particular request. Argument  |
|                                         | *target* should be an IP address. Optional argument *timeout* specifies timeout in milliseconds.    |
|                                         | Default timeout is 1 second. Optional argument *psize* specifies packet size in bytes, including    |
|                                         | IP header. If this argument is omitted, value from DefaultPacketSize configuration parameter        |
|                                         | will be used.                                                                                       |
|                                         |                                                                                                     |
|                                         | Please note that other parameters just return result of background ping process, while this         |
|                                         | parameter waits for actual ping completion and then returns the result. Because of this behavior,   |
|                                         | it is not recommended to use **Icmp.Ping** parameter for instant monitoring, only for               |
|                                         | occasional tests. For instant monitoring, you should configure targets for background ping and use  |
|                                         | **Icmp.AvgPingTime** or **Icmp.LastPingTime** parameters to retrieve results.                       |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------+
| Icmp.PingStdDev(*target*)               | :wikipedia:`Standard deviation <Standard deviation>` of the response time for the                   |
|                                         | *target* for last minute. Argument *target* can be either IP address or name specified in Target    |
|                                         | configuration record (see below).                                                                   |
+-----------------------------------------+-----------------------------------------------------------------------------------------------------+


Tables
------

+-----------------+---------------------------------------------+
| Table           | Description                                 |
+=================+=============================================+
| Icmp.Targets    | Table of configured ping targets. Columns:  |
|                 |                                             |
|                 | * IP address                                |
|                 | * Last response time (milliseconds)         |
|                 | * Average response time (milliseconds)      |
|                 | * Packet loss (percents)                    |
|                 | * Configured packet size                    |
|                 | * Name                                      |
|                 | * DNS name                                  |
|                 | * Automatic                                 |
+-----------------+---------------------------------------------+

Lists
-----

+-----------------+---------------------------------------+
| List            | Description                           |
+=================+=======================================+
| Icmp.Targets    | List of configured ping target names. |
+-----------------+---------------------------------------+

Configuration file
------------------

All configuration parameters related to PING subagent should be placed into **[PING]** section of agent's configuration file.
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

   [PING]
   Timeout = 1000
   PacketRate = 12 # every 5 seconds
   Target = 10.0.0.1:target_1
   Target = 10.0.0.2:target_2:1000

.. note::
  Response time of 10000 indicate timeout
