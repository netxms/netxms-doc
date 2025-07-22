.. _installation:

############
Installation
############

Major changes between releases
==============================

5.1.4
-----

IP v4 addresses are now supported only in a.b.c.d format with decimal numbers


5.1
---

NXSL changes: node attribute 'ipAddr' is deprecated. The newly added 'ipAddress'
attribute should be used instead.


5.0
---

Aditionally loaded MIB files will not work. They should be uploaded again in the
:guilabel:`Configuration` --> :guilabel:`SNMP MIB files` configuration view.
Starting with version 5.0, the MIB compilation file extension changed to ".mib"
and the already compiled MIB file extension is now ".cmib". The default MIB file
location has changed to $HOME/share/netxms/mibs/ and user additional MIB files
should be loaded in :guilabel:`Configuration` --> :guilabel:`SNMP MIB files`.

The default format of SNMP OID changes to a format without leading dot. Potentially
this can break some scripts that use SNMP OID string comparisons.

The NXSL syntax has changed. During upgrade, existing scripts get
converted automatically . If you need to manually convert a script, this could be
done via the nxscript command line utility (``nxscript -5 script-file.nxsl``). NXSL
syntax major changes:

.. list-table::
   :header-rows: 1
   :widths: 300 100 100

   * - Description
     - Old example
     - New example
   * - String concatenation changes from '.' to '..'
     - variable = "Text first part " . "text second part";
     - variable = "Text first part " .. "text second part";
   * - Dereference changed form '->' to '.'
     - equals = $node->getInterface($5) == variable->interfaceAttribute;
     - equals = $node.getInterface($5) == variable.interfaceAttribute;
   * - Use '[]' to initialize an array instead of '%()'
     - a = %(1,2,3);
     - a = [1,2,3];
   * - Use safe dereference '?.' instead of '@'
     - customAttributeValue = test@$node;
     - customAttributeValue = $node?.test;
   * - Use 'import' keyword instead of 'use' for library import
     - use ToolBox;
     - import ToolBox;
   * - Use 'function' keyword instead of 'sub' for function definition
     - sub EnumerateNodes(obj, level)
     - function EnumerateNodes(obj, level)


Class 'TIME' is now renamed as 'DateTime'. Created Math, Base64, Crypto, Net, and IO
modules, and functions moved under them. The most used functions are left as deprecated,
but others were just renamed. The table below shows the full renamed list containing
functions that were just renamed and do not have deprecated versions:


.. list-table::
   :header-rows: 1
   :widths: 100 100 100

   * - Old name
     - New name
     - Type
   * - TIME
     - DateTime
     - class
   * - asin
     - Math::Asin
     - function
   * - acos
     - Math::Acos
     - function
   * - atan
     - Math::Atan
     - function
   * - atan2
     - Math::Atan2
     - function
   * - cosh
     - Math::Cosh
     - function
   * - exp
     - Math::Exp
     - function
   * - gethostbyaddr
     - Net::ResolveAddress
     - function
   * - gethostbyname
     - Net::ResolveHostname
     - function
   * - log
     - Math::Log
     - function
   * - log10
     - Math::Log10
     - function
   * - md5
     - Crypto::MD5
     - function
   * - md5
     - Crypto::MD5
     - function
   * - sha1
     - Crypto::SHA1
     - function
   * - sha256
     - Crypto::SHA256
     - function
   * - sinh
     - Math::Sinh
     - function
   * - tanh
     - Math::Tanh
     - function
   * - weierstrass
     - Math::Weierstrass
     - function
   * - decode
     - Base64::Decode
     - function
   * - encode
     - Base64::Encode
     - function
   * - CopyFile
     - IO::CopyFile
     - function
   * - CreateDirectory
     - IO::CreateDirectory
     - function
   * - DeleteFile
     - IO::DeleteFile
     - function
   * - FileAccess
     - IO::FileAccess
     - function
   * - OpenFile
     - IO::OpenFile
     - function
   * - RemoveDirectory
     - IO::RemoveDirectory
     - function
   * - RenameFile
     - IO::RenameFile
     - function

Abort and other runtime errors in the script DCI will set DCI to an error state.
Before version 5.0, DCI changed state to unsupported.

Importing the dashboard configuration exported from the previous version of
NetXMS will not upgrade the script syntax to the 5.0 format.


4.4
---
The minimal JRE (Java Runtime Environment) version for both web and management client is now Java 17.


4.2
---

The NXSL functions 'AgentExecuteAction' and 'AgentExecuteActionWithOutput' are renamed to 'AgentExecuteCommand' and
'AgentExecuteCommandWithOutput'.

4.1
---

The CreateDCI NXSL method changed. In the new version the last two parameters "polling interval" and "retention time" should
be set to null instead of 0 to have a default value in the DCI configuration.

NXSL decimal numbers written with leading zeros will NOT be interpreted as octal.

4.0
---

Incompatible attributes in NXSL DCI class:
instance now refers to an instance value (as in {instance} macro), not instance name as before.
The instance name can be accessed via the attribute "instanceName".

Several WEB API endpoints were renamed, e.g. *API_HOME*/summaryTable/adHoc became *API_HOME*/summary-table/ad-hoc.

3.8
---
The minimal JRE (Java Runtime Environment) version for the management client is Java 11.
A Desktop Management Client with bundled JRE is provided for Windows.

3.7
---
Introduced boolean type in NXSL. Comparisons like "func() == 1", where 'func' is a function that returns a boolean type, will
always result as false as the boolean value 'true' is not equal to 1. This might require fixes in some NXSL scripts.

Regexp matching operation in NXSL returns an array with capture groups or false as a result.

Clusters now have configuration poll. If you have a configuration poll hook script that is referring to the ``$node`` object, this will
produce an error message in the server log each time a configuration poll runs on a cluster. Replace ``$node`` with ``$object`` or
use the condition ``if (classof($object) == "Node")`` or  ``if ($node != null)`` prior to accessing attributes or methods of ``$node``.

3.6
---
In this version the "Certificate manager" was removed from server. All CA certificates configuration should be manually moved
to the "TrustedCertificate" configuration parameter in the server configuration file.

3.5
---
External Metrics (ExternalMetric, etc...) expect UTF-8 encoding on Windows. It might be needed to adjust scripts called
by external metrics if non-ASCII characters are returned.

3.1
---
Regexp matching operation in NXSL returns array with capture groups or NULL as result. NXSL objects and arrays in logical
expressions are evaluated to TRUE. This might require some NXSL script adjustments.

3.0
---
Notification channels are introduced as new functionality. SMS configuration automatically moved from server configuration to
notification channel depending on old driver with one of the next names: AnySMS, DBTable, Dummy, GSM, Kannel, MyMobile, Nexmo,
NXAgent, Portech, Slack, SMSEagle, Text2Reach, WebSMS. No manual actions are required.

Flags and dynamic flags are moved to the NetObject class. Separated node flags set by user and capability flags set by system to
flags and capabilities. Numeric values for flags, capabilities and dynamic flags were changed. This affects only NXSL scripts
that checked those flags directly.

The 32 bit version of management client is not available any more.

The Agent always requires encryption unless the RequireEncryption parameter explicitly set to off. It might be required to manually add
the "RequireEncryption" configuration parameter where required to disable encryption.

Agent policies were merged with templates. Each policy was converted to a template. No changes required.

Planning
========

Operating system
----------------

Both |product_name| server and agent work fine on most operating systems, including Windows, Linux, and commercial UNIXes.
However, we test and officially support only some of them.

Supported platforms for |product_name| server and agent:

   * Debian 10 (Buster), 11 (Bullseye), 12 (Bookworm)
   * Ubuntu 18.04 LTS (Bionic), 20.04 LTS (Focal Fossa), 22.04 LTS (Jammy Jellyfish), 24.04 (Noble)
   * Linux Mint 19.3 (Tricia), 20.3 (Una), 21.2 (Victoria)
   * Linux Mint Debian Edition 4
   * Devuan ASCII
   * Red Hat Enterprise Linux 8, 9
   * CentOS 8
   * Windows 11, Windows 10, Windows Server 2016, 2019, 2022
   * FreeBSD 12
   * ArchLinux (Latest)
   * AlpineLinux 3.8+
   * Raspbian Buster


Support for the following platforms is provided only to customers with an active support contract:

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


Linux kernel tuning
-------------------

An important requirement on large systems might be the need to tune Linux network buffer size.
Default values may not be enough if the system is sending many ICMP pings, for example.
The following kernel parameters should be changed:

* net.core.rmem_default
* net.core.wmem_default
* net.core.rmem_max
* net.core.wmem_max

In our test lab, value 1703936 seems to be working well (default was 212992).

Example:

* sudo sysctl -w net.core.rmem_default=1703936
* sudo sysctl -w net.core.wmem_default=1703936
* sudo sysctl -w net.core.rmem_max=1703936
* sudo sysctl -w net.core.wmem_max=1703936

Kernel changes will not be preserved after reboot unless sysctl commands are applied in the system
configuration file, which is typically located at /etc/sysctl.conf. Increasing these kernel values also
increases kernel memory space in use and may impact other applications.

Database
--------

.. _supported-db-list:

Database engines supported by |product_name| server:

   * PostgreSQL 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17
   * PostgreSQL with TimescaleDB 11, 12, 13, 14, 15, 16, 17
   * MySQL 5.6, 5.7, 8.0
   * MariaDB 10.1, 10.2, 10.3, 10.4
   * Oracle 12c, 18c, 19c
   * Microsoft SQL Server 2012, 2014, 2016, 2017, 2022
   * SQLite (only for test purposes)

PostgreSQL database tuning might be required depending on database size.
Increasing ``shared_buffers`` might be needed. A rough recommendation is 25% of available RAM.
Increasing ``max_locks_per_transaction`` is needed if using TimescaleDB. A rough recommendation is 512.

Database size and load is very hard to predict, because it is depending on the number of
monitored nodes and collected metrics. If you plan to install a database engine on
the same machine as |product_name| server, increase your hardware requirements accordingly.


Java
----

A Java Runtime Environment (JRE) is needed for the Desktop Management Client (nxmc) and for the Web Management Client.
The Supported Java version is 17 and higher.

Since version 3.8 the Desktop Management Client with a bundled JRE is provided for Windows.


Agent
-----

Agent resource usage is negligible and can be ignored.


Installing from DEB repository
==============================

We host a public APT repository at http://packages.netxms.org/ for most deb-based distributions (Debian, Ubuntu, Mint, Raspbian, etc.).
Packages are signed, and you'll need to install an additional encryption key for signature verification.

Supported URLs (*CODENAME* should be replaced with output of `lsb_release -sc`):

  * Debian, LMDE - "deb http://packages.netxms.org/debian CODENAME main"
  * Ubuntu, Mint - "deb http://packages.netxms.org/ubuntu CODENAME main"
  * Raspbian - "deb http://packages.netxms.org/raspbian CODENAME main"


Add APT repository
------------------

There are two options to add an APT repository: by hand or by using the netxms-release
package. Use of the release package is strongly encouraged because it allows
easy change in repository configuration and encryption keys will be updated in the future.


Using the netxms-release package
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Download and install the netxms-release-latest.deb package, which contain a source list file of the repository as well as a signing key.

.. code-block:: sh

  wget http://packages.netxms.org/netxms-release-latest.deb
  sudo dpkg -i netxms-release-latest.deb
  sudo apt-get update


Manually
~~~~~~~~

Add the repository to your sources.list:

.. code-block:: sh

  echo "deb http://packages.netxms.org/$(lsb_release -si | tr A-Z a-z) $(lsb_release -sc | tr A-Z a-z) main" > /etc/apt/sources.list.d/netxms.list
  wget -q -O - https://packages.netxms.org/netxms-keyring.gpg | gpg --dearmor -o /etc/apt/trusted.gpg.d/netxms-keyring.gpg
  sudo apt-get update


Installing packages
-------------------

Server
~~~~~~

The server requires two components to function: the server itself (package "netxms-server") and at least one database abstraction layer driver
(multiple can be installed at the same time, e.g. for migration purposes). These database drivers are also used by the agent for database
monitoring (performing queries to databases).

Provided driver packages:

  * netxms-dbdrv-pgsql - PostgreSQL driver
  * netxms-dbdrv-mariadb - Mariadb driver
  * netxms-dbdrv-mysql - MySQL driver (not built for Ubuntu 20 / Mint 20)
  * netxms-dbdrv-odbc - unixODBC driver (can be used with DB/2 and Microsoft SQL)
  * netxms-dbdrv-oracle - Oracle driver ( requires Oracle client installation )

#. Install required packages (adjust command to match your environment):

   .. code-block:: sh

     apt-get install netxms-server netxms-dbdrv-pgsql

#. Create user and database (:ref:`examples <db_creation>`).

#. Modify server configuration file ("/etc/netxmsd.conf" to match your environment.

#. Load database schema and default configuration:

   .. code-block:: sh

     nxdbmgr init

#. Start server:

   .. code-block:: sh

     systemctl start netxms-server

#. Enable automatic startup of server:

   .. code-block:: sh

     systemctl enable netxms-server

#. If the database engine is running on the same system, add ordering dependency for
   database in the netxmsd systemd unit override file. This will ensure database
   shutdown only after netxmsd process completion on system shutdown/restart. To
   add the dependency e.g. for the PostgreSQL database, run:

   .. code-block:: sh

     systemctl edit netxms-server

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

Install the core agent package ("netxms-agent") and optional subagent packages, if required:

.. code-block:: sh

  apt-get install netxms-agent

Start agent

.. code-block:: sh

  systemctl start netxms-agent

Enable automatic startup of agent

.. code-block:: sh

  systemctl enable netxms-agent


Management Client
~~~~~~~~~~~~~~~~~

Desktop Management Client
^^^^^^^^^^^^^^^^^^^^^^^^^

Due to a limitation of the Eclipse platform used to build the Management Client, only a x64 build is provided.

 1. Make sure you have 64-bit Java version 17 installed you your system.

 2. Download the latest .jar file from http://www.netxms.org/download/, for example nxmc-5.1.0-standalone.jar.

 3. Run the .jar file using java, for example java -jar nxmc-xxx.jar .


The desktop management client produces a log file named :file:`.nxmc/data/.metadata/.log` in
the home folder of the currently logged in user. Inspect this log file if you encounter
errors when running the client.


Web Management Client
^^^^^^^^^^^^^^^^^^^^^

The |product_name| web interface is java based and should be deployed into a
servlet container to run. Servlet container should support servlet-api version
4. Supported versions are: Jetty 10, 11, 12, Tomcat 9. The supported Java
version is 17 or later.

  1. Install one of the servlet containers that support servlet-api version 4.

  2. Download the latest version of WAR file from the Web Interface Binaries section
     https://www.netxms.org/download/ named nxmc-VERSION.war, for example
     nxmc-5.1.0.war.

  3. Copy nxmc.war to the webapps directory. In a few seconds it will be autodeployed and
     available at http://SERVER_IP:SERVER_PORT/nxmc/

     Tomcat default folder:  /var/lib/tomcat9/webapps

     Jetty default folder: $JETTY_HOME/webapps/


The web management client produces a log file. For Tomcat it is located at
:file:`/var/lib/tomcat9/work/Catalina/localhost/nxmc/eclipse/workspace/.metadata/.log.`
Inspect this log file if you encounter errors when running the web client.


Installing from RPM repository
==============================

We provide RPM packages for RHEL and Fedora, both amd64 and aarch64.
If you need a build for another system, please contact us for support or check this section: :ref:`Installing from source <install_from_sources>`.

The RHEL repository is at https://packages.netxms.org/epel/.

The Fedora repository is at https://packages.netxms.org/fedora/.

A complete repository file and signing key is available in each corresponding root.

Add repository
--------------

DNF provides a simple way to add a repository. Please note that you may need to install the EPEL repository first. `See details <https://docs.fedoraproject.org/en-US/epel/>`_ ):

.. code-block:: sh

   # RHEL and compatible
   dnf config-manager --add-repo https://packages.netxms.org/epel/netxms.repo
   # Fedora
   dnf config-manager --add-repo https://packages.netxms.org/fedora/netxms.repo

Once added, you can install any package with ``dnf install`` (e.g. ``dnf install netxms-agent``).


Installing packages
-------------------

Server
~~~~~~

The server requires two components to function - the server itself (package "netxms-server") and at least one database abstraction layer driver
(multiple can be installed at the same time, e.g. for migration purposes). These database drivers are also used by the agent for database
monitoring (performing queries to databases).

Provided driver packages:

  * netxms-dbdrv-pgsql - PostgreSQL driver
  * netxms-dbdrv-mariadb - Mariadb driver
  * netxms-dbdrv-mysql - MySQL driver, currently under development (not built for Ubuntu 20 / Mint 20)
  * netxms-dbdrv-odbc - unixODBC driver (can be used with DB/2 and Microsoft SQL)
  * netxms-dbdrv-oracle - Oracle driver ( requires Oracle client installation )

#. Instal required packages (adjust command to match your environment):

   .. code-block:: sh

     dnf install netxms-server netxms-dbdrv-pgsql

#. Create user and database (:ref:`examples <db_creation>`).

#. Modify the server configuration file ("/etc/netxmsd.conf" to match your environment.

#. Load database schema and default configuration:

   .. code-block:: sh

     nxdbmgr init

#. Start server:

   .. code-block:: sh

     systemctl start netxms-server.service

#. Enable automatic startup of server:

   .. code-block:: sh

     systemctl enable netxms-server.service

#. If the database engine is running on the same system, add ordering dependency for
   database into netxmsd systemd unit override file. This will ensure database
   shutdown only after netxmsd process completion on system shutdown/restart. To
   add the dependency e.g. for the PostgreSQL database, run:

   .. code-block:: sh

     systemctl edit netxmsd

   and add the following lines:

   .. code-block:: sh

     [Unit]
     After=network.target postgresql.service

   After editing, run ``systemctl daemon-reload`` to reload systemd
   configuration.

.. note::

  Default credentials - user "admin" with password "netxms".


Agent
~~~~~

Install the core agent package ("netxms-agent") and optional subagent packages, if required:

.. code-block:: sh

  dnf install netxms-agent

Start agent

.. code-block:: sh

  systemctl start netxms-agent

Enable automatic startup of agent

.. code-block:: sh

  systemctl enable netxms-agent


Management Client
~~~~~~~~~~~~~~~~~

Desktop Management Client
^^^^^^^^^^^^^^^^^^^^^^^^^

Due to a limitation of the Eclipse platform used to build the Management Client, only a x64 build is provided.

 1. Make sure you have 64-bit Java version 17 installed you your system.

 2. Download the latest .jar file from https://www.netxms.org/download/, for example nxmc-5.1.0-standalone.jar.

 3. Run the .jar file using java, for example java -jar nxmc-xxx.jar .


The desktop management client produces a log file named :file:`.nxmc/data/.metadata/.log` in
the home folder of the currently logged in user. Inspect this log file if you encounter
errors when running the client.


Web Management Client
^^^^^^^^^^^^^^^^^^^^^

The |product_name| web interface is java based and should be deployed into a servlet container to
run. Minimal supported versions are: Jetty 10, Tomcat 9. The supported Java version is 17, but is found to be working with later versions, for example 21.

  1. Install one of the servlet containers that support servlet-api version 4.

  2. Download the latest version of WAR file from Web Interface Binaries section
     https://www.netxms.org/download/ named nxmc-VERSION.war, for example
     nxmc-5.0.6.war.

  3. Copy nxmc.war to the webapps directory. In a few seconds it will be autodeployed and
     available at http://SERVER_IP:SERVER_PORT/nxmc/

     Tomcat default folder:  /var/lib/tomcat9/webapps

     Jetty default folder: $JETTY_HOME/webapps/


The web management client produces a log file. For Tomcat it is located at
:file:`/var/lib/tomcat9/work/Catalina/localhost/nxmc/eclipse/workspace/.metadata/.log.`
Inspect this log file if you encounter errors when running the web client.

Installing on Windows
=====================

Server
------

  1. Download the latest version from http://www.netxms.org/download/.
     You will need Windows the installer named netxms-VERSION-x64.exe, e.g.
     netxms-server-5.0.8-x64.exe. Please note that in
     the following steps VERSION will be used as a substitution for an actual version
     number.
  2. Run the installer package on your server. The installation wizard will be
     displayed. Follow the prompts until the Select Components window opens.
  3. On the Select Components window, select the |product_name| Server option and an appropriate
     database client library. You do not have to install a database client library
     from |product_name| package if it is already installed on the machine (however, it might
     be required to add the folder where the client library is installed to system path).

    .. figure:: _images/win_netxms_setup_components.png

  4. For a typical installation, keep default settings in the Select Additional Tasks window.
     :guilabel:`Set hardened file system permissions` makes the installation folder
     accessible only to members of the Administrators group and the SYSTEM user.

    .. figure:: _images/win_netxms_setup_additional_tasks.png



   5. The Database selection window will open:

    .. figure:: _images/win_server_config_step2.png

  * Select the desired database type. Enter the name of database server.
  * In the DBA login name and DBA password fields, enter the database administrator login
    name and password. You have to fill these fields only if you have chosen the
    :guilabel:`Create database and database user before initialization` option.
  * Enter the desired database name, database user name and password.


    **Note for MySQL**:

    The bundled MySQL database driver does not support caching_sha2_password authentication
    which is the default for MySQL starting from version 8. Either select
    Legacy Authentication Method when installing MySQL, or use the database driver
    installed along with MySQL.
    The database driver gets installed when installing MySQL with Server-only option, however these
    two folders should be included into system path: :file:`C:\\Program Files\\MySQL\\MySQL Server 8.0\\lib`
    :file:`C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin`.


    **Note for Microsoft SQL Server**:

    Please refer to the Appendix for detailed Windows/MSSQL setup installation instructions :ref:`instructions<windows_mssql_install>`


    **Note for Oracle**:

    We recommend to use the native database driver (oracle.ddr).

  6. On the Ready to Install window, check whether everything is correct, then press the Install button.

  7. After installation, start the Netxms client and connect with the following credentials

Server default credentials:

Login: admin

Password: netxms


Agent
-----

  1. Download the latest version from http://www.netxms.org/download/. You will need Windows Agent installer (named nxagent-VERSION.exe or
     nxagent-VERSION-x64.exe, for example nxagent-5.0.8-x64.exe).

  2. Run the installer package on the target server. The installation wizard will be displayed.
     Follow the prompts until the |product_name| Server window opens:

     .. figure:: _images/win_agent_config.png


     Enter the IP address or host name of your |product_name| server. You can specify multiple
     management servers, separating them by commas. Press the Next button to continue.


  3. The subagent selection window will open:

     .. figure:: _images/win_agent_subagents.png

     In this window you can select which subagents you wish to load. Each subagent
     extends the agents functionality, e.g.:

.. list-table::
   :header-rows: 1
   :widths: 50 200

   * - Subagent
     - Description
   * - filemgr.nsm
     - Provides access to specified folders on the monitored host from the  |product_name| Management Client File Manager.
       This is also used for distributing Agent Policy configuration files (see :ref:`agent-policies-label`.)
   * - logwatch
     - Allows monitoring log files and Windows Event Log and sending matched events to |product_name| server.
   * - ping.nsm
     - Adds the possibility to send ICMP pings from the monitored host. Ping round-trip times can be collected by management server.
   * - netsvc.nsm, portcheck.nsm
     - Adds the possibility to check network services (like FTP or HTTP) from the monitored host.
   * - winperf.nsm
     - Provides access to Windows performance counters. This subagent is required if you need to collect CPU utilization from monitored host.
   * - wmi.nsm
     - Provides access to WMI data.
   * - ups.nsm
     - Adds support for UPS monitoring. The UPS can be attached to host via a serial cable or USB.


For more information on subagents, please refer to :ref:`subagent_list`.


  1. Follow the prompts to complete the installation.


Management Client
-----------------

Desktop Management Client:

 1. Download the latest version from https://www.netxms.org/download/.
    Since version 3.8 there are three options -
    archive (e.g. nxmc-5.0.8-win32-x64.zip), archive with bundled JRE (nxmc-5.0.8-win32-x64-bundled-jre.zip)
    and installer, which also has JRE bundled (e.g. netxms-client-5.0.8-x64.exe).
    If using the archive without JRE, make sure you have JRE version 11 or 15 installed.
    Due to a limitation of the Eclipse platform used to build the Management Client, only an x64 build is currently provided.

 2. If using the archive version, extract the zip in the preferred directory. If using the installer, launch it and follow the instructions.

 3. Run the nxmc file from the extracted catalog, or launch from the Windows Start Menu, if you used the installer.

Web Management Client:

On the Windows platform there are two options: one is to manually install the .war file into a servlet container and
the second one is to use the netxms-webui-VERSION-x64.exe installer. The installer will
install Jetty and copy the .war file into required folder. Here the
installation via the installer is described:

  1. Download the latest version from https://www.netxms.org/download. You will need
     Windows installer netxms-webui-VERSION-x64.exe (e.g.: netxms-webui-5.0.8-x64.exe).
     Due to a limitation of the Eclipse platform used to build the Management Client,
     only an x64 build is currently provided.

  2. Run the installer package on your server. The Installation wizard will be
     displayed. Follow the prompts. The installer allows to change the installation path and port.

  3. After the installation procedure is finished, check that the WEB GUI is available at
     http://SERVER_IP:SERVER_PORT/nxmc/


Unattended installation of the |product_name| Agent
---------------------------------------------------

The Windows Agent installer, named nxagent-VERSION.exe, for example nxagent-5.0.8-x64.exe,
has various command line options for unattended installation. Installation will ignore
any configuration file options (/CONFIGENTRY, /NOSUBAGENT, /SERVER, /SUBAGENT, etc) if a config
file already exists or if the /CENTRALCONFIG option is used. However, it is possible to
delete and recreate the configuration file using the /FORCECREATECONFIG command line option.


The options are the following:

.. list-table::
   :header-rows: 1
   :widths: 12 30

   * - Option
     - Description
   * - /CENTRALCONFIG
     - Enable read configuration from server on startup. See :ref:`agent_configuration_files_on_server`
       for more information.
   * - /CONFIGENTRY=value
     - It can be used to add any parameter to the configuration file during initial install.
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
     - Causes Setup to create a log file in the TEMP directory of the user detailing file
       installation and [Run] actions taken during the installation process.
   * - /LOG=filename
     - Same as /LOG, except it allows to specify a fixed path/filename to use for the log file.
       If a file with the specified name already exists it will be overwritten.
       If the file cannot be created, Setup will abort with an error message.
   * - /LOGFILE=filename
     - Set agent log file (will be set in configuration file as ``LogFile``).
   * - /MERGETASKS=”tasknames”
     - Comma-separated list of tasks for installation. If a task is specified with ! character
       prior to its name, it will be deselected. Possible values are ``fspermissions`` - set hardened file system permissions,
       ``sessionagent`` - Install session agent, ``useragent`` - Install user support application.
       e.g. ``/MERGETASKS="!fspermissions,useragent"``
   * - /NOSUBAGENT=name
     - Disable subagent name
   * - /NOTUNNEL
     - Disable tunnel operation (it is the default)
   * - /REINSTALLSERVICE
     - Reinstalls Windows service
   * - /SERVER=IP
     - Set server IP address or host name (will be set in the configuration file as ``MasterServers``).
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

:command:`nxagent-5.0.8-x64.exe /VERYSILENT /SUPPRESSMSGBOXES /SERVER=10.0.0.1 /SUBAGENT=UPS /SUBAGENT=FILEMGR /CONFIGENTRY=ZoneUIN=15 /CONFIGENTRY=[FILEMGR] /CONFIGENTRY=RootFolder=C:\\`

This command will add 3 lines at the end of generated config file:

.. code-block:: ini

    ZoneUIN=15
    [FILEMGR]
    RootFolder=C:\


Unattended uninstallation of |product_name| Agent
-------------------------------------------------

The uninstaller application is named unins???.exe and is located in the agent folder (``C:\NetXMS`` by default).
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
     - Causes to create a log file in the TEMP directory of the user.
   * - /LOG=filename
     - Same as /LOG, except it allows to specify a fixed path/filename to use for the log file.
   * - /SUPPRESSMSGBOXES
     - Don't ask user anything. Only has an effect when combined with ``/SILENT`` and ``/VERYSILENT``.
   * - /NORESTART
     - Instructs the uninstaller not to reboot even if it would be necessary.

Example:

:command:`unins000.exe /SUPPRESSMSGBOXES /VERYSILENT /NORESTART`


Install on Android
==================

Management Client
-----------------

To install Android management client download netxms-console-VERSION.apk (example:
netxms-console-3.4.178.apk) file from the http://www.netxms.org page. Check that
installation of applications from unknown sources is allowed in security settings of
your phone. Run this installer on required device.

After the agent is installed, go to settings and in the main menu, connection part, set all
required connection credentials: server address, port, user name, password.

.. note::
  The user configured for the connection should have the :guilabel:`Login as mobile device`
  user permission.


.. _install_from_sources:

Installing from sources
=======================

Server
------

  #. Download the source archive (netxms-VERSION.tar.gz) from https://www.netxms.org/download/. *VERSION* is used in names instead of an actual version number.
  #. Unpack the archive:

        :command:`tar zxvf netxms-VERSION.tar.gz`

  #. Since version 3.8, the reporting server is being built along with the sources. This requires maven to be installed on the system. You need Oracle and MS SQL JDBC drivers in your local maven repository.

        The Oracle JDBC driver library can be obtained here: https://oracle.com/otn-pub/otn_software/jdbc/199/ojdbc8.jar

        the Microsoft SQL JDBC driver library can be obtained from here: https://www.microsoft.com/en-us/details.aspx?id=54671
        You will need sqljdbc_4.2/enu/jre8/sqljdbc42.jar file from this archive.

        To install these libraries:
        :command:`mvn install:install-file -DgroupId=com.microsoft.sqlserver -DartifactId=sqljdbc4 -Dversion=4.2 -Dpackaging=jar -Dfile=sqljdbc42.jar`
        :command:`mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc8 -Dversion=12.2.0.1 -Dpackaging=jar -Dfile=ojdbc8.jar`

  #. Change directory to netxms-VERSION and run the configure script:

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

  #. Download the source archive (netxms-VERSION.tar.gz) from https://www.netxms.org/download/. *VERSION* is used in names instead of an actual version number.
  #. Unpack the archive:

        :command:`tar zxvf netxms-VERSION.tar.gz`

  #. Change directory to netxms-VERSION and run the configure script:

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
             - Build monitoring agent. It is strongly recommended to install the agent on a server

  #. Run build binaries and install them into /usr/local (unless changed with configure flag ``--prefix``)

        :command:`make`

        :command:`make install`

  #. Copy sample config file:

        :command:`cp contrib/nxagentd.conf-dist /usr/local/etc/nxagentd.conf`

        By default the agent load configuration file is PREFIX/etc/netxmsd.conf (where PREFIX is installation prefix set by configure), unless a different file is specified with the command line switch "-c".

  #. Adjust the agent configuration file if required.

     Detailed information about each configuration parameter can be found in section :ref:`agent_configuration_file`.

     Minimal required configuration:

     .. code-block:: ini

       MasterServers = 172.16.1.1 # server IP - agent will drop connections unless address is provided here
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

There are a few settings available for configuration of the WebUI.

  * autoLoginOnReload - autologin on page reload in browser (default: true)
  * enableCompression - enable protocol compression between Web UI and server process (default: true)
  * loginFormImage - path to custom login image
  * loginFormImageBackground - colour of background around custom login image
  * loginFormImageMargins - margins in px around custom login image (default: 10)
  * server - server DNS name or IP (default: 127.0.0.1)

There are multiple ways to set the connection configuration from WebUI to NetXMS server.
Configuration is checked in this order:

  1. Using JNDI. Environment should be set like nxmc/NAME for example: nxmc/server

  2. nxmc.properties properties file in the class path of your application server. This file should be created in ini format: NAME=VALUE. For example:

    .. code-block:: ini

      server = 127.0.0.1

    Default locations:

    **Jetty**


    **Tomcat**

    The default location of this file on Debian and Ubuntu is in /usr/share/tomcat9/lib. Other Linux distributions
    may use a different location.

    **Oracle Weblogic**

    $WEBLOGIC_HOME/user_projects/domains/YOURDOMAIN

  3. jvm parameter in format -Dnxmc.NAME=VALUE.  For example: -Dnxmc.server=127.0.0.1

  4. Environment variable NXMC_NAME=VALUE. For example NXMC_server=127.0.0.1

  5. If none of the above configurations exist, the Web UI tries to resolve the "NETXMS_SERVER" DNS name as server connection.

  6. If none of above configurations exist, the Web UI uses "127.0.0.1" as a server address.


Custom logo on login screen
---------------------------

It is possible to change the default logo on the login screen to a custom image by setting
the loginFormImage property in nxmc.properties file. The image file must be located within
the application server class path and the file name must be given relative to the class path
root with a leading slash. For example, if the custom image is in a file logo.jpg located
in the same directory as nxmc.properties, the correct entry will be:

.. code-block:: ini

  loginFormImage = /logo.jpg



.. _linux_jetty_install:


How to configure the NetXMS web client with jetty in Linux
----------------------------------------------------------


1. Download the latest version of Jetty (12.0.13 at the moment of writing).

.. code-block:: sh

      curl -O https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-home/12.0.13/jetty-home-12.0.13.tar.gz

2. Create directories and extract Jetty, then create the initial configuration by running start.jar.

.. code-block:: sh

      tar -xvf jetty-home-12.0.13.tar.gz -C /opt

      ln -s /opt/jetty-home-12.0.13 /opt/jetty-home-12

      mkdir -p /opt/netxms-webui/{etc,logs} && cd /opt/netxms-webui

      java -jar /opt/jetty-home-12/start.jar --add-modules=ee8-deploy,gzip,http,http2,https,logging-logback,plus,server,ssl,work

3. Download the war file (version 5.1.2 at the moment of writing) and place it in the webapps directory.

.. code-block:: sh

      curl -o webapps/ROOT.war https://netxms.com/releases/5.1/nxmc-5.1.2.war

4. Generate ssl key (for testing purposes) and adjust the ssl.ini file. A reverse proxy with proper certificate should be used in production. Adjust DN, keyStorePassword and keyStorePath as per requirements.

.. code-block:: sh

      keytool -genkeypair -alias jetty -keyalg RSA -keysize 2048 -keystore /opt/netxms-webui/etc/keystore.p12 -storetype PKCS12 -storepass password -keypass password -validity 3650 -dname "CN=netxms-webui, OU=netxms, O=netxms, L=netxms, ST=netxms, C=netxms"

      sed 's,# jetty.sslContext.keyStorePassword=,jetty.sslContext.keyStorePassword=password,' -i'' start.d/ssl.ini

5. Run Jetty to verify the configuration. Once verified, stop with Ctrl+C.

.. code-block:: sh

      java -Dnxmc.logfile=/opt/netxms-webui/logs/nxmc.log -jar /opt/jetty-home-12/start.jar

6. Create a systemd service file for Jetty (sample is bellow).

.. code-block:: sh

      systemctl edit --force --full netxms-webui.service

.. code-block:: ini

   [Unit]
    Description=NetXMS WebUI
    StartLimitIntervalSec=0

   [Service]
    Type=simple
    WorkingDirectory=/opt/netxms-webui
    Environment=JETTY_HOME=/opt/jetty-home-12
    Environment=JETTY_BASE=/opt/netxms-webui
    User=jetty
    Group=jetty
    ExecStart=java -Dnxmc.logfile=/opt/netxms-webui/logs/nxmc.log -jar /opt/jetty-home-12/start.jar
    Restart=on-failure
    RestartSec=30
    TimeoutSec=900

   [Install]
    WantedBy=multi-user.target
    EnableDefaultCounters = yes


7. Enable netxms-web.service and start it.

.. code-block:: sh

     systemctl enable --now netxms-web.service



Default login credentials
=========================

The default login is "admin" with password "netxms". On first login, the user will be prompted to change their password immediately.

If required, the password can be reset back to default using :ref:`nxdbmgr utility <password-reset>`.

.. _db_creation:


Database creation examples
==========================

This chapter provides some database creation SQL examples. Please consult the relevant database documentation for the initial install.

PostgreSQL
----------

.. code-block:: sh

  createuser -P netxms
  createdb -O netxms netxms

If the TimescaleDB extension is to be used, it should be added to the newly created database:

.. code-block:: sh

  psql netxms
  CREATE EXTENSION IF NOT EXISTS timescaledb CASCADE;
  \q

Configuration file example:

.. code-block:: ini

  DBDriver = pgsql.ddr
  DBServer = localhost
  DBName = netxms
  DBLogin = netxms
  DBPassword = PaSsWd

MariaDB
-------

.. code-block:: sh

  echo "CREATE DATABASE netxms CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;" | mysql -u root -p
  echo "CREATE USER 'netxms'@'localhost' IDENTIFIED BY 'PaSsWd';" | mysql -u root -p
  echo "GRANT ALL on netxms.* to 'netxms'@'localhost';" | mysql -u root -p


Configuration file example:

.. code-block:: ini

  DBDriver = mariadb.ddr
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

.. code-block:: ini

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

.. code-block:: ini

  DBDriver = oracle.ddr
  DBServer = //127.0.0.1/XE # instant client compatible connection string
  DBLogin = netxms
  DBPassword = PaSsWd


.. _windows_mssql_install:

How to install NetXMS server on Windows Server with local Microsoft SQL Server Express
--------------------------------------------------------------------------------------

1. Login as adiministrator
2. Install Microsoft SQL Server Express with defaut options.

If enabling mixed authentication mode:


3. Enable mixed authentication mode as per https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/change-server-authentication-mode Don't forget to restart SQL Server after changing authentication mode.
4. Run NetXMS Server installer. When prompted for database information, use the following answers:

    - Server type: MS SQL
    - Server name: localhost\SQLEXPRESS
    - Database name: (any valid name, we use "netxms")
    - Login name: (any valid account name, we use "netxms")
    - Password: (any password complex enough to match OS password policy)
    - Create database and database user: check
    - DBA login name: *
    - DBA password: (left empty)

This assumes the currently logged in user has DBA access to the SQL Server instance. This should be the case if SQL Server was just installed by the same user.
An alternative approach is to enable the "sa" user in SQL server and use sa login and password as DBA login name and password.

The installer should create database, database user, assignthe  user as database owner, and the NetXMS Core service should start successfully.


If mixed authentication is not an option:


Currently the installer does not support automatic database creation for Windows authentication mode, so there will be more manual steps.

3. Login to SQL Server Management Studio
4. Create a new database with the default owner (owner should be set to currently logged in administrator user)
5. Run the NetXMS Server installer. On "Select additional tasks" page uncheck "Start NetXMS Core service".
6. When prompted for database information, use the following answers:

    - Server type: MS SQL
    - Server name: localhost\SQLEXPRESS
    - Database name: (database name from step 4)
    - Login name: *
    - Password: (left empty)
    - Create database and database user: uncheck

7. After installation is complete, go to "Services", find the "NetXMS Core" service, and set it to login as administrator user (same user used for installation)
8. Start NetXMS Core service


How to install NetXMS server on Windows Server with remote Microsoft SQL Server Express
---------------------------------------------------------------------------------------

Assumptions:
 * Both the SQL Express Server and the NetXMS Server are in the same domain
 * TCP/IP is enabled in SQL Server network properties
 * TCP/IP is configured to use a fixed port
 * A firewall rule is added to allow incoming connections on the SQL Server TCP port (it may be needed to add this manually)
 * Mixed authentication mode is already enabled on SQL Server (only for scenario 1 below)

If using a SQL account for NetXMS services is acceptable


1. Log in to the NetXMS Server machine with a domain account that has local administrator rights as well as sysadmin rights on SQL Server
2. Install ODBC Driver for SQL Server
3. Run the NetXMS Server installer. When prompted for database information, use the following answers:

    - Server type: MS SQL
    - Server name: SQL server domain computer name or fully qualified DNS name (if the TCP port is not 1433, then use the form server_name,port)
    - Database name: (any valid name, we use "netxms")
    - Login name: (any valid account name, we use "netxms")
    - Password: (any password complex enough to match OS password policy)
    - Create database and database user: check
    - DBA login name: *
    - DBA password: (left empty)

The installer should create database, database user, assign user as database owner, and the NetXMS Core service should start successfully.

In this scenario the server will use login and password on SQL server, so the service can continue to run under Local System account, or you can change it to any domain account.

If the server has to use domain account for accessing the database


1. Install ODBC Driver for SQL Server
2. If not already done, create a new login on SQL Server for the domain user to be used by NetXMS Core service
3. Create the new database, assign login from step 2 as owner
4. Log in to the NetXMS Server machine with the same domain user
5. Run the NetXMS Server installer. On "Select additional tasks" page, uncheck "Start NetXMS Core service".
6. When prompted for database information, use the following answers:

    - Server type: MS SQL
    - Server name: SQL server domain computer name or fully qualified DNS name (if the TCP port is not 1433, then use the form server_name,port)
    - Database name: (database name from step 4)
    - Login name: *
    - Password: (left empty)
    - Create database and database user: uncheck

7. After installation is complete, go to "Services", find the "NetXMS Core" service, and set it to login as administrator user (same user used for installation)
8. Start the NetXMS Core service
