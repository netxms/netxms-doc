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

1. **Add Parameter:** In Data Collection, add ``etherStatsOctets`` to monitor total bytes on an interface.
2. **Graph Data:** View utilization over time in |product_name| graphs.
3. **Alarm Configuration:** Set an alarm for "High Utilization" if octet count increases beyond a set threshold.
4. **Report:** Generate a periodic report showing interface usage trends.

Troubleshooting
===============

- If RMON data is missing, verify SNMP configuration and device support.
- Use the MIB browser to check for the presence of RMON MIBs.
- Review |product_name| server logs for SNMP collection errors.

References
==========

- `RFC 2819: RMON MIB <https://datatracker.ietf.org/doc/html/rfc2819>`_
- Device-specific SNMP and RMON configuration guides
