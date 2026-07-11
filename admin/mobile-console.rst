.. _mobile-console:

#############
Mobile Client
#############

The |product_name| mobile client is a monitoring app for Android that connects to
the |product_name| server through the built-in Web API. It is available on Google
Play:

  https://play.google.com/store/apps/details?id=org.netxms.android


Requirements
============

* An Android device.
* A |product_name| server with the built-in Web API enabled.
* An HTTPS endpoint for the Web API that is reachable from the device.

The mobile client always connects over HTTPS. The built-in Web API itself serves
plain, unencrypted HTTP, so TLS must be terminated by a reverse proxy (Nginx,
reproxy, Traefik, or any other TLS-offloading service) placed in front of it.

.. warning::

   Never expose the raw Web API HTTP port directly to the network. Always place a
   TLS-terminating reverse proxy in front of it.


Enabling the Web API
====================

The mobile client relies on the built-in Web API. Enable it by adding the
following line to the server configuration file (:file:`netxmsd.conf`) and
restarting the server:

.. code-block:: ini

   Module = webapi

By default the API listens on ``127.0.0.1:8000``. For the full set of
configuration parameters — listener address and port, TLS termination, and the
recommended way to expose the endpoint securely — see :ref:`rest-api`.


Connecting
==========

1. Install the app from Google Play and open it.
2. Enter the server address (the Web API base URL). The ``https://`` prefix is
   added automatically, so only the host name is required.
3. Enter your user name and password.
4. If two-factor authentication is configured for your account, enter the
   verification code when prompted.

Once connected, the app uses the same credentials and access rights as your
|product_name| user account.
