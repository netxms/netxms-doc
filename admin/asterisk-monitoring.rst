.. _asterisk-monitoring:

===================
Asterisk monitoring
===================

|product_name| can be used to monitor health and performance of Asterisk PBX. All monitoring data
collected and provided by subagent **asterisk.nsm**. One agent can collect data from multiple
Asterisk systems.

Configuration
=============

All Asterisk systems should be defined in subagent configuration. For simplified setup for single
system monitoring subagent supports "local" system. Configuration for local system can be
defined in **Asterisk** section of agent configuration file. For each additional system new section
should be created in configuration file named **Asterisk/Systems/SystemName** (*SystemName* should be
replaced with unique name). Each section can have the following parameters:

.. list-table::
   :header-rows: 1
   :widths: 50 200 40

   * - Parameter
     - Description
     - Default value
   * - Hostname
     - DNS name or IP address of Asterisk PBX
     - 127.0.0.1
   * - Login
     - Login name
     - root
   * - Password
     - Password
     - *empty*
   * - Port
     - TCP port number for AMI connection
     - 5038

It is also possible to configure subagent to periodically perform SIP registration tests. Each test
should be configured in separate configuration section named **Asterisk/SIPRegistrationTests/TestName**
for local system and **Asterisk/Systems/SystemName/SIPRegistrationTests/TestName** for other systems.
*SystemName* and *TestName* should be replaced with unique system and test names respectively. Each test
configuration section can have the following parameters:

.. list-table::
   :header-rows: 1
   :widths: 50 200 40

   * - Parameter
     - Description
     - Default value
   * - Domain
     - Domain name used for registration
     - *empty*
   * - Interval
     - Check interval in seconds
     - 300
   * - Login
     - SIP login name
     - netxms
   * - Password
     - SIP password
     - netxms
   * - Proxy
     - SIP proxy
     - sip:*Asterisk IP address*

Configuration Examples
----------------------

Local system without SIP tests:

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = asterisk.nsm

   [Asterisk]
   Login = root
   Password = password1

Local system with two SIP tests:

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = asterisk.nsm

   [Asterisk]
   Login = root
   Password = password1

   [Asterisk/SIPRegistrationTests/104]
   Login = 104
   Password = 12345
   Domain = demo.netxms

   [Asterisk/SIPRegistrationTests/115]
   Login = 115
   Password = 12345
   Domain = demo.netxms
   Interval = 60

Local system and remote system (named **Remote1**) on address 10.0.0.1 with one SIP test each:

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = asterisk.nsm

   [Asterisk]
   Login = root
   Password = password1

   [Asterisk/SIPRegistrationTests/104]
   Login = 104
   Password = 12345
   Domain = demo.netxms

   [Asterisk/Systems/Remote1]
   Hostname = 10.0.0.1
   Login = root
   Password = password1

   [Asterisk/Systems/Remote1/SIPRegistrationTests/120]
   Login = 120
   Password = 12345
   Domain = remote.netxms

Metrics
=======

Single-value metrics
--------------------

All metrics accept system name as first argument. Name for default local system is **LOCAL**.
If system name is omitted local system is assumed. If system name is the only argument braces can be omitted as well.

.. list-table::
   :header-rows: 1
   :widths: 50 10 40

   * - Metric
     - Type
     - Meaning
   * - Asterisk.AMI.Status(*system*)
     - Integer
     - AMI connection status (1 if AMI session is ready, 0 if not)
   * - Asterisk.AMI.Version(*system*)
     - Integer
     - AMI version
   * - Asterisk.Channels.Active(*system*)
     - Integer
     - Number of active channels
   * - Asterisk.Channels.Busy(*system*)
     - Integer
     - Number of busy channels
   * - Asterisk.Channels.Dialing(*system*)
     - Integer
     - Number of dialing channels
   * - Asterisk.Channels.OffHook(*system*)
     - Integer
     - Number of off-hook channels
   * - Asterisk.Channels.Reserved(*system*)
     - Integer
     - Number of reserved channels
   * - Asterisk.Channels.Ringing(*system*)
     - Integer
     - Number of ringing channels
   * - Asterisk.Channels.Up(*system*)
     - Integer
     - Number of up channels
   * - Asterisk.Channels.CurrentCalls(*system*)
     - Integer
     - Number of currently active calls
   * - Asterisk.Events.CallBarred(*system*)
     - Integer
     - Global cumulative counter of "call barred" events
   * - Asterisk.Events.CallRejected(*system*)
     - Integer
     - Global cumulative counter of "call rejected" events
   * - Asterisk.Events.ChannelUnavailable(*system*)
     - Integer
     - Global cumulative counter of "channel unavailable" events
   * - Asterisk.Events.Congestion(*system*)
     - Integer
     - Global cumulative counter of "congestion" events
   * - Asterisk.Events.NoRoute(*system*)
     - Integer
     - Global cumulative counter of "no route" events
   * - Asterisk.Events.SubscriberAbsent(*system*)
     - Integer
     - Global cumulative counter of "subscriber absent" events
   * - Asterisk.Peer.Events.CallBarred(*system*, *peer*)
     - Integer
     - Cumulative counter of "call barred" events for given peer
   * - Asterisk.Peer.Events.CallRejected(*system*, *peer*)
     - Integer
     - Cumulative counter of "call rejected" events for given peer
   * - Asterisk.Peer.Events.ChannelUnavailable(*system*, *peer*)
     - Integer
     - Cumulative counter of "channel unavailable" events for given peer
   * - Asterisk.Peer.Events.Congestion(*system*, *peer*)
     - Integer
     - Cumulative counter of "congestion" events for given peer
   * - Asterisk.Peer.Events.NoRoute(*system*, *peer*)
     - Integer
     - Cumulative counter of "no route" events for given peer
   * - Asterisk.Peer.Events.SubscriberAbsent(*system*, *peer*)
     - Integer
     - Cumulative counter of "subscriber absent" events for given peer
   * - Asterisk.Peer.RTCP.AverageJitter(*system*, *peer*)
     - Integer
     - Average jitter for given peer in milliseconds (moving average over last 180 measurements)
   * - Asterisk.Peer.RTCP.AveragePacketLoss(*system*, *peer*)
     - Integer
     - Average packet loss for given peer (moving average over last 180 measurements)
   * - Asterisk.Peer.RTCP.AverageRTT(*system*, *peer*)
     - Integer
     - Average round trip time in milliseconds for given peer (moving average over last 180 measurements)
   * - Asterisk.Peer.RTCP.LastJitter(*system*, *peer*)
     - Integer
     - Last reported jitter for given peer in milliseconds
   * - Asterisk.Peer.RTCP.LastPacketLoss(*system*, *peer*)
     - Integer
     - Last reported packet loss for given peer
   * - Asterisk.Peer.RTCP.LastRTT(*system*, *peer*)
     - Integer
     - Last reported round trip time in milliseconds for given peer
   * - Asterisk.Peer.RTCP.MaxJitter(*system*, *peer*)
     - Integer
     - Maximum reported jitter for given peer in milliseconds
   * - Asterisk.Peer.RTCP.MaxPacketLoss(*system*, *peer*)
     - Integer
     - Maximum reported packet loss for given peer
   * - Asterisk.Peer.RTCP.MaxRTT(*system*, *peer*)
     - Integer
     - Maximum reported round trip time in milliseconds for given peer
   * - Asterisk.Peer.RTCP.MinJitter(*system*, *peer*)
     - Integer
     - Minimum reported jitter for given peer in milliseconds
   * - Asterisk.Peer.RTCP.MinPacketLoss(*system*, *peer*)
     - Integer
     - Minimum reported packet loss for given peer
   * - Asterisk.Peer.RTCP.MinRTT(*system*, *peer*)
     - Integer
     - Minimum reported round trip time in milliseconds for given peer
   * - Asterisk.SIP.Peer.Details(*system*, *peer*, *tag*)
     - String
     - Value of specific tag from SIPshowpeer AMI message
   * - Asterisk.SIP.Peer.IPAddress(*system*, *peer*)
     - String
     - SIP peer IP address
   * - Asterisk.SIP.Peer.Status(*system*, *peer*)
     - String
     - SIP peer status
   * - Asterisk.SIP.Peer.Type(*system*, *peer*)
     - String
     - SIP peer type
   * - Asterisk.SIP.Peer.UserAgent(*system*, *peer*)
     - String
     - SIP peer user agent information
   * - Asterisk.SIP.Peer.VoiceMailbox(*system*, *peer*)
     - String
     - SIP peer voice mailbox information
   * - Asterisk.SIP.Peers.Connected(*system*)
     - Integer
     - Number of connected SIP peers
   * - Asterisk.SIP.Peers.Total(*system*)
     - Integer
     - Total count of configured SIP peers
   * - Asterisk.SIP.Peers.Unknown(*system*)
     - Integer
     - Number of SIP peers in unknown state
   * - Asterisk.SIP.Peers.Unmonitored(*system*)
     - Integer
     - Number of unmonitored SIP peers
   * - Asterisk.SIP.Peers.Unreachable(*system*)
     - Integer
     - Number of unreachable SIP peers
   * - Asterisk.SIP.RegistrationTest.ElapsedTime(*system*, *test*)
     - Integer
     - Elapsed time for last run of given registration test
   * - Asterisk.SIP.RegistrationTest.Status(*system*, *test*)
     - Integer
     - Status of last run of given registration test
   * - Asterisk.SIP.RegistrationTest.Timestamp(*system*, *test*)
     - Integer
     - Timestamp last run of given registration test as UNIX time (number of seconds since 1.1.1970 00:00:00 UTC)
   * - Asterisk.SIP.TestRegistration(*system*, *login*, *password*, *domain*)
     - Integer
     - Status of ad-hoc registration
   * - Asterisk.TaskProcessor.HighWatermark(*system*, *processor*)
     - Integer
     - High watermark for given task processor
   * - Asterisk.TaskProcessor.LowWatermark(*system*, *processor*)
     - Integer
     - Low watermark for given task processor
   * - Asterisk.TaskProcessor.MaxDepth(*system*, *processor*)
     - Integer
     - Maximum queue depth for given task processor
   * - Asterisk.TaskProcessor.Processed(*system*, *processor*)
     - Integer
     - Number of processed tasks for given task processor
   * - Asterisk.TaskProcessor.Queued(*system*, *processor*)
     - Integer
     - Number of queued tasks for given task processor
   * - Asterisk.Version(*system*)
     - String
     - Asterisk version


Tables
------

All tables accept system name as first argument. Name for default local system is **LOCAL**.
If system name is omitted local system is assumed. If system name is the only argument braces can be omitted as well.

.. list-table::
   :header-rows: 1
   :widths: 50 50
   
   * - Metric
     - Description
   * - Asterisk.Channels(*system*)
     - Active channels
   * - Asterisk.CommandOutput(*system*, *command*)
     - Output of given Asterisk console command
   * - Asterisk.SIP.Peers(*system*)
     - SIP peers
   * - Asterisk.SIP.RegistrationTests(*system*)
     - Configured SIP registration tests
   * - Asterisk.TaskProcessors(*system*)
     - Task processors


Lists
-----

All lists accept system name as first argument. Name for default local system is **LOCAL**.
If system name is omitted local system is assumed. If system name is the only argument braces can be omitted as well.

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Metric
     - Description
   * - Asterisk.Channels(*system*)
     - Active channels
   * - Asterisk.CommandOutput(*system*, *command*)
     - Output of given Asterisk console command
   * - Asterisk.SIP.Peers(*system*)
     - SIP peers
   * - Asterisk.SIP.RegistrationTests(*system*)
     - Configured SIP registration tests
   * - Asterisk.Systems
     - Configured Asterisk systems
   * - Asterisk.TaskProcessors(*system*)
     - Task processors
