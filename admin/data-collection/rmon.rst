.. _rmon:

#########################
Using RMON Data in NetXMS
#########################

What Is RMON?
=============

RMON (RFC 2819) and RMON2 (RFC 4502) defines a set of SNMP MIBs that allow network administrators to monitor statistics and events on network segments. 
RMON provides insight into traffic patterns, performance issues, and unusual activity. Key groups include:

- **Statistics:** Packet and byte counts, errors, and utilization.
- **History:** Time-based historical data.
- **Alarm:** Threshold-based event triggers.
- **Event:** Actions based on alarms.
- **Host:** Per-host statistics.

Prerequisites
=============

- SNMP-enabled devices that support RMON (consult device documentation).
- SNMP credentials configured in |product_name| for target devices.

Configuring NetXMS to Collect RMON Data
========================================

1. Ensure your network device is configured to support SNMP and RMON OIDs.
2. Add the device to |product_name| as a node and configure SNMP credentials.
3. Use the MIB Browser to verify that RMON/RMON2 MIB tree returns data for the device. Base OID for RMON is `1.3.6.1.2.1.16` and for RMON2 extension is `1.3.6.1.2.1.16.9` and `1.3.6.1.2.1.16.10`.
4. Add required :term:`DCI`\ s for RMON/RMON2 parameters.


How-To: Monitoring Interface Dropped packets with RMON
=======================================================

In this example, we will monitor dropped packets on network interfaces whose expected state is UP. We will use the RMON to collect this data.

To monitor dropped packets on all interfaces using RMON:

1. Create a new DCI for the device with next configuration:

  General tab:
    - DCI origin to SNMP 
    - Set metric to `1.3.6.1.2.1.16.1.1.1.3.{instance}` (where `{instance}` will be expanded to the interface index by :guilabel:`Instance discovery` poll).
    - Set data type to `Counter64` or `Counter32` depending on the expected range of values.
    - Set the Display name to something like "Dropped Packets on {instance-name}".
  Instance discovery Tab:
    - Set the Instance discovery method to :guilabel:`Internal Table`
    - Table name: `Network.Interfaces`
    - Instance discovery filter:

    .. code-block:: none

      interfaceTypes = [6, 7, 22]; // 6 - ethernetCsmacd, 7 - iso88023Csmacd, 22 - propPointToPointSerial

      interface = FindObject($1); //find interface by first column in Network.Interfaces table (interface object id)
      if (interface == null) return false; // if interface not found, skip this instance
      if (interface.isLoopback or interface.name == "lo") return false; // skip loopback interfaces
      if (!(interface.ifType in interfaceTypes)) return false; // skip interfaces that are not in the specified types
      if (interface.expectedState != InterfaceExpectedState::UP) return false; // skip interfaces that are not expected to be UP

      return [interface.ifIndex, interface.ifName, interface]; // return instance index, name and object for further processing

2. Run an :guilabel:`Instance discovery` poll to create DCIs for all interfaces that match the filter.

.. note::

    An optional threshold can be set on the DCI to trigger an event when dropped packets exceed a certain value.


References
==========

- `RFC 2819: RMON MIB <https://datatracker.ietf.org/doc/html/rfc2819>`_
- `RFC 4502: RMON2 MIB <https://datatracker.ietf.org/doc/html/rfc4502>`_
