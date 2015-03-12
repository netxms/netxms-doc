################
Agent management
################

Introduction
============
   
NetXMS agent is daemon or service that runs on a :term:`node<Node>` to provide additional
monitoring options. This is optional for installation, but it's installation gives next advantages:

   * Centralized configuration - you can change configuration of agent from management console; if needed, you can even store agent configs on NetXMS server
   * More secure: communications between NetXMS server and agent can be encrypted, additional authentication on agent can be configured
   * TCP instead of UDP is used for communications with agent - this can help in case of slow and poor quality links
   * Remote command execution - agents can be used to execute commands on managed systems as a reaction to certain events
   * Proxy functionality: agent can be used as a proxy to reach agents on hosts not directly accessible by NetXMS server
   * :term:`SNMP` proxy: agent can be used as a proxy to reach remote SNMP devices
   * :term:`SNMP Trap` proxy: agent can be used as a proxy to get messages from remote SNMP device
   * Extensible: you can add new parameters very easy using configuration option like ``ExternalParamer`` or by writing your own subagents
   * Easy upgrade - you can upgrade all agents at once from console
   * Provides file management possibilities on agent. 


Agent configuration files
=========================

Agent have 2 types of configuration files: master configuration file and additional 
configuration file(Agent Policies files). Only master configuration file is mandatory file. 
Minimal configuration for master configuration file is server address. To afterwards be able to
apply all other changes from the server, address of it should be should be given as MasterServers.

**After configuration file change agent should be restarted to apply new changes.** 

.. _master-configuration-file-label:

Master configuration file
-------------------------
File nxagentd.conf is a master configuration file for NetXMS agent. It contains all 
information necessary for agent's operation. Default location for this file is 
:file:`/etc/nxagentd.conf` on UNIX systems and 
:file:`'installation directory'\\etc\\nxagentd.conf'` on Windows. The file can 
contain one or more parameters in *Parameter = Value* form, each parameter should 
be on its own line. Comments can be inserted after "#" sign. This file can also 
contain configuration for subagents. In this case, subagents’ parameters should 
be placed in separate sections. Beginning of the section is indicated by "*" sign, 
followed by a section name or in section name in braces(example: "[sectionName]").

If build configuration was done with --prefix='prefix' parameter, then configuration file will 
be searched in the following order (UNIX):

   1. :file:`$NETXMS_HOME/etc/nxagentd.conf`
   2. :file:`'prefix'/etc/nxagentd.conf`
   3. :file:`/etc/nxagentd.conf`
   4. :file:`/Database/etc/nxagentd.conf`
   5. :file:`/usr/etc/nxagentd.conf`
   
For Windows systems:

   1. :file:`'installation directory'\\etc\\nxagentd.conf`
   
For Windows location of NetXMS config can be change in registry. 


If configuration file is placed in different location or named in different way,
then it's location and file name can be given to agent with -c parameter. 

Detailed list of parameters can be found there: :ref:`agent_configuration_file`.
     
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

   1. :file:`'installation directory'\\etc\\nxagentd.conf`
   
   
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

Agent policies can be configured on server in :guilabel:`Policies` part. There can be 
used the same parameters as in main configuration file in XML or 'key = value' format. 

To create policy in menu of container where should be created policy select 
:guilabel:`Create agent policy(configuration file)` and give required object name and 
press :guilabel:`OK`. Than in newly created object's properties add configuration 
parameters in :guilabel:`Configuration File` tab. 

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
run it with new configuration. To install policy in object menu select :guilabel:`Install...`,
select :guilabel:`Install on nodes selected below`, select required nodes in object browser and 
click :guilabel:`OK`.

Installed policy configurations are stored as additional config files. List of applied 
policies is stored in Windows registry on in registry file in UNIX. If policy is successfully 
applied on a :term:`node <Node>` it will be seen under this policy.
 

Example:

      .. figure:: _images/applied_policy.png

If Policies have changed it should be reapplied manually. Is is done with command in 
object menu :guilabel:`Install...`, then select :guilabel:`Install on all nodes where this 
policy already installed` and click :guilabel:`OK`.

Policy can be also uninstalled. To do this right click on policy object and select 
:guilabel:`Uninstall...`, select node from witch this policy will be removed and click :guilabel:`OK`.
In this case additional configuration file and registry recored connected to this policy are removed
from node. In order to apply the changes it is required manually to restart agent. 
      
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


Agent registration
==================

There are few ways to register agent:
   1. To enter it manually by creating a node
   2. Run the network discovery and enter the range of IP addresses.
   3. Register agent on management server "nxagentd -r <addr>",  where <addr> is the IP address of server. 
      To register agents using this option also ``EnableAgentRegistration`` parameter should be set to 1.
   
Subagents
=========
Subagents are used to extend agent functionality. NetXMS subagent are libraries that are loaded by agent.
By default all subagents are included in agent build. Subagent may be not included in build
only if on time of the build there were no required libraries for subagent build. To enable 
subagent is require just to add line in main agent configuration file(example: "Subagent=dbquery.nsm").
More about configuration and usage of subagents will be described in :ref:`getting-things-monitored` chapter.

There is list of available manually loaded NetXMS subagents:

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
  
Load of subagent as separate process
------------------------------------

Load of subagent as separate process can be used in case it is necessary to load agent and subagent 
under different users. It can be done by adding ``ExternalSubagent`` parameter with unique ID that 
will represent connection name between agent and subagent. Create second configuration file for this 
subagent and add there ``ExternalMasterAgent`` parameter with same ID and run instance of :file:`nxagentd` with 
this config. Now external subagent will communicate with master agent using Named Pipe. Only master agent will 
communicate with server. 

Agent Proxy node configuration
==============================

In case it is required to monitor nodes behind firewall, it can be configured 
access to one of subnet nodes and used this node as a proxy node for others. 

Proxy node can be set while node creation or in :guilabel:`Communications` tab 
of node properties. To configure proxy node select node in object selector 
:guilabel:`NetXMS Agent Proxy`.

.. figure:: _images/create_node.png

.. figure:: _images/node_communications_tab.png

