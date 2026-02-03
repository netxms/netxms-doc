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

This subagent collects data from devices and sensors that use the MQTT protocol.
It connects to MQTT brokers, subscribes to topics, and provides received data as
agent metrics. It can also generate events when messages are received.

There are three ways to set up MQTT data collection:

1. **MQTT origin in DCI** - use ``MQTT`` origin in DCI properties with format
   ``broker_name:mqtt_topic``. No agent configuration needed beyond broker
   connection - agent subscribes to topics on first request. Use when message
   payload is the metric value directly.

   The agent which performs MQTT data collection is selected automatically. If
   the node is in a zone, the zone proxy is used. If a MQTT proxy is specified
   in the node properties, that will be used.         

2. **Topic to metric mapping** - map MQTT topics to agent metrics in agent
   configuration file. DCIs should be created with Agent origin. Use when
   message payload is the metric value directly.

3. **Structured data extraction** - parse JSON, XML or text from MQTT messages
   and extract specific elements as metrics. Use when messages contain
   structured data.


Basic configuration
-------------------

To use the MQTT subagent, load it and configure at least one broker connection:

.. code-block:: ini

   SubAgent = mqtt.nsm

   [MQTT/Brokers/MyBroker]
   Hostname = 10.10.10.3

This minimal configuration connects to an MQTT broker. You can then create DCIs
with ``MQTT`` origin using metric format ``MyBroker:topic/name`` to collect data
from any topic.


Topic to metric mapping
-----------------------

To map MQTT topics directly to agent metrics, add a ``Metrics`` section:

.. code-block:: ini

   SubAgent = mqtt.nsm

   [MQTT/Brokers/Office]
   Hostname = mqtt.office.example.com

   [MQTT/Brokers/Office/Metrics]
   MeterHub.Telemetry.RSSI = "tele/5C:CF:7F:25:79:D6/RSSI"
   MeterHub.Telemetry.Time = "tele/5C:CF:7F:25:79:D6/TIME"

This creates two agent metrics: ``MeterHub.Telemetry.RSSI`` and
``MeterHub.Telemetry.Time``. Each returns the last message payload received on
its configured topic. Create DCIs with ``NetXMS Agent`` origin to collect these.

To generate events when messages arrive, add an ``Events`` section:

.. code-block:: ini

   [MQTT/Brokers/Office/Events]
   MQTT_METERHUB_RAW_DATA = "cmnd/5C:CF:7F:25:79:D6/#"

Event ``MQTT_METERHUB_RAW_DATA`` will be generated whenever data is published to
any topic matching the pattern. MQTT wildcards (``+``, ``#``) are supported.                     


.. _mqtt-structured-data:

Structured data extraction
--------------------------

.. versionadded:: 5.2.0

Extractors parse JSON, XML or text from MQTT messages and provide specific
elements as metrics. This is similar to :ref:`ExternalDataProvider
<external-data-provider>` but for MQTT data sources.

The agent autodetects JSON and XML payloads. Use ``jq`` syntax for JSON queries,
``XPath`` for XML. Set ``ForcePlainTextParser = true`` to use PCRE regex with
one capture group for text extraction.

**Basic extractor setup:**

.. code-block:: ini

   SubAgent = mqtt.nsm

   [MQTT/Brokers/Office]
   Hostname = mqtt.office.example.com

   [MQTT/Brokers/Office/Extractors/SensorData]
   Topic = sensors/temperature/room1
   Description = Temperature sensor data

This subscribes to the topic and creates a generic metric ``SensorData(*)``.
If the topic receives ``{"temperature": 23.5, "humidity": 45}``, then
``SensorData(.temperature)`` returns ``23.5``.

**Defining named metrics:**

Add a ``Metrics`` subsection to create metrics for specific data elements:

.. code-block:: ini

   [MQTT/Brokers/Office/Extractors/SensorData/Metrics]
   Room1.Temperature = .temperature
   Room1.Temperature.description = Current temperature in Room 1
   Room1.Temperature.dataType = float
   Room1.Humidity = .humidity
   Room1.Humidity.dataType = int32

Use ``.description`` and ``.dataType`` suffixes to set metric properties.
Metrics can accept parameters using ``$1``, ``$2``, ... placeholders:

.. code-block:: ini

   Room1.Sensor(*) = .sensors.$1

**Defining list metrics:**

Add a ``Lists`` subsection for list metrics. The query can return arrays,
newline-separated strings, or JSON objects (returns keys):

.. code-block:: ini

   [MQTT/Brokers/Office/Extractors/SensorData/Lists]
   Room1.AvailableSensorsFromArray = .|keys
   Room1.AvailableSensorsFromStrings = .|keys[]
   Room1.AvailableSensorsFromObjects = .


Complete example
----------------

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

If topic ``weather/station1/data`` receives:

.. code-block:: json

   {
     "temp": 22.5,
     "humidity": 65,
     "pressure": 1013.25,
     "wind": {"speed": 12.3, "direction": "NW"}
   }

The following values will be available for the metrics:

* ``WeatherStation(.temp)`` returns ``22.5`` (generic metric with query)
* ``Weather.Temperature`` returns ``22.5``
* ``Weather.Humidity`` returns ``65``
* ``Weather.Pressure`` returns ``1013.25``
* ``Weather.WindSpeed`` returns ``12.3``
* ``Weather.WindDirection`` returns ``NW``
* ``Weather.AvailableReadings`` returns list: ``temp``, ``humidity``,
  ``pressure``, ``wind``


Configuration reference
-----------------------

Broker connection
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*name*]
     - Yes
     - Section name, where ``name`` is the broker name used in DCI metrics
       and other configuration sections.
   * - Hostname
     - Yes
     - MQTT broker hostname or IP address.
   * - Port
     - No
     - MQTT broker port. Default is ``1883``.
   * - Login
     - No
     - Username for MQTT broker authentication.
   * - Password
     - No
     - Password for MQTT broker authentication.


Events
~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*name*/Events]
     - No
     - Section for event configuration.
   * - *EVENT_NAME*
     - No
     - Event name and MQTT topic pattern. Event is generated when a message
       is received on matching topic. MQTT wildcards (``+``, ``#``) are
       supported.


Metrics (topic mapping)
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*name*/Metrics]
     - No
     - Section for direct topic-to-metric mapping.
   * - *metricName*
     - No
     - Metric name and MQTT topic. Returns last received message payload.
       MQTT wildcards are supported.


Extractors
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*]
     - No
     - Section name. ``name`` becomes the generic metric name (with ``(*)``).
   * - Topic
     - Yes
     - MQTT topic to subscribe to.
   * - Description
     - No
     - Textual description shown in metric list.
   * - ForcePlainTextParser
     - No
     - If ``true``, parse payload as plain text using regex with one capture
       group instead of JSON/XML. Default is ``false``.


Extractor metrics
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*/Metrics]
     - No
     - Section for named metrics extracted from structured data.
   * - *metricName*
     - No
     - Metric name and extraction query (jq for JSON, XPath for XML, regex
       for text). Use ``$1``, ``$2``, ... for parameterized metrics.
   * - *metricName*.dataType
     - No
     - Data type: ``int32``, ``uint32``, ``int64``, ``uint64``, ``string``,
       ``float``, ``counter32``, ``counter64``. Default is ``string``.
   * - *metricName*.description
     - No
     - Textual description shown in metric list.


Extractor lists
~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 10 65

   * - Parameter
     - Required
     - Description
   * - [MQTT/Brokers/*broker*/Extractors/*name*/Lists]
     - No
     - Section for list metrics extracted from structured data.
   * - *listName*
     - No
     - List name and extraction query. Query should return array, newline-
       separated strings, or object (returns keys).
   * - *listName*.description
     - No
     - Textual description shown in list browser.
