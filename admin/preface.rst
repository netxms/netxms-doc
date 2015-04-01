#######
Preface
#######


Purpose of this document
========================

Purpose of this document is to provide knowledge about NetXMS installation, 
configuration and usage. 

Document contain :ref:`quick-start` chapter, that describes default installation 
and some simple metric configuration. :ref:`installation-and-upgrade` chapter 
contain more detailed information about NetXMS and its components installation 
and upgrade. To get familiar with main concepts of NetXMS use :ref:`concepts` 
chapter. :ref:`administration` is main chapter, that provides all necessary 
information to successfully operate NetXMS. List of built in monitoring 
options can be found there: :ref:`getting-things-monitored` chapter. There 
is also big chapter about :ref:`NXLS scripting<scripting>`

This document does not contain detailed description of NetXMS and it's 
architecture. To get this information please refer to Concept guide. 

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
   * Windows XP, all from server
   * Linux (all glibc2-based flavors)
   * FreeBSD, NetBSD, OpenBSD
   * Solaris
   * HP-UX
   * AIX
  

Where to get support
====================

Forum, Facebook/Twitter/G+
--------------------------

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
