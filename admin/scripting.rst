.. _scripting:


#########
Scripting
#########


NXSL
====

Overview
--------

In many parts of the system, fine tuning can be done by using |product_name| built-in
scripting language called NXSL (stands for |product_name| Scripting Language). NXSL was
designed specifically to be used as embedded scripting language within |product_name|,
and because of this has some specific features and limitations. Most notable is
very limited access to data outside script boundaries - for example, from NXSL
script you cannot access files on server, nor call external programs, nor even
access data of the node object other than script is running for without
explicit permission. NXSL is interpreted language - scripts first compiled into
internal representation (similar to byte code in Java), which is then executed
inside NXSL Virtual Machine. Language syntax and available functions can be
found in `NXSL documentation <https://www.netxms.org/documentation/nxsl-latest/>`_.

List of places where NXSL scripting is used
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - Script library
  - DCI transformation scripts
  - DCI instance filter script
  - DCI scripted threshold
  - DCI summary table object filter script
  - Container, template, cluster auto-bind script
  - SNMP trap transformation script
  - EPP filter script
  - EPP inline script actions
  - Map object filter script
  - Map link styling script
  - Dashboard scripted chart
  - Dashboard status indicator
  - Context dashboard auto-bind script
  - Business service scripted check
  - Business service DCI auto apply script
  - Business service object auto apply script  
  - Business service prototype instance filter script
  - Asset attribute auto fill script
  - Object query
  - Agent configuration filter script
  - Condition status calculation script
  - Custom housekeeping scripts (see :ref:`custom-housekeeping-scripts`)


Scripting library
-----------------

:guilabel:`Script Library` is used to store scripts that can be afterwards executed as macros,
part of other script or from debug server console. Scripts can be added, deleted and modified in
in this view.

.. figure:: _images/script_library.png


Usage
~~~~~

Scripts from Script Library can be accessed as:
  1. a macros %[\ `scriptName`\ ]
  2. used in action of type "Execute NXSL script"
  3. executed from DCIs with "Script" source
  4. functions can be called from other scripts either by using "import
     `scriptName`\ " and calling functions by name, or without import, by
     calling "\ `scriptName`::`functionName`\ "
  5. executed from server debug console "execute `scriptName`\ "
  6. scripts having name starting with "`Hook::`\ " are executed automatically,
     e.g. "Hook::ConfigurationPoll" is being run on each node's configuration
     poll


.. note::
   All parameters provided to script are accessible via $ARGS array. The other 
   option to use parameters is to specify `main()` function in the script and 
   define parameters in it's definition. 

.. _execute_server_script:


Execute Server Script
---------------------

This view allows to execute arbitrary script. Script can be manually created just before execution,
and afterwards saved, can be taken from the script library, can be used modified script from the
script library and afterwards saved or saved as. If this view is opened on a node, then in the
script is available ``$node`` variable with node object.

.. note::
   All parameters provided to script are accessible via $ARGS array.
   
.. figure:: _images/execute_server_script.png


NXShell
=======

NxShell is based on Jython and provide access to |product_name| Java API using interactive
shell. NxShell binary comes with server distribution suite and can be run from shell or crontab. NxShell is also build as single jar file, which includes all required libraries.

Download: http://www.netxms.org/download/nxshell-VERSION.jar
(example: http://www.netxms.org/download/nxshell-5.0.8.jar)


Usage 
-----

Nxshell binary gets installed in $NETXMS_HOME directory, for example /usr/bin/nxshell.
As of version 5.1, nxshell launcher accepts command line -r or --properties= for providing path to 
nxshell properties file.

~# nxshell -h
NetXMS Interactive Shell  Version 5.1.0-rc320
Copyright (c) 2006-2024 Raden Solutions

Usage: nxshell [OPTIONS] [script]

Options:
  -C, --classpath <path>      Additional Java class path.
  -D, --debug                 Show additional debug output (use twice for extra output).
  -h, --help                  Display this help message.
  -H, --host <hostname>       Specify host name or IP address. Could be in host:port form.
  -j, --jre <path>            Specify JRE location.
  -n, --no-sync               Do not synchronize objects on connect.
  -p, --port <port>           Specify TCP port for connection. Default is 4701.
  -P, --password <password>   Specify user's password. Default is empty.
  -r, --properties <file>	    File with additional Java properties.
  -t, --token <token>         Login to server using given authentication token.
  -u, --user <user>           Login to server as user. Default is "admin".
  -v, --version               Display version information.



There are two options of this jar usage:

  1. it can be started as interactive shell;

     :command:`java -jar nxshell-5.0.8.jar`

  2. it can be started with the script name as a first parameter. Then it will just
     execute this script and exit. Example:

     :command:`java -jar nxshell-5.0.8.jar test.py`

When NxShell is started, it tries to get server IP, login and password from Java
properties. In interactive mode, user will be asked for details, otherwise
default values will be used.

Start as interactive shell, with IP and Login provided (password will be asked):

:command:`java -Dnetxms.server=127.0.0.1 -Dnetxms.login=admin -jar nxshell-5.0.8.jar`

Properties
~~~~~~~~~~

These properties should be set with JVM's "-D" option. Please make sure that all
"-D" options are before "-jar".

======================= ================
Parameter               Default Value
======================= ================
netxms.server           127.0.0.1
netxms.login            admin
netxms.password         netxms
netxms.encryptSession   true
======================= ================


Scripting
---------

For details on API please refer to javadoc at
http://www.netxms.org/documentation/javadoc/latest/.

NxShell provide user with already connected and synchronized session to simplify
scripting. Most required packages are imported as well to minimize typing.


Global Variables
~~~~~~~~~~~~~~~~

=============== ================================ =====================
Variable        Type                             Notes
=============== ================================ =====================
session         org.netxms.client.NXCSession
s               org.netxms.client.NXCSession     Alias for "session"
=============== ================================ =====================

Helper Functions
~~~~~~~~~~~~~~~~

Example
~~~~~~~

More examples can be found on a
`NetXMS wiki <https://wiki.netxms.org/wiki/Using_nxshell_to_automate_bulk_operations>`_.

.. code-block:: python

  parentId = objects.GenericObject.SERVICEROOT # Infrastructure Services root
  cd = NXCObjectCreationData(objects.GenericObject.OBJECT_CONTAINER, "Sample Container", parentId);
  containerId = session.createObject(cd) # createObject return ID of newly created object
  print '"Sample Container" created, id=%d' % (containerId, )

  flags = NXCObjectCreationData.CF_DISABLE_ICMP | \
          NXCObjectCreationData.CF_DISABLE_NXCP | \
          NXCObjectCreationData.CF_DISABLE_SNMP
  for i in xrange(0, 5):
      name = "Node %d" % (i + 1, )
      cd = NXCObjectCreationData(objects.GenericObject.OBJECT_NODE, name, containerId);
      cd.setCreationFlags(flags);
      cd.setPrimaryName("0.0.0.0") # Create node without IP address
      nodeId = session.createObject(cd)
      print '"%s" created, id=%d' % (name, nodeId)
