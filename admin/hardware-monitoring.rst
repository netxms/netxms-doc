.. _hardware-monitoring:

============================
Hardware (sensor) monitoring
============================

|product_name| has subagents that allow to monitor hardware sensors.
  * lm-sensors - Can collect data from all sensors that are supported by
    `lm-sensors <http://www.lm-sensors.org/wiki/Devices>`_ drivers on Linux.
  * DS18x20 - This subagent collects temperature data from ds18x20 sensors. Linux only.
  * RPI - This subagent is created for Raspberry Pi. It can collect data from DHT22
    sensor and get the status of any GPIO pin.

lm-sensors
==========

This subagent can be used to read hardware status using the lm_sensors package.

Pre-requisites
--------------

The package lm_sensors should be installed and configured properly. The output of
the `sensors <http://www.lm-sensors.org/wiki/man/sensors>`_ command
should produce meaningful output (see example below).

.. code-block:: sh

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

When loaded, the lm_sensors subagent adds the following metrics:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Metric
     - Description
   * - LMSensors.Value(*chip*, *label*)
     - Current value returned by hardware sensor


Configuration file
------------------

All configuration parameters related to lthe m_sensors subagent should be placed into
the **\*LMSENSORS** section of agent's configuration file.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 20 15 40 25

   * - Parameter
     - Format
     - Description
     - Default value
   * - UseFahrenheit
     - Boolean
     - If set to "yes", all temperature reading will be converted to Fahrenheit
     - no
   * - ConfigFile
     - String
     - Path to `sensors.conf <http://www.lm-sensors.org/wiki/man/sensors.conf>`_
     - none, use system default (usually /etc/sensors3.conf)


Configuration example
---------------------

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = lmsensors.nsm

   [LMSENSORS]
   UseFahrenheit = yes
   ConfigFile = /etc/sensors.netxms.conf

Sample usage
------------

(based on output of "sensors" from Pre-requisites section)

.. code-block:: sh

   alk@b08s02ur:~$ nxget netxms.demo 'LMSensors.Value(coretemp-isa-0001,Core 1)'
   38.000000
   alk@b08s02ur:~$ nxget netxms.demo 'LMSensors.Value(w83627dhg-isa-0290,AVCC)'
   3.312000


.. _ds18x20-subagent:

DS18x20
=======

This subagent collects temperature from DS18x20 sensor. Subagent available for Linux
only. To use this subagent the 1-Wire driver should be installed.

Metrics
-------

.. list-table::
   :header-rows: 1
   :widths: 20 20 30

   * - Metric
     - Type
     - Meaning
   * - Sensor.Temperature(*)
     - Float
     - Sensor temperature

Configuration file
------------------

All configuration parameters related to the lm_sensors subagent should be placed into
the **\*DS18X20** section of the configuration file of the agent.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 20 20 30

   * - Parameter
     - Format
     - Description
   * - Sensor
     - String
     - Sensor identification in format sensorName:uniqueID

Configuration example
---------------------

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = DS18X20.nsm

   [DS18X20]
   Sensor = sensorName:uiniqueID123456788990


.. _rpi-subagent:

RPI
===

This subagent collects data from the Raspberry Pi DHT22 sensor as well as the status of GPIO pins.

Metrics
-------

.. list-table::
   :header-rows: 1
   :widths: 20 20 30

   * - Metric
     - Type
     - Meaning
   * - GPIO.PinState(number)
     - Integer
     - State of pin with given number. This pin number should be enabled in the agent
       configuration file.
   * - Sensors.Humidity
     - Integer
     - Sensors data for humidity
   * - Sensors.Temperature
     - Integer
     - Sensors data for temperature

Configuration file
------------------

All configuration parameters related to the lm_sensors subagent should be placed into
the **\*RPI** section of the configuration file of the agent.
The following configuration parameters are supported:

.. list-table::
   :header-rows: 1
   :widths: 20 20 30

   * - Parameter
     - Format
     - Description
   * - DisableDHT22
     - Boolean
     - Disables dht22 sensor if ``yes``. By default ``no``.
   * - EnabledPins
     - Comma separated list of numbers
     - List of pins that are enabled for status check.

Configuration example
---------------------

.. code-block:: ini

   MasterServers = netxms.demo
   SubAgent = rpi.nsm

   [RPI]
   DisableDHT22 = no
   EnabledPins = 1,4,5,8


.. _mqtt-subagent:

MQTT
====

This is a subagent that can be used to collect data from devices and sensors
that use the MQTT protocol for communication. The subagent can be used to
connect to existing MQTT brokers, listen to user specified topics, map posted
data to metrics and generate events.

There are three ways how to set up data collection for MQTT:

1. **Topic to metric mapping** - specify MQTT topic to agent metric mapping in
   agent configuration file using ``[MQTT/Brokers/broker_name/Metrics]``
   section. In this case DCIs are created with origin ``NetXMS Agent``. This
   approach is suitable when MQTT message payload is used directly as metric
   value.

2. **MQTT origin in DCI** - use the ``MQTT`` origin in DCI properties. The
   metric has the following format ``broker_name:mqtt_topic``, where
   ``broker_name`` is name specified in the agent configuration file. The agent
   which performs MQTT data collection is selected automatically. If the node is
   in a zone, the zone proxy is used. If a MQTT proxy is specified in the node
   properties, that will be used. With this approach there is no need to specify
   metrics in the agent configuration file - when the server requests MQTT topic
   for the first time, the agent subscribes to that topic.

3. **Structured data extraction** - use extractors to parse JSON, XML or textual
   data from MQTT topics. This approach is suitable when MQTT messages contain
   structured data (JSON, XML) and you need to extract specific elements as
   metrics. Extractors are configured using
   ``[MQTT/Brokers/broker_name/Extractors/...]`` sections. See
   :ref:`mqtt-structured-data` for details. 

Configuration file
------------------

These are configuration sections and parameters for the MQTT subagent:

.. list-table::
	:header-rows: 1
	:widths: 45	25 20 20

	* - Section
	  - Parameters
	  - Format
	  - Description
	* - [MQTT/Brokers/broker_name]
	  - Hostname, Port, Login, Password
	  - String
	  - This section holds the data needed to connect to the MQTT broker
	* - [MQTT/Brokers/broker_name/Events]
	  - ``EVENT_NAME``
	  - String
	  - This section is optional and allows to specify event that would be generated when MQTT topic gets new value
	* - [MQTT/Brokers/broker_name/Metrics]
	  - ``Metric.Name``
	  - Dot separated string
	  - This section is optional and sets mapping of data posted to MQTT topics to agent metrics
	* - [MQTT/Brokers/broker_name/Extractors/extractor_name]
	  - Topic, Description, ForcePlainTextParser
	  - String, Boolean
	  - This section defines a structured data extractor. See :ref:`mqtt-structured-data`
	* - [MQTT/Brokers/broker_name/Extractors/extractor_name/Metrics]
	  - ``Metric.Name``
	  - Dot separated string
	  - Metrics extracted from structured data using jq/XPath queries
	* - [MQTT/Brokers/broker_name/Extractors/extractor_name/Lists]
	  - ``List.Name``
	  - Dot separated string
	  - Lists extracted from structured data using jq/XPath queries


Configuration example
---------------------

.. code-block:: ini

  SubAgent = mqtt.nsm

  [MQTT/Brokers/Local]
  Hostname = 10.10.10.3


Configuration example with metric and event configuration
---------------------------------------------------------

.. code-block:: ini

  SubAgent = mqtt.nsm

  [MQTT/Brokers/Office]
  Hostname = mqtt.office.radensolutions.com

  [MQTT/Brokers/Office/Events]
  MQTT_METERHUB_RAW_DATA = "cmnd/5C:CF:7F:25:79:D6/#"

  [MQTT/Brokers/Office/Metrics]
  MeterHub.Telemetry.RSSI = "tele/5C:CF:7F:25:79:D6/RSSI"
  MeterHub.Telemetry.Time = "tele/5C:CF:7F:25:79:D6/TIME"

This configuration will connect to an MQTT broker Office at the Hostname.
Whenever data is published to the topic ``cmnd/5C:CF:7F:25:79:D6/#``, the event
``MQTT_METERHUB_RAW_DATA`` will be triggered. It will also provide two metrics,
``MeterHub.Telemetry.RSSI`` and ``MeterHub.Telemetry.Time`` which will report data
received on the topics ``tele/5C:CF:7F:25:79:D6/RSSI`` and ``tele/5C:CF:7F:25:79:D6/TIME``
respectively.


.. _mqtt-structured-data:

Structured data extraction
--------------------------

.. versionadded:: 5.2.0

Extractors allow parsing JSON, XML or textual data from MQTT topics. When a
message is received on the configured topic, the agent caches and parses its
content. Specific elements of the cached data can then be accessed via agent
metrics. This is similar to :ref:`ExternalDataProvider
<external-data-provider>` but for MQTT data sources.

Agent autodetects if the message payload is JSON or XML. ``jq`` syntax is used
to extract data from JSON, ``XPath`` is used for XML. If ``ForcePlainTextParser``
is set to true, the payload is treated as plain text and PCRE regular expression
with one capture group is used for extraction.


Configuring extractors
~~~~~~~~~~~~~~~~~~~~~~

Extractors are configured as sections in agent configuration file. The section
name format is ``[MQTT/Brokers/broker_name/Extractors/extractor_name]``.

.. code-block:: ini

   SubAgent = mqtt.nsm

   [MQTT/Brokers/Office]
   Hostname = mqtt.office.example.com

   [MQTT/Brokers/Office/Extractors/SensorData]
   Topic = sensors/temperature/room1
   Description = Temperature sensor data
   ForcePlainTextParser = false

Above configuration subscribes to the topic ``sensors/temperature/room1`` and
creates a generic metric ``SensorData(*)``. This metric accepts one parameter -
a path in JSON or XML document (or regex if text parsing is used). For example,
if the topic receives JSON ``{"temperature": 23.5, "humidity": 45}``, the metric
``SensorData(.temperature)`` will return ``23.5``.


Defining metrics
~~~~~~~~~~~~~~~~

Additional named metrics can be defined for specific data elements by adding
a ``Metrics`` subsection:

.. code-block:: ini

   [MQTT/Brokers/Office/Extractors/SensorData/Metrics]
   Room1.Temperature = .temperature
   Room1.Temperature.description = Current temperature in Room 1
   Room1.Temperature.dataType = float
   Room1.Humidity = .humidity
   Room1.Humidity.description = Current humidity in Room 1
   Room1.Humidity.dataType = int32

This configuration adds ``Room1.Temperature`` and ``Room1.Humidity`` metrics
that directly return the extracted values without requiring query parameters.

``.description`` and ``.dataType`` are special suffixes used to set metric
description and data type respectively, so metric names cannot end with these
suffixes.

Metrics can also accept parameters using ``$1``, ``$2``, etc. placeholders:

.. code-block:: ini

   [MQTT/Brokers/Office/Extractors/SensorData/Metrics]
   Room1.Sensor(*) = .sensors.$1
   Room1.Sensor(*).description = Sensor value by name
   Room1.Sensor(*).dataType = float


Defining lists
~~~~~~~~~~~~~~

List metrics can be defined by adding a ``Lists`` subsection. The jq query can
return:

* Array - all elements are returned as list items
* Newline-separated strings - each line is returned as a list item
* JSON Object - keys of the object are returned as list items

Below are examples of each case based on a topic that receives the following
JSON:  ``{"temperature": 23.5, "humidity": 45}``

.. code-block:: ini

   [MQTT/Brokers/Office/Extractors/SensorData/Lists]
   Room1.AvailableSensors = .|keys
   Room1.AvailableSensors = .|keys[]
   Room1.AvailableSensors = .


Extractor configuration reference
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*]
     - Yes
     - Section name, where ``broker`` is the broker name and ``name`` is the
       extractor name. The extractor name will be used as the base metric name.
   * - Topic
     - Yes
     - MQTT topic to subscribe to.
   * - Description
     - No
     - Textual description of the extractor.
   * - ForcePlainTextParser
     - No
     - If set to ``true``, treat payload as plain text even if it looks like
       JSON or XML. Default is ``false``.


.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*/Metrics]
     - No
     - Section for defining named metrics.
   * - *metricName*
     - No
     - Metric name and extraction query. The query uses jq syntax for JSON,
       XPath for XML, or regex for plain text.
   * - *metricName*.dataType
     - No
     - Metric data type. Possible values: ``int32``, ``uint32``, ``int64``,
       ``uint64``, ``string``, ``float``, ``counter32``, ``counter64``.
       Default is ``string``.
   * - *metricName*.description
     - No
     - Textual description of the metric.


.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*/Lists]
     - No
     - Section for defining list metrics.
   * - *listName*
     - No
     - List name and extraction query.
   * - *listName*.description
     - No
     - Textual description of the list.


Complete example
~~~~~~~~~~~~~~~~

.. code-block:: ini

   SubAgent = mqtt.nsm

   [MQTT/Brokers/IoT]
   Hostname = mqtt.iot.example.com
   Port = 1883
   Login = netxms
   Password = secret

   [MQTT/Brokers/IoT/Extractors/WeatherStation]
   Topic = weather/station1/data
   Description = Weather station sensor data

   [MQTT/Brokers/IoT/Extractors/WeatherStation/Metrics]
   Weather.Temperature = .temp
   Weather.Temperature.description = Outside temperature
   Weather.Temperature.dataType = float
   Weather.Humidity = .humidity
   Weather.Humidity.dataType = int32
   Weather.Pressure = .pressure
   Weather.Pressure.dataType = float
   Weather.WindSpeed = .wind.speed
   Weather.WindDirection = .wind.direction

   [MQTT/Brokers/IoT/Extractors/WeatherStation/Lists]
   Weather.AvailableReadings = .|keys
   Weather.AvailableReadings.description = List of available weather readings

With this configuration, if the topic ``weather/station1/data`` receives the
following JSON message:

.. code-block:: json

   {
     "temp": 22.5,
     "humidity": 65,
     "pressure": 1013.25,
     "wind": {"speed": 12.3, "direction": "NW"}
   }

The following metrics will be available:

* ``Weather.Temperature`` returns ``22.5``
* ``Weather.Humidity`` returns ``65``
* ``Weather.Pressure`` returns ``1013.25``
* ``Weather.WindSpeed`` returns ``12.3``
* ``Weather.WindDirection`` returns ``NW``
* ``WeatherStation(.temp)`` returns ``22.5`` (generic metric)
* ``Weather.AvailableReadings`` returns list: ``temp``, ``humidity``, ``pressure``, ``wind``
