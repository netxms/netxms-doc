==============
JVM monitoring
==============

|product_name| has Java plugin that allow to monitor JVM. This subagent is build using
JMX functionality. 

Metrics
=======

Single-value Metrics
--------------------

.. list-table::
   :header-rows: 1
   :widths: 50 20 30
   :class: longtable


   * - Metric
     - Type
     - Meaning
   * - JMX.ObjectAttribute(name,object,attribute,[item])
     - String
     - Get attribute of any connection, object. Optional attribute *item* is used when attribute is a list. 
   * - JMX.Memory.ObjectsPendingFinalization(name)
     - Unsigned integer
     - JVM objects pending finalization
   * - JMX.Memory.Heap.Committed(name)
     - Unsigned integer 64
     - JVM committed heap memory
   * - JMX.Memory.Heap.Current(name)
     - Unsigned integer 64
     - JVM current heap size
   * - JMX.Memory.Heap.Init(name)
     - Unsigned integer 64
     - JVM initial heap size
   * - JMX.Memory.Heap.Max(name)
     - Unsigned integer 64
     - JVM maximum heap size
   * - JMX.Memory.NonHeap.Committed(name)
     - Unsigned integer 64
     - JVM committed non-heap memory
   * - JMX.Memory.NonHeap.Current(name)
     - Unsigned integer 64
     - JVM current non-heap memory size
   * - JMX.Memory.NonHeap.Init(name)
     - Unsigned integer 64
     - JVM initial non-heap memory size
   * - JMX.Memory.NonHeap.Max(name)
     - Unsigned integer 64
     - JVM maximum non-heap memory size
   * - JMX.Threads.Count(name)
     - Unsigned integer
     - JVM live threads count
   * - JMX.Threads.DaemonCount(name)
     - Unsigned integer
     - JVM daemon threads count
   * - JMX.Threads.PeakCount(name)
     - Unsigned integer
     - JVM peak number of threads
   * - JMX.Threads.TotalStarted(name)
     - Unsigned integer
     - JVM total threads started
   * - JMX.VM.BootClassPath(name)
     - String
     - JVM boot class path
   * - JMX.VM.ClassPath(name)
     - String
     - JVM class path
   * - JMX.VM.LoadedClassCount(name)
     - Unsigned integer
     - JVM loaded class count
   * - JMX.VM.Name(name)
     - String
     - JVM name
   * - JMX.VM.SpecVersion(name)
     - String
     - JVM specification version
   * - JMX.VM.TotalLoadedClassCount(name)
     - Unsigned integer 
     - JVM total loaded class count
   * - JMX.VM.UnloadedClassCount(name)
     - Unsigned integer
     - JVM unloaded class count
   * - JMX.VM.Uptime(name)
     - Unsigned integer
     - JVM uptime
   * - JMX.VM.Vendor(name)
     - String
     - JVM vendor
   * - JMX.VM.Version(name)
     - String
     - JVM version

Lists
-----

.. list-table::
   :header-rows: 1
   :widths: 50 200
   
   * - Metric
     - Meaning
   * - JMX.Domains(name)
     - List of JVM domains
   * - JMX.Objects(name)
     - List of JVM objects
   * - JMX.ObjectAttributes(name)
     - List of JVM object's attributes


Configuration
=============

It is required to define java subagent and it's configurations before JMX plugin configuration. More information about Java subagent and it's configuration can be found in :ref:`java-subagent` section. JMS has only one configuration parameter "Server". It is used to define JMX server connection string. 

JMS server connection string declaration options:

   * name:url
   * name:login@url
   * name:login/password@url


Configuration example
---------------------

In example are defined 2 JMS connections: *name* and *serverName2*. 

.. code-block:: sh

   MasterServers = netxms.demo
   SubAgent=java.nsm
   
   [JAVA]
   jvm = /usr/lib/jvm/java-8-oracle/jre/lib/amd64/server/libjvm.so
   Plugin = jmx.jar
   
   [JMX]
   Server=name:login/password@localhost
   Server=serverName2:admin/pwd123@server1
   
