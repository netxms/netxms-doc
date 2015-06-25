.. _upgrade:

#######
Upgrade
#######


Synopsis
========


Planing
=======


Upgrading on Debian or Ubuntu
=============================


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


Upgrading on Red Hat, Fedora, CentOS or ScientificLinux
=======================================================


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


Upgrading on Windows
====================


Adding our YUM repository
-------------------------


Installing packages
-------------------


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


Management console
~~~~~~~~~~~~~~~~~~


Generic installation, upgrade and downgrade using source tarball
================================================================


Centralised agent upgrade
=========================


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
