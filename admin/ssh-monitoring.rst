.. _ssh-monitoring:

==============
SSH monitoring
==============

SSH configuration
-----------------

NetXMS can execute commands via SSH connection and save the output as DCI values.

SSH connection are always established via agent. For this to work, ``ssh.nsm`` subagent should be enabled in agent config file.

Subagent uses built-in libssh. It reads configuration in standard ssh format from ~/.ssh/config.
It's also possible to specify custom location for configuration file by adding ``ConfigFile=`` into ``[SSH]`` section of agent configuration file.

If zoning is not used, agent running on |product_name| server is used for SSH connections.
If zoning is used, zone proxies are used (and if a zone has no proxies configured, agent on |product_name| server is used as last resort).

Username and password are specified in :menuselection:`Node properties -> Communications -> SSH`. Same properties 
page can used to specify ssh port for node, proxy for ssh polling and ssh key if required. 
If proxy node is specified on this property page, connection will be performed via that node only.

.. figure:: _images/ssh_monitoring_node_properties.png

In DCI properties ``SSH`` origin should be chosen. Parameter is the actual ssh command that is executed.

Only first line of the output is stored as DCI value. For numeric data type output is parsed from beginning till first non-numeric character.

.. figure:: _images/ssh_monitoring_dci_properties.png

There's also ``SSH.Command(*)`` parameter of origin ``NetXMS Agent`` that works in a similar way,
but target and credentials are specified as arguments. It's also necessary to manually specify Source node,
otherwise agent of the monitored node will be used for establishing ssh connection.

.. list-table::
   :widths: 100 50
   :header-rows: 1

   * - Parameter
     - Description
   * - SSH.Command(\ *target*\ ,\ *login*\ ,\ *password*\ ,\ *command*\ ,\ *[pattern]*\ ,\ *[ssh_key_id]*\)
     - ``%{node_primary_ip}`` macro can be used to specify node's primary IP address as *target*.


SSH key configuration
---------------------

SSH key can be added in :menuselection:`Configuration ->SSH key configuration` and then used in object configuration 
for SSH connection.

.. figure:: _images/ssh_key_configuration.png
