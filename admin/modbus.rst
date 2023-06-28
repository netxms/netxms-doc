.. _modbus:


######
Modbus
######

.. versionadded:: 4.4

|product_name| can collect data via Modbus-TCP protocol. Data collection is
performed by |product_name| server or by |product_name| agents operating in
proxy mode. 

To enable agent operation as Modbus proxy, add ``EnableModbusProxy=yes`` to
agent configuration file and restart the agent.

Metric for Mosbus data collection items has special format denoting type of
Modbus unit id, register type, register address and the way how obtained data
should be interpreted:


:command:`[[unit-id:]register-type:]register-address[|conversion]`


.. list-table::
   :class: longtable
   :widths: 25 75
   :header-rows: 1

   * - Metric component
     - Description
   * - unit-id
     - Modbus unit ID. Optional, if used, should be specified without [ ]. To
       use it, ``register-type`` should also be provided. 
   * - register-type
     - Type of Modbus register. Optional, if not specified, ``hold`` will be
       used. Should be specified without [ ] if used. Supports following values:

       * ``coil`` - Coil
       * ``discrete`` - Discrete Input
       * ``hold`` - Holding Register
       * ``input`` - Input Register

   * - register-address
     - Address of Modbus register. Can be provided as decimal number or
       hexadecimal number prefixed by ``0x``. 
   * - conversion
     - Conversion of Modbus data. Optional, if not specified, ``uint16`` will be
       used. Should be specified without [ ] if used. Affects the number of
       Modbus registers being read and how read data is interpreted:

       * ``int16`` - 16 bit signed integer
       * ``uint16`` - 16 bit unsigned integer
       * ``int32`` - 32 bit signed integer (will read 2 registers)
       * ``uint32`` - 32 bit unsigned integer (will read 2 registers)
       * ``int64`` - 64 bit signed integer (will read 4 registers)
       * ``uint64`` - 64 bit unsigned integer (will read 4 registers)
       * ``float`` - same as ``float-abcd``
       * ``float-abcd`` - 4 byte floating point number, ABCD byte order
       * ``float-cdab`` - 4 byte floating point number, CDAB byte order
       * ``float-badc`` - 4 byte floating point number, BADC byte order
       * ``float-dcba`` - 4 byte floating point number, DCBA byte order
       * ``double`` - same as ``double-be``
       * ``double-be`` - 8 byte floating point number, big endian byte order
       * ``double-le`` - 8 byte floating point number, little endian byte order
       * ``string-N`` - string of N characters (will read (N + 1) / 2 registers)
       * ``string-N-CP`` - string of N characters encoded using codepage CP (will read (N + 1) / 2 registers)


Modbus metric examples
======================

| ``0x2A``
| Read holding register at address 2A hexadecimal (42 decimal), interpret as
  uint16. 

| ``input:8`` 
| Read input register at address 8 decimal, interpret as uint16. 

| ``10|int16`` 
| Read holding register at address 10 decimal, interpret as int16. 

| ``input:55|float`` 
| Read two input registers starting from 55 decimal, interpret as float with
  ABCD byte order.
