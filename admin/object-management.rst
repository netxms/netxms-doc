.. _object-management:


#################
Object management
#################

For object type description refer to :ref:`concept_object` chapter. 

Object browser
==============

NetXMS has eight top level objects – Entire Network, Service Root, 
Template Root, Policy Root, Network Map Root, Dashboard Root, Report Root, 
and Business Service Root. These objects served as an abstract root for 
appropriate object tree. All top level objects has only one editable 
attribute – name.

Add / remove objects
====================


Containers – bind/unbind
========================

Containers can be created in Infrastructure Services tree. Existing nodes and 
subnets can be added to containers by using Bind operation, and removed by using 
Unbind operation.


Automatic bind option
---------------------

For each container can be configured automatic binding rules. This can be in 
:guilabel:`Automatic Bind Rules` tab of container properties. 

..figure:: _images/automatic_bind_rules.png

There can be defined if script should be used for automatic binding, if script
should be used for node unbinding and can be written script it selves. 

This script will be executed each configuration poll of each node. 

Access control
==============

.. _object_tools:

Object Tools
============

There can be created tools that will be executed on objects. Tools can be managed
in "Object Tools" view. Tools are shown under "Tools" item of node menu.
There are some predefined object tools:

.. figure:: _images/object_tools.png
   :scale: 65%

If object tool should be removed for some time it can be just disabled and then 
enabled when required. When object tool is disabled it is not shown under "Tools"
item of node menu. 


Internal
--------


Action
------


SNMP Table
----------


Agent Table
-----------


URL
---


Local Command
-------------


Server Command
--------------


Download File
-------------


"Download file" tool can be used to monitor agent logs. This tool will retrieve 
the content of the file from agent. 

.. figure:: _images/get_agent_file_properties.png
   :scale: 65%
   
|   
   
.. list-table::
   :widths: 30 70
   :header-rows: 1
 
   * - Field name
     - Description
   * - Name
     - Name that will be shown in node menu.
   * - Description
     - Description is shown in "Object Tools" view. Should be used to describe tool purpose.
   * - Remote File Name
     - Name of file that will be retrieved. In Windows systems should be with double back slash as a separator(C:\\\\log\\\\log.log).     
   * - Limit initial download size
     - Limits the size of download file. If is set not to 500 tool will retrieve last 500 bytes of requested file. If is set to 0,  then will retrieve full file.
   * - Follow file changes
     - If chosen, "File View" will be updated when file will be populated with new data. 
   * - This tool requires confirmation before execution 
     - If chosen, before execution of tool will be shown Yes/No pop-up with text from "Confirmation message" field.
   * - Confirmation message
     - Can be set the message that will be shown in confirmation pop-up. 
   * - Disable Object Tool
     - If chosen, tool it is not shown in node menu. 
     
     
Macro Substitution
------------------

Action, file download, local command, and URL tool types allows macro substitution. Any string enclosed into pair of percent signs considered macro name and is expanded.
The following macros recognized:

.. list-table::
   :widths: 30 70
   :header-rows: 1
 
   * - Name
     - Description
   * - OBJECT_ID
     - ID of selected node object.
   * - OBJECT_IP_ADDR
     - Primary IP address of selected node object.
   * - OBJECT_NAME
     - Name of selected node object.

If object tool called from alarm's pop-up menu the following additional macros are available:

.. list-table::
   :widths: 30 70
   :header-rows: 1
 
   * - Name
     - Description
   * - ALARM_ID
     - ID of selected alarm.
   * - ALARM_MESSAGE
     - Message text of the alarm.
   * - ALARM_SEVERITY
     - Alarm severity as a number.
   * - ALARM_SEVERITY_TEXT
     - Alarm severity as text.
   * - ALARM_STATE
     - Alarm state code (0 for outstanding, 1 for acknowledged, 2 for resolved).
          
For any unknown macro name system will try to read custom attribute with given name (attribute search is case sensitive). If attribute with given name not found,
empty string will be inserted.




Custom attributes
=================

Every object can have custom attributes defined either by user or integrated application 
via NetXMS API. Custom attributes distinguished by names (an attribute name can contain up 
to 127 printable characters), and have string values of unlimited length. However, if you wish 
to access custom attributes in :term:`NXSL` scripts as properties of node object, you should name them 
conforming to NXSL identifier naming constraints. To create or change value of custom attribute 
manually, right-click object in NetXMS console, and select :menuselection:`Properties --> Custom Attributes tab`.

Condition
=========

Conditions may represent more complicated status checks because each condition can have a script attached. 
Interval for evaluation of condition status is configured in Server Configuration Variables as 
ConditionPollingInterval with default value 60 seconds. Input values for the condition script 
can be set in object properties. Such values are accessible via $1, $2, ... variables inside the 
script. If the script returns 0, an activation event with the defined severity is created. 
If the script returns any other value, then a deactivation event is created.
