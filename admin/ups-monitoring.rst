.. _ups-monitoring:

==============
UPS monitoring
==============

There are two options to monitor UPS: first is through USB or serial connection with
help of subagent and second one is through the network with help of SNMP.

Subagent can be used for monitoring UPS (Uninterruptible Power Supply) attached
to serial or USB port on computer where |product_name| agent is running. USB-attached devices
currently supported only on Windows platform, serial is supported on all platforms.
One subagent can monitor multiple attached devices.


USB or serial UPS monitoring
============================

You can monitor UPS devices attached to the hosts via serial cable or USB via UPS
subagent. Once you have your UPS attached to the host and |product_name| agent installed,
you should configure UPS subagent. First, add the following line to agent's
configuration file main section:

.. code-block:: sh

 SubAgent = ups.nsm

Second, configure attached UPS devices. Create ``UPS`` section, and for each UPS
device attached to the host add line in the following format:

.. code-block:: sh

 Device = id:port:protocol

``id`` is an arbitrary but unique number in range 0 to 127, which is used to
distinguish multiple UPS devices in further requests.

``device`` is either name of the serial port (e.g. `COM1:` or `/dev/ttyS0`) or
serial number of the USB device (keyword `ANY` can be used instead of exact serial
number to select first available).

``protocol`` specify which communication protocol should be used. Supported protocols:

* APC
* BCMXCP - Some of the HP/Compaq, PowerWare, etc.
* MEGATEC
* METASYS
* MICRODOWELL
* USB - HID UPS devices (currently Windows only)


Sample configuration section for two devices attached via serial ports, one is APC device
(configured as device 0) and one is HP device (configured as device 1):

.. code-block:: sh

  # UPS subagent configuration section
  [UPS]
  Device = 0:/dev/ttyS0:APC
  Device = 1:/dev/ttyS1:BCMXCP


Once UPS subagent is configured, you can start to monitor UPS devices status via
metrics provided by it:

.. list-table::
   :header-rows: 1
   :widths: 50 30 200

   * - Metric Name
     - Type
     - Meaning
   * - UPS.BatteryLevel(*)
     - Integer
     - Battery charge level in percents.
   * - UPS.BatteryVoltage(*)
     - Float
     - Current battery voltage.
   * - UPS.ConnectionStatus(*
     - Integer
     - Connection status between agent and device. Can have the following values:
        * 0 - Agent is communication with the device
        * 1 - Communication with the device has been lost
   * - UPS.EstimatedRuntime(*)
     - Integer
     - Estimated on-battery runtime in minutes.
   * - UPS.Firmware(*)
     - String
     - Device's firmware version.
   * - UPS.InputVoltage(*)
     - Float
     - Input line voltage.
   * - UPS.LineFrequency(*)
     - Integer
     - Input line frequency in Hz.
   * - UPS.Load(*)
     - Integer
     - Device load in percents.
   * - UPS.MfgDate(*)
     - String
     - Device manufacturing date.
   * - UPS.Model(*)
     - String
     - Device model name.
   * - UPS.NominalBatteryVoltage(*)
     - Float
     - Nominal battery voltage.
   * - UPS.OnlineStatus(*)
     - Integer
     - Device online status. Can have the following values:
        * 0 - Device is online.
        * 1 - Device is on battery power.
        * 2 - Device is on battery power and battery level is low.
   * - UPS.OutputVoltage(*)
     - Float
     - Output line voltage.
   * - UPS.SerialNumber(*)
     - String
     - Device's serial number.
   * - UPS.Temperature(*)
     - Integer
     - Internal device temperature.


Please note that not all metrics are supported by all UPS devices. Many old or
simple models will support only basic things like UPS.OnlineStatus metric. Most
typical approach is to monitor UPS.OnlineStatus for going to 1 or 2, and then
send notifications to administrators and shutdown affected hosts if needed. You
can also monitor UPS.EstimatedRuntime metric for the same purposes if your
devices support it.

SNMP UPS monitoring
===================

Other option to monitor UPS is using SNMP. |product_name| already includes MIBs for some UPS,
like APC UPS and standard UPS MIB.
Description for possible OIDs and some additional information for APC UPS configuration
can be found on a
`NetXMS wiki <https://wiki.netxms.org/wiki/UPS_Monitoring_(APC)_via_SNMP>`_.

Please check :ref:`import-mib` for MIB loading and :ref:`dci-configuration` for
metric collection.
