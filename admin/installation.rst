.. _installation:

############
Installation
############

Major changes between releases
==============================

5.0
---

Abort and other runtime errors in the script DCI will set DCI to an error state. (Before version 5.0, DCI changed its state to unsupported.)
Importing the dashboard configuration exported from the previous version of NetXMS will not upgrade the script syntax to the 5.0 format.

4.4
---
Minimal JRE (Java Runtime Environment) version for management client is Java-17. 


4.2
---

NXSL functions 'AgentExecuteAction' and 'AgentExecuteActionWithOutput' renamed to 'AgentExecuteCommand' and 
'AgentExecuteCommandWithOutput'.

4.1
---

CreateDCI NXSL method changed. In new version last two parameter (polling interval and retention time) should 
be set to null instead of 0 to have default value in DCI configuration. 

NXSL decimal numbers written with leading zeros will NOT be interpreted as octal. 

4.0
---

Incompatible attributes in NXSL DCI class:
instance now refers to instance value (as in {instance} macro), not instance name as before.
Instance name can be accessed via attribute "instanceName".

Several WEB API endpoints were renamed, e.g. *API_HOME*/summaryTable/adHoc became *API_HOME*/summary-table/ad-hoc.

3.8
---
Minimal JRE (Java Runtime Environment) version for management client is Java-11. 

3.7
---
Introduced boolean type in NXSL. Comparisons like "func() == 1", where 'func' is a function that returns boolean type, will 
always result as false as boolean value 'true' is not equal to 1. Might require fixes in some NXSL scripts. 

Regexp matching operation in NXSL returns array with capture groups or false as a result.

Clusters now have configuration poll. If you have configuration poll hook script that is referring to ``$node`` object, this will 
produce error message in server log each time a configuration poll runs on a cluster. Replace ``$node`` with ``$object`` or
use condition ``if (classof($object) == "Node")`` or  ``if ($node != null)`` prior to accessing attributes or methods of ``$node``. 

3.6
---
In this version "Certificate manager" was removed from server. All CA certificates configuration should be manually moved 
to "TrustedCertificate" configuration parameter in server configuration file. 

3.5
---
External Metrics (ExternalMetric, etc...) expect UTF-8 encoding on Windows. Might need to adjust scripts called
by external metrics if non-ASCII characters are returned. 

3.1
---
Regexp matching operation in NXSL returns array with capture groups or NULL as result. NXSL objects and arrays in logical 
expressions are evaluated to TRUE. Might be require some NXSL script adjustments. 

3.0
---
Notification channels introduced as new functionality. SMS configuration automatically moved from server configuration to 
notification channel depending on old driver with one of next names: AnySMS, DBTable, Dummy, GSM, Kannel, MyMobile, Nexmo, 
NXAgent, Portech, Slack, SMSEagle, Text2Reach, WebSMS. No manual actions required. 

Flags and dynamic flags moved to NetObject class. Separated node flags set by user and capability flags set by system to 
flags and capabilities. Numeric values for flags, capabilities and dynamic flags were changed. Will affect only NXSL scripts 
that checked those flags directly. 

32 bit version of management client is not available any more. 

Agent always requires encryption unless RequireEncryption parameter explicitly set to off. Might be required to manually add 
"RequireEncryption" configuration parameter where required to disable encryption. 

Agent policies were merged with templates. Each policy was converted to template. No changes required. 

Planing
=======

Operating system
----------------

Both |product_name| server and agent works fine on most operating systems, including Windows, Linux, and commercial UNIXes.
However, we test and officially support only some of them.

Supported platforms for |product_name| server and agent:

   * Debian 10 (Buster), 11 (Bullseye), 12 (Bookworm)
   * Ubuntu 18.04 LTS (Bionic), 20.04 LTS (Focal Fossa), 22.04 LTS (Jammy Jellyfish)
   * Linux Mint 19.3 (Tricia), 20.3 (Una), 21.2 (Victoria)
   * Linux Mint Debian Edition 4
   * Devuan ASCII
   * Red Hat Enterprise Linux 8
   * CentOS 8
   * Windows 11, Windows 10, Windows Server 2016, 2019, 2022
   * FreeBSD 12
   * ArchLinux (Latest)
   * AlpineLinux 3.8+
   * Raspbian Buster


Support for the following platforms provided only to customers with active support contract:

   * Debian 8 (Jessie)
   * Ubuntu 16.04 LTS (Xenial)
   * Devuan Jessie
   * Red Hat Enterprise Linux 6, 7
   * CentOS 6, CentOS 7
   * FreeBSD 11, FreeBSD 11.3
   * Windows 7, Windows 8.1, Windows Server 2008 R2, 2012, 2012 R2
   * AIX 6.1, AIX 7.x
   * SUSE Linux Enterprise Server 11, 12, 15
   * Solaris 11 (agent only)
   * HP-UX 11.31 (agent only)


Server hardware
---------------

Minimal requirements: Core 2 duo 1GHz, 1024MB RAM, 1GB disk space.


Database
--------

.. _supported-db-list:

Database engines supported by |product_name| server:

   * PostgreSQL 9.5, 9.6, 10, 11, 12, 13, 14
   * PostgreSQL with TimescaleDB 11, 12, 13, 14
   * MySQL 5.6, 5.7, 8.0
   * MariaDB 10.1, 10.2, 10.3, 10.4
   * Oracle 12c, 18c, 19c
   * Microsoft SQL Server 2012, 2014, 2016, 2017
   * SQLite (only for test purposes)

Postgres database tuning might be required depending on database size. 
Increase of ``shared_buffers`` might be needed, rough recommendation is 25% of available RAM. 
Increase of ``max_locks_per_transaction`` is needed if using TimescaleDB, rough recommendation is 512. 

Database size and load is very hard to predict, because it is dependent on a number of
monitored nodes and collected metrics. If you plan to install database engine on
the same machine as |product_name| server, increase your hardware requirements accordingly.

Link to Excel file that allows roughly estimate the size that will be required for
database: http://git.netxms.org/public/netxms.git/blob/HEAD:/doc/misc/database_sizing.xlsx


Java
----

Java Runtime Environment (JRE) is needed for Desktop Management Client (nxmc) and for Web Management Client. 
Supported Java version are 11 and 15. 

Since version 3.8 Desktop Management Client with bundled JRE is provided for Windows. 


Agent
-----

Agent resource usage is negligible and can be ignored.


Installing from DEB repository
==============================

We host public APT repository at http://packages.netxms.org/ for most deb-based distributions (Debian, Ubuntu, Mint, Raspbian, etc.).
Packages are signed, and you'll need to install additional encryption key for signature verification.

Supported URLs (*CODENAME* should be replaced with output of `lsb_release -sc`):

  * Debian, LMDE - "deb http://packages.netxms.org/debian CODENAME main"
  * Ubuntu, Mint - "deb http://packages.netxms.org/ubuntu CODENAME main"
  * Raspbian - "deb http://packages.netxms.org/raspbian CODENAME main"


Add APT repository
------------------

There are two options to add APT repository: by hand or using netxms-release
package. Use of the release package is strongly encouraged because it allow
easy change in repository configuration and encryption keys updated in the feature.


Using netxms-release package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install netxms-release-latest.deb package, which contain source list file of the repository as well as signing key.

.. code-block:: sh

  wget http://packages.netxms.org/netxms-release-latest.deb
  sudo dpkg -i netxms-release-latest.deb
  sudo apt-get update


Manually
~~~~~~~~

Add the repository to your sources.list:

.. code-block:: sh

  echo "deb http://packages.netxms.org/$(lsb_release -si | tr A-Z a-z) $(lsb_release -sc | tr A-Z a-z) main" > /etc/apt/sources.list.d/netxms.list
  wget -q -O - http://packages.netxms.org/netxms.gpg | sudo apt-key add -
  sudo apt-get update


Installing packages
-------------------

Server
~~~~~~

Server require two components to function - server itself (package "netxms-server") and at least one database abstraction layer driver 
(multiple can be installed at the same time, e.g. for migration purposes). These database drivers are also used by agent for database 
monitoring (performing queries to databases). 

Provided driver packages:

  * netxms-dbdrv-pgsql - PostgreSQL driver
  * netxms-dbdrv-mariadb - Mariadb driver
  * netxms-dbdrv-mysql - MySQL driver (not built for Ubuntu 20 / Mint 20)
  * netxms-dbdrv-odbc - unixODBC driver (can be used with DB/2 and Microsoft SQL)
  * netxms-dbdrv-oracle - Oracle driver

#. Instal required packages (adjust command to match your environment):

   .. code-block:: sh

     apt-get install netxms-server netxms-dbdrv-pgsql

#. Create user and database (:ref:`examples <db_creation>`).

#. Modify server configuration file ("/etc/netxmsd.conf" to match your environment.

#. Load database schema and default configuration:

   .. code-block:: sh

     nxdbmgr init

#. Start server:

   .. code-block:: sh

     systemctl start netxmsd

#. Enable automatic startup of server:

   .. code-block:: sh

     systemctl enable netxmsd

#. If database engine is running on the same system, add ordering dependency for
   database into netxmsd systemd unit override file. This will ensure database
   shutdown only after netxmsd process completion on system shutdown/restart. To
   add the dependency e.g. for Postgres database, run:

   .. code-block:: sh

     systemctl edit netxmsd
   
   and add the following lines:

   .. code-block:: sh

     [Unit]
     After=network.target postgresql.service

   After editing run ``systemctl daemon-reload`` to reload systemd
   configuration. 

.. note::

  Default credentials - user "admin" with password "netxms".


Agent
~~~~~

Install core agent package ("netxms-agent") and optional subagent packages, if required:

.. code-block:: sh

  apt-get install netxms-agent

Start agent

.. code-block:: sh

  systemctl start nxagentd

Enable automatic startup of agent

.. code-block:: sh

  systemctl enable nxagentd


Management Client
~~~~~~~~~~~~~~~~~

Desktop Management Client
^^^^^^^^^^^^^^^^^^^^^^^^^

Due to limitation of Eclipse platform used to build the Management Client, only x64 build is provided.

 1. Make sure you have 64-bit Java version 17 installed you your system. 
 
 2. Download the latest version from http://www.netxms.org/download. You will need
    Linux installer (named nxmc-VERSION-linux-gtk-x64.tar.gz, for example
    nxmc-4.4.3-linux-gtk-x64.tar.gz).
    
 3. Expand package to your preferred directory using command:

    :command:`tar zxvf nxmc-VERSION-linux-gtk-x86.tar.gz -C /DESTINATION_DIRECTORY`

 4. Run nxmc file from "/DESTINATION_DIRECTORY".


Desktop management client produces log file :file:`.nxmc/data/.metadata/.log` in
home folder of currently logged user. Inspect this log file if you encounter
errors when running the client. 


Web Management Client
^^^^^^^^^^^^^^^^^^^^^

|product_name| web interface is java based and should be deployed into servlet container to
run. Minimal supported versions: Jetty 10, Tomcat 9. Supported Java version is 17. 

  1. Install one of servlet containers that support servlet-api version 4.

  2. Download latest version of WAR file from Web Interface Binaries section
     http://www.netxms.org/download/ (named nxmc-VERSION.war, for example
     nxmc-4.4.3.war).

  3. Copy nxmc.war to webapps directory, in a few seconds it will be autodeployed and
     available at http://SERVER_IP:SERVER_PORT/nxmc/

     Tomcat default folder:  /var/lib/tomcat9/webapps

     Jetty default folder: $JETTY_HOME/webapps/


Web management client produces log file. For Tomcat it's located at 
:file:`/var/lib/tomcat9/work/Catalina/localhost/nxmc/eclipse/workspace/.metadata/.log.` 
Inspect this log file if you encounter errors when running the web client. 


Installing from RPM repository
==============================

We provide RPM packages for RHEL and Fedora, both amd64 and aarch64.
If you need build for another system, please contact us for support or check this section: :ref:`Installing from source <install_from_sources>`.

RHEL repository is at https://packages.netxms.org/epel/.

Fedora repository is at https://packages.netxms.org/fedora/.

Complete repository file and signing key is available in each corresponding root.

Add repository
------------------------

DNF provide simple way to add repository:

.. code-block:: sh

   # RHEL and compatible
   dnf config-manager --add-repo https://packages.netxms.org/epel/netxms.repo
   # Fedora
   dnf config-manager --add-repo https://packages.netxms.org/fedora/netxms.repo

Once added, you can install any package with ``dnf install`` (e.g. ``dnf install netxms-agent``).


Installing on Windows
=====================

Server
------

  1. Download the latest version from http://www.netxms.org/download.
     You will need Windows installer (named netxms-VERSION-x64.exe, e.g.
     netxms-server-3.4.178-x64.exe). Please note that in
     following steps VERSION will be used as a substitution for an actual version
     number.
  2. Run the installer package on your server machine. Installation wizard will be
     shown. Follow the prompts until the Select Components window opens.
  3. On the Select Components window, select |product_name| Server option and an appropriate
     database client library. You do not have to install database client library
     from |product_name| package, if it is already installed on the machine (however, it might 
     be required to add folder where the client library is installed to system path). 

    .. figure:: _images/win_netxms_setup_components.png

  4. For a typical installation keep default settings on Select Additional Tasks window.
     :guilabel:`Set hardened file system permissions` makes installation folder
     accessible only to members of Administrators group and SYSTEM user.

    .. figure:: _images/win_netxms_setup_additional_tasks.png

  4. Follow the prompts until Ready to Install window opens.

  5. On Ready to Install window, check whether everything is correct, then press the Install button.

  6. After copying files, Server Configuration Wizard will open:

    .. figure:: _images/win_server_config_step1.png

    Press the Next button to start |product_name| server configuration.

  7. Database selection window will open:

    .. figure:: _images/win_server_config_step2.png

  * Select the desired database engine and driver. For most databases, you will have
    two drivers available – native and ODBC. Please note that if you select ODBC, you
    will have to manually configure ODBC source.
  * Enter the name of database server or ODBC source.
  * In DBA login name and DBA password fields, enter database administrator’s login
    name and password. You have to fill these fields only if you have chosen
    :guilabel:`Create new database option`.
  * Enter the desired database name, database user name and password. If you are not
    using ODBC, the wizard will create database and a user for you. If ODBC is used,
    database and user should be created beforehand.

    **MySQL note**
    Bundled MySQL database drive does not support caching_sha2_password authentication 
    which is default for MySQL starting from version 8. Either select 
    Legacy Authentication Method when installing MySQL, or use database driver 
    installed along with MySQL. 
    Database driver gets installed when installing MySQL with Server-only option, however these
    two folders should be included into system path: :file:`C:\\Program Files\\MySQL\\MySQL Server 8.0\\lib` 
    :file:`C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin`. 


    **Microsoft SQL note**:

    If you wish to use Windows authentication for database connectivity, use * (asterisk)
    as a login name and leave the password field blank. If you specify asterisk as DBA
    login, user with which you are logged in to Windows should have administrative rights
    to the database server. If you use asterisk as DB login, you should run |product_name| Server
    service as a user with appropriate rights to the database.

    **Oracle note**:

    We recommend to use native database driver (oracle.ddr).

  9. On the next window, enter address of your SMTP server. |product_name| will use it to send
     notification e-mails.

  10. Then next window will prompt you for logging method. Either check Event Log or
      select file, and press the Next button.

  11. Windows service configuration window will appear:

    .. figure:: _images/win_server_config_step6.png

    In most situations, you can run |product_name| server under Local System account. You may
    need to run it under specific account if you are using Microsoft SQL database and
    Windows authentication, or for security reasons.

  12. Windows service dependency window will appear:

    .. figure:: _images/win_server_config_step7.png

    If you have database engine running on same server, you can find it in service
    list and mark, so |product_name| server's service will depend on database service and
    service startup order will be correct.

  13. Follow the prompts until server configuration will be complete. After successful
  server configuration, installation will be finished, and you will have |product_name| server
  up and running.


Server default credentials:

Login: admin

Password: netxms


Agent
-----

  1. Download the latest version from http://www.netxms.org/download, if you don't
     have it. You will need Windows Agent installer (named nxagent-VERSION.exe or
     nxagent-VERSION-x64.exe, for example nxagent-3.4.178.exe).

  2. Run the installer package on target server. Installation wizard will be shown.
     Follow the prompts until the |product_name| Server window opens:

     .. figure:: _images/win_agent_config.png


     Enter IP address or host name of your |product_name| server. You can specify multiple
     management servers, separating them by commas. Press the Next button to continue.


  3. Subagent selection window will open:

     .. figure:: _images/win_agent_subagents.png

     In this window, you can select which subagents you wish to load. Each subagent
     extends agent's functionality, e.g.:

.. list-table::
   :header-rows: 1
   :widths: 50 200

   * - Subagent
     - Description
   * - filemgr.nsm
     - Provides access to specified folders on monitored host from |product_name| Management Client File Manager.
       Is also being used for distributing Agent Policy configuration files (see :ref:`agent-policies-label`.)
   * - logwatch
     - Allows monitoring log files and Windows Event Log and sending matched events to |product_name| server.
   * - ping.nsm
     - Adds possibility to send ICMP pings from monitored host. Ping round-trip times can be collected by management server.
   * - netsvc.nsm, portcheck.nsm
     - Adds possibility to check network services (like FTP or HTTP) from monitored host.
   * - winperf.nsm
     - Provides access to Windows performance counters. This subagent is required if you need to collect CPU utilization from monitored host.
   * - wmi.nsm
     - Provides access to WMI data.
   * - ups.nsm
     - Adds support for UPS monitoring. UPS can be attached to host via serial cable or USB.


For more information about subagents, please refer to :ref:`subagent_list`.


  4. Follow the prompts to complete the installation.


Management Client
-----------------

Desktop Management Client:

 1. Download the latest version from http://www.netxms.org/download. 
    Since version 3.8 there are three options - 
    archive (e.g. nxmc-3.8.226-win32-x64.zip), archive with bundled JRE (nxmc-3.8.226-win32-x64-bundled-jre.zip)
    and installer, which also has JRE bundled (e.g. netxms-client-3.8.166-x64.exe). 
    If using archive without JRE, make sure you have JRE version 11 or 15 installed. 
    Due to limitation of Eclipse platform used to build the Management Client, only x64 build is currently provided. 

 2. If using archive version, extract zip in preferred directory. If using installer, launch it and follow the instructions. 

 3. Run nxmc file from extracted catalog (or launch from Windows Start Menu, if you used the installer). 

Web Management Client:

Windows have two options: one is to manually install .war file into servlet container and
the second one is to use netxms-webui-VERSION-x64.exe installer. Installer will
install Jetty and copy .war file into required folder. Below will be described
installation via the installer:

  1. Download the latest version from http://www.netxms.org/download. You will need
     Windows installer netxms-webui-VERSION-x64.exe (e.g.: netxms-webui-4.3.178-x64.exe).
     Due to limitation of Eclipse platform used to build the Management Client,
     only x64 build is currently provided.

  2. Run the installer package on your server machine. Installation wizard will be
     shown. Follow the prompts. Installer allows to change installation path and port.

  3. After installation procedure is finished check that WEB GUI is available at
     http://SERVER_IP:SERVER_PORT/nxmc/


Unattended installation of |product_name| Agent
-----------------------------------------------

Windows Agent installer (named nxagent-VERSION.exe, for example nxagent-3.4.178.exe),
has various command line options for unattended installation. Installation will ignore
any configuration file options (/CONFIGENTRY, /NOSUBAGENT, /SERVER, /SUBAGENT, etc) if config
file already exists or if /CENTRALCONFIG option is used. However, it's possible to 
delete and recreate the configuration file with /FORCECREATECONFIG command line option. 


The options are following:

.. list-table::
   :header-rows: 1
   :widths: 12 30

   * - Option
     - Description
   * - /CENTRALCONFIG
     - Enable read configuration from server on startup. See :ref:`agent_configuration_files_on_server` 
       for more information. 
   * - /CONFIGENTRY=value
     - It can be used to add any parameter to configuration file during initial install. 
       You can specify it multiple times to add multiple lines. Section names can be added as well.
   * - /CONFIGINCLUDEDIR=path
     - Set folder containing additional configuration files 
       (will be set in configuration file as ``ConfigIncludeDir``).
   * - /DIR=path
     - Set installation directory (default is ``C:\NetXMS``).
   * - /FILESTORE=path
     - Sets directory to be used for storing files uploaded by management server(s)
       (will be set in configuration file as ``FileStore``).
   * - /FORCECREATECONFIG
     - Delete existing agent configuration file and recreate it. However, settings stored by installer
       in Windows registry will be used, if not explicitly specified by command line parameters. See ``/IGNOREPREVIOUSDATA``.        
   * - /IGNOREPREVIOUSDATA
     - Ignore any settings from previous install that are not explicitly specified in current run. This is 
       related to settings that can be changed when installer is run in GUI mode, e.g. list of selected sub-agents. 
       These settings are stored in Windows registry. 
   * - /LOCALCONFIG
     - Use local configuration file (it is the default).
   * - /LOG
     - Causes Setup to create a log file in the user's TEMP directory detailing file 
       installation and [Run] actions taken during the installation process.
   * - /LOG=filename
     - Same as /LOG, except it allows to specify a fixed path/filename to use for the log file. 
       If a file with the specified name already exists it will be overwritten. 
       If the file cannot be created, Setup will abort with an error message.
   * - /LOGFILE=filename
     - Set agent log file (will be set in configuration file as ``LogFile``).
   * - /MERGETASKS=”tasknames”
     - Comma-separated list of tasks for installation. If a task is specified with ! character
       prior to it's name, it will be deselected. Possible values are ``fspermissions`` - set hardened file system permissions, 
       ``sessionagent`` - Install session agent, ``useragent`` - Install user support application. 
       e.g. ``/MERGETASKS="!fspermissions,useragent"``
   * - /NOSUBAGENT=name
     - Disable subagent name
   * - /NOTUNNEL
     - Disable tunnel operation (it is the default)
   * - /REINSTALLSERVICE
     - Reinstalls Windows service
   * - /SERVER=IP
     - Set server IP address or host name (will be set in configuration file as ``MasterServers``).
   * - /SILENT
     - Don't show installation wizard, only a progress bar
   * - /SUBAGENT=name
     - Add sub-agent loading directive to configuration file. You can specify this
       parameter multiple times to add more than one sub-agent. List of possible subagents: :ref:`subagent_list`.
   * - /SUPPRESSMSGBOXES
     - Don't ask user anything. Only has an effect when combined with ``/SILENT`` and ``/VERYSILENT``.
   * - /TUNNEL
     - Enable tunnel operation to IP address specified with ``/SERVER=``. 
   * - /VERYSILENT
     - Don't show anything

Example:

:command:`nxagent-3.4.178.exe /VERYSILENT /SUPPRESSMSGBOXES /SERVER=10.0.0.1 /SUBAGENT=UPS /SUBAGENT=FILEMGR /CONFIGENTRY=ZoneUIN=15 /CONFIGENTRY=[FILEMGR] /CONFIGENTRY=RootFolder=C:\\`

This command will add 3 lines at the end of generated config file:

.. code-block:: cfg

    ZoneUIN=15
    [FILEMGR]
    RootFolder=C:\


Unattended uninstallation of |product_name| Agent
-------------------------------------------------

Uninstaller application is named unins???.exe and located in agent folder (``C:\NetXMS`` by default). 
The following options are supported:

.. list-table::
   :header-rows: 1
   :widths: 12 30

   * - Option
     - Description
   * - /SILENT
     - Don't show uninstallation wizard, only a progress bar
   * - /VERYSILENT
     - Don't show anything
   * - /LOG
     - Causes to create a log file in the user's TEMP directory.
   * - /LOG=filename
     - Same as /LOG, except it allows to specify a fixed path/filename to use for the log file. 
   * - /SUPPRESSMSGBOXES
     - Don't ask user anything. Only has an effect when combined with ``/SILENT`` and ``/VERYSILENT``.
   * - /NORESTART
     - Instructs the uninstaller not to reboot even if it's necessary.

Example:

:command:`unins000.exe /SUPPRESSMSGBOXES /VERYSILENT /NORESTART`


Install on Android
==================

Client
------

To install Android client download netxms-console-VERSION.apk (example:
netxms-console-3.4.178.apk) file from http://www.netxms.org/download page. Check that
installation of applications from unknown sources is allowed in security settings of
your phone. Run this installer on required device.

After agent is installed go to settings and in main menu, connection part set all
required connection credentials: server address, port, user name, password.

.. note::
  User that is used for connection should have :guilabel:`Login as mobile device`
  user right.

Agent
-----

To install Android agent download netxms-mobile-agent-VERSION.apk (example:
netxms-mobile-agent-3.4.178.apk) file from http://www.netxms.org/download page.
Check that installation of applications from unknown sources is allowed in security
settings of your phone. Run this installer on required device.

After agent is installed go to settings and activate agent. After agent activation
several parameters should be set: server address, port, user name, password. They can be
found in under main menu, parameters section.

.. note::
  User that is used for connection should have :guilabel:`Login as mobile device`
  user right.

  Mobile device should be manually added to server. Find more information see:
  :ref:`monitoring-mobile-device`.


.. _install_from_sources:


Installing from sources
=======================

Server
------

  #. Download source archive (netxms-VERSION.tar.gz) from http://www.netxms.org/download/. *VERSION* is used in names instead of an actual version number.
  #. Unpack the archive:

        :command:`tar zxvf netxms-VERSION.tar.gz`

  #. Since version 3.8 reporting server is being built along with the sources. This requires maven to be installed on the system. You need Oracle and MS SQL JDBC drivers in your local maven repository. 

        Oracle JDBC driver library can be obtained here: https://download.oracle.com/otn-pub/otn_software/jdbc/199/ojdbc8.jar

        Microsoft SQL JDBC driver library can be obtaine here: https://www.microsoft.com/en-us/download/details.aspx?id=54671 
        You will need sqljdbc_4.2/enu/jre8/sqljdbc42.jar file from this archive. 

        To install these libraries:
        :command:`mvn install:install-file -DgroupId=com.microsoft.sqlserver -DartifactId=sqljdbc4 -Dversion=4.2 -Dpackaging=jar -Dfile=sqljdbc42.jar`
        :command:`mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc8 -Dversion=12.2.0.1 -Dpackaging=jar -Dfile=ojdbc8.jar`

  #. Change directory to netxms-VERSION and run configure script:

        :command:`cd netxms-VERSION`

        :command:`./configure --enable-release-build --with-server --with-pgsql --with-agent`

        Most commonly used options (check full list with :command:`./configure --help`):

        .. list-table::
           :header-rows: 1
           :widths: 30 70

           * - Name
             - Description
           * - ``--prefix=DIRECTORY``
             - Installation prefix, all files go to the specified directory (e.g. ``--prefix=/opt/netxms``)
           * - ``--with-server``
             - Build server binaries. You will need to select at least one DB driver as well
           * - ``--with-agent``
             - Build monitoring agent. It is strongly recommended to install agent on a server box
           * - ``--with-pgsql``
             - Build PostgresSQL DB Driver (if you plan to use PostgreSQL as backend database)
           * - ``--with-mysql``
             - Build MySQL DB Driver (if you plan to use MySQL as backend database)
           * - ``--with-odbc``
             - Build ODBC DB driver (if you plan to connect to your backend database via unixODBC)
           * - ``--with-sqlite``
             - Build SQLite DB driver (if you plan to use embedded SQLite database as backend database)

  #. Run build binaries and install them into /usr/local (unless changed with configure flag --prefix)

        :command:`make`

        :command:`make install`

  #. Copy sample config file:

        :command:`cp contrib/netxmsd.conf-dist /usr/local/etc/netxmsd.conf`

        By default, server load configuration file PREFIX/etc/netxmsd.conf (where PREFIX is installation prefix set by configure), unless different file is specified with command line switch "-c".

  #. Create database user and adjust configuration file (netxmsd.conf) accordingly. Database creation examples can be found :ref:`there <db_creation>`.

  #. Further adjust server configuration file if required.

     Detailed information about each configuration parameter can be found in section :ref:`server_configuration_file`.

  #. Create required tables and load initial configuration using nxdbmgr utility:

     .. code-block:: sh

       /usr/local/bin/nxdbmgr init

  #. Run server:

     .. code-block:: sh

       /usr/local/bin/netxmsd -d


Agent
-----

  #. Download source archive (netxms-VERSION.tar.gz) from http://www.netxms.org/download/. *VERSION* is used in names instead of an actual version number.
  #. Unpack the archive:

        :command:`tar zxvf netxms-VERSION.tar.gz`

  #. Change directory to netxms-VERSION and run configure script:

        :command:`cd netxms-VERSION`

        :command:`./configure --enable-release-build --with-agent`

        Most commonly used options (check full list with :command:`./configure --list`):

        .. list-table::
           :header-rows: 1
           :widths: 30 70

           * - Name
             - Description
           * - ``--prefix=DIRECTORY``
             - Installation prefix, all files go to the specified directory
           * - ``--with-agent``
             - Build monitoring agent. It is strongly recommended to install agent on a server box

  #. Run build binaries and install them into /usr/local (unless changed with configure flag ``--prefix``)

        :command:`make`

        :command:`make install`

  #. Copy sample config file:

        :command:`cp contrib/nxagentd.conf-dist /usr/local/etc/nxagentd.conf`

        By default, agent load configuration file PREFIX/etc/netxmsd.conf (where PREFIX is installation prefix set by configure), unless different file is specified with command line switch "-c".

  #. Adjust agent configuration file if required.

     Detailed information about each configuration parameter can be found in section :ref:`agent_configuration_file`.

     Minimal required configuration:

     .. code-block:: cfg

       MasterServers = 172.16.1.1 # server's IP - agent will drop connections unless address is whitelisted here
       LogFile = /var/log/nxagentd

  #. Run agent:

     .. code-block:: sh

       /usr/local/bin/nxagentd -d


Customizing the compilation process
===================================


Adding additional compiler or linker flags
------------------------------------------

(e.g. fixing atomics)


WebUI additional configuration
==============================

Installing web interface on remote system
-----------------------------------------

There are few settings available for configuration in WebUI.

  * autoLoginOnReload - autologin on page reload in browser (default: true)
  * enableCompression - enable protocol compression between Web UI and server process (default: true)
  * loginFormImage - path to custom login image
  * loginFormImageBackground - colour of background around custom login image
  * loginFormImageMargins - margins in px around custom login image (default: 10)
  * server - server DNS name or IP (default: 127.0.0.1)

There are multiple ways to set connection configuration from WebUI to NetXMS server.
Configuration is check in next order:

  1. Using JNDI. Environment should be set like nxmc/NAME for example: nxmc/server

  2. nxmc.properties properties file in class path of your application server. Should be created in ini format: NAME=VALUE. For example:

    .. code-block:: cfg

      server = 127.0.0.1

    Default locations: 

    **Jetty**


    **Tomcat**

    Debian and Ubuntu default is /usr/share/tomcat9/lib. Other versions and Linux distribution
    may have different location.

    **Oracle Weblogic**

    $WEBLOGIC_HOME/user_projects/domains/YOURDOMAIN

  3. jvm parameter in format -Dnxmc.NAME=VALUE.  For example: -Dnxmc.server=127.0.0.1

  4. Environment variable NXMC_NAME=VALUE. For example NXMC_server=127.0.0.1

  5. If non of above configuration exists, Web UI tries to resolve "NETXMS_SERVER" DNS name for server connection.

  6. If none of above configuration exists, Web UI uses "127.0.0.1" as a server address. 


Custom logo on login screen
---------------------------

It is possible to change default logo on login screen to custom image by setting
loginFormImage property in nxmc.properties file. Image file must be located within
application server's class path and file name must be given relative to class path
root with leading slash. For example, if custom image is in file logo.jpg located
in the same directory as nxmc.properties, correct entry will be:

.. code-block:: cfg

  loginFormImage = /logo.jpg


Default login credentials
=========================

Default login is "admin" with password "netxms". On first login, user will be requested to change it immediately.

If required, password can be reset back to default using :ref:`nxdbmgr utility <password-reset>`.

.. _db_creation:


Database creation examples
==========================

This chapter provides some database creation SQL examples.

PostgreSQL
----------

.. code-block:: sh

  createuser -P netxms
  createdb -O netxms netxms

If TimescaleDB extension is about to be used, it should be added to the newly created database:

.. code-block:: sh

  psql netxms
  CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
  \q

Configuration file example:

.. code-block:: cfg

  DBDriver = pgsql.ddr
  DBServer = localhost
  DBName = netxms
  DBLogin = netxms
  DBPassword = PaSsWd

MySQL
-----

.. code-block:: sh

  echo "CREATE DATABASE netxms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" | mysql -u root -p
  echo "CREATE USER 'netxms'@'localhost' IDENTIFIED BY 'PaSsWd';" | mysql -u root -p
  echo "GRANT ALL on netxms.* to 'netxms'@'localhost';" | mysql -u root -p


Configuration file example:

.. code-block:: cfg

  DBDriver = mysql.ddr
  DBServer = localhost
  DBName = netxms
  DBLogin = netxms
  DBPassword = PaSsWd

Oracle
------

.. code-block:: sql

  -- USER SQL
  CREATE USER netxms IDENTIFIED BY PaSwD
  DEFAULT TABLESPACE USERS
  TEMPORARY TABLESPACE TEMP;
  -- QUOTAS
  ALTER USER netxms QUOTA UNLIMITED ON USERS;
  -- ROLES
  GRANT CREATE SESSION, CREATE TABLE, CREATE PROCEDURE TO netxms;

Configuration file example:

.. code-block:: cfg

  DBDriver = oracle.ddr
  DBServer = //127.0.0.1/XE # instant client compatible connection string
  DBLogin = netxms
  DBPassword = PaSsWd
