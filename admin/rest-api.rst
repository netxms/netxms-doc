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
3. Create a :file:`nxapisrv.properties` file and place it in the property file location of your
   web server and specify the |product_name| Server address with the property.

Localhost address will be used if no address was set. Server configuration example:

   .. code-block:: cfg

        netxms.server.address=sever.office.radensolutions.com

If the server is running on a non-standard port, specify it with the following property:

  .. code-block:: cfg

    netxms.server.port=

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
     - Ingeger
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
     - Ingeger
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
     - Ingeger
     - Node agent port
   * - snmpPort
     - Ingeger
     - Node SNMP port
   * - etherNetIpPort
     - Ingeger
     - Node ethernetIP port
   * - sshPort
     - Ingeger
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
     - Ingeger
     - Network map type
   * - seedObjectIds
     - Long[]
     - Network map seed objects
   * - zoneUIN
     - Ingeger
     - Subnet/Node/Zone zone UIN
   * - serviceType
     - Ingeger
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
     - Ingeger
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
     - Ingeger
     - Interface index
   * - ifType
     - Ingeger
     - Interface type
   * - module
     - Ingeger
     - Interface module number
   * - port
     - Ingeger
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
     - Ingeger
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
     - Ingeger
     - Sensor device class
   * - vendor
     - String
     - Sensor vendor
   * - commProtocol
     - Ingeger
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
     -
   * - inheritAccessRights
     - Boolean
     -
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
     -
   * - snmpPrivMethod
     - Integer
     -
   * - snmpAuthName
     - String
     -
   * - snmpAuthPassword
     - String
     -
   * - snmpPrivPassword
     - String
     -
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
     - UUID
   * - mapBackgroundLocation
     - :ref:`Geolocation <geolocation-fields>`
     -
   * - mapBackgroundZoom
     - Integer
     -
   * - mapBackgroundColor
     - Integer
     -
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
     - VPN networks IP adress 
   * - remoteNetworks
     - String[]
     - VPN networks IP adress 
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
     - UUID
   * - rackImageRear
     - String
     - UUID
   * - rackPosition
     - Short
     -
   * - rackHeight
     - Short
     -
   * - rackOrientation
     - String
     - Possible values:
      
        * FILL
        * FRONT
        * REAR
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
   * - certificateMappingData
     - String
     -
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
     - Second binding script used for DCI binding. Urrently used in business service     
     - 
   * - autoBindFlags
     - Auto bind bit flags     
     - Firs script is currently used for object bind/unbind, second for dci bind/unbind. Possible values:
      
        * First script for auto bind is enabeled - 0x0001
        * First script for auto unbind is enabeled - 0x0002
        * Second script for auto bind is enabeled - 0x0004
        * Second script for auto unbind is enabeled - 0x0008
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

Bind node
~~~~~~~~~

Request to bind object to container.

Request type: **POST**

JSON data:

  Bind object to object in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/bind


Bindto node
~~~~~~~~~~~

Request to bind object under container.

Request type: **POST**

JSON data:

  Bind object in URL to "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/bindTo

Unbind node
~~~~~~~~~~~

Request to unbind object from container.

Request type: **POST**

JSON data:

  Unbind object from container in URL:

  .. code-block:: json

      {"id": 15130}

Request path: *API_HOME*/objects/**{object-id}**/unbind


UnbindFrom node
~~~~~~~~~~~~~~~

Request to unbind object from container.

Request type: **POST**

JSON data:

  Unbind object in URL from "Infrastructure service":

  .. code-block:: json

      {"id": 2}

Request path: *API_HOME*/objects/**{object-id}**/unbindFrom


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

Business Services
-----------------

Get checks
~~~~~~~~~~

Request all business service checks

Request type: **GET**

Request path: *API_HOME*/**{object-id}**/checks

Create new check
~~~~~~~~~~~~~~~~

Create new business service check

Request type: **POST**

Request path: *API_HOME*/**{object-id}**/checks

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

Request path: *API_HOME*/**{object-id}**/checks/**check-id**

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


Update existing check
~~~~~~~~~~~~~~~~~~~~~

Delete existing business service check

Request type: **DELETE**

Request path: *API_HOME*/**{object-id}**/checks/**check-id**


Get tickets
~~~~~~~~~~~

Get ticket list for given time range. 

Request type: **GET**

Request path: *API_HOME*/**{object-id}**/tickets

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

Request path: *API_HOME*/**{object-id}**/uptime

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

DCI Data
--------

There are 2 options to get DCI last values. First is to get last values for one DCI and the second one is to create adhoc summary table with required values for all nodes under container.

DCI last values
~~~~~~~~~~~~~~~

Request to get last values of DCI identified by ID for exact object identified by ID or GUID.

Request type: **GET**

Request path: *API_HOME*/objects/**{object-id}**/datacollection/**{dci-id}**/values

Filter options:

    * from=\ *requested period start time as unix timestamp*
    * to=\ *requested period end time as unix timestamp*
    * timeInterval=\ *requested time interval in seconds*
    * itemCount=\ *number of items to be returned*

Return data:

    Will return last values for requested node and DCI limited by filters.

Adhoc summary table
~~~~~~~~~~~~~~~~~~~

Option to get last values for multiple nodes(for all nodes under provided container) for the same DCIs. Required DCIs and container are provided in request.

Request type: **POST**

Request path: *API_HOME*/summaryTable/adHoc

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
