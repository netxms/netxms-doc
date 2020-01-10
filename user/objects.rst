.. _objects:


#################
Object management
#################

Object browser
==============

:guilabel:`Object browser` organize all existing :term:`objects <Object>` in
hierarchical structure. |product_name| has eight top level objects – Entire Network,
Service Root, Template Root, Policy Root, Network Map Root, Dashboard Root,
Report Root, and Business Service Root. These objects served as an abstract
root for appropriate object tree. All top level objects has only one editable
attribute – name.

Overall description about objects can be found in concepts part: :ref:`concept_object`.

Properties
----------

Object browser has next options:
 - Show filter :kbd:`CTRL+F2`, that shows search line that has special syntaxes
   for search. Syntaxes description can be found there: :ref:`object_browser_filters`.
 - Show status indicator :kbd:`CTRL+F3`
 - Hide unmanaged objects
 - Hide check templates. This option will not show :guilabel:`Business Services`
   templates.


.. _object_browser_filters:

Filters
-------

Buy default search is done by node name. In this type of search can be used
'*' and '?' symbols for pattern search.

But there are few prefix that can be used for other search options:
 - '/' - will search in comments
 - '>' - will search by IP address

Objects
=======

Detailed information about objects, it's usage, parents and childes can be found in
concept chapter, :ref:`concept_object`. In this section will be described only actions and
properties that can be applied on different object classes.

Next chapters will describe

Subnet
------

Menu items:

Full subnet can be managed or unamanged. Management status will be applied to all subnet node.
If subnet is deleted and is the only parent of a node, then node also will be deleted with
the subnet. :guilabel:`Upload file` menu item will upload file from server to all nodes
that have agent and have access to upload directory.

Under :guilabel:`Tools` menu are available predefined object tools that will be
executed on each subnet node. More about object tool configuration can be found
there: :ref:`object_tools`.

:guilabel:`Alarms` menu item will open view with all subnet nodes' alarms. And
:guilabel:`802.1x port state` will open table with port authentication states, that can be
exported to CSV.

Node
----

Menu items:

When node is unmanaged/managed - all it's childes like interfaces and service monitoring
are also unmanaged/managed. In unmanaged state :term:`metrics <Metric>` are not
collected and no pols are scheduled.

If zones are enabled, then zone can be changed using :guilabel:`Change zone...` item.
:guilabel:`File manager` will open agent file manager view.
:guilabel:`Upload file` can be used to upload file from server to node. This action can be
applied simultaneously to all nodes.

:guilabel:`Take screenshot` for now halfway implemented functionality. For now screenshot can
be taken only from Windows machines.

Poll options:


.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Poll Name
     - Description
   * - Status
     -
   * - Configuration
     -
   * - Configuration (full)
     -
   * - Instance discovery
     -
   * - Instance names
     -
   * - Topology
     -

Under :guilabel:`Tools` menu are available predefined object tools that will be
executed on selected node. More about object tool configuration can be found
there: :ref:`object_tools`.

If geolocation of the node is set, then with help of :guilabel:`Geolocation` item can be
opened map with shown on it object location. :guilabel:`Software Inventory` will show
full software list for nodes with Windows systems or Linux systems(that used rpn or deb
packages) and have |product_name| agent installed. :guilabel:`Service Dependency` will build
tree from this node with all container where this node is included. :guilabel:`Alarms`
will open alarm view with alarms only for this specific node.

:guilabel:`Find switch port` will open view with log of searchs of switch port that
with which this node is connected. Wile search we will check one by one interfaces
and will show first successful result.

:guilabel:`802.1x port state` will open table with port authentication states, that can be
exported to CSV.

:guilabel:`Topology` menu item contains all options of predefined network maps for this
node and some other options:

:guilabel:`Routing table`
:guilabel:`IP route from...` will build network map with route form selected node to
node that is selected form Object selector window.
:guilabel:`IP route to...` will build network map with route to selected node from
node that is selected form Object selector window.
:guilabel:`IP Neighbors` will show all IP neighbors of this node.

:guilabel:`Switch forwarding database(MAC address table)`
:guilabel:`VLANs`
:guilabel:`Layer 2 Topology`

:guilabel:`Radio interface`
:guilabel:`Wirless stations`

:guilabel:`Last values` will open :ref:`Last Values view<last-values>`.

Mobile Device
-------------

Menu items:

Each phone object can be managed/unmanaged and deleted. In umnanaged state
:term:`metrics <Metric>` of this device are not collected and no pols are scheduled.
When mobile object is deleted all it's data is also deleted. No history data will
be left.

:guilabel:`Geolocation History` will open view were will be shown history of displacement
of this device. From the menu can be selected the period to show on history map.
:guilabel:`Geolocation` will show last known location of this device.
:guilabel:`Alarms` menu item will open view with all subnet nodes' alarms.

:guilabel:`Last values` will open :ref:`Last Values view<last-values>`.

Rack
----

Cluster
-------

Intrface
--------

Network Service
---------------

VPN Connector
-------------


Condition
---------

Conditions may represent more complicated status checks because each condition can have a script attached.
Interval for evaluation of condition status is configured in Server Configuration Variables as
ConditionPollingInterval with default value 60 seconds. Input values for the condition script
can be set in object properties. Such values are accessible via $1, $2, ... variables inside the
script. If the script returns 0, an activation event with the defined severity is created.
If the script returns any other value, then a deactivation event is created.

Menu items:

Condition can be manged\unmanaged. If condition is unmanaged, evaluation of condition is
not run. Condition can be deleted.

Container
---------

Containers can be created in Infrastructure Services tree. Existing nodes and
subnets can be added to containers by using Bind operation, and removed by using
Unbind operation. New nodes, conditions, clusters, containers, mobile devices and racks can also
be created. They can be created using required menu item of container under which this object should
appear. Containers and nodes inside them can be moved by :guilabel:`Move to another container` menu
item or using drag&drop.

Menu items:

There are special menu item for each object that can be created in container. Objects
like rack, container, mobile device, cluster are manually created objects. Node can be
manually created or found by network discovery. In case if it is required to add
already existing object to container use :guilabel:`Bind...` menu item. To remove node
from container, but do not delete it use :guilabel:`Unbind...` menu item.

Using :guilabel:`Manage`/:guilabel:`Unmanage` all nodes will be managed/unmanaged under
container. Container can be deleted. If deleted container was the only one parent of
the object, then this object will be also deleted. :guilabel:`Upload file...` will
upload file from server to all nodes under container, same as each tool under
:guilabel:`Tools` menu item will be executed on each node.

:guilabel:`Geolocation` will show location of container on geographic map.

:guilabel:`Alarms` will open alarm view with all active alarms for all children of this
container.
:guilabel:`802.1x port state` will open table with port authentication states of all
devices that are under this container. This information can be exported to CSV.


Object Details
==============

Object details view provides main information about object. Each object has
:guilabel:`Overview` tab that gisplays general information about object
(like: ID, GUID, Class, and status of the object) and :guilabel:`Comments`.

Subnet
------


.. _object_tools:

Object Tools
============

There can be created tools that will be executed on objects. Tools are shown under
"Tools" item of node menu. There are some pre defined object tools, but they can be
disabled or configured new by |product_name| administrator.

.. _last-values:

Last DCI values View
====================
