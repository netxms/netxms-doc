########
Appendix
########

.. _sms-drivers:

SMS Drivers
===========
NetXMS supports concept of SMS drivers to provide SMS sending functionality. Role of SMS driver 
is to provide level of abstraction on top of different SMS sending mechanisms and uniform SMS 
sending interface for server core. The following drivers are provided by default with NetXMS installation:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Driver
     - Description
   * - dummy.sms
     - Dummy driver for debugging purposes. Do not send actual SMS and only logs them in server log file.
   * - generic.sms
     - Driver for serial or USB attached GSM modems with support for standard GSM AT command set.
   * - kannel.sms
     - Driver for Kannel SMS gateway (`<http://www.kannel.org>`_).
   * - portech.sms
     - Driver for Portech MV-372 and MV-374 GSM gateways (`<https://www.portech.com.tw/p3-product1_1.asp?Pid=14>`_).
   * - websms.sms
     - Driver for websms.ru service (`<https://websms.ru>`_).

To load SMS driver set server configuration parameter :guilabel:`SMSDriver` to name of SMS driver module. On startup 
SMS driver read it's configuration from server configuration parameter :guilabel:`SMSDrvConfig`. Meaning of that 
parameter is driver dependent and described separately for each driver.

Generic GSM modem driver
------------------------

Driver configuration is a string in format *port*:*speed*:*databits*:*parity*:*stopbits*:*mode* where meaning of each element is following:

.. list-table::
   :widths: 20 70 10
   :header-rows: 1

   * - Element
     - Description
     - Default
   * - port 
     - Port name (for example, /dev/ttyS0 on Linux or COM1: on Windows).
     - COM1: on Windows, /dev/ttyS0 on UNIX
   * - speed    
     - Port speed in bits per second.   
     - 9600
   * - databits 
     - Number of data bits per byte (7 or 8).   
     - 8
   * - parity   
     - Parity (N for none, E for even, or O for odd).   
     - N
   * - stopbits 
     - Number of stop bits (1 or 2).    
     - 1
   * - mode 
     - SMS sending mode (P for PDU or T for TEXT).
     - T

All elements are optional and can be omitted.

**NOTE:** Set mode to PDU if you plan to send SMS with non-Latin1 characters.

Kannel SMS gateway driver
-------------------------

Driver configuration is a set of *key=value* pairs separated by semicolon. Possible key values are following:

.. list-table::
   :widths: 20 70 10
   :header-rows: 1

   * - Key
     - Description
     - Default
   * - host
     - Kannel gateway host name or IP address.
     - 127.0.0.1
   * - login
     - Login name.
     - user
   * - password
     - Password.
     - password
   * - port
     - TCP port gateway is listening on.
     - 13001

All elements are optional and can be omitted.

Portech GSM gateways driver
---------------------------

Driver configuration is a set of *key=value* pairs separated by semicolon. Possible key values are following:

.. list-table::
   :widths: 20 70 10
   :header-rows: 1
   
   * - Key
     - Description
     - Default
   * - host
     - Gateway host name or IP address.
     - 10.0.0.1
   * - login
     - Login name.
     - admin
   * - mode
     - SMS sending mode (P for PDU or T for TEXT).
     - P
   * - password
     - Password.
     - admin
   * - secondaryHost
     - Secondary gateway host name or IP address (will be used if primary gateway is not responding).
     -     

All elements are optional and can be omitted.

**NOTE:** Set mode to PDU if you plan to send SMS with non-Latin1 characters.

websms.ru driver
----------------

Driver configuration is a set of *key=value* pairs separated by semicolon. Possible key values are following:

.. list-table::
   :widths: 20 70 10
   :header-rows: 1
   
   * - Key
     - Description
     - Default
   * - login
     - Login name.
     - user
   * - password
     - Password.
     - password

All elements are optional and can be omitted.



.. _agent_configuration_file:

Agent configuration file (nxagentd.conf)
========================================

.. list-table:: 
   :widths: 15 50 15
   :header-rows: 1

   * - Parameter 
     - Description 
     - Default Value
   * - Action
     - Define action, which can be later executed by management server. See the Agent Configuration section for detailed description of this parameter.
     - No defaults
   * - ActionShellExec
     - Same as Action, but on Windows platform agent will use shell to execute command instead of normal process creation. There is no difference between Action and ActionShellExec on UNIX platforms.
     - No defaults
   * - AppAgent
     - The registered name of application with built in subagent library that can be as subagent by agent. 
     - No defaults
   * - BackgroundLogWriter
     - Enable (yes) or disable (no) log writer as separate background thread. Has no effect if logging is done through syslog or Windows Event Log.
     - no
   * - CodePage
     - Code page used by NetXMS agent. Has no effect on Windows or if agent was compiled without iconv support.
     - Depends on your system, usually ISO8859-1
   * - ControlServers
     - A list of management servers, which can execute actions on agent and change agent's config. Hosts listed in this parameter also have read access to the agent. Both IP addresses and DNS names can be used. Multiple servers can be specified in one line, separated by commas. If this parameter is used more than once, servers listed in all occurrences will have access to agent.
     - Empty list
   * - CreateCrashDumps
     - Enable (yes) or disable (no) creation of agent's crash dumps. Windows only
     - no
   * - DataDirectory
     - 
     - 
   * - DailyLogFileSuffix
     - Log file name suffix used when ``LogRotationMode`` is set to 1 (daily), can contain `strftime(3C) <http://www.unix.com/man-page/opensolaris/3c/strftime/>`_ macros
     - %Y%m%d
   * - DebugLevel
     - Set agent debug logging level (0 - 9).  Value of 0 turns off debugging, 9 enables very detailed logging.  Can also be set with command line "-D<level>" option.
     - 0
   * - DisabeIPv4
     - Disables (yes) or enables(no) IPv4 support.
     - no
   * - DisabeIPv6
     - Disables (yes) or enables(no) IPv6 support.
     - no
   * - DumpDirectory
     - Directory for storing crash dumps.
     - C:\\
   * - EnableActions
     - Enable (yes) or disable (no) action execution by agent.
     - yes
   * - EnabledCiphers
     - Controls what ciphers agent can use for connection encryption. A value for this parameter is a cipher code. To enable more than one cipher, the codes should be summed up.
       
       Possible cipher codes:
         
       - 1  - "AES-256" 
       - 2  - "BLOWFISH-256"
       - 4  - "IDEA"    
       - 8  - "3DES"    
       - 16 - "AES-128"
       - 32 - "BLOWFISH-128"
       
       Example (enable AES-256 and IDEA):
       
       **EnabledCiphers = 5**
     - 63
   * - EnableProxy
     - Enable (yes) or disable (no) agent proxy functionality.
     - no
   * - EnableSNMPProxy
     - Enable (yes) or disable (no) SNMP proxy functionality. 
     - no
   * - EnableSNMPTrapProxy
     - Enable (yes) or disable (no) SNMP Trap proxy functionality.  
     - no
   * - EnableSubagentAutoload
     - Enable (yes) or disable (no) loading of platform subagent(s).
     - yes
   * - EnableWatchdog
     - Enable (yes) or disable (no) automatic agent restart in case of unexpected shutdown.
     - no
   * - ExecTimeout
     - Timeout in milliseconds for external metric execution.
     - 2000
   * - ExternalMasterAgent
     - ID that is checked when external subagent connects to master agent. Should have same value as ``ExternalSubagent`` parameter in external subagent configuration file.  
     - No defaults
   * - ExternalList
     - Add list handled by external command. To add multiple parameters, you should use multiple``ExternalList`` entries.
     - No defaults
   * - ExternalParameter
     - Adds metric handled by external command. To add multiple parameters, you should use multiple ``ExternalParameter`` entries. 
     - No defaults
   * - ExternalParameterShellExec
     - 
     - 
   * - ExternalParametersProvider
     - Adds list of metrics that are cashed by agent and returned to server per request. Metrics should be returned in *metric=value* format each pair in new line. 
     - No defaults
   * - ExternalSubagent
     - ID of external subagent. Should be same as ``ExternalMasterAgent`` in master agent configuration file. 
     - No defaults
   * - FileStore
     - Directory to be used for storing files uploaded by management server(s).
     - :file:`/tmp` on UINX
     
       :file:`C:\\` on Windows
   * - FullCrashDumps
     - Enable (yes) or disable (no) full crash dump generation. Windows only
     - no
   * - ListenAddress
     - IP address that the agent should listen on. If 0.0.0.0 or * is specified as listen address, agent will listen on all available IP addresses.
     - 0.0.0.0
   * - ListenPort
     - TCP port to be used for incoming requests.
     - 4700
   * - LogFile
     - Agent's log file. To write log to syslog (or Event Log on Windows), use {syslog} as file name.
     - {syslog}
   * - LogHistorySize
     - Defines how many old log files should be kept after log rotation.
     - 4
   * - LogRotationMode
     - Define log rotation mode.
       Possible values are:
         
       - 0  - No rotation;
       - 1  - Daily rotation (log will be rotated every midnight);
       - 2  - Rotation by size (log will be rotated when it's size will exceed value defined by MaxLogSize parameter).
       
     - 2
   * - LogUnresolvedSymbols
     - If set to yes, all dynamically resolved symbols, which failed to be resolved, will be logged.
     - no
   * - MasterServers
     - List of management servers, which have full access to agent. Hosts listed in this group can upload files to agent and initiate agent upgrade, as well as perform any task allowed for hosts listed in Servers and ControlServers. Both IP addresses and DNS names can be used. Multiple servers can be specified in one line, separated by commas. If this parameter is used more than once, servers listed in all occurrences will have access to agent.
     - Empty list
   * - MaxLogSize
     - Maximum log size, in bytes. When log file reaches this limit, log rotation occurs. Use 0 to disable log rotation.
     - 16777216
   * - MaxSessions
     - Maximum number of simultaneous communication sessions. Possible value can range from 2 to 1024.
     - 32
   * - PlatformSuffix
     - String to be added as suffix to the value of ``System.PlatformName`` parameter.
     - Empty string
   * - RequireAuthentication
     - If set to yes, a host connected to an agent has to provide correct shared secret before issuing any command.
     - no
   * - RequireEncryption
     - If set to yes, a host connected to an agent will be forced to use encryption, and if encryption is not supported by a remote host, the connection will be dropped. If an agent was compiled without encryption support, this parameter has no effect.
     - no
   * - Servers
     - A list of management servers, which have read access to this agent. Both IP addresses and DNS names can be used. Multiple servers can be specified in one line, separated by commas. If this parameter is used more than once, servers listed in all occurrences will have access to agent.
     - Empty list
   * - SessionIdleTimeout
     - Communication session idle timeout in seconds. If an agent will not receive any command from peer within the specified timeout, session will be closed.
     - 60
   * - SharedSecret
     - Agent's shared secret used for remote peer authentication. If ``RequireAuthentication`` set to no, this parameter has no effect.
     - admin
   * - EncryptedSharedSecret
     - Agent's shared secret used for remote peer authentication, encrypted using "nxencpasswd -a". If ``RequireAuthentication`` set to no, this parameter has no effect.
     - 
   * - SNMPTimeout
     - Timeout in milliseconds for SNMP requests sent by agent
     - 3000
   * - SNMPTrapListenAddress
     - Interface address which should be used by server to listen for incoming SNMP trap connections. Use value 0.0.0.0 or * to use all available interfaces.  
     - *
   * - SNMPTrapPort
     - Port that will be used to listen SNMP traps 
     - 162
   * - StartupDelay
     - Number of seconds that agent should wait on startup before start servicing requests. This parameter can be used to prevent false reports about missing processes or failed services just after monitored system startup.
     - 0
   * - SubAgent
     - Subagent to load. To load multiple subagents, you should use multiple SubAgent parameters. Subagents will be loaded in the same order as they appear in configuration file.
     - No defaults
   * - WaitForProcess
     - If specified, an agent will pause initialization until given process starts.
     - No defaults

.. note::
  All boolean parameters understand "Yes/No", "On/Off" and "True/False" values.

  
.. _server_configuration_file:

Server configuration file (netxmsd.conf)
========================================

.. list-table:: 
  :widths: 15 50 15
  :header-rows: 1
   
  * - Parameter 
    - Description 
    - Default Value
  * - CodePage
    - Code page used by NetXMS server. Has no effect on Windows or if server was compiled without iconv support.
    - Depends on your system, usually ISO8859-1
  * - CreateCrashDumps
    - Control creation of server's crash dumps. Possible values: yes or no. Has effect only on Windows platforms.
    - No
  * - DailyLogFileSuffix
    - Log file name suffix used when ``LogRotationMode`` is set to 1 (daily), can contain `strftime(3C) <http://www.unix.com/man-page/opensolaris/3c/strftime/>`_ macros
    - %Y%m%d
  * - DataDirectory
    - Directory where server looks for compiled MIB files, keep server encryption key, etc.
    - :file:`/var/netxms` or :file:`C:\\NetXMS\\var`
  * - DBDriver
    - Database driver to be used.
    - No default value
  * - DBEncryptedPassword
    - Hashed password, as produced by "nxencpass"
    - none
  * - DBDrvParams
    - Additional driver-specific parameters.
    - Empty string
  * - DBLogin
    - Database user name.
    - netxms
  * - DBName
    - Database name (not used by ODBC driver).
    - netxms_db
  * - DBPassword
    - Database user's password.
    - Empty password
  * - DBSchema
    - Schema name
    - not set
  * - DBServer
    - Database server (ODBC source name for ODBC driver).
    - localhost
  * - DebugLevel
    - Set server debug logging level (0 - 9).  Value of 0 turns off debugging, 9 enables very detailed logging.  Can also be set with command line ``-D <level>`` option.
    - 0
  * - DumpDirectory
    - Directory for storing crash dumps.
    - "/" or "C:\"
  * - FullCrashDumps
    - Write full crash dump instead of minidump (Windows only)
    - no
  * - LibraryDirectory
    - Defines location of library folder where drivers(ndd files) are stored. It's highly recommended not to use this parameter. 
    - 
  * - ListenAddress
    - Interface address which should be used by server to listen for incoming connections. Use value 0.0.0.0 or * to use all available interfaces.
    - 0.0.0.0
  * - LogFailedSQLQueries
    - Control logging of failed SQL queries. Possible values: yes or no.
    - yes
  * - LogFile
    - Server's log file. To write log to syslog (or Event Log on Windows), use {syslog} as file name.
    - {syslog}
  * - LogHistorySize
    - Number rotated files to keep, older will be discarded
    - 4
  * - LogRotationMode
    - Define log rotation mode.
      Possible values are:
         
      - 0  - No rotation;
      - 1  - Daily rotation (log will be rotated every midnight);
      - 2  - Rotation by size (log will be rotated when it's size will exceed value defined by MaxLogSize parameter).
      
    - 2
  * - MaxLogSize
    - Maximum log file size in bytes, used only if ``LogRotationMode`` is set to 2
    - 16777216
  * - Module
    - Additional server module to be loaded at server startup. To load multiple modules, add additional Module parameters.
    - No default value
  * - PerfDataStorageDriver
    - 
    - 
  * - ProcessAffinityMask
    - Sets a processor affinity mask for the netxmsd process (Windows only). A process affinity mask is a bit vector in which each bit represents a logical processor on which the threads of the process are allowed to run. See `this MSDN article <http://msdn.microsoft.com/en-us/library/windows/desktop/ms686223%28v=vs.85%29.aspx>`_ for more details.
    - 0xFFFFFFFF

.. note::
  All boolean parameters understand "Yes/No", "On/Off" and "True/False" values.
  

.. _server_configuration_parameters:

Server configuration parameters
===============================

.. list-table:: 
  :widths: 15 50 15 15
  :header-rows: 1
   
  * - Parameter 
    - Description 
    - Default Value
    - Require Restart
  * - ActiveDiscoveryInterval
    - Interval in seconds between active network discovery polls.
    - 7200
    - Yes
  * - ActiveNetworkDiscovery
    - Enable (1) or disable (0) active network discovery. 
      ***This setting is change by Network Discovery GUI***
    - 0
    - Yes
  * - AgentCommandTimeout
    - Timeout in milliseconds for commands sent to agent. If agent did not respond to command within given number of seconds, command considered as failed.
    - 2000
    - Yes
  * - AgentDefaultSharedSecret
    - 
    - 
    - 
  * - AgentUpgradeWaitTime
    - Maximum wait time in seconds for agent restart after upgrade. If agent cannot be contacted after this time period, upgrade process is considered as failed.
    - 600
    - No
  * - AlarmHistoryRetentionTime
    - A number of days the server keeps an alarm history in the database.
    - 180
    - No
  * - AlarmListDisplayLimit
    - 
    - 
    - 
  * - AllowDirectSMS
    - Allow (1) or disallow (0) sending of SMS via NetXMS server using nxsms utility.
    - 0
    - No
  * - AllowedCiphers
    - A bitmask for encryption algorithms allowed in the server(sum the values to allow multiple algorithms at once): 
        - 1 - AES256 
        - 2 - Blowfish
        - 4 - IDEA
        - 8 - 3DES
        - 16 - AES128  
    - 31
    - Yes
  * - AllowTrapVarbindsConversion
    - 
    - 1
    - Yes
  * - AnonymousFileAccess
    - 
    - 0
    - No
  * - ApplyDCIFromTemplateToDisabledDCI
    - Set to 1 to apply all DCIs from a template to the node, including disabled ones.
    - 0
    - Yes
  * - AuditLogRetentionTime
    - Retention time in days for the records in audit log. All records older than specified will be deleted by housekeeping process.
    - 90
    - No
  * - BeaconHosts
    - Comma-separated list of hosts to be used as beacons for checking NetXMS server network connectivity. Either DNS names or IP addresses can be used. This list is pinged by NetXMS server and if none of the hosts have responded, server considers that connection with network is lost and generates specific event.
    - 
    - Yes
  * - BeaconPollingInterval
    - Interval in milliseconds between beacon hosts polls.
    - 1000
    - Yes
  * - BeaconTimeout
    - Timeout in milliseconds to consider beacon host unreachable.
    - 1000
    - Yes
  * - BlockInactiveUserAccounts
    - 
    - 0
    - No
  * - CapabilityExpirationTime
    - 
    - 604800
    - No
  * - CheckTrustedNodes
    - Enable (1) or disable (0) checking of trusted nodes list for cross-node data collection (using Proxy Node DCI attribute).
    - 1
    - Yes
  * - ClientListenerPort
    - The server port for incoming client connections (such as management console).
    - 4701
    - Yes
  * - ConditionPollingInterval
    - Interval in seconds between polling (re-evaluating) of condition objects.
    - 60
    - Yes
  * - ConfigurationPollingInterval
    - Interval in seconds between configuration polls.
    - 3600
    - Yes
  * - ConnectionPoolBaseSize
    - A number of connections to the database created on the server startup.
    - 5
    - Yes
  * - ConnectionPoolCooldownTime
    - 
    - 300
    - Yes
  * - ConnectionPoolMaxSize
    - A maximum number of connections in the connection pool.
    - 20
    - Yes
  * - DBLockInfo
    - 
    - 
    - 
  * - DBLockPID
    - 
    - 
    - 
  * - DBLockStatus
    - 
    - 
    - 
  * - DataDirectory
    - Directory used by server to store additional data – MIB files, agent packages, etc. 
      
      .. deprecated:: 1.2-M1
    - Windows: :file:`\\var` under installation directory;
    
      UNIX: :file:`/share/netxms` under installation prefix.
    - Yes
  * - DefaultCommunityString
    - System-wide default SNMP community string.
    - public
    - No
  * - DefaultConsoleDateFormat
    - 
    - 
    - 
  * - DefaultConsoleShortTimeFormat
    - 
    - 
    - 
  * - DefaultConsoleTimeFormat
    - 
    - 
    - 
  * - DefaultDciPollingInterval
    - Default polling interval for newly created DCI (in seconds).
    - 60
    - No
  * - DefaultDciRetentionTime
    - Default retention time for newly created DCI (in days).
    - 60
    - No
  * - DefaultEncryptionPolicy
    - Set the default encryption policy for communications with agents: 0 - encryption disabled, 1 - allowed, 2 - preferred, 3 - required.
    - 1
    - Yes
  * - DefaultMapBackgroundColor
    - Default background color for new network map objects (as RGB value).
    - 0xffffff
    - No
  * - DeleteAlarmsOfDeletedObject
    - 
    - 
    - 
  * - DeleteEmptySubnets
    - Enable (1) or disable (0) automatic deletion of subnet objects without any nodes within. When enabled, empty subnets will be deleted by housekeeping process.
    - 1
    - Yes
  * - DeleteEventsOfDeletedObject
    - 
    - 
    - 
  * - DeleteUnreachableNodesPeriod
    - Delete nodes which were unreachable for a number of days specified by this parameter. If this parameter is set to 0 then unreachable nodes will never be deleted.
    - 0
    - Yes
  * - DiscoveryFilter
    - 
    - 
    - No
  * - DiscoveryFilterFlags
    - 3
    - 
    - No
  * - DiscoveryPollingInterval
    - Interval in seconds between passive network discovery polls.
    - 900
    - Yes
  * - EnableAdminInterface
    - 
    - 1
    - Yes
  * - EnableAgentRegistration
    - Enable (1) or disable (0) agents self-registration.
    - 1
    - No
  * - EnableAuditLog
    - Enable (1) or disable (0) audit log.
    - 1
    - Yes
  * - EnableCheckPointSNMP 
    - 
    -  
    - 
  * - EnableEventStormDetection 
    - 
    - 0 
    - Yes
  * - EnableISCListener 
    - Enable (1) or disable (0) Inter-Server Communications Listener. 
    - 0 
    - Yes
  * - EnableObjectTransactions 
    - 
    -  
    - 
  * - EnableMultipleDBConnections 
    - Enable (1) or disable (0) multiple database connections from the NetXMS server. This setting has no effect on SQLite databases. 
    - 1 
    - Yes
  * - EnableNXSLContainerFunctions 
    - Enable (1) or disable (0) server-side NXSL functions for container management (such as [[NXSL:CreateContainer|CreateContainer]], [[NXSL:RemoveContainer|RemoveContainer]], [[NXSL:BindObject|BindObject]], [[NXSL:UnbindObject|UnbindObject]]). 
    - 0 
    - Yes
  * - EnableSNMPTraps 
    - Enable (1) or disable (0) SNMP trap processing. A dedicated thread will be created if set to 1. 
    - 1 
    - Yes
  * - EnableSyslogDaemon 
    - Enable (1) or disable (0) receiving of syslog messages. 
    - 0 
    - Yes
  * - EnableTimedAlarmAck 
    - 
    -  
    - 
  * - EnableXMPPConnector 
    - 
    -  
    - 
  * - EnableZoning 
    - Enable (1) or disable (0) zoning support. 
    - 0 
    - Yes
  * - EscapeLocalCommands
    - 
    - 
    - 
  * - EventLogRetentionTime 
    - 
    - 90 
    - No
  * - EventStormDuration 
    - 
    - 15 
    - Yes
  * - EventStormEventsPerSecond 
    - 
    - 100 
    - Yes
  * - ExtendedLogQueryAccessControl 
    - Enable (1) or disable (0) extended access control in log queries. When enabled, server will check user's access to objects and only select those log records where user has read access to related object. Please note that enabling this option can cause slow and inefficient SQL queries depending on number of objects and actual access right assignment. 
    - 0 
    - No 
  * - ExternalAuditFacility 
    - Syslog facility to be used in audit log records sent to external server. 
    - 13 
    - Yes
  * - ExternalAuditPort 
    - UDP port of external syslog server to send audit records to. 
    - 514 
    - Yes
  * - ExternalAuditServer 
    - External syslog server to send audit records to. If set to ''none'', external audit logging is disabled. 
    - none 
    - Yes
  * - ExternalAuditSeverity 
    - Syslog severity to be used in audit log records sent to external server. 
    - 5 
    - Yes
  * - ExternalAuditTag 
    - Syslog tag to be used in audit log records sent to external server. 
    - netxmsd-audit 
    - Yes
  * - FirstFreeObjectId
    - 
    - 
    - 
  * - FixedStatusValue 
    - 
    - 0 
    - Yes
  * - HelpDeskLink
    - 
    - 
    - 
  * - HouseKeepingInterval 
    - Interval of housekeeper'a running (in seconds). Housekeeper deletes old log lines, old DCI data, cleans removed objects and does VACUUM for PostgreSQL. 
    - 3600 
    - Yes
  * - IcmpPingSize 
    - Size of ICMP packets (in bytes, excluding IP header size) used for status polls. 
    - 46 
    - Yes
  * - IcmpPingTimeout 
    - Timeout for ICMP ping used for status polls (in milliseconds). 
    - 1500 
    - Yes
  * - InternalCA 
    - Enable (1) or disable (0) internal certificate authority. 
    - 0 
    - Yes
  * - IntruderLockoutThreshold 
    - 
    - 0 
    - No
  * - IntruderLockoutTime 
    - 
    - 30 
    - No
  * - JobHistoryRetentionTime 
    - 
    - 90 
    - No
  * - KeepAliveInterval 
    - Interval in seconds between sending keep alive packets to connected clients.
    - 60 
    - Yes
  * - LdapGroupClass
    - 
    - 
    - 
  * - LdapConnectionString
    - 
    - 
    - 
  * - LdapMappingDescription
    - 
    - 
    - 
  * - LdapMappingFullName
    - 
    - 
    - 
  * - LdapMappingName
    - 
    - 
    - 
  * - LdapPageSize
    - 
    - 
    - 
  * - LdapSearchBase
    - 
    - 
    - 
  * - LdapSearchFilter
    - 
    - 
    - 
  * - LdapSyncInterval
    - 
    - 
    - 
  * - LdapSyncUser
    - 
    - 
    - 
  * - LdapSyncUserPassword
    - 
    - 
    - 
  * - LdapUserClass
    - 
    - 
    - 
  * - LdapUserDeleteAction
    - 
    - 
    - 
  * - LockTimeout 
    - ''Unused?'' 
    - 60000 
    - Yes
  * - LogAllSNMPTraps 
    - 
    - 0 
    - Yes
  * - MailEncoding 
    - Encoding for mails generated by NetXMS server. 
    - iso-8859-1 
    - No
  * - MailBase64Subjects 
    - Encode email subjects using base64. Encoding enabled if non-zero 
    - 0 
    - No
  * - MaxActiveUploadJobs 
    - 
    - 10 
    - Yes
  * - MinPasswordLength 
    - Default minimum password length for a NetXMS user. The default applied only if per-user setting is not defined. 
    - 0 
    - No
  * - MinViewRefreshInterval
    - 
    - 
    - 
  * - MobileDeviceListenerPort 
    - 
    -  
    - 
  * - NumberOfBusinessServicePollers 
    - A number of threads responsible for business service (SLA) monitoring. 
    - 10 
    - Yes
  * - NumberOfConditionPollers 
    - A number of threads responsible for condition polling. 
    - 10 
    - Yes
  * - NumberOfConfigurationPollers 
    - A number of threads responsible for configuration polling. 
    - 10 
    - Yes
  * - NumberOfDatabaseWriters 
    - The number of threads used to perform delayed writes to database. 
    - 1 
    - Yes
  * - NumberOfDataCollectors 
    - The number of threads used for data collection. 
    - 25 
    - Yes
  * - NumberOfDiscoveryPollers 
    - A number of threads responsible for network discovery polling. 
    - 1 
    - Yes
  * - NumberOfRoutingTablePollers 
    - The number of threads used for polling routing tables on monitored nodes. If you have a really large number of monitored nodes (more than 1000), or if you have decreased routing table update interval, you may need to increase this parameter. 
    - 10 
    - Yes
  * - NumberOfStatusPollers 
    - The number of threads used for status polling. Since accurate status polling is sensitive for normal system operation, it is highly recommended to have this parameter set to approximately 1/10 of the number of monitored nodes. 
    - 25 
    - Yes
  * - NumberOfTopologyPollers 
    - The number of threads used for collecting network topology information. 
    - 10 
    - Yes
  * - NumberOfTopologyTablePollers
    - 
    - 
    - 
  * - NumberOfUpgradeThreads 
    - The number of threads used to perform agent upgrades (i.e. maximum number of parallel upgrades). 
    - 10 
    - No
  * - PasswordComplexity 
    - Set of flags to enforce password complexity (see [[UM::User_Management#Password_Policy|Password Policy]] for more details). 
    - 0 
    - No
  * - PasswordExpiration 
    - Password expiration time in days. If set to 0, password expiration is disabled. 
    - 0 
    - No
  * - PasswordHistoryLength 
    - Number of previous passwords to keep. Users are not allowed to set password if it matches one from previous passwords list. 
    - 0 
    - No
  * - PollCountForStatusChange 
    - The number of consecutive unsuccessful polls required to declare interface as down. 
    - 1 
    - Yes
  * - ProcessTrapsFromUnmanagedNodes 
    - Enable (1) or disable (0) processing of SNMP traps received from node which is in unmanaged state. 
    - 0 
    - Yes
  * - RADIUSNumRetries 
    - The number of retries for RADIUS authentication. 
    - 5 
    - No
  * - RADIUSPort 
    - Port number used for connection to primary RADIUS server. 
    - 1645 
    - No
  * - RADIUSSecondaryPort 
    - Port number used for connection to secondary RADIUS server. 
    - 1645 
    - No
  * - RADIUSSecondarySecret 
    - Shared secret used for communication with secondary RADIUS server. 
    - netxms 
    - No
  * - RADIUSSecondaryServer 
    - Host name or IP address of secondary RADIUS server. 
    - none 
    - No
  * - RADIUSSecret 
    - Shared secret used for communication with primary RADIUS server. 
    - netxms 
    - No
  * - RADIUSServer 
    - Host name or IP address of primary RADIUS server. 
    - none 
    - No
  * - RADIUSTimeout 
    - Timeout in seconds for requests to RADIUS server 
    - 3 
    - No
  * - ReceiveForwardedEvents 
    - Enable (1) or disable (0) reception of events forwarded by another NetXMS server. Please note that for external event reception ISC listener should be enabled as well. 
    - 0 
    - No
  * - ResolveDNSToIPOnStatusPoll
    - 
    - 
    - 
  * - ResolveNodeNames 
    - 
    - 1 
    - No
  * - RoutingTableUpdateInterval 
    - Interval in seconds between reading routing table from node. 
    - 300 
    - Yes
  * - RunNetworkDiscovery 
    - Enable (1) or disable (0) automatic network discovery process.
      ***This setting is change by Network Discovery GUI*** 
    - 0 
    - Yes
  * - ServerID
    - 
    - 
    - 
  * - SMSDriver 
    - Mobile phone driver to be used for sending SMS. 
    - <none> 
    - Yes
  * - SMSDrvConfig 
    - SMS driver parameters. For ''generic'' driver, it should be the name of COM port device. 
    - 
    - Yes
  * - SMTPFromAddr 
    - An address used for sending mail from. 
    - netxms@localhost
    - No
  * - SMTPFromName 
    - A name used for sending mail. 
    - NetXMS Server 
    - No
  * - SMTPPort 
    - TCP port for SMTP server. 
    - 25 
    - No
  * - SMTPRetryCount 
    - Number of retries for sending mail. 
    - 1 
    - No
  * - SMTPServer 
    - An SMTP server used for sending mail. 
    - localhost 
    - No
  * - SNMPRequestTimeout 
    - Timeout in milliseconds for SNMP requests sent by NetXMS server. 
    - 2000 
    - Yes
  * - SNMPTrapLogRetentionTime
    - 
    - 
    - 
  * - SNMPTrapPort
    - 
    - 
    - 
  * - SlmPollingInterval 
    - Interval in seconds between business service polls. 
    - 60 
    - Yes
  * - StatusCalculationAlgorithm 
    - 
    - 1 
    - Yes
  * - StatusPollingInterval 
    - Interval in seconds between status polls. 
    - 60 
    - Yes
  * - StatusPropagationAlgorithm
    - Algorithm for status propagation (how object's status affects its child object statuses). Possible values are: 
        - 0 - Default
        - 1 - Unchanged
        - 2 - Fixed
        - 3 - Relative
        - 4 - Translated
    - 1
    - Yes
  * - StatusShift
    - 
    - 0
    - Yes
  * - StatusSingleThreshold
    - 
    - 75
    - Yes
  * - StatusThresholds
    - 
    - 503C2814
    - Yes
  * - StatusTranslation
    - 
    - 01020304
    - Yes
  * - StrictAlarmStatusFlow
    - 
    - 
    - 
  * - SyncInterval
    - Interval in seconds between writing object changes to the database.
    - 60
    - Yes
  * - SyncNodeNamesWithDNS
    - Enable (1) or disable (0) synchronization of node names with DNS on each configuration poll.
    - 0
    - No
  * - SyslogListenPort
    - UDP port used by built-in syslog server.
    - 514
    - Yes
  * - SyslogNodeMatchingPolicy
    - Node matching policy for built-in syslog daemon. Possible values are:
        - 0 - syslog message source IP address then hostname
        - 1 - hostname then syslog message source IP address
    - 0
    - Yes
  * - SyslogRetentionTime
    - Retention time in days for records in syslog. All records older than specified will be deleted by housekeeping process.
    - 90
    - No
  * - ThresholdRepeatInterval
    - System-wide interval in seconds for resending threshold violation events. Value of 0 disables event resending.
    - 0
    - Yes
  * - TileServerURL
    - 
    - http://tile.openstreetmap.org/
    - No
  * - TopologyDiscoveryRadius
    - 
    - 3
    - No
  * - TopologyExpirationTime
    - 
    - 900
    - No
  * - TopologyPollingInterval
    - 
    - 1800
    - Yes
  * - UseDNSNameForDiscoveredNodes
    - Enable (1) or disable (0) use of DNS name instead of IP address as primary name for newly discovered nodes. If enabled, server will do back resolve of IP address, and then resolve obtained name back to IP address. Only if this IP address will match the original one, DNS name will be used.
    - 0
    - No
  * - UseFQDNForNodeNames
    - Enable (1) or disable (0) use of fully qualified domain names as primary names for newly discovered nodes.
    - 1
    - Yes
  * - UseIfXTable
    - Enable (1) or disable (0) use of SNMP ifXTable instead of ifTable for interface configuration polling.
    - 1
    - No
  * - UseInterfaceAliases
    - Control usage of interface aliases (or descriptions). Possible values are:
        - 0 - Don’t use aliases;
        - 1 - Use aliases instead of names, when possible;
        - 2 - Concatenate alias and name to form interface object name.
        - 3 - Concatenate name and alias to form interface object name.
    - 0
    - No
  * - UseSNMPTrapsForDiscovery
    - 
    - 
    - 
  * - WindowsConsoleUpgradeURL
    - URL pointing to the actual version of NetXMS Console for Windows. Console application will try to download new version from this URL, if it detects that upgrade is needed. You can use %version % macro inside the URL to insert actual server version.
    - http://www.netxms.org/download/netxms-%version%.exe
    - No
  * - XMPPLogin
    - 
    - 
    - 
  * - XMPPPassword
    - 
    - 
    - 
  * - XMPPPort
    - 
    - 
    - 
  * - XMPPServer
    - 
    - 
    - 
    

Bundled Subagents
=================

.. _command_line_tools:

Command line tools
==================

NetXMS provide some additional command line tools. Each tool serves its own purpose.

DB Manager
----------
   
This is tool used to make manipulations with NetXMS database. 
  ::

   Usage: nxdbmgr [<options>] <command>


Valid commands are:

.. list-table:: 
   :widths: 50 150
   
   * - batch <file>
     - Run SQL batch file
   * - check
     - Check database for errors
   * - export <file>
     - Export database to file
   * - get <name> 
     - Get value of server configuration variable
   * - import <file> 
     - Import database from file
   * - init <file>
     - Initialize database
   * - migrate <source>
     - Migrate database from given source
   * - resetadmin
     - Unlock user "admin" and reset password to default ("netxms")
   * - set <name> <value>
     - Set value of server configuration variable
   * - unlock
     - Forced database unlock
   * - upgrade
     - Upgrade database to new version
   
   
Valid options are:

+---------------+--------------------------------------------------------------------+
| -c <config>   |Use alternate configuration file. Default is {search}               |
+---------------+--------------------------------------------------------------------+ 
| -d            |Check collected data (may take very long time).                     |  
+---------------+--------------------------------------------------------------------+
| -D            |Migrate only collected data.                                        |
+---------------+--------------------------------------------------------------------+
| -f            |Force repair - do not ask for confirmation.                         |
+---------------+--------------------------------------------------------------------+
| -h            |Display help and exit.                                              |
+---------------+--------------------------------------------------------------------+
| -I            |MySQL only - specify TYPE=InnoDB for new tables.                    |
+---------------+--------------------------------------------------------------------+
| -M            |MySQL only - specify TYPE=MyISAM for new tables.                    |
+---------------+--------------------------------------------------------------------+
| -N            |Do not replace existing configuration value ("set" command only).   |
+---------------+--------------------------------------------------------------------+  
| -q            |Quiet mode (don't show startup banner).                             |
+---------------+--------------------------------------------------------------------+
| -s            |Skip collected data during migration.                               |
+---------------+--------------------------------------------------------------------+
| -t            |Enable trace mode (show executed SQL queries).                      |
+---------------+--------------------------------------------------------------------+ 
| -v            |Display version and exit.                                           |
+---------------+--------------------------------------------------------------------+
| -X            |Ignore SQL errors when upgrading (USE WITH CAUTION!!!)              |
+---------------+--------------------------------------------------------------------+
   
Database initialization
~~~~~~~~~~~~~~~~~~~~~~~
  ::

   nxdbmgr init initialization.file

Is used to initialize first time database. Database and user should already exist. 
Credentials of connection are taken from server configuration file. 


Database migration
~~~~~~~~~~~~~~~~~~
  ::
 
   nxdbmgr migrate old.configuration.file

Is used to migrate NetXMS database between different database management system from NetXMS 
supported list. 

While migration nxdbmgr should use new configuration file(with new DB credentials) and as 
a parameter should be given the old configuration file. 

In best practises of migration is to do database check with command "nxdbmgr check".


nxaction
--------
   
nxadm
-----
   
   
nxalarm 
-------
   
nxap 
----
   
   
nxappget
--------


.. _nxapush-label:

nxapush
-------
This tool has same usage as nxpush, but it sends data throught local agent. 

When new version of NetXMS is released - version of server protocol is 
changed. Change of version affects on server comunication with other tools 
like nxpush. So after each server update nxpush tool also should be updated. 
In case of usage nxapush - only agent should be updated as this tool uses agent
protocol to send data. 
   
nxdevcfg
--------


.. _nxencpasswd-tools-label:
   
nxencpasswd  
-----------

This tool can be used to encrypt passwords stored 
in server and agent configuration files. 

nxevent  
-------

This tool can be used to push events to NetXMS server. 
   
nxget  
-----

This tool can be used to get agent :term:`Metric` from node. 
   
nxmibc  
------

   
.. _nxpush-label:
   
nxpush
------
nxpush is a tool that allows to push DCI daca from command line.  

There are different options how this tool can be used:
 - with help of this tool data collected with different monitoring system 
   can be pushed also to netxms
 - can be used on nodes where agent can not be installed(not the case for nxapush)
 - can be used on nodes behind NAT with no port forwarding option

Usage: ./nxapush [OPTIONS] [@batch_file] [values]
  
Options:

+--------------+-----------------------------------------------+
|-h            | Display this help message.                    |
+--------------+-----------------------------------------------+
|-o <id>       |Push data on behalf of object with given id.   |
+--------------+-----------------------------------------------+
|-q            |Suppress all messages.                         |
+--------------+-----------------------------------------------+
|-v            |Enable verbose messages. Add twice for debug   |
+--------------+-----------------------------------------------+
|-V            |Display version information.                   |
+--------------+-----------------------------------------------+

Notes:
  * Values should be given in the following format:
    dci=value
    where dci can be specified by it's name
  * Name of batch file cannot contain character = (equality sign)

Examples:
  Push two values:

  .. code-block:: shell

      nxapush PushParam1=1 PushParam2=4

  Push values from file:

  .. code-block:: shell

      nxapush @file

Required server configurations are described there: :ref:`dci-push-parameters-label`
   
nxscript  
--------
   
nxsms  
-----
   
nxsnmpget  
---------

This tool can be used to get :term:`SNMP` :term:`Metric` from node. 
   
nxsnmpset 
---------
   
nxsnmpwalk  
----------
   
nxupload
--------



List of supported metrics
=========================

Metrics are divided by subagents. There are also preset automatically
loaded OS subagents. 

Linux
-----

Windows
-------

Unix
----

.. TODO::
  Add other subagents.
