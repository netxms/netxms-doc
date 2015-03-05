#################
Server management
#################


Configuration file
==================

File netxmsd.conf is a configuration file for NetXMS server. It contains 
information necessary for establishing database connection, and some optional 
server parameters. Default location for this file is :file:`/etc/netxmsd.conf`
on UNIX systems and :file:`InstalationPath\etc\netxmsd.conf on Windows`.

The file can contain one or more parameters in *Parameter = Value* form, 
each parameter should be on its own line. Comments can be inserted after "#" sign.

Detailed list of parameters can be found there: :ref:`server_configuration_file`.    
    
Configuration file example:
::  

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

  
Configuration variables
=======================

Global server parameters can be found in 
This variables are stored in database and can be changed using 
:guilabel:`Server Configuration Editor` :term:`view<View>` accessing it
:menuselection:`Configuration-->Server Configuration` or with help 
of :file:`nxdbmgr`(example: :code:`nxdbmgr set <name> <value>`).
Detailed description of each configuration can be found there: :ref:`server_configuration_parameters`.
Please note that changes to most of the settings will take effect only after server restart. 

Synchronization between servers
===============================

NetXMS does not provide horizontal scalability for server. But there is option to exchange with 
events between servers. Information about configuration can be found there: :ref:`forward_events`
