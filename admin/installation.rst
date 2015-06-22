.. _installation:

############
Installation
############


Synopsis
========


Planing
=======


Installing on Debian or Ubuntu
==============================


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


Installing on Red Hat, Fedora, CentOS or ScientificLinux
========================================================


Adding our YUM repository
-------------------------


Installing packages
-------------------


Server
~~~~~~


Agent
~~~~~


Management console
~~~~~~~~~~~~~~~~~~


Installing on Windows
=====================


Adding our YUM repository
-------------------------


Installing packages
-------------------


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


