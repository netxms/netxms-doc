########
Appendix
########

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



Bundled Subagents
=================

.. _command_line_tools:

Command line tools
==================


List of supported metrics
=========================

