.. _upgrade:

#######
Upgrade
#######

Upgrading on Debian or Ubuntu
=============================

Upgrading server and agent
--------------------------

 1. It's recommended to check database for possible inconsistencies
    prior to the upgrade. To do this, stop the server and run command:

    :command:`nxdbmgr check`

    Proceed to the next step only if database checker does not report any errors!

 2. To update |product_name| server and agent packages run command:

    :command:`apt-get update && apt-get upgrade`

    During package upgrade database schema should be upgraded as well and 
    |product_name| server would start automatically. However, in some cases 
    (e.g. if database engine packages were also upgraded) automatic database
    upgrade may not happen. If this is the case, |product_name| server won't
    get started and it's log would show, e.g.: ``Your database has format
    version 41.07, but server is compiled for version 41.18``. To upgrade
    the database, run command:

    :command:`nxdbmgr upgrade`

    Once database upgrade is complete, start the server. 


Management client
~~~~~~~~~~~~~~~~~

Desktop Management Client:

 1. Download the latest version from http://www.netxms.org/download. You will need
    Linux installer (named nxmc-VERSION-linux-gtk-x86.tar.gz or
    nxmc-VERSION-linux-gtk-x64.tar.gz, for example nxmc-5.1.0-linux-gtk-x64.tar.gz).

 2. Extract and replace old management client with the new one.

    :command:`tar zxvf nxmc-VERSION-linux-gtk-x86.tar.gz -C /DIRECTORY`

 3. Run nxmc file from extracted catalog.

Web Management Client:

  1. Download latest version of WAR file from Web Interface Binaries section 
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example
     nxmc-5.1.0.war).

  2. Replace old WAR file with the new one.

     Sometimes it's possible that new WAR file is not detected and previous
     version of WAR continues to run. In this case stop servlet container, 
     delete the WAR file. Then start servlet container and copy the war
     file to webapps directory. 


Upgrading on Red Hat, Fedora, CentOS or ScientificLinux
=======================================================

Upgrading
---------

Server
~~~~~~

  1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need source archive (named netxms-VERSION.tar.gz, for example netxms-1.2.15.tar.gz). Please note that in the following steps VERSION will be used as a substitution for an actual version number.
  2. Unpack the archive:

    :command:`$ tar zxvf netxms-5.1.0.tar.gz`

  3. Change directory to netxms-version and run configure script:

    :command:`$ cd netxms-5.1.0`

    :command:`$ sh ./configure --enable-release-build --with-server --with-mysql`

    Be sure to include all options that were used at installation time.


  4. Run make:

    :command:`$ make`

  5. Stop |product_name| server.

  6. Stop |product_name| agent.

  7. Check database for possible inconsistencies:

    :command:`$ nxdbmgr check`

    Proceed to the next step only if database checker does not report any errors!

  8. Run make install:

    :command:`$ make install`

  9. Upgrade database:

    :command:`$ nxdbmgr upgrade`

  10. Start |product_name| agent.

  11. Start |product_name| server.

Agent
~~~~~

  1. Download the latest version from http://www.netxms.org/download, if you don't
     have it. You will need source archive (named netxms-VERSION.tar.gz, for example
     netxms-5.1.0.tar.gz). Please note that in the following steps VERSION will be
     used as a substitution for an actual version number.

  2. Unpack the archive:

    :command:`tar zxvf netxms-5.1.0.tar.gz`

  3. Change directory to netxms-version and run configure script:

    :command:`cd netxms-5.1.0`

    :command:`sh ./configure --enable-release-build --with-agent`

    Be sure to include all options that were used at installation time.

  4. Run make and make install:

    :command:`make`

  5. Stop |product_name| agent.

  6. Run make install:

    :command:`make install`

  7. Run agent:

    :command:`$ /usr/local/bin/nxagentd -d`

Management Client
~~~~~~~~~~~~~~~~~

Desktop Management Client:

 1. Download the latest version from http://www.netxms.org/download. You will need
    Linux installer(named nxmc-VERSION-linux-gtk-x86.tar.gz or
    nxmc-VERSION-linux-gtk-x64.tar.gz, for example nxmc-5.1.0-linux-gtk-x64.tar.gz).

 2. Extract and replace old management client with the new one.

    :command:`tar zxvf nxmc-VERSION-linux-gtk-x86.tar.gz -C /DIRECTORY`

 3. Run nxmc file from extracted catalog.

Web Management Client:

  1. Download latest version of WAR file from Web Interface Binaries section
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example
     nxmc-5.1.0.war).

  2. Replace old WAR file with the new one.

     Sometimes it's possible that new WAR file is not detected and previous
     version of WAR continues to run. In this case stop servlet container, 
     delete the WAR file. Then start servlet container and copy the war
     file to webapps directory. 


Upgrading on Windows
====================

Upgrade
-------

Server
~~~~~~

1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need Windows installer (named netxms-VERSION.exe, for example netxms-5.1.0.exe).

2. Stop |product_name| server.

3. Check database for possible inconsistencies:

.. code-block:: cfg

  C:\NetXMS\bin> nxdbmgr check

Proceed to the next step only if database checker does not report any errors!

4. Run |product_name| installer and follow the prompts. Normally, you will not need to change any settings on installation wizard windows. Alternatively, you can run the installer with /SILENT option to disable any prompts:

.. code-block:: cfg

  C:\Download> netxms-5.1.0.exe /SILENT

5. Check whether |product_name| Server service is running again. If it's not, most likely you have to upgrade your database to newer version. To upgrade database, use nxdbmgr utility:

.. code-block:: cfg

  C:\NetXMS\bin> nxdbmgr upgrade

6. Start |product_name| server, if it is not already started.

Agent
~~~~~

We highly recommend using centralized agent upgrade feature for agent upgrades.
However, if you decide to upgrade agent manually, it can be done in just a few steps:

  1. Download the latest version from http://www.netxms.org/download, if you don't
     have it. You will need Windows Agent installer (named nxagent-VERSION.exe or
     nxagent-VERSION-x64.exe, for example nxagent-5.1.0.exe).

  2. Run |product_name| agent installer and follow the prompts. Normally, you will not need
     to change any settings on installation wizard dialog windows. Alternatively, you
     can run installer with /SILENT option to disable any prompts:

      :command:`C:\Download> nxagent-5.1.0.exe /SILENT`

Management Client
~~~~~~~~~~~~~~~~~

Desktop Management Client:

 1. Download the latest version from http://www.netxms.org/download. You will need
    Windows installer(named nxmc-VERSION-win32-x86.zip or
    nxmc-VERSION-win32-x64.zip, for example nxmc-5.1.0-win32-x64.zip).

 2. Replace old old folder with content of the zip.

 3. Run nxmc.exe file from extracted catalog.

Web Management Client:

  1. Download latest version of WAR file from Web Interface Binaries section
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example
     nxmc-5.1.0.war).

  2. Replace old WAR file with the new one. Default path: ``INSTALLATION_DIR\\webapps``.

     Sometimes it's possible that new WAR file is not detected and previous
     version of WAR continues to run. In this case stop servlet container, 
     delete the WAR file. Then start servlet container and copy the war
     file to webapps directory. 


Generic upgrade using source tarball
====================================

Server
------

  1. Download the latest version from http://www.netxms.org/download, if you don't have it. You will need source archive (named netxms-VERSION.tar.gz, for example netxms-5.1.0.tar.gz). Please note that in the following steps VERSION will be used as a substitution for an actual version number.
  2. Unpack the archive:

    :command:`$ tar zxvf netxms-5.1.0.tar.gz`

  3. Change directory to netxms-version and run configure script:

    :command:`$ cd netxms-5.1.0`

    :command:`$ sh ./configure --enable-release-build --with-server --with-mysql`

    Be sure to include all options that were used at installation time.


  4. Run make:

    :command:`$ make`

  5. Stop |product_name| server.

  6. Stop |product_name| agent.

  7. Check database for possible inconsistencies:

    :command:`$ nxdbmgr check`

    Proceed to the next step only if database checker does not report any errors!

  8. Run make install:

    :command:`$ make install`

  9. Upgrade database:

    :command:`$ nxdbmgr upgrade`

  10. Start |product_name| agent.

  11. Start |product_name| server.

Agent
-----

  1. Download the latest version from http://www.netxms.org/download, if you don't
     have it. You will need source archive (named netxms-VERSION.tar.gz, for example
     netxms-5.1.0.tar.gz). Please note that in the following steps VERSION will be
     used as a substitution for an actual version number.

  2. Unpack the archive:

    :command:`tar zxvf netxms-5.1.0.tar.gz`

  3. Change directory to netxms-version and run configure script:

    :command:`cd netxms-5.1.0`

    :command:`sh ./configure --enable-release-build --with-agent`

    Be sure to include all options that were used at installation time.

  4. Run make and make install:

    :command:`make`

  5. Stop |product_name| agent.

  6. Run make install:

    :command:`make install`

  7. Run agent:

    :command:`$ /usr/local/bin/nxagentd -d`

.. _agent-remote-update:

Centralized agent upgrade
=========================

You can use  :ref:`package_mngr` functionality to perform centralized upgrade of
|product_name| agents. 
