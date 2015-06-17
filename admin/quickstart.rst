.. _quick-start:


###########
Quick start
###########

In this section will be described basic configuration that should be done 
after server and agent clean install. Also will be shown monitoring configuration 
for some common metrics like CPU of FS.

Basic agent configuration
=========================

Minimal configuration that should be set for agent is server address and path 
to log file. Action differ depending on a platform where agent is installed. 
On Windows systems configuration file is automatically generated and populated 
by installer, on UNIX systems it should be created/edited manually. 

After all required configuration is done run agent as a service on windows and 
as a daemon(/usr/bin/nxagentd -D6) on UNIX system.

Windows
-------

In case if while installation MasterServer was set correctly no action is 
required form user. 

Automatically generated configuration file can be found there: 
:file:`'installation directory'\\etc\\nxagentd.conf'`.

Configuration file for Windows should look like this:

.. code-block:: cfg  

    #
    # Sample agent’s configuration file
    #
    MasterServers = 127.0.0.1
    LogFile = {syslog}

UNIX/Linux
----------

After agent is installed on a UNIX/Linux system it is required to create/edit file
:file:`/etc/nxagentd.conf`. This file should contain at least this information:

.. code-block:: cfg  

    #
    # Sample agent’s configuration file
    #
    MasterServers = 127.0.0.1
    LogFile = /var/log/nxagentd


Basic server tuning
===================

Server has 2 types of configuration: configuration file parameters and server 
configuration variables.

For server configuration file minimal requirements are path to log file, database 
driver name and all required credentials depending on database. Location and 
required actions depends on what OS is used. More about OS specific configuration 
search in OS subsections of this chapter. 

List of possible database drivers: 

  * db2.ddr
  * informix.ddr 
  * mssql.ddr 
  * mysql.ddr Driver for MySQL database.
  * odbc.ddr ODBC connectivity driver (you can connect to MySQL, PostgreSQL, MS SQL, and Oracle via ODBC).
  * oracle.ddr Driver for Oracle database.
  * pgsql.ddr Driver for PostgreSQL database.
  * sqlite.ddr Driver for embedded SQLite database.
  
There are quite a few important server parameters to be set right after installation. 
These parameters are accessible through the :guilabel:`Server Configuration` window 
in the console. To open it, click on :menuselection:`Configuration --> Server Configuration`. 
To edit a setting, double click on the row in the table or right-click and select 
:guilabel:`Edit`. The following parameters may need to be changed:

.. tabularcolumns:: |p{0.4 \textwidth}|p{0.6 \textwidth}|

================================ ==============================================
Parameter                        Description
================================ ==============================================
``NumberOfStatusPollers``        If you plan to monitor large number of hosts,
                                 increase this parameter from the default value
                                 to approximately 1/10 of host count.
``NumberOfConfigurationPollers`` If you plan to monitor large number of hosts,
                                 increase this parameter from the default value
                                 to approximately 1/20 of host count.
``NumberOfDataCollectors``       If you plan to monitor large number of hosts,
                                 increase this parameter from the default value
                                 to approximately 1/10 – 1/5 of host number.
                                 Use larger value if you plan to gather many
                                 DCIs from each host.
``EnableSyslogDaemon``           Set this parameter to 1 if you want to
                                 enable NetXMS built-in syslog server.
================================ ==============================================

Windows
-------

For Windows systems this information is added to configuration file while 
installation procedure. It can be check that all data was set correctly 
in this file: :file:`'installation directory'\\etc\\nxagentd.conf'`. 

Example of sample Windows configuration for mysql:

.. code-block:: cfg  

  #
  # Sample configuration file for NetXMS server
  #

  DBDriver = mysql.ddr
  DBServer = localhost
  DBName = netxms_db
  DBLogin = netxms
  DBPassword = password
  LogFailedSQLQueries = yes
  LogFile = {syslog}
  

UNIX/Linux
----------
  
For UNIX based systems :file:`/etc/netxmsd.conf` file should be 
created/populated manually. 

Configuration file example for oracle database:

.. code-block:: cfg  

  DBDriver = oracle.ddr
  DBServer = ServerIP/Hostname.DomainName #Here is service (full database name), not SID
  DBName = netxms
  DBLogin = netxms
  DBPassword = PaSwD
  LogFailedSQLQueries = yes
  LogFile = /var/log/netxmsd
  

SMTP
====

SMTP configuration is done to create actions that will send e-mails on 
defined events. This configuration is done through the 
:guilabel:`Server Configuration` window in the console. To open it, click 
on :menuselection:`Configuration --> Server Configuration`. To edit a 
setting, double click on the row in the table or right-click and select 
:guilabel:`Edit`. The following parameters may need to be changed:

.. tabularcolumns:: |p{0.4 \textwidth}|p{0.6 \textwidth}|

================================ ==============================================
Parameter                        Description
================================ ==============================================
``SMTPFromAddr``                 Address that will be shown as a sender address 
                                 when notification from NetXMS will come.
``SMTPFromName``                 Name that will be shown as a sender name 
                                 when notification from NetXMS will come.
``SMTPRetryCount``               Number of retries that NetXMS will try to do 
                                 in case if message sending will fail. 
``SMTPServer``                   Server IP address or DNS name where NetXMS 
                                 will send request for message dispatch. 
================================ ============================================== 

SNMP Defaults
=============

For :term:`SNMP` can be configured some default values for authorization. It is 
required if you will have many :term:`SNMP` devices with similar credentials. 

This information is set on :guilabel:`Network Discovery` view. 

SNMP Communities
----------------

In this section you can add SNMP community strings to be tested during
connection to the SNMP device that requires authorization. 


SNMP USM Credentials
--------------------

In this section you can add SNMP version 3 credentials to be tested during
connection to the SNMP device that requires authorization. 

Actions and Alarms
==================

In this section will be shown how to configure alarm and email notifications 
generation on predefined SYS_THRESHOLD_REACHED event. And alarm termination on 
SYS_THRESHOLD_REARMED event. 

First it should be created :guilabel:`Send E-Mail` action in 
:guilabel:`Action Configuration` view. There we will set recipient of e-mail, 
subject and body of e-mail. In body of e-mail will be used 
:ref:`event-processing-macros`. It means that when message will be sent, macros 
"%n" will be substituted with name of the node and "%1" will be substituted with 
DCI description. Values that are accessible through %1-9 depends on event and 
are described in each event description. 

.. todo::
  add immage


  
Passive discovery
=================



Manually add node
=================

If the automatic network discovery does not detect all of your hosts or
devices, or you decide not to use network discovery at all, you may need to
manually add monitored nodes to the system. The easiest way to accomplish this
is to right-click on :guilabel:`Infrastructure Services` in the
:guilabel:`Objects` pane and select :guilabel:`Create node`. You will be
presented with the following dialog window:

.. figure:: _images/create_node.png

   Create Node window

Please note that adding a new node object may take some time, especially if a
node is down or behind a firewall. After successful creation, a new node object
will be placed into appropriate subnets automatically. As soon as you add a new
node to the system, NetXMS server will start regular polling to determine the
node status.

Add DCI thresholds 
==================

In this section is described how to configure CPU load monitoring and switch traffic 
monitoring over SNMP. There will be also shown threshold configuration for each DCI. 
This threshold will generate SYS_THRESHOLD_REACHED event when defined condition is 
meet and SYS_THRESHOLD_REARMED when condition . 

Earlier we already described how to configure email notifications and alarm generation 
and termination based on this events. In this chapter is described data collection and 
event generation based on collected data. 


SNMP 1 Trafic interface
Agent 1  CPU

