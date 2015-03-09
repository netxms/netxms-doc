.. _visualisation:


##############################
Data and Network visualisation
##############################


Network maps
============

Network map objects can be found in "Object browser" under "Network Maps". There can be 
created and deleted maps and map groups. Maps can be organized in groups. 

.. figure:: _images/Network_maps_in_object_browser.png

Creating Maps
-------------

There are 3 types of map that can be created:
   * Custom - will be created empty map.
   * Layer 2 Topology - will create map(if possible) with layer 2 topology of selected object.
   * IP Topology - will create map with known IP Topology of selected object. (More about network topology can be found there :ref:`topology`)
  

Type of created map affects only on initial map setup.

Edit Maps
---------
   
.. figure:: _images/network_map_menu.png

Adding Objects
--------------

Objects to map can be added in tow ways:
   1. Just drag and drop object to map from object browser.
   2. "Add object..." from menu. 

To remove object from map:
   * Select object, right click and select "Remove from map" option.

Adding Links between Objects
----------------------------

Objects can be linked with a line. 


To link objects:
   * Select two of objects with help of CTRL button and press "Link selected objects" button. 

.. figure:: _images/network_map_top_menue.png

To remove the link:
   * Select line, right click and select "Remove from map" option.


**Link properties:**

Select line, right click and select "Properties".


There can be configured:
   * Line name
   * Line comments shown near each connected object
   * Line colour 
      * Default - grey
      * Based on object status - object should be selected
      * Custom colour
   * Routing algorithm
      * Map Default - will be taken default selection for whole map
      * Direct - straight line without bend points
      * Manhattan - line with automatic bend points
      * Bend points - bend point can be done manually with double click on the line (can be used to do dual link)
   * Data Source(there can be configured DCI values and text near them that will be displayed on a link)
      * For each Data Source can be configured: Data collection item,  name,  java format string(like "Text: %.4f", syntax http://docs.oracle.com/javase/7/docs/api/java/util/Formatter.html#syntax),  in case of table DCI also column and instance
       
Example of DCI data displayed on a link:

.. figure:: _images/link_dci_data.png

Decorations
-----------

To map can be added also decorations like picture and group box. 
To add picture it should be uploaded to "Image Library" before. 


Creating group box you should specify it's size, colour and name. 


.. figure:: _images/network_map_decorations.png


DCI Container
-------------
DCI Container is part of decorations. It can be used to display separate dci values 
on a map.

.. figure:: _images/dci_container_example.png

**Container properties:**

   * Background colour 
   * Text colour
   * If border should be shown and it's colour
   * Data Source - there can be configured DCI values and text near them that will be displayed
      * For each Data Source can be configured: Data collection item,  name,  format string(like "Text: %.4f"),  in case of table DCI also column and instance

More examples: 

.. figure:: _images/dci_container_example2.png


DCI Image
---------
DCI Image is part of decorations. It can be used to display DCI status change in pictures.


**DCI image properties**
   * Data source - DCI witch data will be taken to process picture display rules
   * Column - required only for table DCI
   * Instance - required only for table DCI
   * Default image - image that will be displayed if no rule is applicable on current value
   * Rules 
      * For each rule can be configured: operation,  value,  comment and image that will be displayed if this rule is applicable

Hints:

To use image it should be first uploaded to image library. 


Rules are processed from up to down, so if you want to describe in rules 
something like: 

   * DCI > 3 => image1
   * DCI > 2 => image2
   * DCI > 4 => image3

They should go in this sequence:   

   * DCI > 4 => image3
   * DCI > 3 => image1
   * DCI > 2 => image2


Object Layout and display options
---------------------------------
All object layout properties and display options are applicable only on objects, 
not on decorations.


Grid
~~~~
   * Align to grid - will move all objects to grids 
   * Snap to grid - all objects will be moved in grids and it will not be possible to place them not inside grid. 
   * Show grid - will show grid according to which objects are located. 

.. figure:: _images/network_map_top_menue.png


Layout
~~~~~~
Objects can be placed manually on a map or can be chosen one of automatic layouts:
   * Spring
   * Radial
   * Horizontal tree
   * Vertical tree
   * Sparse vertical tree


If there is chosen automatic layout, then after each refresh object best matching place
will be recalculated. So if new object is add - it is just required to refresh map to have 
correctly placed objects. 


If there is chosen manual layout, then after each object movement map should be saved, 
to save the new place of object. 


Object status
~~~~~~~~~~~~~
   * Show status background - will display background behind object image according to it's state.
   * Show status icon - will display icon of object state near each object
   * Show status frame - will display frame around object icon according to it's state


Routing
~~~~~~~
Default routing type for whole map:
   * Direct
   * Manhattan


Zoom
~~~~
Map can be zoomed in and out with help of top menu buttons and 
to predefined percentage selected from menu. 


Object display options
~~~~~~~~~~~~~~~~~~~~~~
Objects can be displayed in 3 ways:
   * Icons
   * Small labels
   * Large labels


Map Background
--------------
It can be set background for map:
   * Colour
   * Image - image should be uploaded to "Image Library" before. 
   * Geographic Map - place on map is chose with help of zoom and coordinates


This can be used to show object physical please on map or on building plan. 

Examples: 

.. figure:: _images/networkmap_geomap.png
   :scale: 65%



Dashboards
==========


Graphs
======

You can view collected data in a graphical form, as a line chart. To view
values of some DCI as a chart, first open either :guilabel:`Data Collection`
Editor or :guilabel:`Last Values` view for a host. You can do it from the
:guilabel:`Object Browser` or map by selection host, right-clicking on it, and
selecting :guilabel:`Data collection` or :guilabel:`Last DCI values`. Then,
select one or more DCIs (you can put up to 16 DCIs on one graph), right-click
on them and choose :guilabel:`Graph` from the pop-up menu. You will see
graphical representation of DCI values for the last hour.

When the graph is open, you can do various tasks:

Select different time interval
------------------------------

By default, you will see data for the last hour. You can select different time
interval in two ways:

#. Select new time interval from presets, by right-clicking on the graph, and
   then selecting :guilabel:`Presets` and appropriate time interval from the
   pop-up menu.
#. Set time interval in graph properties dialog. To access graph properties,
   right-click on the graph, and then select :guilabel:`Properties` from the
   pop-up menu. Alternatively, you can use main application menu:
   :menuselection:`Graph --> Properties`. In the properties dialog, you will
   have two options: select exact time interval (like ``12/10/2005 from 10:00
   to 14:00``) or select time interval based on current time (like ``last two
   hours``).

Turn on automatic refresh
-------------------------

You can turn on automatic graph refresh at a given interval in graph properties
dialog. To access graph properties, right-click on it, and select
:guilabel:`Properties` from the pop-up menu. Alternatively, you can use main
application menu: :menuselection:`Graph --> Properties`. In the properties
dialog, select the :guilabel:`Refresh automatically` checkbox and enter a
desired refresh interval in seconds in edit box below. When automatic refresh
is on, you will see :guilabel:`Autoupdate` message in the status bar of graph
window.


Change colors
-------------

You can change colors used to paint lines and graph elements in the graph
properties dialog. To access graph properties, right-click on it, and select
:guilabel:`Properties` from the pop-up menu. Alternatively, you can use main
application menu: :menuselection:`Graph --> Properties`. In the properties
dialog, click on colored box for appropriate element to choose different color.


Save current settings as predefined graph
-----------------------------------------

You can save current graph settings as predefined graph to allow quick and easy
access in the future to information presented on graph. Preconfigured graphs
can be used either by you or by other NetXMS users, depending on settings. To
save current graph configuration as predefined graph, select :guilabel:`Save`
as predefined from graph view menu. The following dialog will appear:

.. figure:: _images/define_graph.png

In :guilabel:`Graph name` field, enter desired name for your predefined graph.
It will appear in predefined graph tree exactly as written here. You can use
``->`` character pair to create subtree. For example, if you name your graph
``NetXMS Server->System->CPU utilization (iowait)`` it will appear in the tree
as following:

.. figure:: _images/predefined_graph_tree.png

You can edit predefined graph by right-clicking on it in predefined graph tree,
and selecting :guilabel:`Properties` from context menu. On
:guilabel:`Predefined Graph` property page you can add users and groups who
will have access to this graph. Note that user creating the graph will always
have full access to it, even if he is not in access list.

If you need to delete predefined graph, you can do it by right-clicking on it
in predefined graph tree, and selecting :guilabel:`Delete` from context menu.

History
=======

You can view collected data in a textual form, as a table with two columns -
:guilabel:`timestamp` and :guilabel:`value`. To view values of some DCI as a
table, first open either :guilabel:`Data Collection Editor` or :guilabel:`Last
Values` view for a host. You can do it from the :guilabel:`Object Browser` or
map by selection host, right-clicking on it, and selecting :guilabel:`Data
collection` or :guilabel:`Last DCI values`. Then, select one or more DCIs (each
DCI data will be shown in separate view), right-click on them and choose
:guilabel:`Show history` from the pop-up menu. You will see the last 1000
values of the DCI.

.. todo:: Export DCI data


.. _dci-summary-table-label:

Summary table
=============

It is possible to see DCI data as a table where each line is one node and each 
column is a DCI. It can be configured for each summary table witch DCIs should be 
present on it. 

.. figure:: _images/summary_table.png

Configuration
-------------

DCI summary table can be configured in Configuration -> Summary Table. 

.. figure:: _images/configure_dci_summary_table.png
   :scale: 65%

In general part:

  - Menu path - path where this summary table can be found. You can use
    ``->`` character pair to create subtree like "Linux->System information".
  - Title - title of view.
  
In columns part:

  - There are added DCI's shat should be shown on the summary table. Where 
    Name is name of column and DCI Name is parameter of DCI. 

Usage
-----

After DCI summary table is configured it can be accessed in container 
object(Subnet, container...) menu under "Summary tables". 

