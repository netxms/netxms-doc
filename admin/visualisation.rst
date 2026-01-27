.. _visualisation:


##############################
Data and Network visualisation
##############################

.. _network_map:

Network Maps
============

Network maps provide graphical visualization of your network infrastructure,
showing objects, their relationships, and current status. Maps can be created
manually with custom layouts or generated automatically from topology data.

To access network maps:

1. Switch to the :guilabel:`Maps` perspective using the perspective switcher
   or menu :menuselection:`Window --> Open Perspective --> Maps`.

2. In the :guilabel:`Object Browser` panel, expand :guilabel:`Network Maps`
   to see all available maps and map groups.

.. figure:: _images/network-maps/Network_maps_in_object_browser.png

   Network maps in Object Browser


Map Types Overview
------------------

|product_name| supports six types of network maps:

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - Type
     - Description
     - Auto-updates
   * - Custom
     - User-defined map with manual object placement
     - No
   * - Layer 2 Topology
     - Switching/bridging topology based on MAC tables
     - Yes
   * - IP Topology
     - IP routing topology from routing tables
     - Yes
   * - Internal Communication
     - Agent/proxy connections to management server
     - Yes
   * - OSPF Topology
     - OSPF routing domain topology
     - Yes
   * - Hybrid Topology
     - Combined L2/IP/OSPF in single map
     - Yes


.. _netmap-creating:

Creating Maps
-------------

1. In Object Browser, right-click :guilabel:`Network Maps` or a map group.

2. Select :guilabel:`Create network map`.

3. Enter a name and select the map type:

   - **Custom**: Empty map for manual creation
   - **Layer 2 Topology**: Auto-generated from L2 switching data
   - **IP Topology**: Auto-generated from routing tables
   - **Internal Communication Topology**: Shows agent/proxy connections
   - **OSPF Topology**: Shows OSPF routing relationships
   - **Hybrid Topology**: Combines L2, IP, and OSPF data

4. For automatic topology maps, select the initial seed object in the dialog.

5. Optionally, select an existing map as a template in the :guilabel:`Template network map`
   field. The template provides initial configuration for the new map including:

   - Map settings (background, size, display mode)
   - Link defaults (routing, color, width, style)
   - Filter and link styling scripts
   - Discovery radius
   - Decoration elements (group boxes, images)
   - Text box elements

   Object elements and links are not copied from the template.

.. figure:: _images/network-maps/create-map-dialog.png

   Create Network Map dialog showing all map types

.. figure:: _images/network-maps/l2-topology-seed-selection.png

   Seed object selection for topology map

6. Click :guilabel:`OK`.

.. note::

   :guilabel:`IP Topology` maps are recommended for getting started as they
   work with standard routing information available on most devices.
   :guilabel:`Layer 2 Topology` maps require specific protocol support (LLDP,
   CDP, STP) which may not be available or enabled on all network equipment.


Seed Objects and Discovery Radius
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For automatic topology maps, seed objects define the starting points for
topology discovery. The first seed object is selected when creating the map.
Additional seed objects can be added in map properties:

1. Open map properties (right-click map > :guilabel:`Properties`).

2. Go to the :guilabel:`Seed Nodes` page and click :guilabel:`Add` to add
   more seed objects.

.. figure:: _images/network-maps/networkmap-seed-nodes-propertypage.png

   Map properties dialog - Seed Nodes page

3. Go to the :guilabel:`Map Options` page to configure discovery radius:

   - 0 = show seed and directly connected objects only
   - Higher values = include objects further away

.. figure:: _images/network-maps/map-properties-map-options.png

   Map properties dialog - Map Options page

4. Click :guilabel:`OK`.

The map automatically populates with discovered topology and updates when
the network changes.

.. figure:: _images/network-maps/l2-topology-result.png

   Generated L2 topology map showing discovered nodes and links


.. _netmap-editing:

Editing Maps
------------

.. figure:: _images/network-maps/network_map_menu.png

   Map context menu


Adding Objects
~~~~~~~~~~~~~~

Network maps can be populated automatically or manually. Layer 2, IP Topology,
OSPF, Hybrid, and Internal Communication topology maps are populated automatically.

**To add objects manually:**

- **Drag and drop**: Drag objects from Object Browser onto the map
- **Menu**: Right-click on map > :guilabel:`Add object...` > select object

To use drag and drop, the map editor must be accessible while viewing network
objects. Either:

- Pop out or pin the map editor window, then switch to :guilabel:`Network` or
  :guilabel:`Infrastructure` perspective where objects are located, or
- Use the :guilabel:`Add object...` menu option which works from any perspective

.. figure:: _images/network-maps/drag-drop-object.png

   Dragging a node from Object Browser onto a map

**To remove objects:**

- Select object, right-click > :guilabel:`Remove from map`

.. figure:: _images/network-maps/map-with-nodes.png

   Custom map with connected nodes


Adding Links Between Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Objects can be linked with a line.

**To create links:**

1. Hold :kbd:`Ctrl` and click two objects to select them.

.. figure:: _images/network-maps/link-two-objects.png

   Two objects selected before linking

2. Click :guilabel:`Link selected objects` in toolbar, or right-click >
   :guilabel:`Link selected objects`.

.. figure:: _images/network-maps/link-button-toolbar.png

   Toolbar with Link selected objects button

**To remove links:**

- Select the link, right-click > :guilabel:`Remove from map`


Link Properties
~~~~~~~~~~~~~~~

Select a link, right-click and select :guilabel:`Properties` to configure:

.. figure:: _images/network-maps/link-properties-dialog.png

   Link properties dialog

- **Link name**: Label displayed on the link
- **Connector names**: Labels shown near each connected object
- **Line color**:

  - Default - uses map default color
  - Based on object status - color reflects selected object(s) status
  - Custom color - user-defined static color
  - Script - determined by NXSL script
  - Link utilization - based on interface bandwidth usage

.. figure:: _images/network-maps/link-color-source.png

   Link color source options

- **Routing algorithm**:

  - Map Default - uses map setting
  - Direct - straight line
  - Manhattan - grid-based with right angles
  - Bend points - manual routing (double-click line to add points)

.. figure:: _images/network-maps/link-routing-bendpoints.png

   Link with manual bend points

- **Label position**: Position of link name and DCI values (50 = middle)

- **Data Source**: Configure DCI values to display on the link

.. figure:: _images/network-maps/link-dci-datasource-config.png

   Link data source configuration

**Data Source Configuration:**

For each data source, configure:

- Data collection item
- Name (label prefix)
- Format string
- For table DCIs: column and instance

If format string is not provided, default formatting with multipliers and
measurement units is used.

Format string syntax follows Java Formatter specification. Example: ``Text: %.4f``

Additional format specifiers in curly brackets after ``%``:

- ``units`` or ``u`` - add measurement units from DCI properties
- ``multipliers`` or ``m`` - display with SI multipliers (e.g., 1230000 becomes 1.23 M)
- Combined: ``%{units,multipliers}f`` or ``%{u,m}f``

.. figure:: _images/network-maps/link_dci_data.png

   Example of DCI data displayed on a link


.. _netmap-decorations:

Decorations
-----------

Decorations like pictures and group boxes can be added to maps.

.. figure:: _images/network-maps/network_map_decorations.png

   Map decorations example


Group Boxes
~~~~~~~~~~~

Group boxes visually organize related objects.

1. Right-click on the map canvas.

2. Select :guilabel:`Add decoration` > :guilabel:`Group box`.

3. Configure: title, color, and size.

.. figure:: _images/network-maps/group-box-creation.png

   Group box properties dialog

4. Position behind objects you want to group.


Images
~~~~~~

To add an image, first upload it to the :ref:`image-library`, then:

1. Right-click on the map canvas.

2. Select :guilabel:`Add decoration` > :guilabel:`Image`.

3. Select the image from the library.


.. _netmap-dci-container:

DCI Container
-------------

DCI Container displays live DCI values on a map.

.. figure:: _images/network-maps/dci_container_example.png

   DCI Container example

**To add a DCI Container:**

1. Right-click on the map canvas.

2. Select :guilabel:`Add DCI container`.

3. Configure appearance:

   - Background color
   - Text color
   - Border (optional) and border color

4. Add data sources:

   - Click :guilabel:`Add`
   - Select node and DCI
   - Configure name and format string (e.g., ``Text: %.4f`` or ``%{u,m}f``)
   - For table DCIs: specify column and instance

.. figure:: _images/network-maps/dci-container-on-map.png

   DCI Container showing live metrics on map

.. figure:: _images/network-maps/dci_container_example2.png

   More DCI Container examples


.. _netmap-dci-image:

DCI Image
---------

DCI Image displays different images based on DCI values, useful for conditional
status indicators.

**To add a DCI Image:**

1. Right-click on the map canvas.

2. Select :guilabel:`Add DCI image`.

3. Configure:

   - **Data source**: DCI to evaluate
   - **Column/Instance**: For table DCIs only
   - **Default image**: Shown when no rule matches

4. Add rules (click :guilabel:`Add`):

   - **Operation**: Comparison operator (>, <, =, etc.)
   - **Value**: Threshold value
   - **Image**: Image to display when rule matches
   - **Comment**: Optional description

.. figure:: _images/network-maps/dci-image-rules.png

   DCI Image rules configuration

**Important**: Rules are processed top to bottom. Order from most specific to
least specific.

**Example rule order for temperature:**

.. code-block:: none

   > 80  => critical.png    (checked first)
   > 60  => warning.png     (checked second)
   > 0   => normal.png      (checked third)


.. _netmap-text-box:

Text Box
--------

Text boxes display static text with optional drill-down navigation.

**To add a Text Box:**

1. Right-click on the map canvas.

2. Select :guilabel:`Add text box`.

3. Configure:

   - **Text**: Content to display
   - **Font size**: Text size
   - **Colors**: Text and background colors
   - **Drill-down object**: Optional target for click navigation

.. figure:: _images/network-maps/text-box-properties.png

   Text Box properties dialog

.. figure:: _images/network-maps/text-box-drilldown-config.png

   Text Box drill-down object selection


.. _netmap-layout:

Layout and Display Options
--------------------------

Layout and display options apply to objects, not decorations.


Map Size
~~~~~~~~

Map size defines the canvas dimensions for the network map. This is particularly
important for automatically layouted maps, as the layout algorithm uses these
dimensions to position objects.

To configure map size:

1. Open map properties (right-click map > :guilabel:`Properties`).

2. Go to the :guilabel:`Map Options` page.

3. Set :guilabel:`Width` and :guilabel:`Height` values in pixels.

For automatic topology maps, larger dimensions provide more space for the layout
algorithm to spread objects, resulting in less cluttered visualization.


Grid
~~~~

- **Align to grid**: Move all objects to grid positions
- **Snap to grid**: Constrain object movement to grid
- **Show grid**: Display grid lines

.. figure:: _images/network-maps/network_map_top_menu.png

   Map toolbar


Layout Algorithms
~~~~~~~~~~~~~~~~~

Objects can be positioned manually or using automatic layouts:

- **Manual**: No automatic positioning (default for Custom maps)
- **Spring**: Force-directed layout
- **Radial**: Circular arrangement from center
- **Horizontal tree**: Left-to-right hierarchy
- **Vertical tree**: Top-to-bottom hierarchy
- **Sparse vertical tree**: Vertical tree with more spacing

.. figure:: _images/network-maps/layout-algorithms-menu.png

   Layout algorithm selection menu

With automatic layout, positions recalculate on each refresh. With manual
layout, save the map after moving objects.


Display Options
~~~~~~~~~~~~~~~

- **Show status background**: Colored background based on object status
- **Show status icon**: Status icon overlay on objects
- **Show status frame**: Colored frame around objects based on status
- **Floor plan**: Objects as resizable rectangles for physical layout

.. figure:: _images/network-maps/status-display-options.png

   Display options menu with status settings

.. figure:: _images/network-maps/map-with-status-icons.png

   Map showing objects with status icons


Object Display Mode
~~~~~~~~~~~~~~~~~~~

Objects can be displayed as:

- Icons (default)
- Small labels
- Large labels
- Status icon
- Floor plan

.. figure:: _images/network-maps/display-modes-comparison-icons.png

   Display mode: Icons

.. figure:: _images/network-maps/display-modes-comparison-small-labels.png

   Display mode: Small Labels

.. figure:: _images/network-maps/display-modes-comparison-large-labels.png

   Display mode: Large Labels

.. figure:: _images/network-maps/display-modes-comparison-status-icon.png

   Display mode: Status Icon

.. figure:: _images/network-maps/display-modes-comparison-floor-plan.png

   Display mode: Floor Plan

.. figure:: _images/network-maps/floor-plan-mode.png

   Map in floor plan mode with resizable rectangles


Default Link Routing
~~~~~~~~~~~~~~~~~~~~

- **Direct**: Straight lines
- **Manhattan**: Grid-based with right angles


Zoom
~~~~

Map can be zoomed using toolbar buttons or selecting a percentage from the menu.


.. _netmap-public-access:

Public Access
-------------

When |product_name| WebUI is configured, network maps can be shared publicly
via a direct URL without requiring authentication. This is useful for displaying
maps on information screens or sharing with users who don't have system accounts.

**To enable public access:**

1. Right-click on a network map in Object Browser.

2. Select :guilabel:`Enable public access...`

3. A dialog appears with:

   - **Access token**: Unique token for this map's public access
   - **Direct access URL**: Full URL to access the map

4. Copy the URL and share it as needed.

The URL format is::

   {BaseURL}/nxmc-light.app?auto&kiosk-mode=true&token={token}&map={mapId}

The map will be displayed in kiosk mode without navigation elements, suitable
for dashboards and information displays.

.. note::

   Public access requires WebUI to be properly configured with a base URL.
   Each time you enable public access, a new token is generated.


.. _netmap-background:

Map Background
--------------

Background options:

- **Color**: Solid background color
- **Image**: Upload to :ref:`image-library` first, then select
- **Geographic Map**: Specify latitude, longitude, and zoom level

.. figure:: _images/network-maps/background-image-config.png

   Image background selection from Image Library

.. figure:: _images/network-maps/background-geomap-config.png

   Geographic map background configuration

Use backgrounds to show physical placement on floor plans or geographic locations.

.. figure:: _images/network-maps/networkmap_geomap.png

   Map with geographic background


.. _netmap-filter-script:

Object Filter Script
--------------------

Filter scripts control which objects appear on automatic topology maps.

1. Open map properties.

2. Go to the :guilabel:`Filter` tab.

.. figure:: _images/network-maps/map-properties-filter.png

   Map properties - Filter script configuration

3. Enter an NXSL script returning ``true`` (include) or ``false`` (exclude).

4. Enable :guilabel:`Filter objects` option.

**Context variables:**

- ``$object`` or ``$node``: Object being evaluated
- ``$map``: The NetworkMap object

**Example - include only nodes:**

.. code-block:: c

   return $object.isNode;

**Example - exclude nodes in maintenance:**

.. code-block:: c

   return !$node.isInMaintenanceMode;

**Example - include only specific subnet:**

.. code-block:: c

   if ($node.ipAddr.inSubnet("10.1.0.0", 16))
      return true;
   return false;


.. _netmap-link-styling-script:

Link Styling Script
-------------------

Link styling scripts dynamically modify link appearance during map updates.

1. Open map properties.

2. Go to the :guilabel:`Link Styling Script` section.

.. figure:: _images/network-maps/map-properties-link-styling.png

   Map properties - Link styling script configuration

3. Enter an NXSL script that modifies the ``$link`` object.

**Example - set link width based on bandwidth:**

.. code-block:: c

   iface = $link.interface1;
   if (iface != null) {
      speed = iface.speed;
      if (speed >= 10000000000)
         $link.setWidth(4);  // 10G+
      else if (speed >= 1000000000)
         $link.setWidth(3);  // 1G
      else
         $link.setWidth(2);  // Below 1G
   }

**Example - add interface descriptions as connector names:**

.. code-block:: c

   if ($link.interface1 != null)
      $link.setConnectorName1($link.interface1.description);
   if ($link.interface2 != null)
      $link.setConnectorName2($link.interface2.description);

For complete NXSL reference including all available methods and attributes for
``$link`` object, see `NetworkMapLink class <https://netxms.org/documentation/nxsl-latest/#class-networkmaplink>`_
in the NXSL documentation.


.. _netmap-reference:

Reference Tables
----------------


Map Types
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 55 10 10

   * - Type
     - Description
     - Auto-updates
     - Seed Required
   * - Custom
     - User-defined manual map
     - No
     - No
   * - Layer 2 Topology
     - Switching/bridging topology
     - Yes
     - Yes
   * - IP Topology
     - IP routing topology
     - Yes
     - Yes
   * - Internal Communication
     - Agent/proxy connections
     - Yes
     - Yes (auto)
   * - OSPF Topology
     - OSPF routing topology
     - Yes
     - Yes
   * - Hybrid Topology
     - Combined L2/IP/OSPF
     - Yes
     - Yes

.. figure:: _images/network-maps/ospf-topology-map.png

   OSPF topology map showing router relationships

.. figure:: _images/network-maps/hybrid-topology-map.png

   Hybrid topology map combining L2/IP/OSPF


Element Types
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Type
     - Description
   * - Object
     - Managed |product_name| object (node, interface, etc.)
   * - Decoration
     - Group box or static image
   * - DCI Container
     - Live DCI value display
   * - DCI Image
     - Dynamic image based on DCI value
   * - Text Box
     - Text annotation with optional drill-down

.. figure:: _images/network-maps/element-types-overview.png

   All element types shown on one map


Link Types
~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 25 55

   * - Type
     - Visual
     - Description
   * - Normal
     - Solid line
     - Standard connection
   * - VPN
     - Dashed
     - VPN tunnel
   * - Multilink
     - Double line
     - Aggregated links (LAG)
   * - Agent Tunnel
     - Red indicator
     - Agent tunnel connection
   * - Agent Proxy
     - Green indicator
     - Agent proxy
   * - SSH Proxy
     - Cyan indicator
     - SSH proxy
   * - SNMP Proxy
     - Yellow indicator
     - SNMP proxy
   * - ICMP Proxy
     - Blue indicator
     - ICMP proxy
   * - Sensor Proxy
     - Default color
     - Sensor proxy
   * - Zone Proxy
     - Magenta indicator
     - Zone proxy


Link Color Sources
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Source
     - Description
   * - Default
     - Uses map default color
   * - Object Status
     - Based on selected object(s) status
   * - Custom Color
     - User-defined static color
   * - Script
     - Determined by NXSL script
   * - Link Utilization
     - Based on interface utilization
   * - Interface Status
     - Based on interface operational status


Layout Algorithms
~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Algorithm
     - Description
   * - Manual
     - User positions objects
   * - Spring
     - Force-directed layout
   * - Radial
     - Circular arrangement
   * - Horizontal Tree
     - Left-to-right tree
   * - Vertical Tree
     - Top-to-bottom tree
   * - Sparse Vertical Tree
     - Spread-out vertical tree


Link Routing
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Algorithm
     - Description
   * - Default
     - Uses map setting
   * - Direct
     - Straight line
   * - Manhattan
     - Grid-based with right angles
   * - Bendpoints
     - User-defined routing points


Link Styles
~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Style
     - Description
   * - Default
     - System default (solid)
   * - Solid
     - Continuous line
   * - Dash
     - Dashed line
   * - Dot
     - Dotted line
   * - Dash-Dot
     - Alternating dash and dot
   * - Dash-Dot-Dot
     - Dash and two dots


NXSL Classes Reference
~~~~~~~~~~~~~~~~~~~~~~

For scripting with network maps, refer to the NXSL documentation:

- `NetworkMap class <https://netxms.org/documentation/nxsl-latest/#class-networkmap>`_ - Map object available as ``$map``
- `NetworkMapLink class <https://netxms.org/documentation/nxsl-latest/#class-networkmaplink>`_ - Link object available as ``$link``


Dashboards
==========

Dashboards are defined by administrator and allow to combine any available
visualization components with data from multiple sources in order to create
high-level views to see network (or parts of it) health at a glance. For
example, below is a dashboard showing traffic information from core router, as
well as CPU usage from vital nodes:

.. figure:: _images/DashboardExample.png

There are two ways to access dashboards:

Open dashboard from Object Browser

- Open dashboard from :guilabel:`Object Browser`
- Switch to :guilabel:`Dashboard` perspective and select dashboard with
  left-click

Configuration
-------------

Dashboards is a special type of objects created in :guilabel:`Dashboards` tree.
To create a new dashboard, right click on :guilabel:`Dashboards` root object or
any other existing dashboard and select :guilabel:`Create dashboard`. To
configure dashboard content, open object's properties and go to
:guilabel:`Dashboard Elements:guilabel:` page. Here you can define number of
columns and manage list of elements. Press :guilabel:`Add:guilabel:` to add new
element. You will be prompted with element type selection dialog:

.. figure:: _images/DashboardProperties.png

When a new element is added, you can edit it by double-clicking on it's record in
the elements list, or by pressing the :guilabel:`Edit` button. Each element have
:guilabel:`Layout` property page which controls the element's layout inside the
dashboard, and one or more element type specific pages to control element's
appearance and displayed information. The following element types are
available:

Label
~~~~~

Text label with configurable text and colors.

.. figure:: _images/dashboard_labelW.png

Line Chart
~~~~~~~~~~

Line chart.

.. figure:: _images/dashboard_line_charW.png

Bar Chart
~~~~~~~~~

Bar chart.

.. figure:: _images/dashboard_bar_chart.png

Pie Chart
~~~~~~~~~

Pie chart.

.. figure:: _images/dashboard_pie_chartW.png

Status Chart
~~~~~~~~~~~~

Bar chart which shows current status distribution for nodes under given root.

.. figure:: _images/dashboard_status_chartW.png

Status Indicator
~~~~~~~~~~~~~~~~

Shows current status of selected object.

.. figure:: _images/dashboard_status_indicatorW.png

Dashboard
~~~~~~~~~

Another dashboard object (or multiple objects) rendered
as element of this dashboard.

Network Map
~~~~~~~~~~~

:ref:`Network map<network_map>` object rendered as dashboard element.

Custom Widget
~~~~~~~~~~~~~

Custom widget provided by third party management client plugin. This options
allows to add widget from third party loaded plugin.

Get Map
~~~~~~~

Geographic map centered at given location.

.. figure:: _images/dashbard_geo_mapW.png

Alarm Viewer
~~~~~~~~~~~~

:ref:`List of alarms<alarms>` for given object subtree.

.. figure:: _images/dashbard_alarm_viewerW.png

Availability Chart
~~~~~~~~~~~~~~~~~~

Pie chart showing availability percentage for given business service

.. figure:: _images/dashbard_availability_chartW.png

Gauge
~~~~~

Gauge have 3 types of widgets

    - Dial is radial gauge with configurable maximum, minimum values. Scale can have fixed color or can be separated to  3 color configurable zones.
    - Dar is linear gauge with configurable maximum, minimum values. Scale can have fixed color or can be separated to  3 color configurable zones. (Not yet implemented)
    - Text is text gauge, that can be colored using fixed color, changed depending on 3 configurable color zones or colored using threshold color (severity).

.. figure:: _images/dashboard_gauge_3typesW.png

Web Page
~~~~~~~~

Web page at given URL rendered within dashboard.

Bar Chart for Table DCI
~~~~~~~~~~~~~~~~~~~~~~~

Bar chart built from data collected via single table DCI.

.. figure:: _images/dashboard_table_bar_chartW.png

Pie Chart for Table DCI
~~~~~~~~~~~~~~~~~~~~~~~

Pie chart built from data collected via single table DCI.

.. figure:: _images/dashboard_table_pie_chartW.png

Separator
~~~~~~~~~

Separator, can be shown as line, box, or simply empty space.

.. figure:: _images/dashboard_separatorW.png

Table Value
~~~~~~~~~~~

This widget displays table with last values of Table DCI.

Status Map
~~~~~~~~~~

Status map has three views: Flat view, Group view and Radial view.

Flat view and Group view display nodes as rectangles, using color to indicate
their status. In Flat view nodes are displayed without grouping, whether in
Group view nodes are grouped by containers.

.. figure:: _images/dashboard_status_mapW.png

Radial view displays containers and nodes as hierarchical colored radial layout.

DCI Summary Table
~~~~~~~~~~~~~~~~~

:ref:`DCI Summary Table<dci-summary-table-label>` widget provides summary DCI information
about objects under container.

.. figure:: _images/dashboard_summary_tableW.png

Syslog Monitor
~~~~~~~~~~~~~~
Syslog monitor widget. Has additional option to set root object to filter objects what will be shown in monitor.
One object or a container that contains required objects can be set as root object.

.. figure:: _images/dashboard_syslog_monitor.png

SNMP Trap Monitor
~~~~~~~~~~~~~~~~~
SNMP Trap monitor widget. Has additional option to set root object to filter objects what will be shown in monitor.
One object or a container that contains required objects can be set as root object.

.. figure:: _images/dashboard_snmp_trap_monitor.png

Event monitor
~~~~~~~~~~~~~
Event monitor widget. Has additional option to set root object to filter objects what will be shown in monitor.
One object or a container that contains required objects can be set as root object.

.. figure:: _images/dashboard_event_monitor.png

Service component map
~~~~~~~~~~~~~~~~~~~~~
Map displays hierarchy of objects in :guilabel:`Infrastructure Service` starting from selected root object.

.. figure:: _images/dashboard_service_component_map.png

Rack diagram
~~~~~~~~~~~~
Shows rack front, back or both views with object placement in it.

.. figure:: _images/dashboard_rack_diagram.png

Object tools
~~~~~~~~~~~~
Shows buttons with pre configured object tools, that are executed on click.

.. figure:: _images/dashboard_object_tools.png


.. _dashboards-object-query:

Object query
~~~~~~~~~~~~
Shows columns with filtered objects' information.

Object query has 2 main configurations. :guilabel:`Query` that filterers objects
and provide option to create additional information about object in columns and
:guilabel:`Object Properties` that lists information that should be shown in
table.

**Query**

Script is executed on each object and if it returns ``true`` object is included
in the result set, if ``false`` - not. Script can define additional variables
that will be displayed as columns in the result set. Three variants for the
syntax are available: 

  1. Special syntax with ``with`` block for additional columns calculation. This
     syntax allows to define metadata for the additional columns such as column
     title, sorting, etc. 
  2. Usual NXSL script that returns ``true`` or ``false`` and uses global
     variables for additional columns.
  3. Usual NXSL script that returns map with additional columns (where keys are
     column names and values are value for this column) or ``false``.


Special syntax:

.. code-block::

  with
    varName = { code or expression },
    varName = { code or expression }
    /* Might be as many blocks as required.
     * varName is a name of the variable where result of a code will be assigned.
     * It can be used later in the code in expression or to be displayed in table
     * using the same name in the Object Properties part.
    */
  expression
  /* Short circuit evaluated expression. This expression is executed first and if
   * it contains not yet calculated varName then variable is calculated and used 
   * in expression. Expression that should result as true or false as a sign if
   * this object should be displayed in table or not. No semicolon at the end.
  */

This page provides option to configure columns that should be used for ordering,
refresh interval and record limit. To order column write a comma-separated list
of attribute named or varNames with ``-`` sign to order in descending order and
with ``+`` sign to order in ascending order.

**Object Properties**

This property page is used to organize required columns and column order in table.
Each column configuration consists of name of object's attribute or varName defined
in Query page, display name used as a name for a column and data type of the column.

**Example**

This example will show how to filter nodes that only have alarms on them, are
not in maintenance mode and show count of critical alarms on the node, order by
critical alarm count the list and then by node name. Example shows two different
options how to write the same script so only one of them should be used.

Configuration:

.. figure:: _images/dashboard_object_query_query.png

  Option 1. Query script with "with" syntax

.. figure:: _images/dashboard_object_query_query2.png

  Option 2. Query script  with usual NXSL script and global variables

.. figure:: _images/dashboard_object_query_object_properties.png

  Configuration of :guilabel:`Properties to display` will be the same for both scripts

Result:

.. figure:: _images/dashboard_object_query.png

Port view
~~~~~~~~~
Shows ports schematic with each port status.
One object or a container that contains required objects can be set as root object.

.. figure:: _images/dashboard_port_view.png


Element Property Pages
----------------------

Chart
~~~~~

:guilabel:`Chart` page is available for all chart type elements: Bar Chart, Bar
Chart for Table DCI, Dial Chart, Line Chart, Pie Chart, Pie Chart for Table
DCI. It defines basic properties of a chart.

.. figure:: _images/ChartElementConfig.png

Data Sources
~~~~~~~~~~~~

:guilabel:`Data sources` page is available for all DCI based elements: Bar
Chart, Dial Chart, Line Chart and Pie Chart. Here you can define
what DCIs should be used as data sources for the chart. Up to 16 DCIs can be
added to a single chart. You can configure multiple properties for each data
source. To edit data source, either double click on appropriate item in the
list, or press :guilabel:`Edit` button. Data source configuration dialog looks
like following:

.. figure:: _images/ChartDataSourceConfig.png

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Property
     - Description
   * - Data collection item
     - DCI object to be used.
   * - Display name
     - Name for this data source to be used in chart's legend. If left empty,
       DCI description will be used.
   * - Colour
     - Allows you to define specific color for this data source or let system
       to pick one automatically.
   * - Area chart
     - This option is valid only for line charts and toggles data source
       display as filled area instead of line.
   * - Show thresholds
     - This option is valid only for line charts and toggles display of
       configured thresholds.


Layout
~~~~~~

.. figure:: _images/DashboardElementLayoutPage.png

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Property
     - Description
   * - Horizontal alignment
     - Horizontal alignment for this element. Possible values are
       :guilabel:`FILL`, :guilabel:`CENTER`, :guilabel:`LEFT`, and
       :guilabel:`RIGHT`.
   * - Vertical alignment
     - Vertical alignment for this element. Possible values are
       :guilabel:`FILL`, :guilabel:`CENTER`, :guilabel:`TOP`, and
       :guilabel:`BOTTOM`.
   * - Horizontal span
     - Specify how many grid cells this element will occupy horizontally.
   * - Vertical span
     - Specify how many grid cells this element will occupy vertically.
   * - Width hint
     - Hint for element's width in pixels. Default value of ``-1`` means that
       layout manager will decide width for element.
   * - Height hint
     - Hint for element's height in pixels. Default value of ``-1`` means that
       layout manager will decide width for element.

See detailed information about layout in section :ref:`dashboards-layout`.

Web Page
~~~~~~~~

:guilabel`Web Page` property page is available for web page type elements. Here
you can define URL to be displayed and optional title. If title is not empty,
it will be displayed above page content.


.. _dashboards-layout:

Understanding Element Layout
----------------------------

Dashboard uses grid concept to layout it's elements. Available space is divided
into rows and columns, and each element occupies one or more cells. The number of
columns is configured in dashboard object properties, and number of rows is
calculated automatically based on number of columns, elements, and
cells occupied by each element. Elements are laid out in columns from
left to right, and a new row is created when there are no space left for next
element on current row. Each element has horizontal and vertical alignment
properties. Default for both is :guilabel:`FILL`. Possible alignment values are
following:


.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Value
     - Description
   * - FILL
     - Make element to fill whole cell. Also causes to grab excess free space
       available inside dashboard. If more than one element is trying to grab
       the same space, then the excess space is shared evenly among the
       grabbing elements.
   * - CENTER
     - Center element within cell.
   * - LEFT/TOP
     - Align element to left/top of the cell.
   * - RIGHT/BOTTOM
     - Align element to right/bottom of the cell.


.. figure:: _images/DashboardComplexLayoutConfig.png

   Complex layout configuration

This configuration will be rendered into this layout:

.. image:: _images/DashboardComplexLayoutExample.png

Dashboard Rotation
------------------

To create configuration when management client displays multiple dashboards one by one in
a loop, follow these steps:

- Create all dashboards you want to show
- Create additional dashboard object, with single element of type
  :guilabel:`Dashboard` inside
- Add all dashboards you want to show to dashboard list of that element and set
  desired time between changing dashboards.

.. figure:: _images/DashboardRotationConfig.png

   Sample configuration of two dashboards displayed in a loop for 40 seconds each.

Tutorials
---------

Dashboard creation tutorial available on `Youtube <http://youtu.be/ZfJQiUIDHY4>`_

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
can be used either by you or by other |product_name| users, depending on settings. To
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


Save current settings as template graph
---------------------------------------

.. figure:: _images/save_as_temp_graph.png

Current graph settings can be saved as a template graph for an easy template graph creation. The difference between predefined graphs and template graphs are that template graphs are not configured to view specific DCI`s on a node, instead they are configured to view DCI names that can be found on many nodes (e.g. ``FileSystem.FreePerc(/)``). This allows for the creation of certain graph templates to monitor, for example, disk usage that can be reused on any node to which the appropreate DCI`s are applied on via :ref:`dci-configuration`.

See detailed information on template graphs in the section :ref:`template-graph-conf`.

In the Graph name field of the pop-up save dialog, enter the desired name for the template graph by which you can later identify your it in the :ref:`template-graph-conf` which can be found in :menuselection:`Configuration-->Template Graph Configuration`.

.. figure:: _images/temp_graph_menu.png

Template graphs can be accessed in the :guilabel:`Object Browser` as seen on the screenshot above. When a template graph is created, it will appear in the sub-menus of the nodes found in :guilabel:`Object Browser`, the rest of the settings can be accessed by editing a template graph in the :ref:`template-graph-conf`.

.. _template-graph-conf:

Template Graph Configuration
----------------------------

Template graphs are used to ease the monitoring of a pre-set list of DCI`s on multiple nodes by adding a list of DCI names to the template source. This allows for the possibility to create templates to monitor specific data on any node to which the appropriate DCI`s are applied on.

.. figure:: _images/temp_graph_conf.png

The :guilabel:`Template Graph Configuration` is used to create and edit template graphs. Properties for already created template graphs can be brought up by double clicking the template graph you wish to edit and new ones can be added by pressing the green cross on the top right or by right clicking and selecting :guilabel:`Create new template graph`.

.. figure:: _images/temp_graph_conf_acl.png

	Name and access rights of a graph

The above property page provides the possibility to configure the name of the template graph and the access rights. The user who has created the template graph will have full access to it even though the username will not show up in the access right list.

.. figure:: _images/temp_graph_conf_gen.png

	General graph properties.

Title:

	- The title that the graph will have when opened.
	- The title can contain special characters described in :ref:`object_tools_macro`.

Options:

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Option
     - Description
   * - Show grid lines
     - Enable or disable grid lines for the graph.
   * - Stacked
     - Stacks the graphs of each value on top of one another to be able to see the total value easier (e.g. useful when monitoring cpu usage).
   * - Show legend
     - Enable or disable the legend of the graph.
   * - Show extended legend
     - Enable or disable the extended legend of the graph (Max, Avg, Min, Curr).
   * - Refresh automatically
     - Enable or disable auto-refresh.
   * - Logarithmic scale
     - Use the logarithmic scale for the graph.
   * - Translucent
     - Enable or disable the translucency of the graph.
   * - Show host names
     - Show host name of the node from which the value is taken.
   * - Area chart
     - Highlights the area underneath the graph.
   * - Line width
     - Adjust the width of the lines.
   * - Legend position
     - Set the position of the legend.
   * - Refresh interval
     - Set the refresh interval.

Time Period:

Provides the possibility to configure the time period of the graph. It is possible to set a dynamic time frame (Back from now) and a static time frame (Fixed time frame).

Y Axis Range:

Adjust the range of the Y axis on the graph.

.. figure:: _images/temp_graph_conf_filter.png

	Template graph filter properties.

It may be necessary to set certain filters for a template graph. This can be useful if the graph contains DCI names that are only available on |product_name| agent or are SNMP dependant.

More information on filters can be found in :ref:`object_tools_filter`.

.. figure:: _images/temp_graph_conf_source.png

	Template graph sources

There are two options to add sources to the template graph. Sources can be added manually by configuring the Data Source parameters yourself or by importing data source information from DCI`s that have already been applied to other nodes.

.. figure:: _images/temp_graph_conf_modify.png

When adding or editing a source, it is possible to use Java regex in the DCI Name and DCI Description fields. This can be handy when used with the Multiple match option which will use all DCI`s that match the particular regex. The order in which the DCI list is searched is first by DCI Name and then by DCI Description.

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
column is a DCI. It can be configured for each summary table which DCIs should be
present on it.

.. figure:: _images/summary_table.png

Configuration
-------------

DCI summary table can be configured in Configuration -> Summary Table.

.. figure:: _images/configure_dci_summary_table.png

General:

  - Menu path - path where this summary table can be found. You can use
    ``->`` character pair to create subtree like "Linux->System information".
  - Title - title of the summary table.

Columns:

  - This is the list if DCI's that will be shown on the summary table.
    Name is the name of column and DCI Name is DCI parameter name.

     - Multivalued column is intended to present string DCIs that contain several
       values divided by specified separator. Each value is presented on a separate line in the column.
     - If **Use regular expression for parameter name matching** is enabled, a regular expression is specified in **DCI name** field.
       If several DCIs will be matched on a node, only one will be displayed.
  - Import button allows to select a DCI from existing object.


Filter:
  - Filter script is executed for each node to determine, if that node should be included in a summary table.
    Filter script is defined with help of :term:`NXSL` scripting language.


Usage
-----

After DCI summary table is configured it can be accessed in container
object (Subnet, container...) context menu under "Summary tables".
