.. _device-backup:


#####################
Network Device Backup
#####################

.. versionadded:: 6.1

Network device backup provides centralized visibility into configuration backups
of network devices managed by |product_name|. Administrators can view backup
status, browse configuration history, compare configuration versions, and
trigger on-demand backups directly from the management console.

|product_name| uses a pluggable provider interface for device configuration
backup. Only one provider can be active at a time. The following providers are
available:

.. list-table::
   :header-rows: 1
   :widths: 20 15 65

   * - Provider
     - Edition
     - Description
   * - Built-in
     - Enterprise
     - Native backup engine that uses device drivers to collect configurations
       via SSH and stores them in the |product_name| database.
   * - Unimus
     - Enterprise
     - Integration with `Unimus <https://unimus.net>`_ network device backup
       service.
   * - Oxidized
     - Community
     - Integration with `Oxidized <https://github.com/ytti/oxidized>`_
       open-source network device configuration backup tool.


.. _device-backup-concepts:

Concepts
========

Provider Interface
------------------

When a backup provider module is loaded, the server registers a ``DEVBACKUP``
component and the management console shows a :guilabel:`Device Backup` section
on node overview pages and a :guilabel:`Device Config Backup` view for
registered nodes.

Device Registration
-------------------

Before a device can be backed up, it must be registered with the backup
provider. Registration creates a mapping between the |product_name| node and the
corresponding device in the backup system. Once registered, the node displays
backup status information and provides access to configuration history.

Devices are registered automatically during configuration poll using the
``Hook::RegisterForConfigurationBackup`` NXSL script. The script receives the
node object as ``$node`` and should return ``true`` to register the device or
``false`` to skip it. If the script is not defined, all eligible nodes are
registered automatically.

Example hook script that registers only SNMP-capable devices:

.. code-block:: c

   return $node->isSNMP;

For already-registered devices, the hook is re-evaluated on each configuration
poll. If the script returns ``false``, the device is unregistered.

Configuration Change Detection
------------------------------

Each time a backup is retrieved, |product_name| computes a SHA-256 hash of the
configuration content. By comparing hashes between consecutive backups, the
system detects configuration changes and generates events:

- **SYS_RUNNING_CONFIG_CHANGED** -- fired when the running configuration changes
  between backups (parameters: ``previousHash``, ``newHash``)
- **SYS_STARTUP_CONFIG_CHANGED** -- fired when the startup configuration changes
  between backups (parameters: ``previousHash``, ``newHash``)

These events can be used in event processing policies to send notifications or
create alarms when device configurations change unexpectedly.


Using Device Backup
===================

Viewing Backup Status
---------------------

Once a device is registered, the node overview page shows a
:guilabel:`Device Backup` section with:

- **Registered** -- whether the device is registered for backup
- **Last job status** -- the result of the most recent backup attempt
  (Successful, Failed, or Unknown)
- **Last job time** -- when the last backup was attempted
- **Failure reason** -- if the last backup failed, the reason is displayed


Browsing Configuration History
------------------------------

To view the configuration backup history for a registered device:

1. Open the node in the management console.

2. Select the :guilabel:`Device Config Backup` view.

3. The backup list shows all available configuration versions with:

   - **Timestamp** -- when the backup was taken
   - **Running config** -- size of the running configuration
   - **Startup config** -- size of the startup configuration (if available)
   - **Status** -- change indicator: ``R`` if running config changed, ``S`` if
     startup config changed, ``R S`` if both changed, ``Initial`` for the first
     backup

4. Select a backup to view its content. The view provides three tabs:

   - :guilabel:`Running` -- the running configuration text
   - :guilabel:`Startup` -- the startup configuration text (if available)
   - :guilabel:`Diff` -- a side-by-side diff comparing two selected backups


Triggering an On-Demand Backup
------------------------------

To trigger an immediate backup for a registered device, open the
:guilabel:`Configuration Backup` view and click the :guilabel:`Backup Now`
button in the view toolbar.


.. _builtin-backup:

Built-in Backup Provider
=========================

The built-in backup provider (``devbackup.nxm``) is a native |product_name|
module available in the Enterprise Edition. It connects directly to network
devices using device drivers to retrieve configurations via SSH, and stores them
in the |product_name| database.

How It Works
------------

1. The module runs a background scheduler that checks all registered nodes
   against their configured backup interval.

2. When a node is due for backup, the scheduler submits a backup job to the
   thread pool.

3. The backup job uses the node's device driver to retrieve the running and
   startup configurations via SSH (interactive or command channel).

4. If the configuration has changed since the previous backup (determined by
   SHA-256 hash comparison), a new backup record is stored in the database and
   change events are fired.

5. If the configuration has not changed, only the last check timestamp is
   updated on the existing record.

6. Old backups are automatically cleaned up by the housekeeper based on the
   configured retention period.


Supported Devices
-----------------

The built-in provider uses device drivers to collect configurations. The
following drivers currently support configuration backup:

.. list-table::
   :header-rows: 1
   :widths: 30 30 40

   * - Driver
     - Method
     - Notes
   * - Cisco IOS
     - SSH interactive
     - Running and startup configs via ``show running-config`` /
       ``show startup-config``
   * - Cisco Nexus
     - SSH interactive
     - Running and startup configs
   * - MikroTik RouterOS
     - SSH command or interactive
     - Running config via ``/export``
   * - Hirschmann Classic
     - SSH interactive
     - Running and startup configs via ``show running-config`` /
       ``show startup-config``
   * - Hirschmann HiOS
     - SSH interactive
     - Running and startup configs
   * - Dell PowerConnect
     - SSH interactive
     - Running config via ``show running-config``

Devices must have SSH credentials configured in |product_name| for the driver to
connect.


Setting Up Built-in Provider
-----------------------------

Add the following to the |product_name| server configuration file
(``netxmsd.conf``):

.. code-block:: ini

   Module = devbackup.nxm

The module reads its configuration from server configuration variables:

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Server Configuration Variable
     - Default
     - Description
   * - DeviceConfigBackup.Interval
     - 86400
     - Backup interval in seconds (default 24 hours). Can be overridden per
       node by setting the ``SysConfig:DeviceConfigBackup.Interval`` custom
       attribute.
   * - DeviceConfigBackup.MaxJobs
     - 10
     - Maximum number of concurrent backup jobs.
   * - DeviceConfigBackup.RetentionDays
     - 90
     - Number of days to keep backup history. Older backups are deleted by the
       housekeeper.

Restart the |product_name| server after changing the configuration. Check the
server log for the message::

   Network device backup interface is provided by module DEVBACKUP


.. _unimus-integration:

Unimus Integration
==================

`Unimus <https://unimus.net>`_ is a commercial network device backup and
configuration management service. The |product_name| Unimus integration module
(``unimus.nxm``) connects to a Unimus instance via its REST API, allowing
administrators to manage device backup registration and view backup data from
within the |product_name| management console. This module is available in the
Enterprise Edition.


How It Works
------------

1. The administrator configures the Unimus module with the Unimus API URL and
   authentication token.

2. When a device is registered for backup, |product_name| checks if the device
   already exists in Unimus by IP address. If found, the existing Unimus device
   is linked. If not, a new device is created in Unimus.

3. Unimus handles all device connectivity, configuration collection, and
   scheduling independently.

4. When an administrator views backup data in |product_name|, the module
   retrieves it from the Unimus API on demand.


Setting Up Unimus Integration
-----------------------------

Add the following to the |product_name| server configuration file
(``netxmsd.conf``):

.. code-block:: ini

   Module = unimus.nxm

   [UNIMUS]
   BaseURL = http://unimus-host:8085
   Token = your-api-token

.. list-table::
   :header-rows: 1
   :widths: 20 10 20 50

   * - Parameter
     - Required
     - Default
     - Description
   * - BaseURL
     - No
     - ``http://127.0.0.1:8085``
     - Base URL of the Unimus instance.
   * - Token
     - Yes
     -
     - Unimus API authentication token.

Restart the |product_name| server after changing the configuration.


.. _oxidized-integration:

Oxidized Integration
====================

`Oxidized <https://github.com/ytti/oxidized>`_ is an open-source network device
configuration backup tool. It connects to network devices via SSH or Telnet,
retrieves their configurations, and stores them in a Git repository with full
version history.

The |product_name| Oxidized integration module (``oxidized.nxm``) connects to an
Oxidized instance via its REST API. |product_name| acts as an
`HTTP source <https://github.com/ytti/oxidized/blob/master/docs/Sources.md>`_
for Oxidized, providing the list of devices to back up. This means device
registration is managed from |product_name| and automatically synchronized to
Oxidized. This module is available in the Community Edition.


How It Works
------------

1. The administrator configures the Oxidized module in the |product_name| server
   configuration file with the Oxidized REST API URL and credentials.

2. On startup, |product_name| loads the module and registers a REST API endpoint
   (``/api/oxidized/nodes``) that Oxidized uses as its HTTP source to retrieve
   the list of devices to back up.

3. When a node is registered for backup (via the
   ``Hook::RegisterForConfigurationBackup`` script during configuration poll),
   |product_name| resolves the Oxidized model name from the node's properties
   (see :ref:`oxidized-model-resolution`) and stores the mapping as custom
   attributes on the node.

4. Oxidized periodically polls the ``/api/oxidized/nodes`` endpoint to get the
   current list of registered devices, then connects to each device on its
   configured schedule to retrieve and store configurations.

5. When an administrator views backup data in |product_name|, the module
   retrieves it from the Oxidized REST API on demand.

The ``/api/oxidized/nodes`` endpoint returns a JSON array with the following
fields for each registered node: ``name`` (node ID), ``ip``, ``model``,
``group``, ``username``, and ``password`` (from the node's SSH credentials).


Prerequisites
-------------

- A running Oxidized instance with the REST API enabled (``oxidized-web`` gem)
- Network connectivity from the |product_name| server to the Oxidized REST API
- Network connectivity from the Oxidized instance to the |product_name| REST API
  (for the HTTP source)
- Network connectivity from Oxidized to the managed network devices


.. _oxidized-setup:

Setting Up Oxidized Integration
-------------------------------

Configuring the |product_name| Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following to the |product_name| server configuration file
(``netxmsd.conf``):

.. code-block:: ini

   Module = oxidized.nxm

   [OXIDIZED]
   BaseURL = http://oxidized-host:8888
   Login = admin
   Password = secret
   DefaultModel = ios

See :ref:`oxidized-config-reference` for a full list of configuration
parameters.

Restart the |product_name| server after changing the configuration. Check the
server log for the message::

   Oxidized integration module initialized

If the Oxidized instance is reachable, the log will also show::

   Oxidized server responded successfully (N nodes)


Configuring Oxidized to Use |product_name| as Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure Oxidized to use |product_name| as its HTTP source. The
``/api/oxidized/nodes`` endpoint requires authentication. You must create an API
token in |product_name| and use it in the Oxidized configuration as a Bearer
key.

In the Oxidized configuration file (typically ``~/.config/oxidized/config``):

.. code-block:: yaml

   source:
     default: http
     http:
       url: https://netxms-server/api/oxidized/nodes
       headers:
         Authorization: Bearer your-api-token
       map:
         name: name
         ip: ip
         model: model
         group: group
         username: username
         password: password

Replace ``netxms-server`` with the hostname or IP address of the |product_name|
server and ``your-api-token`` with a valid API token.

After updating the Oxidized configuration, restart the Oxidized service.


SSH Key Authentication
~~~~~~~~~~~~~~~~~~~~~~

|product_name| passes username and password credentials to Oxidized through the
HTTP source API. However, SSH private keys are not passed through the API for
security reasons — exposing key material via a REST endpoint would be a security
risk.

SSH key authentication must be configured directly in the Oxidized configuration.
Oxidized supports per-node key paths via the ``vars(:ssh_keys)`` mechanism. To
configure a global SSH key for all nodes, add a ``vars`` section to the Oxidized
configuration file:

.. code-block:: yaml

   vars:
     ssh_keys: /path/to/private/key

The key file must be readable by the Oxidized process. Oxidized will use the
configured key for SSH authentication while still using the username from the
|product_name| API. If key authentication fails, Oxidized falls back to password
authentication.


.. _oxidized-config-reference:

Oxidized Configuration Reference
---------------------------------

The following parameters are available in the ``<OXIDIZED>`` section of
``netxmsd.conf``:

.. list-table::
   :header-rows: 1
   :widths: 20 10 20 50

   * - Parameter
     - Required
     - Default
     - Description
   * - BaseURL
     - No
     - ``http://127.0.0.1:8888``
     - Base URL of the Oxidized REST API.
   * - Login
     - No
     - (empty)
     - Username for HTTP Basic authentication to the Oxidized API.
   * - Password
     - No
     - (empty)
     - Password for HTTP Basic authentication to the Oxidized API.
   * - DefaultModel
     - No
     - (empty)
     - Default Oxidized model to use when no mapping is found through any of
       the automatic resolution tiers. If not set and no mapping is found,
       device registration will fail.


.. _oxidized-model-resolution:

Model Resolution
~~~~~~~~~~~~~~~~~

When a device is registered for backup, |product_name| resolves the Oxidized
model name using a multi-tier approach. The first tier that produces a match
wins:

1. **Custom attribute override** — if the ``oxidized.model`` custom attribute is
   set on the node, its value is used directly. This allows per-node overrides
   when automatic resolution produces an incorrect result.

2. **NDD driver name** — the node's network device driver name is looked up in
   the driver-to-model mapping table. The ``GENERIC`` driver is skipped because
   it matches all SNMP devices and is not useful for model selection.

3. **sysDescr substring match** — the node's SNMP sysDescr string is checked
   against a set of known patterns. This helps disambiguate devices that share
   a driver but run different operating systems (e.g. Cisco IOS vs. IOS-XR vs.
   ASA).

4. **Vendor name** — the node's vendor string is looked up in the vendor-to-model
   mapping table.

5. **Default model** — the ``DefaultModel`` configuration parameter is used as a
   last resort.

All lookups are case-insensitive.

.. tip::

   To override the model for a specific node, set the ``oxidized.model`` custom
   attribute on the node to the desired Oxidized model name (e.g. ``ios``,
   ``junos``, ``routeros``). This takes priority over all automatic resolution.

Driver-to-Model Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 40 30

   * - Driver Name
     - Oxidized Model
   * - CISCO-GENERIC / CATALYST-GENERIC / CATALYST-2900XL / CISCO-ESW
     - ios
   * - CISCO-NEXUS
     - nxos
   * - CISCO-SB
     - ciscosmb
   * - CISCO-WLC
     - aireos
   * - JUNIPER
     - junos
   * - NETSCREEN
     - screenos
   * - MIKROTIK
     - routeros
   * - HUAWEI-SW / OPTIX
     - vrp
   * - FORTIGATE
     - fortios
   * - ARUBA-SW
     - aoscx
   * - PROCURVE / HPSW
     - procurve
   * - H3C
     - comware
   * - EXTREME
     - xos
   * - DELL-PWC
     - powerconnect
   * - UBNT-AIRMAX
     - airos
   * - UBNT-EDGESW
     - edgeswitch
   * - HIRSCHMANN-HIOS / HIRSCHMANN-CLASSIC
     - hirschmann
   * - DLINK
     - dlink
   * - TPLINK
     - tplink
   * - ELTEX
     - eltex
   * - EDGECORE-ESW
     - edgecos
   * - TELTONIKA
     - openwrt

sysDescr Pattern Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^^

These patterns are matched as case-insensitive substrings within the node's
SNMP sysDescr. They are useful for devices that use the ``GENERIC`` driver or
a broad driver that covers multiple OS variants.

.. list-table::
   :header-rows: 1
   :widths: 50 30

   * - sysDescr Pattern
     - Oxidized Model
   * - Adaptive Security Appliance
     - asa
   * - IOS-XR / IOS XR
     - iosxr
   * - NX-OS
     - nxos
   * - Dell EMC Networking OS10 / OS10 Enterprise
     - os10
   * - Force10 / FTOS
     - ftos

Vendor-to-Model Mappings
^^^^^^^^^^^^^^^^^^^^^^^^^^

Used as a fallback when neither the driver nor sysDescr produce a match.

.. list-table::
   :header-rows: 1
   :widths: 40 30

   * - Vendor
     - Oxidized Model
   * - Cisco / Cisco Systems Inc.
     - ios
   * - Juniper Networks
     - junos
   * - MikroTik
     - routeros
   * - Huawei
     - vrp
   * - Fortinet
     - fortios
   * - HPE Aruba Networking
     - arubaos
   * - Hewlett Packard Enterprise
     - procurve
   * - Extreme Networks
     - xos
   * - D-Link
     - dlink
   * - TP-Link
     - tplink
   * - Dell
     - powerconnect
   * - Ubiquiti
     - edgeos
   * - Ubiquiti, Inc.
     - airos
   * - Eltex Ltd.
     - eltex
   * - Moxa
     - moxa
   * - Hirschmann
     - hirschmann
   * - Teltonika
     - openwrt
   * - Edgecore
     - edgecos


Debugging
=========

To enable detailed logging for backup providers, set the appropriate debug tag
in ``netxmsd.conf`` or via the server console:

.. code-block:: ini

   # Built-in backup provider
   DebugTag = devbackup:7

   # Unimus integration
   DebugTag = unimus:7

   # Oxidized integration
   DebugTag = oxidized:7
