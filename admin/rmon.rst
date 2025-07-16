.. _rmon:

#########################
Using RMON Data in NetXMS
#########################

What Is RMON?
=============

RMON (RFC 2819) defines a set of SNMP MIBs that allow network administrators to monitor statistics and events on network segments. RMON provides insight into traffic patterns, performance issues, and unusual activity. Key groups include:

- **Statistics:** Packet and byte counts, errors, and utilization.
- **History:** Time-based historical data.
- **Alarm:** Threshold-based event triggers.
- **Event:** Actions based on alarms.
- **Host:** Per-host statistics.

Prerequisites
=============

- |product_name| server installed and running.
- SNMP-enabled devices that support RMON (consult device documentation).
- SNMP credentials configured in |product_name| for target devices.

Configuring NetXMS to Collect RMON Data
========================================

Discovering RMON-Capable Devices
---------------------------------

1. Ensure your network device is configured to support SNMP and RMON MIBs.
2. Add the device to |product_name| as a node.
3. During node polling, |product_name| will automatically discover supported SNMP MIBs, including RMON.

Enabling RMON Data Collection
-----------------------------

- **MIB Browsing:** Open the node in |product_name|, navigate to the :guilabel:`MIB Browser`, and search for RMON MIBs (e.g., ``RMON-MIB``, ``EtherStats``, ``History``).
- **Data Collection:** Use the Data Collection Configuration to add parameters based on RMON OIDs, such as:

  - ``1.3.6.1.2.1.16.1.1.1.1`` (etherStatsIndex)
  - ``1.3.6.1.2.1.16.1.1.1.10`` (etherStatsOctets)
  - ``1.3.6.1.2.1.16.2.1.1.2`` (historySampleIndex)

- **Templates:** Create or modify data collection templates to include RMON parameters for consistent monitoring across similar devices.

Setting Up Thresholds and Events
---------------------------------

- Use |product_name| thresholds to trigger alarms or notifications when RMON parameters exceed defined values (e.g., high error rate, utilization spikes).
- Define event processing rules to automate responses or escalate incidents.

Reporting and Visualization
----------------------------

- RMON data appears in the node's :guilabel:`Graphs` and :guilabel:`Reports` sections.
- Custom dashboards can display historical and real-time RMON statistics (errors, traffic, host conversations).
- Use scheduled reports for trending and capacity planning.

Example: Monitoring Interface Utilization with RMON
====================================================

This detailed example demonstrates how to set up RMON monitoring for interface utilization on a switch.

Step 1: Device Discovery and RMON Capability Verification
---------------------------------------------------------

1. **Add the device to NetXMS:**
   
   - Navigate to :guilabel:`Object Browser` → :guilabel:`Infrastructure Services` → :guilabel:`Entire Network`
   - Right-click and select :guilabel:`Create` → :guilabel:`Node`
   - Enter the device IP address and SNMP community string
   - Click :guilabel:`OK` to add the node

2. **Verify RMON support:**
   
   - Right-click the new node and select :guilabel:`Manage` → :guilabel:`Manage node`
   - Go to the :guilabel:`SNMP` tab and click :guilabel:`Walk` to browse available MIBs
   - Look for RMON MIB objects under ``1.3.6.1.2.1.16`` (RMON-MIB)

Step 2: Configure RMON Data Collection
--------------------------------------

1. **Access Data Collection Configuration:**
   
   - Right-click the node and select :guilabel:`Data Collection Configuration`
   - Click :guilabel:`Add` → :guilabel:`Parameter`

2. **Add etherStatsOctets parameter:**
   
   - **Parameter Name:** ``etherStatsOctets_1``
   - **Description:** ``Total bytes on interface 1``
   - **Data Type:** ``Counter64``
   - **SNMP OID:** ``1.3.6.1.2.1.16.1.1.1.10.1`` (where .1 is the interface index)
   - **Polling Interval:** ``60`` seconds
   - **Retention Time:** ``90`` days
   - Click :guilabel:`OK`

3. **Add etherStatsPkts parameter:**
   
   - **Parameter Name:** ``etherStatsPkts_1``
   - **Description:** ``Total packets on interface 1``
   - **Data Type:** ``Counter64``
   - **SNMP OID:** ``1.3.6.1.2.1.16.1.1.1.5.1``
   - **Polling Interval:** ``60`` seconds
   - **Retention Time:** ``90`` days
   - Click :guilabel:`OK`

4. **Add error counters:**
   
   - **etherStatsCRCAlignErrors:** ``1.3.6.1.2.1.16.1.1.1.6.1``
   - **etherStatsUndersizePkts:** ``1.3.6.1.2.1.16.1.1.1.7.1``
   - **etherStatsOversizePkts:** ``1.3.6.1.2.1.16.1.1.1.8.1``

Step 3: Create Performance Graphs
---------------------------------

1. **Navigate to Performance Graphs:**
   
   - Right-click the node and select :guilabel:`Performance` → :guilabel:`Configure Graphs`
   - Click :guilabel:`Add` to create a new graph

2. **Configure Interface Utilization Graph:**
   
   - **Graph Name:** ``Interface 1 RMON Utilization``
   - **Y-axis Label:** ``Bytes per second``
   - **Time Period:** ``24 hours``
   - Add data source:
     
     - **Parameter:** ``etherStatsOctets_1``
     - **Color:** ``Blue``
     - **Line Width:** ``2``
     - **Calculation:** ``Rate`` (to convert counter to rate)

Step 4: Configure Thresholds and Alarms
---------------------------------------

1. **Create Threshold:**
   
   - Go to :guilabel:`Data Collection Configuration`
   - Select the ``etherStatsOctets_1`` parameter
   - Click :guilabel:`Thresholds` tab
   - Click :guilabel:`Add`

2. **Configure High Utilization Threshold:**
   
   - **Function:** ``last()`` 
   - **Operation:** ``>``
   - **Value:** ``800000000`` (800 Mbps for gigabit interface at 80% utilization)
   - **Event:** ``SYS_THRESHOLD_REACHED``
   - **Repeat Interval:** ``300`` seconds
   - Click :guilabel:`OK`

3. **Set up Event Processing:**
   
   - Navigate to :guilabel:`Configuration` → :guilabel:`Event Processing Policy`
   - Create a new rule for ``SYS_THRESHOLD_REACHED`` events
   - Configure actions such as sending email notifications or SNMP traps

Step 5: Create Dashboard Widget
--------------------------------

1. **Create Dashboard:**
   
   - Go to :guilabel:`Dashboards` and create a new dashboard
   - Add a :guilabel:`Performance Chart` widget

2. **Configure Widget:**
   
   - **Data Source:** Select the node and ``etherStatsOctets_1`` parameter
   - **Chart Type:** ``Line Chart``
   - **Time Range:** ``Last 24 hours``
   - **Refresh Interval:** ``60`` seconds

Step 6: Generate Reports
-------------------------

1. **Create Report Template:**
   
   - Navigate to :guilabel:`Reporting` → :guilabel:`Report Templates`
   - Create a new template with RMON data for interface utilization trends

2. **Schedule Regular Reports:**
   
   - Set up weekly or monthly reports showing:
     
     - Peak utilization times
     - Average utilization
     - Error rates and trends
     - Capacity planning recommendations

Expected Results
-----------------

After completing this configuration, you will have:

- Real-time monitoring of interface utilization using RMON data
- Historical trending and graphical visualization
- Automated alerting when utilization exceeds thresholds
- Regular reports for capacity planning and performance analysis
- Dashboard widgets showing current network performance

This setup provides comprehensive monitoring using RMON capabilities and enables proactive network management.

Troubleshooting
===============

- If RMON data is missing, verify SNMP configuration and device support.
- Use the MIB browser to check for the presence of RMON MIBs.
- Review |product_name| server logs for SNMP collection errors.

References
==========

- `NetXMS Documentation <https://netxms.org/documentation/>`_
- `RFC 2819: RMON MIB <https://datatracker.ietf.org/doc/html/rfc2819>`_
- Device-specific SNMP and RMON configuration guides