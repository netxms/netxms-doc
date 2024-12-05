.. _hypervisor-monitoring:

=====================
Hypervisor monitoring
=====================

|product_name| has subagents that allow to monitor hypervisors. This subagent is build using
libvirt functionality. Due to the fact that libvirt is poorly supported on Windows platforms,
vmgr subagent is not provided on Windows.

When installing |product_name| from packages, vmgr subagent is provided as a separate package named netxms-agent-vmgr.
If building from source, ./configure should be ran with --with-vmgr. 

Configuration
=============

Configuration is separated into two parts: **vmgr** section defines all monitored hosts, and each host configuration
is defined in separate section for each host.

Each host configuration should contain connection URL. Login and password parameters are optional. URL creation
rules for each vitalization solution type can be found `in libvirt documentation <http://libvirt.org/drivers.html>`_.

Not all api functions are supported by all hypervisors in libvirt. See `libvirt API support matrix <https://libvirt.org/hvsupport.html>`_ for more information.


Configuration example
---------------------

In this example two hosts are defined: **localESX1** and **test**. **localESX1** connection details are described in section **vmgr:localESX1**
and **test** connection details are described in section **vmgr:test**.

.. code-block:: sh

   MasterServers = netxms.demo
   SubAgent = vmgr.nsm

   [vmgr]
   host = localESX1
   host = test

   [vmgr:localESX1]
   Url = esx://root@10.5.0.21/?no_verify=1
   Login = root
   Password = password

   [vmgr:test]
   Url = test:///default


Provided Metrics
================

Single-value Metrics
--------------------

.. list-table::
   :header-rows: 1
   :widths: 50 20 30

   * - Metric
     - Type
     - Description
   * - VMGR.Host.CPU.Arch(hostName)
     - String
     - Host CPU architecture
   * - VMGR.Host.CPU.MaxCount(hostName)
     - Unsigned integer
     - Host maximum virtual CPU count
   * - VMGR.Host.FreeMemory(hostName)
     - Unsigned integer 64
     - Host free memory
   * - VMGR.Host.MemorySize(hostName)
     - Unsigned integer 64
     - Host memory size
   * - VMGR.Host.CPU.Model(hostName)
     - String
     - Host CPU model name
   * - VMGR.Host.CPU.Frequency(hostName)
     - Unsigned integer
     - Host CPU frequency
   * - VMGR.Host.ConnectionType(hostName)
     - String
     - Connection type
   * - VMGR.Host.LibraryVersion(hostName)
     - Unsigned integer 64
     - Library version
   * - VMGR.Host.ConnectionVersion(hostName)
     - Unsigned integer 64
     - Connection version
   * - VMGR.VM.Memory.Used(hostName,vmName)
     - Unsigned integer 64
     - Memory currently used by VM
   * - VMGR.VM.Memory.UsedPrec(hostName,vmName)
     - Unsigned integer
     - Percentage of currently memory usage by VM
   * - VMGR.VM.Memory.Max(hostName,vmName)
     - Unsigned integer 64
     - Maximum VM available memory
   * - VMGR.VM.CPU.Time(hostName,vmName)
     - Unsigned integer 64
     - Maximum VM CPU time

Tables
------

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Metric
     - Description
   * - VMGR.VM(hostName)
     - Connection VM table
   * - VMGR.InterfaceList(hostName)
     - Connection interface list
   * - VMGR.VMDisks(hostName,vmName)
     - VM Disks
   * - VMGR.VMController(hostName,vmName)
     - VM Controllers
   * - VMGR.VMInterface(hostName,vmName)
     - VM Interfaces
   * - VMGR.VMVideo(hostName,vmName)
     - VM Video adapter settings
   * - VMGR.Networks(hostName)
     - Networks table
   * - VMGR.Storages(hostName)
     - Storages table

Lists
-----

.. list-table::
   :header-rows: 1
   :widths: 50 50

   * - Metric
     - Description
   * - VMGR.VMHost
     - List of hosts
   * - VMGR.VMList(hostName)
     - List of VM for the host
