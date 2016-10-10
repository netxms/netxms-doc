.. _ups-monitoring:

=====================
Hypervisor monitoring
=====================

NetXMS has subagents that allow to monitor hypervisors. This subagent is build using
libvirt functionality. 

Metrics
=======

Parameters
----------

.. list-table::
   :header-rows: 1
   :widths: 50 30 200

   * - Metric
     - Type
     - Meaning
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
   :widths: 50 200

   * - Metric
     - Meaning
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
   :widths: 50 200
   
   * - Metric
     - Meaning
   * - VMGR.VMHost
     - List of hosts
   * - VMGR.VMList(hostName)
     - List of VM for the host


Configuration
=============

Configuration is separeted to two parts. In "vmgr" part are defined all monitored hosts. Host configuration is 
descibed afterwards in separate section for each host. 

Each host configuration should contain connection URL. Login and password parameters are optional. URL creation 
rules for each vitalization solution type can be found `in libvirt documentation: http://libvirt.org/drivers.html <http://libvirt.org/drivers.html>`_.


Configuration example
---------------------

In example are defined 2 hosts: localESX1 and test. localESX1 connection details are described in "vmgr:localESX1" 
section and test connection details are described in "vmgr:test" section.

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent=vmgr.nsm

   [vmgr]
   host=localESX1
   host=test
   
   [vmgr:localESX1]
   Url=esx://root@10.5.0.21/?no_verify=1
   Login=root
   Password=password

   [vmgr:test]
   Url=test:///default
   

