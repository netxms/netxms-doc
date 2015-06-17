#######
Preface
#######


Purpose of this document
========================

Purpose of this document is to provide knowledge about NetXMS installation, 
configuration and usage. It contains all required information for installation 
and operation managers. 

Document contain :ref:`quick-start` chapter, that describes default installation 
and some simple metric configuration. :ref:`installation-and-upgrade` chapter 
contain more detailed information about NetXMS and its components installation 
and upgrade. To get familiar with main concepts of NetXMS use :ref:`concepts` 
chapter. :ref:`concepts` is main chapter, that provides all necessary 
information to successfully operate NetXMS. List of built in monitoring 
options can be found there: :ref:`getting-things-monitored` chapter. There 
is also big chapter about :ref:`NXLS scripting<scripting>`. 

Mostly this document describes work with Desktop and Web management consoles. Mostly 
they have similar functionality so there is no separated descriptions of them. Web 
based console have some limitation, this limitations will be described in a feature 
text as a notes. There is separate part that describes 
:ref:`Mobile NetXMS agent configuration GUI<monitoring-mobile-device>` and 
:ref:`Mobile Console<mobile-console>`.

This document does not contain detailed description of NetXMS architecture. 
To get this information please refer to Concept guide. 

What is NetXMS
==============

NetXMS is an enterprise grade multi-platform modular open source network management 
and monitoring system. It provides comprehensive event management, 
performance monitoring, alerting, reporting and graphing for all layers of 
IT infrastructure — from network devices to business application layer. 
Having been designed with flexibility and scalability in mind, NetXMS features 
a wide range of supported platforms. It is licensed under the GNU General Public 
License version 2 as published by the Free Software Foundation.

Supported operating systems and databases
=========================================

NetXMS supports most popular operation systems. 

Supported operating systems for NetXMS server:
   * Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * RedHat Enterprise Linux, SUSE Linux, CentOS, Debian Linux, Ubuntu Linux
   * FreeBSD, NetBSD, OpenBSD
   * Solaris 10, 11
   * HP-UX 11.23, 11.31
   * AIX 5.3 +

.. _supported-db-list:
   
Supported DBMS engines for NetXMS server
   * Microsoft SQL Server 2005, Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * MySQL 5.0 +
   * Oracle 11g, 12
   * PostgreSQL 8+
   * DB/2
   * SQLite(it is highly recommended use this option only for test purpose)
   
Supported operating systems for NetXMS agent
   * Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008,  Windows Server 2008R2, Windows 7, Windows 8, Windows 8.1, Windows Server 2012, Windows Server 2012R2
   * Linux (all glibc2-based flavors)
   * FreeBSD, NetBSD, OpenBSD
   * Solaris
   * HP-UX
   * AIX
  

Where to get support
====================

.. todo::
  Add that solutions and FAQ can be found on wiki. 

Forum, Facebook/Twitter/G+/IRC
------------------------------

Links to NetXMS in social media:

  * `Forum <https://www.netxms.org/forum>`_
  * `Facebook <https://www.facebook.com/netxms>`_
  * `Google+: <https://plus.google.com/u/0/s/netxms>`_
  * `Twitter: <https://twitter.com/netxms>`_
  * IRC: #netxms on freenode. `List of servers <https://freenode.net/irc_servers.shtml>`_

Stay informed of new releases
-----------------------------

Conventions
===========

The following typographical conventions are used in this manual.

+----------------------------------+------------------------------------------+
| Sample                           | Description                              |
+==================================+==========================================+
| :guilabel:`Button`               | Any GUI element: Button, Menu item       |
+----------------------------------+------------------------------------------+
| `Another Guide`                  | Reference to external manual or man page |
+----------------------------------+------------------------------------------+
| :kbd:`Control-M`                 | Keyboard shortcut                        |
+----------------------------------+------------------------------------------+
| :term:`DCI`                      | Term which could be found in glossary    |
+----------------------------------+------------------------------------------+
| :menuselection:`&File --> &Exit` | Menu selection path, you must click on   |
|                                  | :guilabel:`File`, then :guilabel:`Exit`  |
+----------------------------------+------------------------------------------+

Changelog
=========

Only major changes are lister here. Complete change log is available at
`<http://www.netxms.org/download/ChangeLog>`_. 
