.. _visualisation:


##############################
Data and Network visualisation
##############################


Network maps
============


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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~~~~~~~~~~~~~

You can turn on automatic graph refresh at a given interval in graph properties
dialog. To access graph properties, right-click on it, and select
:guilabel:`Properties` from the pop-up menu. Alternatively, you can use main
application menu: :menuselection:`Graph --> Properties`. In the properties
dialog, select the :guilabel:`Refresh automatically` checkbox and enter a
desired refresh interval in seconds in edit box below. When automatic refresh
is on, you will see :guilabel:`Autoupdate` message in the status bar of graph
window.


Change colors
~~~~~~~~~~~~~

You can change colors used to paint lines and graph elements in the graph
properties dialog. To access graph properties, right-click on it, and select
:guilabel:`Properties` from the pop-up menu. Alternatively, you can use main
application menu: :menuselection:`Graph --> Properties`. In the properties
dialog, click on colored box for appropriate element to choose different color.


Save current settings as predefined graph
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
~~~~~~~~~~~~~

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
~~~~~

After DCI summary table is configured it can be accessed in container 
object(Subnet, container...) menu under "Summary tables". 

