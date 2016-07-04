.. _upgrade:

#######
Upgrade
#######

Upgrading on Debian or Ubuntu
=============================

Upgrading packages
------------------

To update all NetXMS packages run command:

:command:`apt-get update && apt-get upgrade`


Management console
~~~~~~~~~~~~~~~~~~

Desktop Management Console:

 1. Download the latest version from http://www.netxms.org/download. You will need 
    Linux installer(named nxmc-VERSION-linux-gtk-x86.tar.gz or 
    nxmc-VERSION-linux-gtk-x64.tar.gz, for example nxmc-1.2.17-linux-gtk-x64.tar.gz).
    
 2. Extract and replace old management console with the new one.
 
    :command:`tar zxvf nxmc-VERSION-linux-gtk-x86.tar.gz -C /DIRECTORY`
    
 3. Run nxmc file form extracted catalog. 
 
Web Management Console:

  1. Download latest version of WAR file from Web Interface Binaries section 
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example 
     nxmc-1.2.17.war).
     
  2. Replace old WAR file with the new one. 
  

Upgrading on Red Hat, Fedora, CentOS or ScientificLinux
=======================================================


Adding our YUM repository
-------------------------

Upgrading
---------

Server
~~~~~~

  1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need source archive (named netxms-VERSION.tar.gz, for example netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be used as a substitution for an actual version number.
  2. Unpack the archive:

    :command:`$ tar zxvf netxms-1.2.15.tar.gz`
    
  3. Change directory to netxms-version and run configure script:

    :command:`$ cd netxms-1.2.15`
    
    :command:`$ sh ./configure --with-server --with-mysql`
    
    Be sure to include all options that were used at installation time.


  4. Run make:

    :command:`$ make`
    
  5. Stop NetXMS server. 
  
  6. Stop NetXMS agent. 
  
  7. Check database for possible inconsistencies:

    :command:`$ nxdbmgr check`
    
    Proceed to the next step only if database checker does not report any errors!

  8. Run make install:

    :command:`$ make install`
    
  9. Upgrade database:

    :command:`$ nxdbmgr upgrade`
    
  10. Start NetXMS agent.

  11. Start NetXMS server.

Agent
~~~~~

  1. Download the latest version from http://www.netxms.org/download, if you don't 
     have it. You will need source archive (named netxms-VERSION.tar.gz, for example 
     netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be 
     used as a substitution for an actual version number.
     
  2. Unpack the archive: 
  
    :command:`tar zxvf netxms-1.2.15.tar.gz`
    
  3. Change directory to netxms-version and run configure script:
  
    :command:`cd netxms-1.2.15`
    
    :command:`sh ./configure --with-agent`        
   
    Be sure to include all options that were used at installation time. 
    
  4. Run make and make install:
  
    :command:`make`
    
  5. Stop NetXMS agent. 
    
  6. Run make install:
   
    :command:`make install`  
    
  7. Run agent:
  
    :command:`$ /usr/local/bin/nxagentd -d`

Management console
~~~~~~~~~~~~~~~~~~

Desktop Management Console:

 1. Download the latest version from http://www.netxms.org/download. You will need 
    Linux installer(named nxmc-VERSION-linux-gtk-x86.tar.gz or 
    nxmc-VERSION-linux-gtk-x64.tar.gz, for example nxmc-1.2.17-linux-gtk-x64.tar.gz).
    
 2. Extract and replace old management console with the new one.
 
    :command:`tar zxvf nxmc-VERSION-linux-gtk-x86.tar.gz -C /DIRECTORY`
    
 3. Run nxmc file form extracted catalog. 
 
Web Management Console:

  1. Download latest version of WAR file from Web Interface Binaries section 
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example 
     nxmc-1.2.17.war).
     
  2. Replace old WAR file with the new one. 
  

Upgrading on Windows
====================

Upgrade
-------

Server
~~~~~~

1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need Windows installer (named netxms-VERSION.exe, for example netxms-1.2.15.exe).

2. Stop NetXMS server.

3. Check database for possible inconsistencies:

.. code-block:: cfg

  C:\NetXMS\bin> nxdbmgr check

Proceed to the next step only if database checker does not report any errors!

4. Run NetXMS installer and follow the prompts. Normally, you will not need to change any settings on installation wizard windows. Alternatively, you can run the installer with /SILENT option to disable any prompts:

.. code-block:: cfg

  C:\Download> netxms-1.2.15.exe /SILENT

5. Check whether NetXMS Server service is running again. If it's not, most likely you have to upgrade your database to newer version. To upgrade database, use nxdbmgr utility:

.. code-block:: cfg

  C:\NetXMS\bin> nxdbmgr upgrade

6. Start NetXMS server, if it is not already started.
  
Agent
~~~~~

We highly recommend using centralized agent upgrade feature for agent upgrades. 
However, if you decide to upgrade agent manually, it can be done in just a few steps:

  1. Download the latest version from http://www.netxms.org/download, if you don't 
     have it. You will need Windows Agent installer (named nxagent-VERSION.exe or 
     nxagent-VERSION-x64.exe, for example nxagent-1.2.0.exe).

  2. Run NetXMS agent installer and follow the prompts. Normally, you will not need 
     to change any settings on installation wizard dialog windows. Alternatively, you 
     can run installer with /SILENT option to disable any prompts:

      :command:`C:\Download> nxagent-1.2.0.exe /SILENT`

Management console
~~~~~~~~~~~~~~~~~~

Desktop Management Console:

 1. Download the latest version from http://www.netxms.org/download. You will need 
    Windows installer(named nxmc-VERSION-win32-x86.zip or 
    nxmc-VERSION-win32-x64.zip, for example nxmc-1.2.17-win32-x64.zip).
    
 2. Replace old old folder with content of the zip. 
    
 3. Run nxmc.exe file form extracted catalog.  
 
Web Management Console:

  1. Download latest version of WAR file from Web Interface Binaries section 
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example 
     nxmc-1.2.17.war).
     
  2. Replace old WAR file with the new one. Default path: INSTALLATION_DIR\webapps.

Generic upgrade using source tarball
====================================

Server
------

  1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need source archive (named netxms-VERSION.tar.gz, for example netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be used as a substitution for an actual version number.
  2. Unpack the archive:

    :command:`$ tar zxvf netxms-1.2.15.tar.gz`
    
  3. Change directory to netxms-version and run configure script:

    :command:`$ cd netxms-1.2.15`
    
    :command:`$ sh ./configure --with-server --with-mysql`
    
    Be sure to include all options that were used at installation time.


  4. Run make:

    :command:`$ make`
    
  5. Stop NetXMS server. 
  
  6. Stop NetXMS agent. 
  
  7. Check database for possible inconsistencies:

    :command:`$ nxdbmgr check`
    
    Proceed to the next step only if database checker does not report any errors!

  8. Run make install:

    :command:`$ make install`
    
  9. Upgrade database:

    :command:`$ nxdbmgr upgrade`
    
  10. Start NetXMS agent.

  11. Start NetXMS server.

Agent
-----

  1. Download the latest version from http://www.netxms.org/download, if you don't 
     have it. You will need source archive (named netxms-VERSION.tar.gz, for example 
     netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be 
     used as a substitution for an actual version number.
     
  2. Unpack the archive: 
  
    :command:`tar zxvf netxms-1.2.15.tar.gz`
    
  3. Change directory to netxms-version and run configure script:
  
    :command:`cd netxms-1.2.15`
    
    :command:`sh ./configure --with-agent`        
   
    Be sure to include all options that were used at installation time. 
    
  4. Run make and make install:
  
    :command:`make`
    
  5. Stop NetXMS agent. 
    
  6. Run make install:
   
    :command:`make install`  
    
  7. Run agent:
  
    :command:`$ /usr/local/bin/nxagentd -d`
    
.. _agent-remote-update:

Centralized agent upgrade
=========================

Steps to update agent remotely:
   1. Download NetXMS agent installer from http://www.netxms.org/download/
   2. Download the appropriate NPI file for your agent installer(NPI file is just a reference to actual package file. You should have it as well in the same directory as NPI file.)
   3. Open "Package Manager"  
   
      .. figure:: _images/package_manager.png    
      
   4. Chose "Install new package..."
   5. Browse for NPI file
   6. When new package appeared - right click on it and chose "Deploy to managed nodes..."
   7. Select the nodes you want to upgrade by holding CTRL key
