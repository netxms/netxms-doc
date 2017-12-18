.. _hardware-monitoring:

============================
Hardware(sensor) monitoring 
============================

NetXMS has subagents that allow to monitor hardware sensors.
  * lm-sensors - Can collect data from all sensors that are supported by
    `lm-sensors <http://www.lm-sensors.org/wiki/Devices>`_ drivers on Luinux.
  * DS18x20 - This subagent collects temperature data form ds18x20 sensors. Linux only.
  * RPI - This subagent is created for Raspberry Pi. It can collect data from dht22
    sensor and get status of any GPO pin.

lm-sensors
==========

This subagent can be used to read hardware status using lm_sensors package.

Pre-requisites
--------------

Package lm_sensors should be installed and configured properly. Output of
`sensors <http://www.lm-sensors.org/wiki/man/sensors>`_ command
should produce meaningful output (see example below).

.. code-block:: shell

   alk@b08s02ur:~$ sensors
   w83627dhg-isa-0290
   Adapter: ISA adapter
   Vcore:       +1.14 V  (min =  +0.00 V, max =  +1.74 V)
   in1:         +1.61 V  (min =  +0.05 V, max =  +0.01 V)   ALARM
   AVCC:        +3.31 V  (min =  +2.98 V, max =  +3.63 V)
   VCC:         +3.31 V  (min =  +2.98 V, max =  +3.63 V)
   in4:         +1.79 V  (min =  +1.29 V, max =  +0.05 V)   ALARM
   in5:         +1.26 V  (min =  +0.05 V, max =  +1.67 V)
   in6:         +0.10 V  (min =  +0.26 V, max =  +0.08 V)   ALARM
   3VSB:        +3.30 V  (min =  +2.98 V, max =  +3.63 V)
   Vbat:        +3.18 V  (min =  +2.70 V, max =  +3.30 V)
   fan1:       3308 RPM  (min = 1188 RPM, div = 8)
   fan2:       6250 RPM  (min = 84375 RPM, div = 8)  ALARM
   fan3:          0 RPM  (min = 5273 RPM, div = 128)  ALARM
   fan4:          0 RPM  (min = 10546 RPM, div = 128)  ALARM
   fan5:          0 RPM  (min = 10546 RPM, div = 128)  ALARM
   temp1:       +39.0°C  (high =  +4.0°C, hyst =  +1.0°C)  ALARM  sensor = diode
   temp2:       +17.0°C  (high = +80.0°C, hyst = +75.0°C)  sensor = diode
   temp3:      +124.5°C  (high = +80.0°C, hyst = +75.0°C)  ALARM  sensor = thermistor
   cpu0_vid:   +2.050 V

   coretemp-isa-0000
   Adapter: ISA adapter
   Core 0:      +37.0°C  (high = +76.0°C, crit = +100.0°C)

   coretemp-isa-0001
   Adapter: ISA adapter
   Core 1:      +37.0°C  (high = +76.0°C, crit = +100.0°C)


Parameters
----------

When loaded, lm_sensors subagent adds the following parameters:

+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Parameter                             | Description                                                                                         |
+=======================================+=====================================================================================================+
| LMSensors.Value(*chip*, *label*)      | Current value returned by hardware sensor                                                           |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+


Configuration file
------------------

All configuration parameters related to lm_sensors subagent should be placed into
**\*LMSENSORS** section of agent's configuration file.
The following configuration parameters are supported:

+----------------+---------+--------------------------------------------------------------------------+-------------------------------------------------------+
| Parameter      | Format  | Description                                                              | Default value                                         |
+================+=========+==========================================================================+=======================================================+
| UseFahrenheit  | Boolean | If set to "yes", all temperature reading will be converted to Fahrenheit | no                                                    |
+----------------+---------+--------------------------------------------------------------------------+-------------------------------------------------------+
| ConfigFile     | String  | Path to `sensors.conf <http://www.lm-sensors.org/wiki/man/sensors.conf>`_| none, use system default (usually /etc/sensors3.conf) |
+----------------+---------+--------------------------------------------------------------------------+-------------------------------------------------------+


Configuration example
---------------------

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent = lmsensors.nsm

   *LMSENSORS
   UseFahrenheit = yes
   ConfigFile = /etc/sensors.netxms.conf

Sample usage
------------

(based on output of "sensors" from Pre-requisites section)

.. code-block:: cfg

   alk@b08s02ur:~$ nxget netxms.demo 'LMSensors.Value(coretemp-isa-0001,Core 1)'
   38.000000
   alk@b08s02ur:~$ nxget netxms.demo 'LMSensors.Value(w83627dhg-isa-0290,AVCC)'
   3.312000


DS18x20
=======

This subagent collects temperature from DS18x20 sensor. Subagent available for Linux
only. To use this subagent 1-Wire driver should be installed.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 50 30 200

   * - Parameter
     - Type
     - Meaning
   * - Sensor.Temperature(*)
     - Float
     - Sensor temperature

Configuration file
------------------

All configuration parameters related to lm_sensors subagent should be placed into
**\*DS18X20** section of agent's configuration file.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 25 50 200

   * - Parameter
     - Format
     - Description
   * - Sensor
     - String
     - Sensor identification in format sensorName:uniqueID

Configuration example
---------------------

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent = DS18X20.nsm

   *DS18X20
   Sensor = sensorName:uiniqueID123456788990

RPI
===

This subagent collects data from Raspberry Pi dht22 sensor and status of GPO pins.

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 50 30 200

   * - Parameter
     - Type
     - Meaning
   * - GPIO.PinState(pinNumber)
     - Integer
     - State of pin with given number. This pin number should be enabled in agent
       configuration file.
   * - Sensors.Humidity
     - Integer
     - Sensors data for humidity
   * - Sensors.Temperature
     - Integer
     - Sensors data for temperature

Configuration file
------------------

All configuration parameters related to lm_sensors subagent should be placed into
**\*RPI** section of agent's configuration file.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 25 50 200

   * - Parameter
     - Format
     - Description
   * - DisableDHT22
     - Boolean
     - Disables dht22 sensor if ``yes``. By default ``no``.
   * - EnabledPins
     - Coma separated list of numbers
     - List of pins that are enabled for status check.

Configuration example
---------------------

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent = rpi.nsm

   *RPI
   DisableDHT22 = no
   EnabledPins = 1,4,5,8

MQTT
====

This is a subagent that can be used to collect data from devices and sensors
that use MQTT protocol for communication. The subagent can be used to connect to
existing MQTT brokers, listen to user specified topics, map posted data to metrics
and generate events.

Configuration file
------------------

These are the necessary configuration sections and parameters for the MQTT subagent:

.. list-table::
	:header-rows: 1
	:widths: 25	50 50 200

	* - Section
	  - Parameters
	  - Format
	  - Description
	* - [MQTT/Brokers/broker_name]
	  - Hostname, Port, Login, Password
	  - String
	  - This section holds the data needed to connect to the MQTT broker
	* - [MQTT/Brokers/broker_name/Events]
	  - "EVENT_NAME"
	  - String
	  - This section is for specifying MQTT topic and event matching
	* - [MQTT/Brokers/broker_name/Metrics]
	  - "Metric.Name"
	  - Dot separated string
	  - This section is for mapping data posted to MQTT topics to metrics

Configuration example
---------------------

.. code-block:: cfg

	SubAgent = mqtt.nsm

	[MQTT/Brokers/Office]
	Hostname = mqtt.office.radensolutions.com

	[MQTT/Brokers/Office/Events]
	MQTT_METERHUB_RAW_DATA = "cmnd/5C:CF:7F:25:79:D6/#"

	[MQTT/Brokers/Office/Metrics]
	MeterHub.Telemetry.RSSI = "tele/5C:CF:7F:25:79:D6/RSSI"
	MeterHub.Telemetry.Time = "tele/5C:CF:7F:25:79:D6/TIME"