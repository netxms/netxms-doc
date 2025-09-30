.. _ups-monitoring:

==============
UPS monitoring
==============

There are two options to monitor a UPS: the first is through a USB or serial connection with
help of a subagent and the second one is through the network with help of SNMP.

A subagent can be used for monitoring a UPS (Uninterruptible Power Supply) attached
to a serial or USB port on a computer where the |product_name| agent is running. USB-attached devices
are currently only supported on the Windows platform. Serial devices are supported on all platforms.
One subagent can monitor multiple attached devices.


USB or serial UPS monitoring
============================

You can monitor UPS devices attached to the hosts via serial cable or USB via the UPS
subagent. Once you have your UPS attached to the host and the |product_name| agent installed,
you should configure the UPS subagent. First, add the following line to the agents
configuration file main section:

.. code-block:: ini

 SubAgent = ups.nsm

Second, configure the attached UPS devices. Create a ``UPS`` section and for each UPS
device attached to the host add a line in the following format:

.. code-block:: ini

 Device = id:port:protocol

``id`` is an arbitrary but unique number in the range 0 to 127, which is used to
distinguish multiple UPS devices in further requests.

``device`` is either the name of the serial port (e.g. `COM1:` or `/dev/ttyS0`) or
the serial number of the USB device. For the MEC0003 protocol, this field should contain
the USB device instance ID (e.g. `186144F5`). The keyword `ANY` can be used instead of an exact
serial number or instance ID to select the first available device.

``protocol`` specifies which communication protocol should be used. Supported protocols are:

* APC
* BCMXCP - Some of the HP/Compaq, PowerWare, etc.
* MEC0003 - Off-brand USB UPS devices with VID 0x0001/PID 0x0000 (Windows only, uses Fry's Electronics MEC0003/megatec protocol)
* MEGATEC
* METASYS
* MICRODOWELL
* USB - HID UPS devices (currently Windows only)


A sample configuration section for two devices attached via serial ports where one is an APC device
(configured as device 0) and one is a HP device (configured as device 1):

.. code-block:: ini

  # UPS subagent configuration section
  [UPS]
  Device = 0:/dev/ttyS0:APC
  Device = 1:/dev/ttyS1:BCMXCP

For USB devices using the MEC0003 protocol on Windows, you can specify the instance ID to distinguish
between multiple connected devices, or use the `ANY` keyword to match the first available device:

.. code-block:: ini

  # UPS subagent configuration section for MEC0003 devices
  [UPS]
  Device = 1:ANY:MEC0003
  Device = 2:186144F5:MEC0003


Once the UPS subagent is configured, you can start monitoring the UPS device status via
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
simple models will support only basic metrics like UPS.OnlineStatus. The most
typical approach is to monitor UPS.OnlineStatus for going to 1 or 2, and then
send notifications to administrators and shutdown affected hosts if needed. You
can also monitor the UPS.EstimatedRuntime metric for the same purpose, if your
device supports it.

SNMP UPS monitoring
===================

Another option is to monitor the UPS using SNMP. |product_name| already includes MIBs for some UPSs,
like APC UPS and the standard UPS MIB.
The description for possible OIDs and some additional information for APC UPS configuration
can be found on a
`NetXMS wiki <https://wiki.netxms.org/wiki/UPS_Monitoring_(APC)_via_SNMP>`_.

Please check :ref:`import-mib` for MIB loading and :ref:`dci-configuration` for
metric collection.
