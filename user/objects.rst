.. _objects:


#################
Object management
#################


Objects
=======

Detailed information about objects, it's usage, parents and children can be
found in concept chapter, :ref:`concept_object`. In this section will be
described only actions and properties that can be applied on different object
classes.


Node context menu
-----------------

Many of menu items described here are also available on other types of objects -
sensors, collectors, racks, access points, etc. 

When node is unmanaged/managed - all it's children like interfaces and service
monitoring are also unmanaged/managed. In unmanaged state :term:`metrics
<Metric>` are not collected and no pols are scheduled.

Node's zone can be changed using :guilabel:`Change zone...` menu item.
:guilabel:`File manager` will open agent file manager view. :guilabel:`Upload
file` can be used to upload file from server to node. This action can be applied
simultaneously to multiple nodes.

:guilabel:`Remote control` allows to access remote node via VNC.

:guilabel:`Take screenshot` takes screenshot. Requires |product_name| agent to
be installed on the node. Currently screenshot can be taken only from Windows
machines.

:guilabel:`Poll` menu contains a list of available polls that can be performed
on a node. The following options are available: 


.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Poll Name
     - Description
   * - Status
     - Determine current status of an object
   * - Configuration
     - Determine current configuration of an object (list of interfaces,
       supported protocols, etc.) By default executes auto bind scripts for
       templates and containers, use "Objects.AutobindOnConfigurationPoll"
       server configuration variable to disable.
   * - Configuration (full)
     - Same as usual configuration poll but resets previously detected
       capabilities and detects them again. (can only be executed manually)
   * - Instance discovery
     - Perform Instance Discovery to add/remove DCIs
   * - Topology
     - Gather information related to network link layer topology

Under :guilabel:`Tools` menu are available predefined object tools that will be
executed on selected node. More about object tool configuration can be found
there: :ref:`object_tools`.

:guilabel:`Logs` menu provides access available logs.

:guilabel:`Execute script...` opens NXSL (built-in scripting language) execution
view.

:guilabel:`Topology maps` menu gives options to build adhoc topology maps based
on Layer 2, IP and Internal Connection topology. 

:guilabel:`Route to...` will build network map with route to selected node from
node that is selected from Object selector window.

:guilabel:`Route from...` will build network map with route from selected node to
node that is selected from Object selector window.

:guilabel:`Route from NetXMS Server` will build network map with route from
|product_name| server to selected node.

:guilabel:`MIB Explorer` (available only on SNMP-capable nodes) opens MIB
explorer view that allows walking SNMP OIDs and reading information from MIB
files. 

:guilabel:`Change zone...` allows to change zone of selected node.


Subnet, Container and Collector context menu
--------------------------------------------

Some actions, performed on objects, whose children are nodes (sensors, access
points, etc) are executed on these nodes and not on object where it was called.
These actions are:

:guilabel:`Manage` / :guilabel:`Unmanage`. Management status will be applied to
all nodes under subnet or container. 

:guilabel:`Upload file` menu item will upload file from server to all nodes that
have agent.

Under :guilabel:`Tools` menu are available predefined object tools that will be
executed on each subnet node. More about object tool configuration can be found
there: :ref:`object_tools`.

:guilabel:`Alarms` menu item will open view with all subnet nodes' alarms. 


If subnet or container is deleted and is the only parent of a node, then node
also will be deleted with the subnet. 


Condition
---------

Conditions may represent more complicated status checks because each condition
can have a script attached. Interval for evaluation of condition status is
configured in Server Configuration Variables as ConditionPollingInterval with
default value 60 seconds. Input values for the condition script can be set in
object properties. Such values are accessible via $1, $2, ... variables inside
the script. If the script returns 0, an activation event with the defined
severity is created. If the script returns any other value, then a deactivation
event is created.

Condition can be manged/unmanaged. If condition is unmanaged, evaluation of
condition is not executed. 


Container
---------

Everything described in this chapter is also related to collectors, which are
basically containers with data collection capabilities. 

Containers can be created in Infrastructure Services tree. Existing nodes and
subnets can be added to containers by using Bind operation, and removed by using
Unbind operation. New nodes, conditions, clusters, containers, collectors,
sensors and racks can also be created. They can be created using required menu
item of container under which this object should appear. Containers and nodes
inside them can be moved by :guilabel:`Move to another container` menu item or
using drag&drop.

Menu items:

There are special menu item for each object that can be created in container. Objects
like rack, container, mobile device, cluster are manually created objects. Node can be
manually created or found by network discovery. In case if it is required to add
already existing object to container use :guilabel:`Bind...` menu item. To remove node
from container, but do not delete it use :guilabel:`Unbind...` menu item.


.. _object_tools:

Object Tools
============

Object tools are configured in |product_name| settings for executed on objects.
Tools are shown under "Tools" item of node menu. There are some pre defined
object tools, they can be disabled and new ones can be configured by
|product_name| administrator.
