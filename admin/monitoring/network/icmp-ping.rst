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
the server configuration parameter ``ICMP.CollectPollStatistics`` or locally on each
node. The ICMP polling interval and statistic calculation period (expressed in
number of polls), timeout and ICMP packet size are configured via server
configuration parameters. See for more details :ref:`server_configuration_parameters`.

ICMP requests are sent to the primary IP address of the node. Additional targets
can be specified in the node properties. It is also possible to set interfaces
of the node as targets by enabling :guilabel:`Collect ICMP response statistic
for this interface` in the properties of the interface. Please note that
enabling this for the interface that corresponds to the primary IP address will
lead to pinging this address twice.

ICMP polling is performed either from the server, from a zone proxy if zoning is
used, or from a specific proxy when this is configured in the node properties.
The proxying agent should have the ``ping.nsm`` subagent enabled.

The results of the ICMP response statistic collection for primary IP address are
visible in :guilabel:`Object Details -> Overview` and are available as internal
metrics:

* ICMP.Jitter
* ICMP.PacketLoss
* ICMP.ResponseTime.Average
* ICMP.ResponseTime.Last
* ICMP.ResponseTime.Max
* ICMP.ResponseTime.Min

The results of the ICMP response statistic collection for additional targets and
interfaces are available as internal metrics:

* ICMP.Jitter(*)
* ICMP.PacketLoss(*)
* ICMP.ResponseTime.Average(*)
* ICMP.ResponseTime.Last(*)
* ICMP.ResponseTime.Max(*)
* ICMP.ResponseTime.Min(*)

For example, the ``ICMP.PacketLoss(8.8.8.8)`` internal metric will provide packet
loss for the target with IP address 8.8.8.8.

No historical data is stored by default. It is necessary to configure DCIs using
the above mentioned internal metric to store historical data.


Ping subagent
=============

This subagent can be used to measure ICMP ping response times from one location
to another. When loaded, the PING subagent adds a number of metrics to the agent.
Measurements can be either requested by the server or scheduled by the agent
itself.


Metrics requested by the server
-------------------------------

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Metric
     - Description
   * - Icmp.Ping(*target*, *timeout*, *psize*, *dontfragmentflag*, *retrycount*)
     - ICMP ping response time from *target*. Agent will send echo request as
       soon as it receives request for the value of the metric, and will return
       the response time for that particular request.

       Arguments:

       * *target* should be an IP address or hostname.

       * *timeout* specifies timeout in milliseconds. This is an optional argument.
         If omitted, the value from the *Timeout* configuration parameter will be used.

       * *psize* specifies the packet size in bytes including the IP header. This is
         an optional argument. If omitted, the value from the *DefaultPacketSize*
         configuration parameter will be used.

       * *dontfragmentflag* defines if the don't fragment flag is set in ICMP
         requests. This is an optional argument. If omitted, the value from the
         DefaultDoNotFragmentFlag configuration parameter will be used.

       * *retrycount* defines the number of retries. This is an optional argument. If
         omitted, a default value of 1 is used.

       Please note that while metrics scheduled by the agent just return the result of
       the background ping process, this metric waits for actual ping completion and
       then returns the result. Because of this behavior, it is not recommended
       to use the **Icmp.Ping** metric for regular monitoring but instead only for
       occasional tests. For instant monitoring, you should configure targets
       for background ping and use the **Icmp.AvgPingTime** or **Icmp.LastPingTime**
       metrics to retrieve results.


Metrics scheduled by the agent
------------------------------

There is a number of metrics that are collected based on the background ping process
scheduled by the agent (based on the "PacketRate" parameter).

Targets for these metrics can be either defined in the agent configuration file
(using one or more "Target" parameters), or registered automatically on first
request from server. If targets are registered automatically, the default packet
size is used. The first request to a non-existing target will return "0" as a value.
Automatically registered targets are automatically removed after a timeout, when
the server stops requesting metrics for that target.


Single-value metrics
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Metric
     - Description
   * - Icmp.AvgPingTime(*target*)
     - Average ICMP ping response time from *target* for the last minute. The argument
       *target* can be either an IP address or a name specified in the Target
       configuration record (see below).
   * - ICMP.MovingAvgPingTime(*target*)
     - Moving average of response time from *target*. Time period for moving
       average calculation is set by the `MovingAverageTimePeriod` agent
       configuration parameter (see below).
   * - Icmp.LastPingTime(*target*)
     - Last ICMP ping response time from *target*.
   * - ICMP.MaxPingTime(*target*)
     - Maximum ICMP ping response time from *target* for the last minute.
   * - ICMP.MinPingTime(*target*)
     - Minimum ICMP ping response time from *target* for the last minute.
   * - ICMP.CumulativeMaxPingTime(*target*)
     - Maximum encountered ICMP ping response time from *target* since that
       target was added.
   * - ICMP.CumulativeMinPingTime(*target*)
     - Minimum encountered ICMP ping response time from *target* since that
       target was added.
   * - Icmp.PacketLoss(*target*)
     - ICMP ping packet loss (in percents) for *target* for the last minute.
   * - Icmp.PingStdDev(*target*)
     - :wikipedia:`Standard deviation <Standard deviation>` of the response time
       for the *target* for last minute.
   * - ICMP.Jitter(*target*)
     - :wikipedia:`Jitter <Jitter>` of ICMP ping response time from *target* for
       last minute.
   * - ICMP.MovingAvgJitter(*target*)
     - Moving average of response time jitter from *target*. Time period for
       moving average calculation is set by `MovingAverageTimePeriod` agent
       configuration parameter (see below).


Tables
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - Table
     - Description
   * - Icmp.Targets
     - Table of configured ping targets. Columns:

       * IP address
       * Last response time (milliseconds)
       * Average response time (milliseconds)
       * Minimal response time (milliseconds)
       * Maximum response time (milliseconds)
       * Moving average response time (milliseconds)
       * Standard deviation of response time (milliseconds)
       * Jitter of response time (milliseconds)
       * Moving average jitter of response time (milliseconds)
       * Cumulative minimal response time (milliseconds)
       * Cumulative maximum response time (milliseconds)
       * Packet loss (percents)
       * Configured packet size
       * Name
       * DNS name
       * Automatic


Lists
~~~~~

.. list-table::
   :header-rows: 1
   :widths: 36 64

   * - List
     - Description
   * - Icmp.Targets
     - List of configured ping target names


Configuration file
------------------

All configuration parameters related to the PING subagent should be placed into
**[PING]** section of the configuration file of the agent. The following configuration
parameters are supported:


.. list-table::
   :header-rows: 1
   :widths: 30 15 45 10

   * - Parameter
     - Format
     - Description
     - Default value
   * - AutoConfigureTargets
     - *boolean*
     - Allow automatic registration of ICMP targets when the metrics for a new
       target are requested from the server.
     - yes
   * - DefaultDoNotFragmentFlag
     - *boolean*
     - Default value for the Don't Fragment flag in ICMP requests.
     - no
   * - DefaultPacketSize
     - *bytes*
     - Set default packet size to *bytes*.
     - 46
   * - MaxTargetInactivityTime
     - *seconds*
     - Timeout to remove an automatically registered ICMP target if the server stops
       requesting metrics for that target.
     - 86400
   * - MovingAverageTimePeriod
     - *seconds*
     - Set time period used for the moving average value calculation.
     - 3600
   * - PacketRate
     - *packets*
     - Set ping packet rate per minute.  Allowed values are between 1 and 60 and
       values below or above will be adjusted automatically.
     - 4
   * - Target
     - *ip*:*name*:*psize*
     - Add target with IP address *ip* to the background ping target list and assign
       an optional name *name* to it. The target will be pinged using packets of
       *psize* bytes. The name and packet size fields are optional and can be
       omitted. This parameter can be given multiple times to add multiple
       targets.
     - *none*
   * - ThreadPoolMaxSize
     - *threads*
     - Maximal number of threads in the thread pool of the agent that is serving
       scheduled ICMP measurements.
     - 1024
   * - ThreadPoolMinSize
     - *threads*
     - Minimal number of threads in the thread pool of the agent that is serving
       scheduled ICMP measurements.
     - 1
   * - Timeout
     - *milliseconds*
     - Set response timeout to *milliseconds*. Allowed values are between 500 and
       5000 and values below or above will be adjusted automatically.
     - 3000


Configuration example:

.. code-block:: ini

   # This sample nxagentd.conf instructs agent to:
   #   1. load the PING subagent
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
  Response time of 10000 indicates timeout
