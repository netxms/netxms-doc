.. _package_mngr:

##################
Package management
##################

Introduction
============

Package management functionality can upload and execute installers via
|product_name| agent. This allows to perform centralized upgrade of
|product_name| agent, install other software or upload and extract archive files
onto target systems. 

To access package management, open :guilabel:`Configuration` perspective and
select :guilabel:`Packages`. Software packages are first uploaded to
|product_name| server. In order to do this, select :guilabel:`Upload to server`
and select a file. 

For some types of packages additional dialog :guilabel:`Edit Package Metadata`
is displayed, allowing to specify additional metadata for a package. Whenever
possible, metadata information is filled in automatically based on information
contained in file name. 

You can open metadata editor by double-clicking on a package in the list. In
metadata editor `Name`, `Version` and `Description` are just informative fields,
they are not used in package processing. 

`Platform` denotes for which platforms a package is applicable. Actual platform
of a node is compared to this field as string value using wildcard characters.
Two wildcard characters are supported: ``*`` - represents zero, one or multiple
characters. ``?`` - represents any single character. Setting `Platform` to ``*``
would mean any platform. ``Linux*`` would mean both 32 and 64 bit Linuxes.

`Type` defines package type. This defines how agent should process the package
when installing it. Meaning of `Command` field depends on package type. See
information in the below table. 

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
     - `Command` contains additional parameters passed to msiexec.exe
   * - Windows Installer Patch
     - .msp
     - `Command` contains additional parameters passed to msiexec.exe
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
     - `Command` is optional. If specified, it defines path the archive should
       be extracted to. 
   * - ZIP Archive
     - .zip
     - `Command` is optional. If specified, it defines path the archive should
       be extracted to. 


To deploy a package, select one or several nodes from :guilabel:`Infrastructure
services` or :guilabel:`Entire Network`. You can also select container(s) or
subnet(s). Right-click on the selected item(s) and select :guilabel:`Deploy
package...`. Select the package and click :guilabel:`OK`. 

During package deployment process server will request platform name from agent
and check if it matches `Platform` from package's metadata. Deployment process
is shown in :guilabel:`Package deployment monitor` tab that is visible on all
containers, subnets and nodes concerned. 
