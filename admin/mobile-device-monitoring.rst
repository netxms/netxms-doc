.. _monitoring-mobile-device:

=========================
Monitoring mobile devices
=========================

.. Used version on wiki:  00:14, 16 February 2013‎ Marco Incalcaterra

|product_name| has mobile agent for Android devices running version 2.2. and later. Currently,
a very limited set of info can be monitored and reported to a |product_name| server.

Metrics
=======

Unlike other metrics mobile ones are provided with :guilabel:`Internal` origin as they
are not collected by server, but pushed from mobile agent.


.. list-table::
   :widths: 50 100
   :header-rows: 1

   * - Parameter
     - Description
   * - MobileDevice.BattaryLevel
     - Battery charging level in percents.
   * - MobileDevice.DeviceId
     - Id of device
   * - MobileDevice.LastReportTime
     - Last time device reported data
   * - MobileDevice.Model
     - Phone model
   * - MobileDevice.OS.Name
     - Operating system mane
   * - MobileDevice.OS.Version
     - Operating system version
   * - MobileDevice.SerialNumber
     - Serial number
   * - MobileDevice.UsedId
     -
   * - MobileDevice.Vendor
     - Mobile device vendor

GUI
===

Main Window
-----------

.. figure:: _images/mobile_agent.png

Sections:
  1. Agent status. In case agent is active, reports the basic info about configuration such as scheduler for new location acquisition and connection to server where to update info collected.
  2. Last location section reports info about the last location acquired (date/time, source provider, geo coordinates and estimated accuracy.
  3. Last connection section reports info about the status of last connection: date/time and status of connection to the server:port specified in the configuration section. In case of errors during connection, here is reported also the error message.
  4. Next connection section reports info about the next scheduled connection.
  5. Device ID section reports the device ID (IMEI in case of devices with phone).
  6. Device Serial section reports the device serial number.

Main menu
---------

  * :guilabel:`Reconnect`: select this item to force a reconnection to the server to send new collected data.
  * :guilabel:`Disconnect & Exit`: select this item to stop the agent and exit from the app.
  * :guilabel:`Settings`: select this item to configure the agent.

Settings
--------

This section is used to configure the behaviour of the agent.

Global settings
---------------

  * :guilabel:`Activate agent`: when set makes the agent operational.
  * :guilabel:`Autostart on boot`: automatically starts the agent on boot (to be effective, agent must be set to be active).
  * :guilabel:`Scheduler`: provides the ability to define a “one range” daily on which the agent is operational. Out of the specified range the agent will not collect any new position and will not try to make connections to the server. When set it is possible to specify:
      1. :guilabel:`Daily activation on`: start time for daily activation.
      2. :guilabel:`Daily activation off`: stop time for daily activation.

Connection
----------

  * Parameters: allows selecting the parameters used to connect to the server:
      1. :guilabel:`Server`: address of the server (IP or name).
      2. :guilabel:`Port`: port of the server (default 4747).
      3. :guilabel:`User name`: username to connect to the server.
      4. :guilabel:`Password`: password to connect to the server.
      5. :guilabel:`Encrypt connection`: when selected challenges an encryption strategy with the server (depending on supported/configured providers).
  * :guilabel:`Frequency`: amount of time, in minutes, that has to elapse between each tentative of connection to the server to send the gathered info.
  * :guilabel:`Override frequency`: when selected overrides the previous frequency values and forces a new connection to the server (thus resetting the timer) every time a new connection is detected. NB if you are in a situation where connection is not stable it is advised to clear this flag to avoid multiple connections that will drain the battery.

Location
--------

  * :guilabel:`Force position update`: when cleared instruct the agent to relay on position updates made from other apps in the system (this means that position can be very old if no other apps are trying to get a new fix). When set, instructs the agent to try to gather a new position.
  * :guilabel:`Frequency (min)`: amount of time, in minutes, that has to elapse before trying to acquire a new position (:guilabel:`Force position update` set) or before trying to check if someone else updated a position.
  * :guilabel:`Duration (min)`: maximum amount of time, in minutes, that has to elapse before giving up on acquiring a new position.
  * :guilabel:`Location strategy`: allows selecting the source provider that has to be used to acquire a new position, allowed providers:
      1. :guilabel:`Network only`: tries to acquire position from network provider. Network provider is usually fast in acquiring a new position but it is not much accurate, especially using data connection (range from 1Km to 2Km, depending on antennas deployment), the service is not available all around the world. Wi-Fi connection seems to guarantee much higher precision due to a correlation between last known position acquired from GPS.
      2. :guilabel:`GPS only`: tries to acquire position from GPS provider. GPS provider is usually slow in acquiring a new position, time depends on several factors such as how much time has elapsed since last position, number of satellites in free view (inside buildings can be really had to get a position).
      3. :guilabel:`Network and GPS`: tries to acquire a position from Network provider or GPS provider, the first one that gives a position is considered ok. There is no special algorithm to evaluate accuracy, the unique criteria is the speed of the fix.

.. note::
  Please note that on 2G networks (GPRS/EDGE) data connection is not available
  while you are busy in a conversation, position acquisition will fail. On 3G
  networks (UMTS/HSxPA) data connection is available and so the position
  acquisition. However, if the agent is not able to get a new fix within the
  time-frame specified, it will try to gather a position from any available
  provider that has a valid cached position to provide.

Notification
------------

Toast notification: when set allows the agent to display “toast” notifications
to the user (such as pushing data to the server, inform user about the start of
the agent, etc.).
