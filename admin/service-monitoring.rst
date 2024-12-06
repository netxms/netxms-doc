.. _service-monitoring:

==========================
Network Service Monitoring
==========================

There are two options to add service monitoring: the first one is to add it through node
menu option :guilabel:`Create --> Create Network Service...` as an object with the status
that will be propagated on a node, and the second one is to add it's monitoring as
DCI.

In both cases monitoring is done by the help of |product_name| agent. In agent's 
configuration file `NetSVC` subagent should be enabled. 

Network Service Object
======================

Object representing network service running on a node (like http or ssh), which
is accessible online (via TCP IP). Network Service objects are always created
manually. Currently, the system works with the following protocols - SSH, POP3,
SMTP, FTP, HTTP, HTTPS, Telnet and Custom protocol type. For Custom protocol,
user should define TCP port number and the system will be checking if it's
possible to establish connection to that port. For the predefined standard
services the system will also check whether an appropriate response is returned.
In case of SMTP, the system will send a test mail, in case of POP3 – try to log
in with a certain user, in case of HTTP – check whether the contents of a
desired web page correspond to a certain given template. As soon as the Network
Service object is created, it will be automatically included into the status
poll. Each time when the status poll for the particular node is carried out, all
Network Service objects are polled for a reply. If an object's reply corresponds
to a certain condition, its status is set as NORMAL. If an object is not
responding, it's status will be changed to CRITICAL. It is possible to create a
:term:`DCI` that will collect status of Network Service object.

.. figure:: _images/create_network_service.png

In default configuration request is done with the help of |product_name| agent
(by it's NetSVC subagent) on the server node. If it should be done through
different node is should be changed in it's properties after service creation by
selecting Poller node. There is also possibility to set number of polls that is
required to be sure that state have changed.

.. figure:: _images/network_service_properties.png


Network service monitoring using DCI
====================================

Second option is to use :term:`DCI` to monitor service. Service monitoring
metrics are provided |product_name| agent (by it's NetSVC 
:ref:`subagent <subagent_list>`). DCIs should either be created on the node 
where agent is running, or they can be created on another node and the node with
agent can be specified in `Source node override` in DCI's properties. 

More about URL options can be found there: https://curl.se/docs/url-syntax.html

This subagent will add the following metrics to list of metrics available on
agent:

.. list-table::
   :widths: 60 100
   :header-rows: 1
   :class: longtable

   * - Metric Name
     - Description

   * - HTTP.Checksum.MD5(\ *URL*\, [\ *named parameters*\])

       HTTP.Checksum.SHA1(\ *URL*\, [\ *named parameters*\])

       HTTP.Checksum.SHA256(\ *URL*\, [\ *named parameters*\])
     - Calculate hash for the provided URL. Port number can be specified in the
       URL. *http* and *https* schemes are supported in the URL. Calculates hash
       only if web server returns 200 status code. 
       
       Starting from second parameter this metric accepts named parameters in
       *name = value* form. When parameter(s) are used, they should be used
       without [ ]. 
       
       The following parameters are supported (all parameters are optional):

         - *follow-location* - *true* - follow redirects which web server sends
           as part of an HTTP header in a 3xx response; *false* (default) - do
           not follow redirects 
         - *timeout* - timeout in milliseconds
         - *verify-host* - *true* (default) - verify that host name from URL
           matches one from certificate (CURLOPT_SSL_VERIFYHOST = 2); *false* -
           do not verify that host name from URL match one from certificate
           (CURLOPT_SSL_VERIFYHOST = 0)
         - *verify-peer* - *true* (default) - verify peer certificate; *false* -
           do not verify peer certificate. 

   * - NetworkService.Status(\ *URL*\, [\ *named parameters*\])
     - Check status of network service and return numeric value denoting the
       result.  Port number can be specified in the URL. URL supports the
       following schemes: *http*, *https*, *ssh*, *telnet*, *tcp*, *smtp* and
       *smtps*. 
       
       For *ssh* protocol connection is established. For *telnet* it's checked
       that host sends some characters after connection is established. For
       *tcp* only ability to establish connection to specified port is checked.
       For *smtp* and *smtps* test email is being sent. 

       Starting from second parameter this metric accepts named parameters in
       *name = value* form. When parameter(s) are used, they should be used
       without [ ]. 
       
       Optional parameter supported for all schemes:

         - *timeout* - timeout in milliseconds       
       
       Parameters supported for *http* and *https* schemes (all parameters are
       optional):

         - *follow-location* - *true* - follow redirects which web server sends
           as part of an HTTP header in a 3xx response; *false* (default) - do
           not follow redirects 
         - *include-headers* - if set to *true* (default), *pattern* is matched
           within headers and body of the web page. If set to *false*, *pattern*
           is matched in web page body only. 
         - *pattern* - regular expression to match. 
         - *response-code* - web server response code to match.     

       Parameters supported for *smtp* and *smtps* schemes:

         - *to* - test email will be sent to this address. Obligatory parameter
         - *from* - test email will be sent from this address. Optional
           parameter, default value depends on configuration of NetSVC subagent. 

       Parameters supported for all schemas except *ssh*, *telnet*, *tcp*:

         - *verify-host* - *true* (default) - verify that host name from URL
           matches one from certificate (CURLOPT_SSL_VERIFYHOST = 2); *false* -
           do not verify that host name from URL match one from certificate
           (CURLOPT_SSL_VERIFYHOST = 0)
         - *verify-peer* - *true* (default) - verify peer certificate; *false* -
           do not verify peer certificate.  
         - *tls-mode* - TLS mode that should be used. One of: *none*, *try*, *always*
         - *login* - login
         - *password* - password (can be encrypted by :ref:`nxencpasswd-tools-label` tool)

       Metric returns one of the following values:

         - 0 - Success, connection to target was established and expected
           response was received.
         - 2 - Can not connect to target (connection refused or connection timeout)
         - 3 - Invalid / unexpected response from target (e.g. pattern or
           response-code not matched)
         - 4 - Agent internal error 
         - 5 - Protocol handshake error (e.g. wrong data or no data expected by
           protocol received, SSL certificate problem)

   * - NetworkService.ResponseTime(\ *URL*\, [\ *named parameters*\])
     - Measures response time, returns value in milliseconds. For *http* and
       *https* schemas time to fully load the web page is measured. Metric
       support same parameters as NetworkService.Status. 

   * - NetworkService.TLSStatus(\ *host*\, \ *port*\, [\ *named parameters*\])
     - Check remote TLS service and return return numeric value denoting the
       result.

       Starting from third parameter this metric accepts named parameters in
       *name = value* form. When parameter(s) are used, they should be used
       without [ ]. The following optional parameter is supported:

         - *timeout* - timeout in milliseconds            
   
       Metric returns one of the following values:

         - 0 - Success, connection to target was established and expected
           response was received.
         - 2 - Can not connect to target (connection refused or connection timeout)
         - 3 - Invalid / unexpected response from target 
         - 4 - Agent internal error 
         - 5 - Protocol handshake error 

   * - NetworkService.TLSResponseTime(\ *host*\, \ *port*\, [\ *named parameters*\])
     - Measures time to perform TLS handshake, returns value in milliseconds.
       Metric support same parameters as NetworkService.TLSStatus. 

   * - TLS.Certificate.ExpirationDate(\ *host*\, \ *port*\)
     - Returns expiration date (YYYY-MM-DD) of X.509 certificate of remote TLS service 

   * - TLS.Certificate.ExpirationTime(\ *host*\, \ *port*\)
     - Returns expiration time (Unix time) of X.509 certificate of remote TLS service

   * - TLS.Certificate.ExpiresIn(\ *host*\, \ *port*\)
     - Returns number of days until expiration of X.509 certificate of remote TLS service

   * - TLS.Certificate.Issuer(\ *host*\, \ *port*\)
     - Returns issuer of X.509 certificate of remote TLS service

   * - TLS.Certificate.Subject(\ *host*\, \ *port*\)
     - Returns subject of X.509 certificate of remote TLS service

   * - TLS.Certificate.TemplateID(\ *host*\, \ *port*\)
     - Returns template ID of X.509 certificate of remote TLS service


Examples
--------

| ``NetworkService.Status(http://www.netxms.org)`` 
| This metric will return 0 (success). In this case we are just checking that
  web server provides response, without checking for pattern or status code
  (which is 301 in this case, as we receive redirect to https://www.netxms.org/)

| ``NetworkService.Status(http://www.netxms.org, response-code=200)`` 
| Returns 3 (unexpected response) as response code (301) does not match the value
  we are checking for. 

| ``NetworkService.Status(http://www.netxms.org, follow-location=true, response-code=200)`` 
| Returns 0 (success) as it follows redirects and ultimately gets web page with
  response code 200. 

| ``NetworkService.Status(https://netxms.org, pattern="^HTTP\/(1\.[01]|2) 200 .*")``
| Here we are checking for specific pattern both in headers and web page
  (*include-headers* parameter is not specified and it's default value is
  *true*).

| ``NetworkService.Status(http://www.netxms.org, include-headers=false,
  pattern=".*Moved Permanently.*")``\
| Checking for specific pattern only in web page itself, but not in headers. 

| ``NetworkService.Status(https://a.web.site.with.self.signed.certificate)``
| Returns 5 (Protocol handshake error) because libcurl can not verify the
  self-signed certificate. 

| ``NetworkService.Status(https://a.web.site.with.self.signed.certificate,
  verify-peer=false)``
| Returns 0 (Success) as we disabled peer certificate verification. 

| ``NetworkService.Status(tcp://netxms.org:80)``
| Returns 0 (Success) as we were able to establish TCP connection to port 80

| ``NetworkService.Status(tcp://netxms.org:88, timeout=2000)``
| Returns 2 (Timeout) as it was not possible to establish TCP connection to port
  1.  Waits for 2 seconds according to *timeout* that we have specified. 

| ``NetworkService.ResponseTime(https://www.google.com)``
| Returns time in milliseconds it took to fully retrieve the web page from the
  server. 

| ``NetworkService.TLSStatus(netxms.org, 443)``
| Returns 0 (success). This only performs TLS handshake, without retrieving any
  web page from the server. 

| ``NetworkService.TLSResponseTime(www.google.com, 443)``
| Returns the time it takes to perform TLS handshake with the server.


.. _netsvc-subagent:

NetSVC configuration
====================

This subagent performs network services checks by employing libcurl. More
information about syntax can be found here: http://curl.haxx.se/docs/manpage.html.

.. note::
  If agent is build from sources, then libcurl-dev should be installed to
  build netsvc subagent.


To operate, NetSVC subagent should be loaded. All configuration parameters
related to NetSVC subagent should be placed into **[netsvc]** section of agent's
configuration file. The following configuration parameters are supported:


.. list-table::
   :widths: 40 70 20
   :header-rows: 1

   * - Parameter
     - Description
     - Default value
   * - CA
     - Path to a file holding one or more certificates to verify the peer with (CURLOPT_CAINFO)
     - 
   * - DomainName
     - Used in SMTP check. Default *from* email address is composed as *noreply@DomainName*. 
     - netxms.org
   * - NegativeResponseTimeOnError
     - For metrics that measure response time, return negative time value instead of data collection error. 
     - false
   * - VerifyPeer
     - Verify peer certificate
     - true
   * - Timeout
     - Timeout in milliseconds. 
     -


Agent's configuration file example:

.. code-block:: ini

   SubAgent = netsvc
   [netsvc]
   Timeout = 3000
   
