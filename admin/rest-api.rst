.. _rest-api:

################
Web API/Rest API
################

Introduction
============

The |product_name| WebAPI is being developed to support larger integration possibilities for the |product_name|
server and is based on the RESTful philosophy. API calls are REST-like (although not purely RESTful)
and uses JSON for data exchange. The API currently supports Grafana integration and
some additional parameters for integration. The |product_name| WebAPI is currently in very early development!

Information about Grafana configuration can be found :ref:`here <grafana-integration>`.

Installation
============

Requirements
------------

   * A running instance of the |product_name| server.
   * Access to a web server.

Setup
-----

1. Download netxms-websvc-VERSION.war (example: netxms-websvc-2.2.15.war) file from http://www.netxms.org/download page.
2. Copy the downloaded .war file to your web server.

By default localhost address is used to connect to |product_name| Server. To specify server address or other parameters, 
create a :file:`nxapisrv.properties` file and place it in the property file location of your web server. 
File should have parameters in ini format: NAME=VALUE. The following parameters are supported:

   * netxms.server.address
   * netxms.server.enableCompression
   * netxms.server.port
   * session.timeout

Configuration example:

   .. code-block:: ini

        netxms.server.address=server.office.radensolutions.com
        netxms.server.port=44701


Implemented functionality
=========================

Authentication
--------------

Login
~~~~~

Any user account configured in NetXMX can be used to authenticate to Rest API, however
this user should have access right to objects that will be requested through the API.

There are 3 implemented options of authentication:

   1. Basic authentication for Rest API session creation, more information can be found on :wikipedia:`Wikipedia <Basic access authentication>`
   2. Through POST request for Rest API session creation
   3. Through POST request to allow external software user authentication using |product_name| user accounts.
      To be able to login using this authentication type, user account should have "External tool integration account" access right set.

Creating Rest API session:
%%%%%%%%%%%%%%%%%%%%%%%%%%

Request type: **POST**

JSON data:

.. code-block:: json

    {"login":"admin","password":"netxms"}

Request path: *API_HOME*/sessions

Return data:

    On success server will set cookie session_handle and json with session GUID and server version.
    When performing subsequent requests, session GUID should be provided in `Session-Id:` field of request's header
    or the cookie should be passed.

Performing external authentication:
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Request type: **POST**

JSON data:

.. code-block:: json

    {"login":"admin","password":"netxms"}

Request path: *API_HOME*/authenticate

Return data:

    The API will return a 200 response if the credentials are correct, a 400 response if
    either login or password is not provided or 401 if the provided credentials are incorrect.

Authentication used to gain Rest API session.

Logout
~~~~~~

To log out request with given session ID.

Request type: **DELETE**

Request path: *API_HOME*/sessions/**{sid}**

Return data:

    The API will return a 200 response if log out succeed.

Objects
-------

Get multiple objects with filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to get all objects available to this user or to get objects that fulfill
filter requirements and are available to this user.

Request type: **GET**

Request path: *API_HOME*/objects

Filter options:

    * area=\ *geographical area*
    * class=\ *comma-separated class list*
    * name=\ *pattern or regex, if useRegex=true*
    * parent=\ *parent object id*
    * topLevelOnly=\ *boolean - select top level objects only. false by default*
    * useRegex=\ *boolean - treat name and custom attribute value as regex. false by default*
    * zone=\ *comma-separated list of zone UINs*
    * @custom_attribute_name=\ *pattern or regex, if useRegex=true*

Return data:

    Will return filtered objects or all objects available to user.

Get object by id
~~~~~~~~~~~~~~~~

Request to get exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**

Return data:

    Object information identified by provided ID or GUID.

Create object
~~~~~~~~~~~~~

Request to create new object.

Request type: **POST**

JSON data:

  JSON object can contain fields form 2 filed entities: 

    * :ref:`creation-fields`
    * :ref:`modification-fields`

  Minimal JSON for node creation under "Infrastructure Services" object:

  .. code-block:: json

      {"objectType": 2, "name":"testNode", "parentId": 2, "primaryName":"10.5.0.12" }

  Minimal JSON for container creation under "Infrastructure Services" object:

  .. code-block:: json

      {"objectType": 5, "name":"New container", "parentId": 2}

Request path: *API_HOME*/objects

Return data:

    New object ID.

  .. code-block:: json

    { "id": 15130 }

Update object
~~~~~~~~~~~~~

Request to update object.

Request type: **PATCH**

Request path: *API_HOME*/objects/**{object-id}**

JSON data:

  JSON object can contain :ref:`modification-fields`.

  Fields that are not set will not be updated. Array elements will be replaced fully (if new array does not contain old elements - they will be deleted).

  Json to update object's custom attributes (json should contain all custom attributes, attributes that are not part of JSON will be deleted):

  .. code-block:: json

    {
      "customAttributes": {
          "test attr2": {
              "value": "new value"
          },
          "test attr": {
              "value": "new value"
          }
      }
    }


Get object by id
~~~~~~~~~~~~~~~~

Request to delete object.

Request type: **DELETE**

Request path: *API_HOME*/objects/**{object-id}**

Return data:

    Object information identified by provided ID or GUID.

.. _creation-fields:

Creation fields
~~~~~~~~~~~~~~~
This list represents all fields that are object creation fields. Note that this is common list for any type of object.

.. list-table::
   :widths: 21 21 34
   :header-rows: 1

   * - Field name
     - Type
     - Comment
   * - objectType
     - Integer
     - Possible options:
  
       * SUBNET: 1
       * NODE: 2
       * INTERFACE: 3
       * NETWORK: 4
       * CONTAINER: 5
       * ZONE: 6
       * SERVICEROOT: 7
       * TEMPLATE: 8
       * TEMPLATEGROUP: 9
       * TEMPLATEROOT: 10
       * NETWORKSERVICE: 11
       * VPNCONNECTOR: 12
       * CONDITION: 13
       * CLUSTER: 14
       * OBJECT_BUSINESSSERVICE_PROTOTYPE: 15
       * NETWORKMAPROOT: 19
       * NETWORKMAPGROUP: 20
       * NETWORKMAP: 21
       * DASHBOARDROOT: 22
       * DASHBOARD: 23
       * BUSINESSSERVICEROOT: 27
       * BUSINESSSERVICE: 28
       * NODELINK: 29
       * SLMCHECK: 30
       * MOBILEDEVICE: 31
       * RACK: 32
       * ACCESSPOINT: 33
       * CHASSIS: 35
       * DASHBOARDGROUP: 36
       * SENSOR: 37  
   * - name
     - String
     - Object name
   * - parentId
     - Long
     - Parent object id this object to be created under
   * - comments
     - String
     - Object comment
   * - creationFlags
     - Integer
     - Bit flags for object creation. Possible options:

       * DISABLE ICMP: 0x0001
       * DISABLE NXCP: 0x0002
       * DISABLE SNMP: 0x0004
       * CREATE UNMANAGED: 0x0008
       * ENTER MAINTENANCE: 0x0010
       * AS ZONE PROXY: 0x0020
       * DISABLE ETHERNET IP: 0x0040
       * SNMP SETTINGS LOCKED: 0x0080
       * EXTERNAL GATEWAY: 0x0100
   * - primaryName
     - String
     - Node primary name (IP address or dns name)
   * - agentPort
     - Integer
     - Node agent port
   * - snmpPort
     - Integer
     - Node SNMP port
   * - etherNetIpPort
     - Integer
     - Node ethernetIP port
   * - sshPort
     - Integer
     - Node ssh port
   * - ipAddress
     - String
     - Interface IP address
   * - agentProxyId
     - Long
     - Node agent proxy id
   * - snmpProxyId
     - Long
     - Node SNMP proxy id
   * - etherNetIpProxyId
     - Long
     - Node ethernetIP proxy id
   * - icmpProxyId
     - Long
     - Node ICMP proxy id
   * - sshProxyId
     - Long
     - Node ssh proxy id
   * - mapType
     - Integer
     - Network map type
   * - seedObjectIds
     - Long[]
     - Network map seed objects
   * - zoneUIN
     - Integer
     - Subnet/Node/Zone zone UIN
   * - serviceType
     - Integer
     - Network service types: 
      
       * CUSTOM: 0
       * SSH: 1
       * POP3: 2
       * SMTP: 3
       * FTP: 4
       * HTTP: 5
       * HTTPS: 6
       * TELNET: 7
   * - ipPort
     - Integer
     - Network Service IP port
   * - request
     - String
     - Network Service request
   * - response
     - String
     - Network Service response
   * - linkedNodeId
     - Long
     - Linked object for Node Link object
   * - template
     - Boolean
     - If service check object is template 
   * - macAddress
     - String
     - Interface or sensor MAC address
   * - ifIndex
     - Integer
     - Interface index
   * - ifType
     - Integer
     - Interface type
   * - module
     - Integer
     - Interface module number
   * - port
     - Integer
     - Interface port
   * - physicalPort
     - Boolean
     - IF interface has physical port
   * - createStatusDci
     - Boolean
     - IF status DCI should be created for network service
   * - deviceId
     - String
     - Mobile device ID
   * - height
     - Integer
     - Rack height
   * - controllerId
     - Long
     - Chassis controller node id
   * - sshLogin
     - String
     - Node ssh login
   * - sshPassword
     - String
     - Node password
   * - deviceClass
     - Integer
     - Sensor device class
   * - vendor
     - String
     - Sensor vendor
   * - commProtocol
     - Integer
     - Sensor communication protocol
   * - xmlConfig
     - String
     - Sensor XML config
   * - xmlRegConfig
     - String
     - Sensor XML registration config
   * - serialNumber
     - String
     - Sensor serial number
   * - deviceAddress
     - String
     - Sensor device address
   * - metaType
     - String
     - Sensor meta type
   * - description
     - String
     - Sensor description
   * - sensorProxy
     - Long
     - Sensor proxy node id
   * - instanceDiscoveryMethod
     - Business service instance discovery method     
     - Possible values:
      
        * IDM_AGENT_LIST - 1
        * IDM_AGENT_TABLE - 2
        * IDM_SCRIPT - 5


.. _modification-fields:

Modification fields
~~~~~~~~~~~~~~~~~~~

.. note::

  Starting from version 4 isAutoBindEnabled and isAutoUnbindEnabled replaced by autoBindFlags

.. list-table::
   :widths: 21 21 34
   :header-rows: 1

   * - Field name
     - Type
     - Comment
   * - name
     - String
     -
   * - primaryName
     - String
     -
   * - alias
     - String
     -
   * - nameOnMap
     - String
     -
   * - acl
     - :ref:`AccessListElement <access-list-element-fields>`\ []
     - inheritAccessRights should be provided in the same request
   * - inheritAccessRights
     - Boolean
     - acl should be provided in the same request
   * - customAttributes 
     - JSON object {String: :ref:`CustomAttribute<custom-attribute-element-fields>`}
     - Object name is custom attribute name and value is in :ref:`CustomAttribute<custom-attribute-element-fields>` object
   * - autoBindFilter
     - String
     -
   * - version
     - Integer
     -
   * - description
     - String
     -
   * - agentPort
     - Integer
     -
   * - agentSecret
     - String
     -
   * - agentProxy
     - Long
     -
   * - snmpPort
     - Integer
     -
   * - snmpVersion
     - String
     - Node SNMP version:
      
       * V1
       * V2C
       * V3
       * DEFAULT
   * - snmpAuthMethod
     - Integer
     - snmpAuthName, snmpAuthPassword, snmpPrivPassword, snmpPrivMethod should be provided in the same request
   * - snmpPrivMethod
     - Integer
     - snmpAuthName, snmpAuthPassword, snmpPrivPassword, snmpAuthMethod should be provided in the same request
   * - snmpAuthName
     - String
     - snmpAuthPassword, snmpPrivPassword, snmpAuthMethod, snmpPrivMethod should be provided in the same request
   * - snmpAuthPassword
     - String
     - snmpAuthName, snmpPrivPassword, snmpAuthMethod, snmpPrivMethod should be provided in the same request
   * - snmpPrivPassword
     - String
     - snmpAuthName, snmpAuthPassword, snmpAuthMethod, snmpPrivMethod should be provided in the same request
   * - snmpProxy
     - Long
     -
   * - icmpProxy
     - Long
     -
   * - trustedNodes
     - Long[]
     -
   * - geolocation
     - :ref:`Geolocation <geolocation-fields>`
     -
   * - mapBackground
     - String
     - UUID.
       
       mapBackgroundLocation, mapBackgroundLocation, mapBackgroundZoom, mapBackgroundColor should be provided in the same request.
   * - mapBackgroundLocation
     - :ref:`Geolocation <geolocation-fields>`
     - mapBackground, mapBackgroundLocation, mapBackgroundZoom, mapBackgroundColor should be provided in the same request.
   * - mapBackgroundZoom
     - Integer
     - mapBackground, mapBackgroundLocation, mapBackgroundLocation, mapBackgroundColor should be provided in the same request.
   * - mapBackgroundColor
     - Integer
     - mapBackground, mapBackgroundLocation, mapBackgroundLocation, mapBackgroundZoom should be provided in the same request.
   * - mapImage
     - String
     - UUID
   * - columnCount
     - Integer
     -
   * - script
     - String
     -
   * - activationEvent
     - Integer
     -
   * - deactivationEvent
     - Integer
     -
   * - sourceObject
     - Long
     -
   * - activeStatus
     - Integer
     -
   * - inactiveStatus
     - Integer
     -
   * - drillDownObjectId
     - Long
     -
   * - pollerNode
     - Long
     -
   * - requiredPolls
     - Integer
     -
   * - serviceType
     - Integer
     -
   * - ipProtocol
     - Integer
     -
   * - ipPort
     - Integer
     -
   * - ipAddress
     - String
     - Network service IP address
   * - request
     - String
     - Network service IP request
   * - response
     - String
     - Network service IP response
   * - objectFlags
     - Integer
     - Object flags specific for each object. Possible values can be found in NXSL documentation under each object. (Example: `Node flags <https://www.netxms.org/documentation/nxsl-latest/#_constants_6>`_) 
       
       objectFlagsMask should be provided in the same request. 
   * - objectFlagsMask
     - Integer
     - Bitmask that defines which bits in objectFlags will have effect. objectFlags should be provided in the same request.
   * - ifXTablePolicy
     - Integer
     -
   * - reportDefinition
     - String
     -
   * - networkList
     - String[]
     - IP address list
   * - statusCalculationMethod
     - Integer
     -
   * - statusPropagationMethod
     - Integer
     -
   * - fixedPropagatedStatus
     - String
     - Object status: 
      
       * NORMAL
       * WARNING
       * MINOR
       * MAJOR
       * CRITICAL
       * UNKNOWN
       * UNMANAGED
       * DISABLED
       * TESTING
   * - statusShift
     - Integer
     -
   * - statusTransformation
     - ObjectStatus[]
     - Object status mapping list. Possible values:
      
       * NORMAL
       * WARNING
       * MINOR
       * MAJOR
       * CRITICAL
       * UNKNOWN
       * UNMANAGED
       * DISABLED
       * TESTING
   * - statusSingleThreshold
     - Integer
     -
   * - statusThresholds
     - Integer[]
     -
   * - expectedState
     - Integer
     -
   * - linkColor
     - Integer
     -
   * - connectionRouting
     - Integer
     -
   * - discoveryRadius
     - Integer
     -
   * - height
     - Integer
     -
   * - filter
     - String
     -
   * - peerGatewayId
     - Long
     -
   * - localNetworks
     - String[]
     - VPN networks IP address. remoteNetworks should be provided in the same request.
   * - remoteNetworks
     - String[]
     - VPN networks IP address. localNetworks should be provided in the same request.
   * - postalAddress
     - :ref:`PostalAddress<postal-address-fields>`
     -
   * - agentCacheMode
     - String
     - Possible values:
      
        * DEFAULT
        * ON
        * OFF
   * - agentCompressionMode
     - String
     - Possible values:
      
        * DEFAULT
        * ENABLED
        * DISABLED
   * - mapObjectDisplayMode
     - String
     - Possible values:
      
        * ICON
        * SMALL_LABEL
        * LARGE_LABEL
        * STATUS
        * FLOOR_PLAN
   * - physicalContainerObjectId
     - Long
     -
   * - rackImageFront
     - String
     - UUID. 
       
       rackImageRear, rackPosition, rackHeight, rackOrientation should be provided in the same request.
   * - rackImageRear
     - String
     - UUID. 
       
       rackImageFront, rackPosition, rackHeight, rackOrientation should be provided in the same request.
   * - rackPosition
     - Short
     - rackImageFront, rackImageRear, rackHeight, rackOrientation should be provided in the same request.
   * - rackHeight
     - Short
     - rackImageFront, rackImageRear, rackPosition, rackOrientation should be provided in the same request.
   * - rackOrientation
     - String
     - Possible values:
      
        * FILL
        * FRONT
        * REAR

       rackImageFront, rackImageRear, rackPosition, rackHeight should be provided in the same request.
   * - dashboards
     - Long[]
     -
   * - rackNumberingTopBottom
     - Boolean
     -
   * - controllerId
     - Long
     -
   * - chassisId
     - Long
     -
   * - sshProxy
     - Long
     -
   * - sshLogin
     - String
     -
   * - sshPassword
     - String
     -
   * - sshPort
     - Integer
     -
   * - sshKeyId
     - Integer
     -
   * - zoneProxies
     - Long[]
     -
   * - urls
     - ObjectUrl[]
     -
   * - seedObjectIds
     - Long[]
     -
   * - macAddress
     - String
     - Sensor mac address
   * - deviceClass
     - Integer
     -
   * - vendor
     - String
     -
   * - serialNumber
     - String
     -
   * - deviceAddress
     - String
     -
   * - metaType
     - String
     -
   * - sensorProxy
     - Long
     -
   * - xmlConfig
     - String
     -
   * - snmpPorts
     - String[]
     -
   * - responsibleUsers
     - Long[]
     -
   * - icmpStatCollectionMode
     - String
     - Possible values:
      
        * DEFAULT
        * ON
        * OFF
   * - icmpTargets
     - String[]
     - ICMP ping targets IP addresses 
   * - chassisPlacement
     - String
     -
   * - etherNetIPPort
     - Integer
     -
   * - etherNetIPProxy
     - Long
     -
   * - certificateMappingMethod
     - String
     - Possible values:
      
        * SUBJECT
        * PUBLIC_KEY
        * COMMON_NAME
        * TEMPLATE_ID

       certificateMappingData should be provided in the same request. 
   * - certificateMappingData
     - String
     - certificateMappingMethod should be provided in the same request. 
   * - categoryId
     - Integer
     -
   * - geoLocationControlMode
     - GeoLocationControlMode
     - Possible values:
      
        * NO_CONTROL
        * RESTRICTED_AREAS
        * ALLOWED_AREAS
   * - geoAreas
     - long[]
     -
   * - instanceDiscoveryMethod
     - Business service instance discovery method     
     - Possible values:
      
        * IDM_AGENT_LIST - 1
        * IDM_AGENT_TABLE - 2
        * IDM_SCRIPT - 5
   * - instanceDiscoveryData
     - Business service instance discovery data     
     - 
   * - instanceDiscoveryFilter
     - Business service instance discovery data filtering script     
     - 
   * - autoBindFilter2
     - Second binding script used for DCI binding. Currently used in business service
     - 
   * - autoBindFlags
     - Auto bind bit flags     
     - First script is currently used for object bind/unbind, second for dci bind/unbind. Possible values:
      
        * First script for auto bind is enabled - 0x0001
        * First script for auto unbind is enabled - 0x0002
        * Second script for auto bind is enabled - 0x0004
        * Second script for auto unbind is enabled - 0x0008
   * - objectStatusThreshold
     - Business service default threshold for auto created object checks    
     - Possible values:
      
        * Default - 0
        * Warning - 1 
        * Minor - 2 
        * Major - 3 
        * Critical - 4 
   * - dciStatusThreshold
     - Business service default threshold for auto created DCI checks    
     - Possible values:
      
        * Default - 0
        * Warning - 1 
        * Minor - 2 
        * Major - 3 
        * Critical - 4 
   * - sourceNode
     - Id of source node for business service instance discovery methods    
     - 

.. _geolocation-fields:

GeoLocation fields
~~~~~~~~~~~~~~~~~~

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - type
    - Integer
    - Available options:
     
      * UNSET: 0
      * MANUAL: 1
      * GPS: 2
      * NETWORK: 3
  * - latitude
    - Double
    -
  * - longitude
    - Double
    -
  * - accuracy
    - int
    -	Location accuracy in meters
  * - timestamp
    - Integer
    - UNIX timestamp

.. _access-list-element-fields:

AccessListElement fields
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - userId
    - Long
    -
  * - accessRights
    - Integer
    - Bit flag field. Available options:
     
      * OBJECT ACCESS READ: 0x00000001
      * OBJECT ACCESS MODIFY: 0x00000002
      * OBJECT ACCESS CREATE: 0x00000004
      * OBJECT ACCESS DELETE: 0x00000008
      * OBJECT ACCESS READ ALARMS: 0x00000010
      * OBJECT ACCESS ACL: 0x00000020
      * OBJECT ACCESS UPDATE ALARMS: 0x00000040
      * OBJECT ACCESS SEND EVENTS: 0x00000080
      * OBJECT ACCESS CONTROL: 0x00000100
      * OBJECT ACCESS TERM ALARMS: 0x00000200
      * OBJECT ACCESS PUSH DATA: 0x00000400
      * OBJECT ACCESS CREATE ISSUE: 0x00000800
      * OBJECT ACCESS DOWNLOAD: 0x00001000
      * OBJECT ACCESS UPLOAD: 0x00002000
      * OBJECT ACCESS MANAGE FILES: 0x00004000
      * OBJECT ACCESS MAINTENANCE: 0x00008000
      * OBJECT ACCESS READ AGENT: 0x00010000
      * OBJECT ACCESS READ SNMP: 0x00020000
      * OBJECT ACCESS SCREENSHOT: 0x00040000

.. _custom-attribute-element-fields:

CustomAttribute fields
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - value
    - String
    - Attribute value
  * - flags
    - Long
    - Available options:
     
      * INHERITABLE: 1

.. _postal-address-fields:

PostalAddress fields
~~~~~~~~~~~~~~~~~~~~

.. list-table::
  :widths: 21 21 34
  :header-rows: 1

  * - Field name
    - Type
    - Comment
  * - country
    - String
    -
  * - city
    - String
    -
  * - streetAddress
    - String
    -
  * - postcode
    - String
    - 

Bind object
~~~~~~~~~~~

Request to bind object to container. Container id is specified in URL, object id in JSON.

Request type: **POST**

JSON data:

  Bind object to object in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/bind


Bind node to
~~~~~~~~~~~~

Request to bind object under container. Container id is specified in JSON, object id in URL. 

Request type: **POST**

JSON data:

  Bind object in URL to "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/bind-to

Unbind node
~~~~~~~~~~~

Request to unbind object from container. Container id is specified in URL, object id in JSON.

Request type: **POST**

JSON data:

  Unbind object from container in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/unbind


UnbindFrom node
~~~~~~~~~~~~~~~

Request to unbind object from container. Container id is specified in JSON, object id in URL. 

Request type: **POST**

JSON data:

  Unbind object in URL from "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/unbind-from


Poll object
~~~~~~~~~~~

Create object poll request

Request type: **POST**

JSON data:

  .. code-block:: json

      {"type": "status"}

One of the following poll types:

  * configuration full
  * configuration
  * discovery
  * interface
  * status
  * topology

Request path: *API_HOME*/objects/**{object-id}**/polls

Return data:

  Will return UUID of request, that should be used to get request output and request type.

  .. code-block:: json

    { "id": 15130,
      "type": "status" }


Get object poll data
~~~~~~~~~~~~~~~~~~~~

Get object poll request data 

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/polls/output/**{request-UUID}**

Return data:

  Will return request output data.

  .. code-block:: json

    { "streamId": 0,
      "completed": false,
      "message": "Poll request accepted..." }


Change object zone
~~~~~~~~~~~~~~~~~~

.. versionadded:: 4.4.4

Request to move object to new zone. Zone UIN is specified in JSON, object id in URL. 

Request type: **POST**

JSON data:

  Move object specified in URL to "Default" zone:

  .. code-block:: json

      {"zoneUIN": 0}

Request path: *API_HOME*/objects/**{object-id}**/change-zone


Business Services
-----------------

Get checks
~~~~~~~~~~

Request all business service checks

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/checks

Create new check
~~~~~~~~~~~~~~~~

Create new business service check

Request type: **POST**

Request path: *API_HOME*/objects/**{object-id}**/checks

JSON data:

  Create new script business service check:

  .. code-block:: json

      {
          "checkType": "SCRIPT",
          "description": "Web created script",
          "script": "return OK;",
          "objectId": 0,
          "dciId": 0,
          "threshold": 0
       }


Update existing check
~~~~~~~~~~~~~~~~~~~~~

Update existing business service check

Request type: **PUT**

Request path: *API_HOME*/objects/**{object-id}**/checks/**check-id**

JSON data:

  Update existing business service check to object check with object ID "166":

  .. code-block:: json

      {
          "checkType": "OBJECT",
          "description": "Web created script",
          "script": "return OK;",
          "objectId": 166,
          "dciId": 0,
          "threshold": 0
      }


Delete existing check
~~~~~~~~~~~~~~~~~~~~~

Delete existing business service check

Request type: **DELETE**

Request path: *API_HOME*/objects/**{object-id}**/checks/**check-id**


Get tickets
~~~~~~~~~~~

Get ticket list for given time range. 

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/tickets

Time range can be requested in 2 ways.

First option is back from now with given parameters:

    * timeUnit=\ *Type of time range. Possible values: MINUTE, HOUR, DAY*
    * timeRage=\ *Range in given units*

Second option is fixe time range:

    * start=\ *UNIX timestamp*
    * end=\ *UNIX timestamp*


Get uptime
~~~~~~~~~~

Get uptime for given time range. 

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/uptime

Time range can be requested in 2 ways.

First option is back from now with given parameters:

    * timeUnit=\ *Type of time range. Possible values: MINUTE, HOUR, DAY*
    * timeRage=\ *Range in given units*

Second option is fixe time range:

    * start=\ *UNIX timestamp*
    * end=\ *UNIX timestamp*

Alarms
------

Full scope of currently active alarms can be obtained or object specific list.

Get multiple alarms with filters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to get all active alarms available to this user or to get active alarms that fulfill
filter requirements and are available to this user.

Request type: **GET**

Request path: *API_HOME*/alarms

Filter options:

    * alarm=\ *list of alarm states. Possible values: outstanding, acknowledged, resolved*
    * createdBefore=\ *UNIX timestamp*
    * createdAfter=\ *UNIX timestamp*
    * objectId=\ *ID or related object*
    * objectGuid=\ *GUID or related object*
    * includeChildObjects=\ *boolean. Set to true to get alarms of container child objects*
    * resolveReferences=\ *resolve IDs into human readable data*
    * updatedBefore=\ *UNIX timestamp*
    * updatedAfter=\ *UNIX timestamp*

Return data:

    Will return filtered active alarms or all active alarms available to user.

Alarm by id
~~~~~~~~~~~

Request to get an alarm by it's ID.

Request type: **GET**

Request path: *API_HOME*/alarms/**{alarm-id}**

Return data:

    Will return alarm specified by ID.


Data collection configuration
-----------------------------

Get data collection configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/data-collection

Filter options (all are case-insensitive):

    * dciName=\ *text that name should contain*
    * dciNameRegexp=\ *regular expression for name*
    * dciDescription=\ *text that description should contain*
    * dciDescriptionRegexp=\ *regular expression for description*

Return data:

    Will return data collection configuration.


Create DCI
~~~~~~~~~~

Request type: **POST**

Request path: *API_HOME*/objects/**{object-id}**/data-collection

JSON data:

  Create new DCI (name, description and valueType are obligatory fields):

  .. code-block:: json

      {
          "name": "Agent.Version",
          "description": "Version of agent",
          "origin": "AGENT",
          "pollingInterval": "120",
          "pollingScheduleType": "1",
          "retentionType": "1",
          "retentionTime": "60",
          "valueType" : "single"
      }

.. note::

  valueType should be one of the following:
  * single
  * table

Update DCI
~~~~~~~~~~

Request to get last values of DCI identified by ID for exact object identified by ID or GUID.

Request type: **PUT**

Request path: *API_HOME*/objects/**{object-id}**/data-collection/**{dci-id}**

JSON data:

  Update existing DCI setting custom polling interval and custom retention time
  (name and description are obligatory fields):

  .. code-block:: json

      {
          "name": "Agent.Version",
          "description": "Version of agent",
          "pollingInterval": "120",
          "pollingScheduleType": "1",
          "retentionType": "1",
          "retentionTime": "60"
      }


DCI data
--------

DCI values
~~~~~~~~~~

Request to get last values of DCI identified by ID for exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/data-collection/**{dci-id}**/values

Filter options:

    * from=\ *requested period start time as unix timestamp*
    * to=\ *requested period end time as unix timestamp*
    * timeInterval=\ *requested time interval in seconds*
    * itemCount=\ *number of items to be returned*

Return data:

    Will return DCI values for requested node limited by filters.


DCI last value
~~~~~~~~~~~~~~

Request to get last value of DCI identified by ID for exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/data-collection/**{dci-id}**/last-value

Filter options:

    * rowsAsObjects=\ *true or false. Determines how table DCI is returned*

Return data:

    Will return last value of DCI.


Object last values
~~~~~~~~~~~~~~~~~~

Request to get DCI last values of object.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/last-values

Filter options (all are case-insensitive):

    * dciName=\ *text that name should contain*
    * dciNameRegexp=\ *regular expression for name*
    * dciDescription=\ *text that description should contain*
    * dciDescriptionRegexp=\ *regular expression for description*

Return data:

    Will return DCI last values of object.


Query last values
~~~~~~~~~~~~~~~~~

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/data-collection//query?query=**{filter string}**

Filter string options:
    * NOT *negation of following filtering parameter*
    * Description
    * GUID
    * Id
    * Name
    * PollingInterval
    * RetentionTime
    * SourceNode

Example filter string:

    Name:FileSystem.UsedPerc PollingInterval:60


Adhoc summary table
~~~~~~~~~~~~~~~~~~~

Option to get last values for multiple nodes(for all nodes under provided container) for the same DCIs. Required DCIs and container are provided in request.

Request type: **POST**

Request path: *API_HOME*/summary-table/ad-hoc

POST request JSON

.. code-block:: json

    {
        "baseObject":"ContainerName",
        "columns": [
            {
            "columnName":"Free form name that will be used in return table for this column",
            "dciName":"Name of DCI, that will be used for filtering"
            },
            {
            "columnName":"Name2",
            "dciName":"DCIName2"
            }
        ]
    }

Return data:

    Will return adhoc summary table configured accordingly to request json.

Object tools
------------

List of available object tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to object tools available to specified object.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/object-tools


Execute object tool
~~~~~~~~~~~~~~~~~~~

Request to object tools available to specified object.

Request type: **POST**

Request path: *API_HOME*/objects/**{object-id}**/object-tools

JSON data:

  .. code-block:: json

    {
      "toolData":{
          "id": "1234",
          "inputFields":{
            "field1": "value1",
            "field2": "1000"
          } 
      }
    }

Return data:

    Will return JSON with UUID and toolId. UUID can be supplied to this endpoint (with GET request)
    to view object tool output:
    *API_HOME*/objects/**{object-id}**/object-tools/output/**{uuid}**. With POST
    request to the same endpoint execution of object tool can be stopped. 




Persistent storage
------------------

Get all persistent storage variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to get all persistent storage variables available to this user.

Request type: **GET**

Request path: *API_HOME*/persistent-storage

Return data:

    Will return all persistent storages in "*key*":"*value*" format.


Get persistent storage variable by key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to get persistent storage value by key.

Request type: **GET**

Request path: *API_HOME*/persistent-storage/**{key}**

Return data:

    Will return corresponding persistent storages value in "value":"*value*" format.


Create persistent storage variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to create new persistent storage variable.

Request type: **POST**

JSON data:

  JSON object should contain two fields: key and value.

  .. code-block:: json

      {"key": "a"}
      {"value": "10"}

Request path: *API_HOME*/persistentstorage

Return data:

    Will return newly created persistent storages in "*key*":"*value*" format.


Update persistent storage variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to update specified persistent storage variable value.

Request type: **PUT**

JSON data:

  JSON object should contain one field: new value.

  .. code-block:: json

      {"value": "10"}

Request path: *API_HOME*/persistentstorage/**{key}**

Return data:

    Will return updated persistent storages in "*key*":"*value*" format.


Delete persistent storage variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Request to delete persistent storage variable.

Request type: **DELETE**

Request path: *API_HOME*/persistentstorage/**{key}**


User agent notifications
------------------------

TODO


Push DCI data
-------------

Request to push values for one or multiple DCIs. Node and DCI can be specified
either by id or by name. If both id and name are provided, id has priority. 

Request type: **POST**

JSON data:

  To send value for one DCI JSON object should contain the following:

  .. code-block:: json

      {
        "nodeId" : 10,
        "dciId" : 20,
        "value" : "Value"
      }


  Or, alternatively using node and DCI names:

  .. code-block:: json

      {
        "nodeName" : "Node name",
        "dciName" : "DCI name",
        "value" : "Value"
      }


  To send value for several DCIs JSON object should contain an array:

  .. code-block:: json

      [
        {
          "nodeId" : 10,
          "dciId" : 20,
          "value" : "Value"
        },
        {
          "nodeName" : "Node name",
          "dciName" : "DCI name",
          "value" : "Value"
        }
      ]

Request path: *API_HOME*/pushData


Predefined graphs
-----------------

TODO

