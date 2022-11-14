.. _service-monitoring:

==========================
Network Service Monitoring
==========================

There are two options to add service monitoring: the first one is to add it through node
menu option :guilabel:`Create --> Create Network Service...` as an object with the status
that will be propagated on a node, and the second one is to add it's monitoring as
DCI.

Network Service Object
======================

Object representing network service running on a node (like http or
ssh), which is accessible online (via TCP IP). Network Service objects
are always created manually. Currently, the system works with the following
protocols - HTTP, POP3, SMTP, Telnet, SSH and Custom protocol type. For Custom
protocol, a user should define the TCP port number and the system will be
checking whether that port is available. For the predefined standard services
the system will also check whether an appropriate response is returned. In case
of SMTP, the system will send a test mail, in case of POP3 – try to log in with
a certain user, in case of HTTP – check whether the contents of a desired web
page correspond to a certain given template. As soon as the Network Service
object is created, it will be automatically included into the status poll. Each
time when the status poll for the particular node is carried out, all Network
Service objects are polled for a reply. If an object's reply corresponds to a
certain condition, its status is set as NORMAL. If an object is not responding,
it's status will be changed to CRITICAL. It is possible to create a :term:`DCI`
that will collect status of Network Service object.

.. figure:: _images/create_network_service.png

In default configuration request is done
with help of Port Check subagent on the server node. If it should be done through
different node is should be changed in it's properties after service creation by
selecting Poller node. There is also possibility to set quantity of polls that is
required to be sure that state have changed.

.. figure:: _images/network_service_properties.png

Network service monitoring using DCI
====================================

Second option is to use :term:`DCI` to monitor service. There are 2 subagents that
provide service monitoring metrics: NetSVC and PortCheck (deprecated). It is recommended to use
NetSVC for all `curl supported protocols <https://everything.curl.dev/protocols/curl>`_, as it can check not only availability, but
also response.

For HTTP services there is also option to use ECS subagent. This subagent has metrics that
are capable of hash calculation and time measurement.


.. _netsvc-subagent:

NetSVC configuration
--------------------

This subagent can be used to check network services supported by libcurl. More
information about syntax can be found here: http://curl.haxx.se/docs/manpage.html.

This subagent will add this metric to list of metrics available on agent:

.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Metric Name
     - Description
   * - NetworkService.Check(\ *URL*\[\[, \ *regex*\], \ *options*\])
     - Check if data retrieved from *ULR* matches regular expression \ *regex*\.
       \ *regex*\ can be omitted, it that case "^HTTP/(1\\.[01]|2) 200 .*" will be used.
       \ *options*\ is optional string parameter, it can contain one or several space-separated options:

         - *verify-host* - verify that host name from URL match one from certificate (CURLOPT_SSL_VERIFYHOST = 2). This is default behavior of libcurl. 
         - *no-verify-host* - do not verify that host name from URL match one from certificate (CURLOPT_SSL_VERIFYHOST = 0)
         - *verify-peer* - verify peer certificate (overrides subagent configuration setting)
         - *no-verify-peer* - do not verify peer certificate (overrides subagent configuration setting)
         - *follow-location* - follow any location: header that the server sends as part of an HTTP header in a 3xx response


.. note::
  Parameter(s) in [ ] are optional, when optional parameter(s) are used they should
  be used without [ ].


NetworkService.Check metric returns the following values:

.. list-table::
   :widths: 15 50
   :header-rows: 1

   * - Value
     - Description
   * - 0
     - Success, connection to *target* was established and expected response was received.
   * - 1
     - Invalid arguments were passed.
   * - 2
     - Cannot connect to *target*.
   * - 3
     - Invalid / Unexpected response from *target*.


HTTP check example:

.. code-block:: cfg

   NetworkService.Check(https://inside.test.ru/,^HTTP/(1\\.[01]|2) 200 .*)

"^HTTP/(1\\.[01]|2) 200 .*" - this is default value and can be omitted in the expression.

.. note::
  If agent is build from sources, then libcurl-dev should be installed to
  build netsvc subagent.


.. _ecs-subagent:

ECS
---

This subagent works with HTTP only. It can be used to measure page load time and checking page
hash. Request timeout for this subagent is 30 seconds.


.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Metric Name
     - Description
   * - ECS.HttpSHA1(\ *URL*\ )
     - Calculates SHA1 hash of provided URL
   * - ECS.HttpMD5(\ *URL*\ )
     - Calculates MD5 hash of provided URL
   * - ECS.HttpLoadTime(\ *URL*\ )
     - Measure load time for provided URL

.. code-block:: cfg

  MasterServers = netxms.demo
  Subagent = ecs.nsm

.. _portcheck-subagent:

PortCheck configuration
-----------------------

**DEPRECATED: Please use NetSVC instead.**

This subagent can be used to check TCP ports and specifically implements checks for
common services. It is highly recommended to use netsvc subagent especially for
HTTP and HTTPS monitoring.

When loaded, PORTCHECK subagent adds the following metrics to node Metric list:

.. list-table::
   :widths: 100 50
   :header-rows: 1
   :class: longtable


   * - Metric Name
     - Description
   * - ServiceCheck.Custom(\ *target*\ ,\ *port*\ [,\ *timeout*\ ])
     - Check that TCP *port* is open on *target*. Optional argument *timeout* specifies timeout in milliseconds, if it's not provided, default timeout 
       from **[portCheck]** section of agent's configuration file will be used. This is a very simple test that does nothing more than checking if the 
       port is open.
   * - ServiceCheck.HTTP(\ *target*\ ,[\ *port*\ ],\ *URI*\ ,\ *hostHeader*\ [,\ *regex*\ [,\ *timeout*\ ]])
     - Check that HTTP service is running on *target*.  Optional argument *port* specifies the port to connect to,
       otherwise 80 will be used.  The *URI* is NOT a URL it is the host header request URI.
       As an example to test URL http://www.netxms.org/index.html enter www.netxms.org:/index.html. *hostHeader* is
       currently not used, but may be the Host option at some point in the request made.
       Optional argument *regex* is PCRE compliant regular expression to check returned from the request,
       otherwise "^HTTP/(1\\.[01]|2) 200 .*" will be used.  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.HTTPS(\ *target*\ ,[\ *port*\ ],\ *URI*\ ,\ *hostHeader*\ [,\ *regex*\ [,\ *timeout*\ ]])
     - Check that HTTP service is running on *target* using TLS encrypted connection. Arguments are the same as for ServiceCheck.HTTP parameter.
   * - ServiceCheck.POP3(\ *target*\ ,\ *username*\ ,\ *password*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that POP3 service is running on *target* and that we are able to login using the supplied *username* and *password*. 
       Optional argument *port* specifies the port to connect to, otherwise 110 will be used. Optional argument *timeout* specifies 
       timeout in milliseconds. 
   * - ServiceCheck.POP3S(\ *target*\ ,\ *username*\ ,\ *password*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that POP3S service is running on *target* and that we are able to login using the supplied *username* and *password*. 
       Optional argument *port* specifies the port to connect to, otherwise 995 will be used. Optional argument *timeout* specifies 
       timeout in milliseconds. 
   * - ServiceCheck.SMTP(\ *target*\ ,\ *toAddress*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that SMTP service is running on *target* and that it will accept an e-mail to *toAddress*.  The e-mail will be from noreply@\ *DomainName* 
       using the *DomainName* option in agent config file **[portCheck]** section or its default value (see below). Optional argument *port* specifies 
       the port to connect to, otherwise 25 will be used. Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.SMTPS(\ *target*\ ,\ *toAddress*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that SMTPS service is running on *target* and that it will accept an e-mail to *toAddress*.  The e-mail will be from noreply@\ *DomainName* 
       using the *DomainName* option in agent config file **[portCheck]** section or its default value (see below). Optional argument *port* specifies 
       the port to connect to, otherwise 465 will be used. Optional argument *timeout* specifies timeout in milliseconds.   
   * - ServiceCheck.SSH(\ *target*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that SSH service is running on *target*.  Optional argument *port* specifies the port to connect with, otherwise 22 will be used.  Optional argument *timeout* specifies timeout in milliseconds.
   * - ServiceCheck.Telnet(\ *target*\ [,\ *port*\ [,\ *timeout*\ ]])
     - Check that Telnet service is running on *target*.  Optional argument *port* specifies the port to connect with, otherwise 23 will be used.  Optional argument *timeout* specifies timeout in milliseconds.

.. note:
  Parameters in [ ] are optional, when optional parameters are used they should
  be used without [ ].


All of the ServiceCheck.* metrics return the following values:

.. list-table::
   :widths: 15 50
   :header-rows: 1

   * - Value
     - Description
   * - 0
     - Success, connection to *target* was established and expected response was received.
   * - 1
     - Invalid arguments were passed.
   * - 2
     - Cannot connect to *target*.
   * - 3
     - Invalid / Unexpected response from *target*.

All configuration parameters related to PORTCHECK subagent should be placed into
***PORTCHECK** section of agent's configuration file. The following configuration parameters
are supported:

.. list-table::
   :widths: 25 20 100 20
   :header-rows: 1

   * - Parameter
     - Format
     - Description
     - Default value
   * - DomainName
     - *string*
     - Set default domain name for processing. Currently this is only used by SMTP check to set the from e-mail address.
     - netxms.org
   * - Timeout
     - *milliseconds*
     - Set default response timeout in *milliseconds*.
     - 3000

Configuration example:

.. code-block:: cfg

   # This sample nxagentd.conf instructs agent to:
   #   1. Load PORTCHECK subagent
   #   2. Set domain name for from e-mail to netxms.demo
   #   3. Default timeout for commands set to 5 seconds (5000 milliseconds)

   MasterServers = netxms.demo
   SubAgent =  portcheck.nsm

   [portCheck]
   DomainName = netxms.demo
   Timeout = 5000

