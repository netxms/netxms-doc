.. _rest-api:

################
Web API/Rest API
################

Introduction
============

The |product_name| Web API provides a REST-like interface for integrating
external systems with the |product_name| server. API calls use JSON for data
exchange. Two implementations are available:

* **Built-in Web API** — embedded directly into the |product_name| server
  process. This is the recommended API for new integrations, however it's still
  work in progress and some endpoints might not yet be available. The API is
  documented using an `OpenAPI specification
  <https://github.com/netxms/netxms/blob/master/src/server/webapi/openapi.yaml>`_.

* **Legacy Web API** — a standalone Java web application (.war file) deployed to
  a separate web server. This implementation will be deprecated in the future.
  The API is documented using an `OpenAPI specification (legacy)
  <https://github.com/netxms/netxms/blob/master/src/client/nxapisrv/openapi.yaml>`_.

Information about Grafana configuration can be found :ref:`here <grafana-integration>`.


Built-in Web API
================

The built-in Web API is integrated directly into the |product_name| server process as a
loadable module.

Setup
-----

To enable the built-in Web API, add the following line to the server configuration file
(:file:`netxmsd.conf`):

.. code-block:: ini

   Module = webapi

The API listens on the loopback address on port 8000 by default. Once enabled, it can be
accessed at ``http://127.0.0.1:8000/``.

Configuration
-------------

All configuration parameters are placed in the ``[WEBAPI]`` section of the server
configuration file (:file:`netxmsd.conf`).

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - Enable
     - true
     - Set to ``false`` to disable the Web API without removing the module.
   * - Address
     - loopback
     - Listener address. Empty value or ``loopback``/``localhost`` binds to the loopback
       interface only. Use ``any`` or ``*`` to listen on all interfaces. A specific IP
       address can also be provided.
   * - Port
     - 8000
     - HTTP listener port.

Example configuration:

.. code-block:: ini

   Module = webapi

   [WEBAPI]
   Address = any
   Port = 8000


TLS Configuration
-----------------

The built-in Web API does not terminate TLS directly. Instead, it uses
`reproxy <https://github.com/umputun/reproxy>`_ as a TLS termination proxy, which is
started and managed automatically by the server when TLS is enabled. Alternatively, any
external reverse proxy (e.g. Nginx) can be used for TLS termination instead of reproxy —
in that case leave TLS disabled in the |product_name| configuration and configure the
proxy to forward HTTPS traffic to the HTTP listener port.

.. list-table::
   :widths: 25 15 60
   :header-rows: 1

   * - Parameter
     - Default
     - Description
   * - TLSEnable
     - false
     - Set to ``true`` to enable TLS termination using reproxy. 
   * - TLSPort
     - 8443
     - HTTPS listener port (reproxy listens on this port).
   * - TLSAddress
     - 0.0.0.0
     - Address reproxy binds to for HTTPS.
   * - TLSCertificate
     - *(none)*
     - Path to the TLS certificate file. Required when TLS is enabled.
   * - TLSCertificateKey
     - *(none)*
     - Path to the TLS certificate private key file. Required when TLS is enabled.
   * - ReproxyPath
     - ``/usr/bin/reproxy``
     - Path to the reproxy executable. On Windows, defaults to :file:`reproxy.exe`
       in the |product_name| bin directory.

Example TLS configuration:

.. code-block:: ini

   [WEBAPI]
   Address = loopback
   Port = 8000
   TLSEnable = true
   TLSPort = 8443
   TLSAddress = 0.0.0.0
   TLSCertificate = /etc/ssl/certs/netxms.crt
   TLSCertificateKey = /etc/ssl/private/netxms.key

.. note::

   When TLS is enabled, it is recommended to keep the HTTP listener bound to the loopback
   address (default) so that unencrypted traffic is not exposed on the network.


Legacy Web API (WAR file)
=========================

Requirements
------------

* A running instance of the |product_name| server.
* Access to a web server capable of deploying Java web applications (e.g. Apache Tomcat).

Setup
-----

1. Download :file:`netxms-websvc-VERSION.war` (example: :file:`netxms-websvc-6.0.2.war`)
   from http://www.netxms.org/download.
2. Copy the downloaded .war file to your web server's deployment directory.

By default, the localhost address is used to connect to the |product_name| server. To
specify the server address or other parameters, create a :file:`nxapisrv.properties` file
and place it in the property file location of your web server. The file uses INI format
(``NAME=VALUE``). The following parameters are supported:

.. list-table::
   :widths: 40 65
   :header-rows: 1

   * - Parameter
     - Description
   * - netxms.server.address
     - |product_name| server address
   * - netxms.server.port
     - |product_name| server port
   * - netxms.server.enableCompression
     - Enable protocol compression
   * - session.timeout
     - Session timeout

Configuration example:

.. code-block:: ini

   netxms.server.address=server.office.example.com
   netxms.server.port=44701
