.. _installation:

############
Installation
############


Synopsis
========


Planing
=======

Operating system
----------------

Supported operating systems for NetXMS server:
   * Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * RedHat Enterprise Linux, SUSE Linux, CentOS, Debian Linux, Ubuntu Linux
   * FreeBSD, NetBSD, OpenBSD
   * Solaris 10, 11
   * HP-UX 11.23, 11.31
   * AIX 5.3 +
   
Supported operating systems for NetXMS agent:
   * Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * Linux (all glibc2-based flavors)
   * FreeBSD, NetBSD, OpenBSD
   * Solaris
   * HP-UX
   * AIX

If you wish to compile NetXMS server with encryption support on UNIX, you must have 
OpenSSL package installed.
   
Server
------

Minimum requirements: Intel Pentium III 500 MHz, 256MB RAM, 100MB of free disk space.

Recommended: Intel Pentium IV 1 GHz, 512MB RAM, 100MB of free disk space.

Additional RAM may be required for large installations (1000+ nodes). For non-Intel 
platforms, an equivalent hardware must be used.

In free disk space requirements is taken into account only initial server size, without 
Database and possible files that can be loaded to server(agent update packages, 
pictures, etc).

If you wish to compile NetXMS server with encryption support on UNIX, you must have 
OpenSSL package installed.

Database
--------

Supported DBMS engines for NetXMS server:
   * Microsoft SQL Server 2005, Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * MySQL 5.0 +
   * Oracle 11g, 12
   * PostgreSQL 8+
   * DB/2
   * SQLite(it is highly recommended use this option only for test purpose)

Database size and load is very hard to predict, because it is dependent on a number of 
monitored nodes and collected parameters. If you plan to install database engine on 
the same machine as NetXMS server, increase your hardware requirements accordingly.

Link to Excel file that allows roughly estimate the size that will be required for 
database: http://git.netxms.org/public/netxms.git/blob/HEAD:/doc/misc/database_sizing.xlsx?js=1

Agent
-----



Installing on Debian or Ubuntu
==============================

We provide deb packages for Debian users at http://packages.netxms.org/, which is our 
public APT repository. Packages are signed, so you'll need to install additional 
encryption key for signature verification.

.. note::

  At the moment (23/3/15) we provide binary packages for Debian only, 
  Ubuntu support will be shortly.
  
There are 2 options for server and agent installation on Debian/Ubuntu systems: 
using APT repository or from source. There will be described instruction only for 
APT repository. I installation using source tarball is described 
:ref:`there <centos_install>`.

Adding our APT repository
-------------------------


Installing packages
-------------------


Server
~~~~~~


Agent
~~~~~


Management console
~~~~~~~~~~~~~~~~~~

.. _centos_install:

Installing on Red Hat, Fedora, CentOS or ScientificLinux
========================================================

Agent and server for this systems can be installed only from source. 

.. note::

  YUM repository for this systems will be created soon. 

Adding our YUM repository
-------------------------


Installing packages
-------------------


Server
~~~~~~

Installing server using source archive:

  1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need source archive (named netxms-VERSION.tar.gz, for example netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be used as a substitution for an actual version number.
  2. Unpack the archive: 
  
    :command:`tar zxvf netxms-1.2.15.tar.gz`
    
  3. Change directory to netxms-version and run configure script:
  
    :command:`cd netxms-1.2.15`
    
    :command:`sh ./configure --with-server --with-mysql --with-agent`    
    
    Important arguments:
    
    --prefix=DIRECTORY: installation prefix, all files go to the specified directory;
    
    --with-server: build server. Don't forget to add at least one DB Driver as well;
    
    --with-pgsql: build Postgres DB Driver (if you plan to use PostgreSQL as backend database);
    
    --with-mysql: build MySQL DB Driver (if you plan to use MySQL as backend database);
    
    --with-odbc: build ODBC DB driver (if you plan to connect to your backend database via ODBC; you will need UNIX ODBC package to do that);
    
    --with-sqlite: build SQLite DB driver (if you plan to use embedded SQLite database as backend database);
    
    --with-agent: build monitoring agent. It is strongly recommended to install agent on a server box;
    
    --disable-encryption: Disable encryption support.
    
    To learn more about possible configure parameters, run it with --help option.
    
  4. Run make and make install:
  
    :command:`make`
    
    :command:`make install`  
    
  5. Copy sample config files to desired locations:
  
    :command:`cp contrib/netxmsd.conf-dist /etc/netxmsd.conf`
    
    :command:`cp contrib/nxagentd.conf-dist /etc/nxagentd.conf`  
    
    By default, both server and agent will look for configuration files in /etc 
    directory. If you wish to place configuration files in a different location, 
    don't forget to use –c command line switch for agent and –config-file command-line 
    switch for server to specify an alternate location.
  
  6. Check that database and user for it are created. :ref:`install_centos_database`
  7. Modify server configuration file (default is /etc/netxmsd.conf). It should look 
     the following way:
     
    .. code-block:: cfg
    
      DBDriver = mysql.ddr
      DBServer = localhost
      DBName = netxms
      DBLogin = netxms
      DBPassword = PaSsWd
      LogFile = /var/log/netxmsd
      LogFailedSQLQueries = yes
        
    More information about each configuration parameter can be found there: 
    :ref:`server_configuration_parameters`.
    
  8. Modify agent's configuration file (/etc/nxagentd.conf). For detailed description 
     of possible parameters, please consult NetXMS User's Manual. For the normal 
     server's operation, you should add at least the following line to your agent's 
     configuration file:
  
    .. code-block:: cfg
      
      MasterServers = 127.0.0.1, your_server_IP_address
      
  9. Initialise this database with nxdbmgr utility using sql-script in 
     sql/dbinit_DBTYPE.sql. DBTYPE can be "mssql", "mysql", "pgsql", "oracle", or 
     "sqlite".
     
     MySQL example:
     
    :command:`$ /usr/local/bin/nxdbmgr init /usr/local/share/netxms/sql/dbinit_mysql.sql`
     
  10. Run agent and server:
  
    :command:`$ /usr/local/bin/nxagentd -d`

    :command:`$ /usr/local/bin/netxmsd -d`
    
.. _install_centos_database:    
    
Database
~~~~~~~~

Create Database and User with access rights to this database.

Example for MySQL:

.. code-block: sql

  mysql -u root -p mysql
  mysql> CREATE DATABASE netxms;
  mysql> GRANT ALL ON netxms.* TO netxms@localhost IDENTIFIED BY 'PaSsWd';
  mysql> \q

`Example for Oracle 11g. <https://wiki.netxms.org/wiki/Oracle>`_


Please note that database user you have created should have rights to create 
new tables.

Agent
~~~~~


Management console
~~~~~~~~~~~~~~~~~~


Installing on Windows
=====================

Installing
----------


Server
~~~~~~

  1. Download the latest version from http://www.netxms.org/download, if you don't 
     have it. You will need Windows installer (named netxms-VERSION.exe or 
     netxms-VERSION-x64.exe, for example netxms-1.2.15.exe). Please note that in 
     following steps VERSION will be used as a substitution for an actual version 
     number.
  2. Run the installer package on your server machine. Installation wizard will be 
     shown. Follow the prompts until the Select Components window opens.
  3. On the Select Components window, select NetXMS Server option and an appropriate 
     database client library. You do not have to install database client library 
     from NetXMS package, if it is already installed on the machine.
     
    .. figure:: _images/win_netxms_setup_components.png

    If you plan to run NetXMS console from the same machine, select Administrator's Console option as well.

  4. Follow the prompts until Ready to Install window opens.

  5. On Ready to Install window, check whether everything is correct, then press the Install button.

  6. After copying files, Server Configuration Wizard will open:

    .. figure:: _images/win_server_config_step1.png

    Press the Next button to start NetXMS server configuration.
    
  7. Database selection window will open:

    .. figure:: _images/win_server_config_step1.png
    
    
    
  * Select the desired database engine and driver. For most databases, you will have 
    two drivers available – native and ODBC. Please note that if you select ODBC, you 
    will have to manually configure ODBC source.
  * Enter the name of database server or ODBC source.
  * In DBA login name and DBA password fields, enter database administrator’s login 
    name and password. You have to fill these fields only if you have chosen Create 
    new database option.
  * Enter the desired database name, database user name and password. If you are not 
    using ODBC, the wizard will create database and a user for you. If ODBC is used, 
    database and user should be created beforehand.
  
    **Microsoft SQL note**:

    If you wish to use Windows authentication for database connectivity, use * (asterisk) 
    as a login name and leave the password field blank. If you specify asterisk as DBA 
    login, user with which you are logged in to Windows should have administrative rights 
    to the database server. If you use asterisk as DB login, you should run NetXMS Server 
    service as a user with appropriate rights to the database.
      
    **Oracle note**:
      
    We recommend to use native database driver (oracle.ddr).

  8. On the next window, you will be prompted for various polling parameters:
  
    .. figure:: _images/win_server_config_step1.png
    
    * Check Run IP autodiscovery process check-box, if you wish NetXMS server to 
      automatically discover your IP network.
    * Increase number of status and configuration pollers if you plan to monitor 
      large number of nodes.
      
  9. On the next window, enter address of your SMTP server. NetXMS will use it to send 
     notification e-mails. If you have mobile phone attached to management server via 
     serial cable or USB, select mobile phone driver and COM port; otherwise, select 
     "<none>".

  10. Then next window will prompt you for logging method. Either check Event Log or 
      select file, and press the Next button.

  11. Windows service configuration window will appear:
  
    .. figure:: _images/win_server_config_step1.png
    
    In most situations, you can run NetXMS server under Local System account. You may 
    need to run it under specific account if you are using Microsoft SQL database and 
    Windows authentication, or for security reasons.
  
  12. Windows service dependency window will appear:
  
    .. figure:: _images/win_server_config_step1.png
    
    If you have database engine running on same server, you can find it in service 
    list and mark, so NetXMS server's service will depend on database service and 
    service startup order will be correct.
  
  13. Follow the prompts until server configuration will be complete. After successful 
  server configuration, installation will be finished, and you will have NetXMS server 
  up and running.
  
Agent
~~~~~


Management console
~~~~~~~~~~~~~~~~~~


Generic installation, upgrade and downgrade using source tarball
================================================================



Cryptographic verification of installation files
================================================


Synopsis
--------


Importing the Phusion Software Signing key
------------------------------------------


Verifying the Phusion Software Signing key
------------------------------------------


Verifying the gem and tarball
-----------------------------


Verifying Git signatures
------------------------


Verifying DEB and RPM packages
------------------------------


Revocation
----------


Customizing the compilation process
===================================


Adding additional compiler or linker flags 
------------------------------------------

(e.g. fixing atomics)


