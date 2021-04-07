################
Agent management
################

Introduction
============

|product_name| agent is daemon or service that runs on a :term:`node<Node>` to provide additional
monitoring options. This is optional for installation, but it's installation gives following advantages:

   * Centralized configuration - you can change configuration of agent from management console; if needed, you can even store agent configs on |product_name| server
   * More secure: communications between |product_name| server and agent can be encrypted, additional authentication on agent can be configured
   * TCP instead of UDP is used for communications with agent - this can help in case of slow and poor quality links
   * Remote command execution - agents can be used to execute commands on managed systems as a reaction to certain events
   * Proxy functionality: agent can be used as a proxy to reach agents on hosts not directly accessible by |product_name| server
   * :term:`SNMP` proxy: agent can be used as a proxy to reach remote SNMP devices
   * :term:`SNMP Trap` proxy: agent can be used as a proxy to get messages from remote SNMP device
   * Extensible: you can add new parameters very easy using configuration option like ``ExternalParameter`` or by writing your own subagents
   * Easy upgrade - you can upgrade all agents at once from console
   * Provides file management possibilities on agent.
   * Provides log file monitoring functionality.


Agent configuration files
=========================

Agent have 3 types of configuration files: master configuration file, additional
configuration files and Agent Policy configuration files.
Master configuration file is the only mandatory file.
Minimal configuration for master configuration file is server address. Address should be
set as MasterServers to be able to apply other configuration settings from the server.

**After configuration file change agent should be restarted to apply new changes.**

Two formats are supported for configuration files and configuration file policies: XML and 'key = value' format.

In 'key = value' format configuration file can contain one or more parameters in
*Parameter = Value* form, each parameter should be on its own line.
Parameters are grouped into sections. Beginning of a section is denoted by section
name in square brackets (example: "[sectionName]").
Section named "[Core]" contains parameters for agent itself. It's the default section, if a
configuration file starts from parameter and not from section name, parameters are treated
as belonging to "Core" section. Subagents’ parameters should be placed in separate sections named by subagent name.
Same section name can be present several times in the configuration file.
Comments can be inserted after "#" sign

In XML format general tag should be <config>, second level tags contain section names and third level tags are
agent or subagent configuration parameters.

'key = value' format example:

.. code-block:: cfg

   [Core]
   MasterServers = 10.0.0.4
   SubAgent = winperf.nsm
   # Below is a configuration for winperf subagent, in separate section
   [WinPerf]
   EnableDefaultCounters = yes

Same example in XML format:

.. code-block:: xml

   <config>
      <Core>
         <MasterServers>10.0.0.4</MasterServers>
         <SubAgent>winperf.nsm</Subagent>
      </Core>
      <!-- Below is a configuration for winperf subagent, in separate section -->
      <WinPerf>
         <EnableDefaultCounters>yes</EnableDefaultCounters>
      </WinPerf>
   </config>

Example of configuration sections:

.. figure:: _images/section_description.png

Detailed list of parameters can be found here: :ref:`agent_configuration_file`.
The following parameters can be specified in master configuration
file only (and will be ignored if found in other configuration files):
``DataDirectory`` and ``ConfigIncludeDir``.

.. _master-configuration-file-label:

Master configuration file
-------------------------
File nxagentd.conf is a master configuration file for |product_name| agent.
Depending on OS there are different locations, where agent tries to find master configuration file.

UNIX-like systems
~~~~~~~~~~~~~~~~~

On UNIX systems master configuration file is searched in the following order:

  #. If :file:`$NETXMS_HOME` environment variable is set: :file:`$NETXMS_HOME/etc/nxagentd.conf`
  #. :file:`'prefix'/etc/nxagentd.conf`. 'prefix' is set during build configuration with ``--prefix='prefix'`` parameter. If that parameter was not specified during build, ``/usr/local`` is used.
  #. :file:`/Database/etc/nxagentd.conf`
  #. :file:`/usr/etc/nxagentd.conf`
  #. :file:`/etc/nxagentd.conf`

If configuration file is placed in a different location or named in a different way,
then it's location and file name can be given to agent with ``-c`` parameter or by
specifying :file:`$NXAGENTD_CONFIG` environment variable. In this cause
search in the locations mentioned above is not performed.

Windows
~~~~~~~

On Windows location of |product_name| config is stored in the registry. Alternatively,
location of configuration file can be provided to agent with ``-c`` command line parameter.
If there is no record in the registry and ``-c`` parameter is not specified, then
agent tries to find configuration files in the following locations:

  #. :file:`'installation directory'\\etc\\nxagentd.conf`
  #. :file:`C:\\nxagentd.conf`

.. _additional-configuration-file-label:

Additional configuration files
------------------------------
To increase maintainability, configuration can be stored in multiple additional
configuration files located in a specific folder.
Additional configuration files override (if a parameter supports only one value)
or supplement (if parameter supports multiple values, e.g. list of servers or root
folders for filemgr subagent) configuration parameters from master file.
Depending on OS there are different locations, where agent tries to find master configuration file.

UNIX-like systems
~~~~~~~~~~~~~~~~~

On UNIX systems it is searched in the following order (search is performed until first existing folder is found):

  1. If :file:`$NETXMS_HOME` environment variable is set: :file:`$NETXMS_HOME/etc/nxagentd.conf.d`
  2. :file:`'prefix'/etc/nxagentd.conf.d`. 'prefix' is set during build configuration with ``--prefix='prefix'`` parameter. If that parameter was not specified during build, ``/usr/local`` is used.
  3. :file:`/Database/etc/nxagentd.conf.d`
  4. :file:`/etc/nxagentd.conf.d`
  5. :file:`/usr/etc/nxagentd.conf.d`

A different configuration file folder name can be given by
specifying $NXAGENTD_CONFIG_D environment variable. In this cause
search in the locations mentioned above is not performed.

Windows
~~~~~~~

On Windows location of configuration file folder is stored in the registry.
If there is no record in the registry, then agent tries to find configuration
file folder in the following locations (search is performed until first existing folder is found):

   1. :file:`'installation directory'\\etc\\nxagentd.conf.d`
   2. :file:`C:\\nxagentd.conf.d`


Agent policy configuration files
--------------------------------

:guilabel:`Agent policies` allow to store agent configuration on server and
deliver it to the agents. More information about Policies can be read there: :ref:`agent-policies-label`.

On agent configuration policy files are stored in a separate folder named
:guilabel:`config_ap` under :guilabel:`DataDirectory` folder. Every policy
is saved into a separate file named by policy GUID.


.. _stored-agent-configurations-label:

Agent configuration options from server
=======================================

.. _edit_agent_configuration_remotely:

Edit configuration file remotely
--------------------------------

Right click on node, select :guilabel:`Edit agent's configuration file` from menu.
When closing the editor, a dialog will be presented. New configuration apply is
performed on agent restart. So to immediately apply new configuration select :guilabel:`Save and Apply`.
This option will save configuration file and automatically restart the agent.
If just :guilabel:`Save` is selected, then agent should be manually restarted to apply new configuration.

.. _agent_configuration_files_on_server:

Agent configuration files on server
-----------------------------------

Agent master configuration files can be stored on server side and requested by agent,
if it is launched with :command:`-M <serverAddress>` command line parameter.
Each configuration file on server is stored along with filter script.
When server receives configuration request from agent, it goes through
available configs and executes filter scripts to find an appropriate configuration.

If appropriate configuration file is found, it is sent to agent and old
:file:`nxagentd.conf` file is overwritten (or a new :file:`nxagentd.conf` file is created, if
it did not exist). When agent can't connect to server or server hasn't found right configuration,
the agent is started with old configuration file. In case if agent configuration file does not
exist and it is not possible to get new one from the server - agent fails to start.

.. versionadded:: 1.2.15

**Doesn't work with tunnel agent connection**

Configuration
~~~~~~~~~~~~~

Each configuration has a name, filter script and the configuration file text.

 - Name just identifies the configuration.
 - Filter script is executed on configuration request to define which configuration file to
   send to the agent. Filter is defined with help of :term:`NXSL` scripting language.
   The following parameters are available in the filter script:

    - $1 - IP address
    - $2 - platform
    - $3 - major version number
    - $4 - minor version number
    - $5 - release number

 - Configuration file is the text of returned configuration file.

.. figure:: _images/agent_config_manager.png

Agent configuration policy
--------------------------

Another option to store and distribute agent configuration are agent policies. In this case agent
configuration is stored on the server side as a policy belonging to template and deployed to the agent when
corresponding template is applied to a node. More information about policies and their types can be found in
:ref:`agent-policies-label` chapter.

Agent Configuration Policies vs. Agent Configuration Files on Server
--------------------------------------------------------------------

A short lists of main points to compare both options:

Agent Configuration Files on Server:
  - Assignment is based on rules described in filter scripts
  - When configuration is changed, agent restart is needed to activate new configuration
  - Config download from server is each time the agent starts (if option '-M servername')
  - When config is found on server, local Master config is overwritten, if not - existing Master
    config is used
  - Works with master configuration file
  - Does not required initial config (agent can be started without config), but in this case agent
    would fail if nothing was returned from server
  - Server provides configuration file without authorization which can be a security
    issue, if sensitive information is present in configuration file.
  - Doesn't work via proxy
  - Doesn't work via tunnel agent connection

Agent Policies:
  - Not possible for bootstrap agent
  - After policy is deployed to agent, the agent should be restarted to activate new configuration.
  - At minimum the server connection parameters must be in master config to be able to start agent
  - Each policy is saved in a separate configuration file
  - If policy and master config have same parameter that can be set only once (e.g. LogFile),
    then policy will overwrite master config configuration
  - If policy and master config have same parameter that can be set multiple times
    (e.g. Target for PING subagent or Query for DBQUERY), then policy will merge lists of configs
  - Can work via proxy
  - Can work with tunnel agent connection

.. _agent-policies-label:

Agent Policies
==============

Agent policies are additional configuration created by user (agent configuration or files) that
are uploaded and updated on agent when template is manually or automatically applied on
the node. Agent policies belong to templates, so they are applied to nodes to which a
corresponding template is applied.

To create policy, right click a template and select :menuselection:`Agent policies`. Click plus
icon to create a new policy, give it a name, choose correct policy type and
click :guilabel:`OK`. Existing policy can be modified by right-clicking it and
selecting :menuselection:`Edit` from the menu or by double clicking on it.

The following policy types are available:
  - Agent configuration policy
  - File delivery policy
  - Log parser policy
  - User support application policy

Policies are automatically deployed to nodes after creation/modification or
when a template is applied to a node. When configuration policy is deleted or
template is removed from a node, the policy is automatically undeployed from node.

Policies get deployed / undeployed:
  - On node configuration poll.
  - When list of Agent Policies is closed in the management console. If
    a node is down at that moment, next attempt will happen on configuration poll.
  - When template is applied or removed from a node. If a node is down at that
    moment, next attempt will happen on configuration poll.

Installed policy configurations are stored as additional files under agent
:guilabel:`DataDirectory`. List of applied policies is stored in agent local database.

If agent discovers for a record in local database, that policy file is missing, it will
delete the record from database.

When performing deployment, server checks information in agent's database with it's
database and issues necessary commands.

Agent configuration policy
--------------------------

Agent configuration policy provides option to populate agent configuration with additional
parts. Main agent configuration is merged with additional rules from policy.
Using policy for configuration file maintenance has advantages that configuration
is edited in centralized way and gives granular control on the configuration that each node gets.
More information about different agent configuration options can be found in above chapters.

It is possible to use the same parameters and format as in any |product_name| agent configuration file
(key=value format or XML format).

Example:

.. code-block:: cfg

  MasterServer=127.0.0.1
  SubAgent=netsvc.nsm
  SubAgent=dbquery.nsm
  SubAgent=filemgr.nsm

  [DBQUERY]
  Database=id=myDB;driver=mysql.ddr;server=127.0.0.1;login=netxms;password=xxxxx;dbname=netxms
  Query=dbquery1:myDB:60:SELECT name FROM images
  ConfigurableQuery=dbquery2:myDB:Comment in param :SELECT name FROM images WHERE name like ?
  ConfigurableQuery=byID:myDB:Comment in param :SELECT name FROM users WHERE id=?

  [filemgr]
  RootFolder=/

.. code-block:: xml

  <config>
    <core>
      <!-- there can be added comment -->
      <MasterServers>127.0.0.1</MasterServers>
      <SubAgent>netsvc.nsm</SubAgent>
      <SubAgent>dbquery.nsm</SubAgent>
      <SubAgent>filemgr.nsm</SubAgent>
    </core>
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

Agent should be manually restarted to apply the configuration after the
configuration policy is deployed or undeployed to node.

Log parser policy
-----------------

Information about log parser format and usage available in :ref:`log-monitoring` chapter.

Log parser configuration is applied right after log parser policy is deployed or
undeployed to node - no agent restart is required.


File delivery policy
--------------------

File delivery policy is created to automatically upload files form server to agents.

First root folder or folders should be created - folders with the full path to place
where uploaded file and folder structure should be placed. After folder
structure is created files can be added to this structure. On policy apply folders will be
created if possible and files will be uploaded.

In file and folder names the following macros can be used:

  - Environment variables as %{ENV_VAR_NAME}
  - `strftime(3C) <http://www.unix.com/man-page/opensolaris/3c/strftime/>`_ macros
  - Text inside \` braces will be executed as a command and first line of output will be taken


Example:

  .. figure:: _images/policy_file_delivery.png

.. note:
  File delivery policy uses :ref:`File Manager<agent_file_managment>` to uplad files
  so :guilabel:`filemgr` subagnt should be loaded and root folders should be defined
  to provide write access to folders.


User support application policy
-------------------------------



Agent registration
==================

Two ways of agent-server communication are available. Standard one is when server initializes
connection to agent, the second one is when tunnel is used and agent initialize connection to server.

Server to agent connection
--------------------------

There are few ways to register agent:
   1. To enter it manually by creating a node
   2. Run the network discovery and enter the range of IP addresses.
   3. Register agent on management server ``nxagentd -r <addr>``,  where <addr> is the IP address of server.
      To register agents using this option :guilabel:`EnableAgentRegistration` server configuration parameter should be set to 1.

.. _agent-to-server-agent-conf-label:

Agent to server connection
--------------------------

This connection requires certificate configuration on server side. More about required actions can be found in
:ref:`server-tunnel-cert-conf`. Agent requires :guilabel:`ServerConnection` parameter set in agentd.conf file to
server :term:`DNS` or server IP address. It is possible to have several :guilabel:`ServerConnection` parameters in
the config, in this case agent will establish tunnel connection to multiple servers. 

Right after agent start it will try to connect to the server. On first connect node will be shown in :guilabel:`Agent Tunnels`.

There are few ways to register agent:
   1. To enter it manually by creating a node and then binding tunnel to already created node.
   2. Create node from :guilabel:`Agent Tunnels` view by selecting one or more tunnels and selecting
      :guilabel:`Create node and bind...` menu item.

Security
========

Message encryption in server to agent communication
---------------------------------------------------

Server encryption policy is configured in :guilabel:`Server Configuration` view by
selecting one of 4 options for :guilabel:`DefaultEncryptionPolicy` parameter. Default
Policy is 2.

Policy types:

  * 0 - Forbid encryption. Will communicate with agents only using unencrypted messages.
    If agent force encryption (:guilabel:`RequireEncryption` agent configuration
    parameter is set to :guilabel:`yes`), server will not accept connection with this agent.
  * 1 - Allow encryption. Will communicate with agents using unencrypted messages
    if encryption is not enforced by setting :guilabel:`RequireEncryption`
    agent configuration parameter to :guilabel:`yes` or by selecting
    :guilabel:`Force encryption` option in Communication properties of node object.
  * 2 - Encryption preferred. Will communicate with agents using encryption. In case if
    agent does not support encryption will use unencrypted communication.
  * 3 - Encryption required. Will communicate with agent using encryption. In case if
    agent does not support encryption will not establish connection.

.. figure:: _images/node_communications_tab.png

    Force encryption option for node.


Security in agent to server connection
--------------------------------------

Agent to server connection uses :term:`TLS` protocol to ensure communication security. Server has root certificate, that
is used to issue public certificate for agent. Server issues certificate to node when user manually
binds tunnel to a node in :guilabel:`Agent Tunnels`, or node is bind automatically
(when :guilabel:`AgentTunnels.UnboundTunnelTimeoutAction` server configuration parameter is set to
:guilabel:`Bind tunnel to existing node` or :guilabel:`Bind tunnel to existing node or create a new node`).
If required, this process can also be automated by NXShell. More information:
`NXShell examples <https://wiki.netxms.org/wiki/Using_nxshell_to_automate_bulk_operations>`_,
`Latest Javadoc <https://www.netxms.org/documentation/javadoc/latest/>`_.

Server access levels
--------------------

Depending on how server's IP address (or domain) is added to in nxagentd.conf, it will
have different access level. It is preferred to use MasterServers. There are 3 levels
of access for an agent:

   1. MasterServers - full access.
   2. ControlServers - can read data and execute predefined actions, but cannot change
      config nor install policies.
   3. Servers - read only access. (Is default for tunneled agent connection if other server level is not defined)

In case if server IP is not listed in one of this parameters agent will not enable
connection with server in server to agent connection or will set access level
to :guilabel:`Servers` if tunnel connection is used.

Shared secret
-------------

Shared secret is another level of server verification. By default authentication is
disabled.

To enable :guilabel:`Shared Secret` verification on agent set :guilabel:`RequireAuthentication`
agent configuration parameter to :guilabel:`yes`. In :guilabel:`SharedSecret` agent
configuration parameter set password what should be used for authentication.

If authentication for agent is enabled, then while connection agent requested shared
secret from the server. Server check if password was set for this specific node in
:guilabel:`Shared secret` field in communication properties of node. In case if there is
no shared secret server sends content of :guilabel:`AgentDefaultSharedSecret` server
configuration variable as shared secret.

.. figure:: _images/node_communications_tab.png

    Shared secret field in node communication properties.

In case shared secrets are not identical connection is not established.

Password encryption
-------------------

When it is required to write password or :guilabel:`Shared Secret` in agent
configuration file, there is possibility to encrypt it. All passwords can
be encrypted with help of :ref:`nxencpasswd-tools-label` command line tool and added
in configuration file in encrypted way.

.. _subagent_list:

Subagents
=========
Subagents are used to extend agent functionality. |product_name| subagent are libraries that are loaded by agent.
By default all subagents are included in agent build. Subagent may be not included in build
only if on time of the build there were no required libraries for subagent build. To enable
subagent is require just to add line in main agent configuration file (example: "Subagent=dbquery.nsm").
More about configuration and usage of subagents will be described in monitoring chapters.

Below is list of available |product_name| subagents:

  * :ref:`Asterisk <asterisk-monitoring>`
  * :ref:`DB2 <db2-subagent>`
  * Database Query
  * :ref:`DS18x20 <ds18x20-subagent>`
  * File Manager
  * :ref:`ECS <ecs-subagent>`
  * :ref:`Informix <informix-subagent>`
  * :ref:`Java <java-subagent>`
  * :ref:`lm-sensors <hardware-monitoring>`
  * :ref:`MongoDB <mongodb-subagent>`
  * :ref:`MQTT <mqtt-subagent>`
  * :ref:`MySQL <mysql-subagent>`
  * :ref:`Network Service Check <netsvc-subagent>`
  * ODBC Query
  * :ref:`Oracle <oracle-subagent>`
  * Ping
  * :ref:`Port Check <portcheck-subagent>`
  * :ref:`Raspberry Pi <rpi-subagent>`
  * :ref:`UPS <ups-monitoring>`
  * Windows Performance
  * WMI
  * XEN


.. _java-subagent:

Java subagent
-------------

This is a special type of subagent, that allows to load Java plugins(subagents written using Java language).
Java subagent does not provide any functionality by itself.

There are several configuration parameters that are supported by Java subagent. None of them is mandatory.

.. list-table::
   :header-rows: 1
   :widths: 50 200

   * - Parameter
     - Description
   * - Jvm
     - Path to JVM. System default is used if not set.
   * - Classpath
     - This parameter is added to java CLASSPATH.
   * - Plugin
     - This parameter defines plugin that should be loaded. Can be used multiple times.

Configuration example:

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent=java.nsm

   [JAVA]
   Jvm = /path/to/jvm
   Classpath = /path/to/user/classes
   Plugin = bind9.jar


Java plugins
~~~~~~~~~~~~

List of available java plugins:

  * JMX
  * Bind9

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

Proxy node can be set during node creation or in :guilabel:`Communications` tab
of node properties. To configure proxy node select node in object selector
:guilabel:`NetXMS Agent Proxy`.

.. figure:: _images/create_node.png

.. figure:: _images/node_communications_tab.png

Agent configuration
-------------------

To enable |product_name| Agent proxy "EnableProxy" agent configuration parameter should
be set to :guilabel:`yes`.


.. _agent-external-parameter:

Agent External Metrics
======================

Other option to define new Metric that can be collected from node is to use
``ExternalParameter``/``ExternalParameterShellExec``, or ``ExternalList``, or
``ExternalParametersProvider`` configuration parameters to define command that will
be executed on a node and it's output will be provided as a Metric. This functionality
provides flexibility to create your own metrics, lists or table metrics.

New Metrics will be visible in the :guilabel:`Available parameters` list only after agent
restarts (agent reads a configuration file only once on start) and configuration poll,
so to force it's appearance run :guilabel:`Configuration poll` manually after agent restart.

.. note::

   Since v. 3.5. on Windows platforms UTF-8 encoding should be returned in External Metrics. 
   
ExternalParameter/ExternalParameterShellExec
--------------------------------------------

``ExternalParameter`` defines name of the metric and command that is executed synchronously
when this metric is requested by server. There can be provided parameters from DCI
configuration, that will be available like $1, $2, $3..., $9 variables. To accept
arguments metric name should contain "(*)" symbols after name. Only first line of
script output will be given as a result of execution(metric value).

``ExternalParameterShellExec`` has same meaning as ``ExternalParameter`` and behaves identically on non-Windows systems.
On Windows systems ``ExternalParameter`` executes specified command using system process execution
API's CreateProcess() function. It will search in PATH, but the command should be with file extension, e.g. ``command.exe``.
``ExternalParameterShellExec`` will use shell to execute specified command on Windows.

To add multiple parameters, you should use multiple
``ExternalParameter``/``ExternalParameterShellExec`` entries.

As this commands are executed synchronously, long commands may cause timeout. In this
case ``ExecTimeout`` configuration parameter can be set to change external parameter
execution timeout or ``ExternalParametersProvider`` can be used.

.. code-block:: cfg

  # Example

  # Without DCI parameters
  ExternalParameter=Name:command
  ExternalParameterShellExec=Name:command

  # With DCI parameters
  ExternalParameter=Name(*):command $1 $2
  ExternalParameterShellExec=Name(*):command $1 $2

  #Real examples
  ExternalParameter = Test:echo test
  ExternalParameter = LineCount(*):cat $1 | wc -l


ExternalList
------------

``ExternalList`` defines name of the list metric and command that is executed
synchronously when this metric is requested by server. There can be provided parameters
from DCI configuration, that will be available like $1, $2, $3..., $9 variables. To
accept arguments metric name should contain "(*)" symbols after name. Lines of list
are separated with new line.

.. code-block:: cfg

  # Example

  # Without DCI parameters
  ExternalList=Name:command

  # With DCI parameters
  ExternalList=Name(*):command $1 $2


ExternalParametersProvider
--------------------------

``ExternalParametersProvider`` defines command(script) and execution interval in seconds. Defined
script will be executed as per interval and agent will cache parameter list. When server
will request one of provided parameters it's value will be read from the agent cache.
Main purpose is to provide data from long-running processes, or return multiple
values at once.

Script should print one or more "Parameter=Value" pairs to standard output. Multiple
pairs should be separated by new line. If parameter takes argument, it should be
included in "Parameter(...)".

Example of the script:

.. code-block:: shell

  #!/bin/sh
  echo 'Parameter1=Value1'
  echo 'Parameter2=Value2'
  echo 'ParameterWithArgs(AAA)=Value3'
  echo 'ParameterWithArgs(BBB)=Value4'

Example of agent configuration:

.. code-block:: cfg

  #Example
  ExternalParametersProvider=PATH_TO_PROVIDER_SCRIPT:POLL_TIME_IN_SECONDS

  #Example (run /tmp/test.sh every 5 seconds)
  ExternalParametersProvider=/tmp/test.sh:5

ExternalTable
-------------

``ExternalTable`` defines name of the table metric, table metric description, column separator,
instance column(s) and command. Instance column(s), descriptions and separator are optional.
If separator is not specified, default value of ``,`` is used.

Instance column should contain unique identifier for each table row. If several instance columns are used, then
combination of these columns should be unique. This is necessary for building graphs and for threshold violation event generation.

Command is executed synchronously when this metric is requested by server.
Each table line is separated with new line symbol. First line in returned text used as a name of the columns
and all next lines will be used like table data. Parameters from DCI configuration can be provided,
that will be available like $1, $2, $3..., $9 variables. To accept arguments metric name should contain
"(*)" symbols after name.

.. code-block:: cfg

  # Example

  # Without DCI parameters
  ExternalTable=dciName:instanceColumns=columnName;description=description;separator=|:command

  # With DCI parameters
  ExternalTable=dciName(*):instanceColumns=columnName;description=description;separator=|:command $1 $2

Separator supports special macros for separator:

    * \\n - \\n
    * \\r - \\r
    * \\s - space
    * \\t - tab
    * \\u115 - unicode character number 115

.. _agent-actions:

Agent Actions
=============

For security reasons actions that can be executed on agent first are defined in
agent configuration file and only then can be used by users. This excludes that an
unauthorized user can access system data through an arbitrary entered command. Only
users with access to the agent configuration file editing can define executed commands.

There are 2 options to define action:

   #. Action - usual action definition. On Windows platform system process execution API's CreateProcess() is used to run the command, it will search in PATH, but the command should be with file extension, e.g. ``command.exe``.
   #. ActionShellExec - Same as Action, but on the Windows platform agent will use shell to execute command instead of normal process creation. There is no difference between Action and ActionShellExec on UNIX platforms.

Both versions accept parameters that will be available like ``$1``, ``$2``, ``$3``..., ``$9`` variables.

After action is defined it can be used in the :ref:`object tools - agent action<object_tool-agent-command>` or in
:ref:`actions - action execution on remote node<action-remote-execute>`. Action should be defined in main section of
agent configuration file.

.. code-block:: cfg

  # Example
  Action=Name:command
  Action=Name:command $1 $2
  Action=cleanLogs:rm /opt/netxms/log/*
  Action=ping:ping $1
  ActionShellExec=listFiles:dir $1
