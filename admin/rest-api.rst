.. _rest-api:

################
Web API/Rest API
################

Introduction
============

The |product_name| Web API provides a REST-like interface for integrating
external systems with the |product_name| server. API calls use JSON for data
exchange. The Web API is embedded directly into the |product_name| server
process and is documented using an `OpenAPI specification
<https://github.com/netxms/netxms/blob/master/src/server/webapi/openapi.yaml>`_.

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
