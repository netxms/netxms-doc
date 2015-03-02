################
Agent management
################

Introduction
============
   
NetXMS agent is daemon or service that runs on a :term:`node<Node>` to provide additional
monitoring options.
This is optional for installation, but it's installation gives next advantages:
   * Centralized configuration - you can change configuration of agent from management console; if needed, you can even store agent configs on NetXMS server
   * More secure: communications between NetXMS server and agent can be encrypted, additional authentication on agent can be configured
   * TCP instead of UDP is used for communications with agent - this can help in case of slow and poor quality links
   * Remote command execution - agents can be used to execute commands on managed systems as a reaction to certain events
   * Proxy functionality: agent can be used as a proxy to reach agents on hosts not directly accessible by NetXMS server
   * :term:SNMP `proxy`: agent can be used as a proxy to reach remote SNMP devices
   * :term:`SNMP Trap` proxy: agent can be used as a proxy to get messages from remote SNMP device
   * Extensible: you can add new parameters very easy using ExternalParamer configuration option or by writing your own subagents
   * Easy upgrade - you can upgrade all agents at once from console
   * Provides file management possibilities on agent. 


Agent configuration files
=========================

Agent have 2 types of configuration files: master configuration file and additional 
configuration file(Agent Policies files). Only master configuration file is mandatory file. 
Minimal configuration for master configuration file is server address. To afterwards apply all 
other changes from server server address should be given as MasterServers.

**After configuration file change agent should be restarted to apply new changes.** 

.. _master-configuration-file-label:

Master configuration file
-------------------------
File nxagentd.conf is a master configuration file for NetXMS agent. It contains all 
information necessary for agent's operation. Default location for this file is 
/etc/nxagentd.conf on UNIX systems and 'installation directory'\etc\nxagentd.conf' on Windows. The file can 
contain one or more parameters in Parameter = Value form, each parameter should 
be on its own line. Comments can be inserted after "#" sign. This file can also 
contain configuration for subagents. In this case, subagents’ parameters should 
be placed in separate sections. Beginning of the section is indicated by "*" sign, 
followed by a section name.

If build configuration was done with --prefix='prefix' parameter, then configuration file will 
be searched in the following order (UNIX):
   1. :file:`$NETXMS_HOME/etc/nxagentd.conf`
   2. :file:`'prefix'/etc/nxagentd.conf`
   3. :file:`/etc/nxagentd.conf`
   4. :file:`/Database/etc/nxagentd.conf`
   5. :file:`/usr/etc/nxagentd.conf`
   
For Windows systems:
   1. :file:`'installation directory'\etc\nxagentd.conf`
   
For Windows location of NetXMS config can be change in registry. 


If configuration file is placed in different location, then it's location and file name
can be given to agent with -c parameter. 


The file can contain the following parameters (in main section):


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
     - 
     - 
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
     - Enable (yes) or disable (no) creation of agent's crash dumps. Only has effect on Windows platforms.
     - no
   * - DataDirectory
     - 
     - 
   * - DailyLogFileSuffix
     - 
     - 
   * - DebugLevel
     - Set agent debug logging level (0 - 9).  Value of 0 turns off debugging, 9 enables very detailed logging.  Can also be set with command line "-D<level>" option.
     - 0
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
   * - EnableSNMPProxy
     - Enable (yes) or disable (no) SNMP proxy functionality.  
     - no
   * - EnableSubagentAutoload
     - Enable (yes) or disable (no) loading of platform subagent(s).
     - yes
   * - EnableWatchdog
     - Enable (yes) or disable (no) automatic agent restart in case of unexpected shutdown.
     - no
   * - ExecTimeout
     - Timeout in milliseconds for external parameter execution.
     - 2000
   * - ExternalMasterAgent
     - 
     -
   * - ExternalList
     - Add list handled by external command. To add multiple parameters, you should use multiple ExternalList entries.
     - No defaults
   * - ExternalParameter
     - Add parameter handled by external command. To add multiple parameters, you should use multiple ExternalParameter entries. See the Agent Configuration section for detailed description of this parameter.
     - No defaults
   * - ExternalParameterShellExec
     - 
     -
   * - ExternalParametersProvider
     - 
     -
   * - ExternalSubagent
     - 
     -
   * - FileStore
     - Directory to be used for storing files uploaded by management server(s).
     - /tmp on UNIX
     
       C:\\ on Windows
   * - FullCrashDumps
     - 
     -
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
   * - TimeOut
     - 
     - 
   * - WaitForProcess
     - If specified, an agent will pause initialization until given process starts.
     - No defaults


     
Configuration file example:
::    
   
   #
   # Sample agent’s configuration file
   #
   MasterServers = 10.0.0.4
   LogFile = {syslog}
   SubAgent = winperf.nsm
   # Below is a configuration for winperf subagent, in separate section
   *WinPerf
   EnableDefaultCounters = yes

   
Notes
~~~~~
Additional notes abut configuration:

There are 3 level of access for an agent. Depending on how server's IP address listen in nxagentd.conf, it will have different access level. It is preferred to use MasterServers. If server listed in:  
   1. MasterServers - full access
   2. ControlServers - can read data and execute predefined actions, but cannot change config nor install policies.
   3. Servers - read only access
   
  
Additional configuration files
------------------------------
Additional configuration files override or supplement configuration parameters form main file. 
They are used to store applied :guilabel:`Policies` configuration, but can be also created 
and updated manually. More information about Policies can be read there: :ref:`agent-policies-label`.

If configuration of build was done with --prefix='prefix' parameter, then config will 
be searched in next order(UNIX):
   1. :file:`$NETXMS_HOME/etc/nxagentd.conf.d`
   2. :file:`'prefix'/etc/nxagentd.conf.d`
   3. :file:`/etc/nxagentd.conf.d`
   4. :file:`/Database/etc/nxagentd.conf.d`
   5. :file:`/usr/etc/nxagentd.conf.d`
   
For Windows systems:
   1. :file:`'installation directory'\etc\nxagentd.conf`
   
   
.. _stored-agent-configurations-label:
   
Agent configuration options from server
=======================================

Edit configuration file remotely
--------------------------------

Right click on node, select from menu: :guilabel:`Edit agent's configuration file`. 

On View exit there will be present dialog. New configuration apply is performed on agent restart. So to 
immediately apply new configuration on config exit select :guilabel:`Save and Apply`. This option will 
save config and automatically restart the agent. If just :guilabel:`Save` is selected, then agent 
should be manually restarted to apply new configuration.


Agent configuration files on server
-----------------------------------
   
Agent master configuration files can be stored on server side and requested by agent with 
parameter :command:`-M <serverAdress>`. On config request server goes through config list 
from beginning till the end and one by one checks if this config is the requested one by 
executing filter scripts. 

If server have found appropriate configuration file then it is sent to agent and old
:file:`nxagentd.conf` file is overwritten with incoming one or created new one if there is no :file:`nxagentd.conf` 
When agent can't connect to server or server hasn't found right config, the agent is started 
with the old one. In case when old configuration file does not exist and it is not possible to 
get new one from server - agent fails to start. 

.. versionadded:: 1.2.15    

Configuration
~~~~~~~~~~~~~

Each config has a name, filter and config content. 

 - Name just identifies config.
 - Filter is check on config request to define witch configuration file to 
   give back. Filter is defined with help of :term:`NXSL`. To configuration are given 
   next parameters:
    - $1 - IP address
    - $2 - platform
    - $3 - major version number
    - $4 - minor version number
    - $5 - release number
 - Configuration file is a content of returned configuration file. 

.. figure:: _images/agent_config_manager.png


.. _agent-policies-label:

Agent Policies
--------------

Agent policies can be configured on server in Policies part. There can be used the same 
parameters as in main configuration file in XML or 'key = value' format. 

In XML format general tag should be <config> and then can be added any agent or subagent 
parameter as a tag. Example:

::

  <config>
    <agent>
      <-- there can be added comment -->
      <MasterServers>127.0.0.1</MasterServers>
      <SubAgent>netsvc.nsm</SubAgent>
      <SubAgent>dbquery.nsm</SubAgent>
      <SubAgent>filemgr.nsm</SubAgent>
    </agent>
    <DBQUERY>
      <Database>id=myDB;driver=mysql.ddr;server=127.0.0.1;login=netxms;password=xxxxx;dbname=netxms</Database>
      <Query>dbquery1:myDB:60:SELECT name FROM images</Query>
      <ConfigurableQuery>dbquery2:myDB:Comment in param :SELECT name FROM images WHERE name like ?</ConfigurableQuery>
      <ConfigurableQuery>byID:myDB:Comment in param :SELECT name FROM users WHERE id=?</ConfigurableQuery>
    </DBQUERY>      
    <filemgr>
      <RootFolder>/</RootFolder>
    </filemgr>
  </config>

Example:

      .. figure:: _images/policy_example.png

After policy is created it should be installed on required nodes. Node and agent on it 
should be up and running and all folder path to additional configuration files and 
register should exist. Nodes should be manually restarted after policy was applied to 
run it with new configuration. 

Installed policy configurations are stored as additional config files. List of applied 
policies is stored in Windows registry on in registry file in UNIX. If policy is successfully 
applied on a node it will be seen under this policy.
 

Example:

      .. figure:: _images/applied_policy.png

If Policies have changed it should be reapplied. Is is done with command ...
      
Advantage of creating configuration in policies - if configuration for nodes is changed, 
then it should be changed only once for all nodes on witch it is applied. 
 
Agent Policies vs. Agent Configuration Files on Server 
------------------------------------------------------

A short lists of main points to compare both options:

Agent Configuration Files on Server:
  - Assignment is Rule based 
  - Config download from server is each time the agent starts (if option '-M servername')
  - When config is found on server, local Master config is overwritten, if not existing Master 
    config is used
  - Works with Master config
  - Do not required initial config(can be started without config), but in this case agent 
    will fail if nothing will be returned from server

Agent Policies:
  - Not possible for bootstrap agent
  - Also possible via proxy
  - Assignment is only direct to nodes, not rule based
  - Can be in XML or 'key = value' format
  - SubAgent config sections also possible
  - Changed policies must be reinstalled on nodes (in console) and need agent restart
  - At minimum the server connection parameters must be in Master config to be able to start agent
  - Works with Additional configuration files(policies)
  - If policy and master config have same parameter that can be set only once 
    like(MasterServers or LogFile), then policy will overwrite master config configuration
  - If policy and master config have same parameter that can be set multiple times 
    like(Target for PING subagent or Query for DBQUERY), then policy will merge lists of configs


Agent registry
==============   
There are few ways of registering agent:

   1. To enter it manually by creating a node
   2. Run the network discovery and enter the range of IP addresses.
   3. Register agent on management server "nxagentd -r <addr>",  where <addr> is the IP address of server. 

   
Subagents
=========
By default all subagents are included in agent build. Subagent may be not included in build
only if on time of the build there were no required libraries for subagent build. To enable 
subagent is require just to add line in main agent configuration file. 

Subagents are used to extend agent functionality.
There is list of available manually loaded subagents:
  * DB2
  * FileMGR
  * DBQuery
  * ECS
  * Informix
  * Java
  * lm-sensors
  * ODBCQuery
  * Oracle
  * Ping
  * PortCheck
  * netsvc
  * UPS
  * WinPref
  * WMI
  * MongoDB
  
