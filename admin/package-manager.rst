.. _package_mngr:

##################
Package management
##################

Introduction
============

The package management functionality can upload and execute installers via the
|product_name| agent. This allows to perform centralized upgrade of the
|product_name| agent, to install other software or upload and extract archive files
onto target systems. 

  .. warning::
     Do not use this package management feature to upgrade |product_name| agent
     installed via system package managers (e.g., apt, dnf, yum). Upgrading
     an agent that is managed by the distribution package manager may conflict with
     the system packaging tools, overwrite files tracked by the package system,
     or leave packages in an inconsistent state. Use your distribution's package
     manager to update the NetXMS agent on such systems.

To access package management, open the :guilabel:`Configuration` perspective and
select :guilabel:`Packages`. Software packages are first uploaded to the
|product_name| server. In order to do this, select :guilabel:`Upload to server`
and select a file. 

For some types of packages, the additional dialog :guilabel:`Edit Package Metadata`
is displayed. This allows to specify additional metadata for a package. Whenever
possible, metadata information is filled in automatically based on information
contained in file name.

You can open the metadata editor by double-clicking on a package in the list. In
the metadata editor `Name`, `Version` and `Description` are just informative fields,
they are not used in package processing. 

`Platform` denotes for which platforms a package is applicable. The actual platform
of a node is compared to this field as string value using wildcard characters.
Two wildcard characters are supported: ``*`` - represents zero, one or multiple
characters. ``?`` - represents any single character. Setting `Platform` to ``*``
would mean any platform. ``Linux*`` would mean both 32 and 64 bit Linuxes.

`Type` defines package type. This defines how the agent should process the
package when installing it. The meaning of the `Command` field depends on the
package type, see information in the table below. Putting ``@`` at the beginning
of `Command` enables macro expansion (``@`` character is stripped from the
command).

The following types of package files are supported by package management:


.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Package type
     - Extension
     - Description
   * - NetXMS Agent Package (agent-installer)
     - .apkg
     - `Command` is not used by this package type. 
   * - Debian/Ubuntu Package
     - .deb
     - `Command` contains additional parameters passed to /usr/bin/dpkg
   * - Executable
     - .exe
     - `Command` is optional. If specified, it sets the actual command executed
       by agent. ``${file}`` macro will be replaced by actual file name.
   * - Windows Installer Package
     - .msi
     - `Command` contains additional parameters passed to Windows installer API
   * - Windows Installer Patch
     - .msp
     - `Command` contains additional parameters passed to Windows installer API
   * - Windows Update Package
     - .msu
     - `Command` contains additional parameters passed to wusa.exe
   * - Red Hat Package
     - .rpm
     - `Command` contains additional parameters passed to /usr/bin/rpm
   * - NetXMS Package Info
     - .npi
     - Deprecated type of metadata file for NetXMS Agent Package. 
   * - Compressed TAR Archive
     - .tgz, .tar.gz
     - `Command` is optional. If specified, it defines the path the archive should
       be extracted to.
   * - ZIP Archive
     - .zip
     - `Command` is optional. If specified, it defines the path the archive should
       be extracted to. 


To deploy a package, select one or several nodes from :guilabel:`Infrastructure
services` or :guilabel:`Entire Network`. You can also select containers or
subnets. Right-click on the selected items and select :guilabel:`Deploy
package...`. Select the package and click :guilabel:`OK`. 

During the package deployment process, the server will request the platform name from agent
and check if it matches `Platform` from the package metadata. The deployment process
is shown in the :guilabel:`Package deployment monitor` tab that is visible on all
relevant containers, subnets and nodes. 
