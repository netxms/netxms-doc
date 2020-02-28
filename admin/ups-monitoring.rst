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

.. code-block:: cfg

 SubAgent = ups.nsm

Second, configure attached UPS devices. Create ``UPS`` section, and for each UPS
device attached to the host add line in the following format:

.. code-block:: cfg

 Device = id:port:protocol

where id is a number in range 0 .. 127 which will be used in requests to identify
device; port is a communication port for serial connection or UPS serial number
for USB connection; and protocol is a communication protocol used by connected device.
Protocol can be either APC (for APC devices), BCMXCP (for devices using BCM/XCP
protocol – for example, HP, Compaq, or PowerWare devices), or USB for USB-attached
devices. Below is an example of UPS configuration section for two devices attached
via serial ports, one is APC device (configured as device 0) and one is HP device
(configured as device 1):

.. code-block:: cfg

  # UPS subagent configuration section
  [UPS]
  Device = 0:/dev/ttyS0:APC
  Device = 1:/dev/ttyS1:BCMXCP


Once UPS subagent is configured, you can start to monitor UPS devices status via
parameters provided by it:

.. list-table::
   :header-rows: 1
   :widths: 50 30 200

   * - Parameter
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


Please note that not all parameters supported by all UPS devices. Many old or simple
models will support only basic things like UPS.OnlineStatus parameter.
Most typical approach is to monitor UPS.OnlineStatus for going to 1 or 2, and then
send notifications to administrators and shutdown affected hosts if needed. You can
also monitor UPS.EstimatedRuntime parameter for the same purposes if your devices
support it.


Simple Scenario
===============

Consider the following simple scenario: you have two servers, Node_A and Node_B,
connected to one UPS device. UPS device is APC Smart UPS 1700, connected with serial
cable to Node_A on first COM port. Both nodes are running Windows operating system.
You need to notify administrator if UPS goes to battery power, and shutdown both
nodes in case of low battery condition. We assume that both nodes have |product_name| agent
installed.
To accomplish this, do the following:

**Step 1.**

Configure UPS monitoring subagent on Node_A. Add the following line to main agent's
config section:

.. code-block:: cfg

  SubAgent = ups.nsm

At the end of configuration file, create UPS subagent configuration section:

.. code-block:: cfg

  # UPS subagent configuration section
  [UPS]
  Device = 0:"COM1:":APC


SNMP UPS monitoring
===================

Other option to monitor UPS is using SNMP. |product_name| already includes MIBs for some UPS,
like APC UPS and standard UPS MIB.
Description for possible OIDs and some additional information for APC UPS configuration
can be found on a
`NetXMS wiki <https://wiki.netxms.org/wiki/UPS_Monitoring_(APC)_via_SNMP>`_.

Please check :ref:`import-mib` for MIB loading and :ref:`dci-configuration` for
metric collection.
