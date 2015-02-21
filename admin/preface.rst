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
It is licensed under the GNU General Public License version 2 as published 
by the Free Software Foundation.

Supported operating systems and databases
=========================================

NetXMS supports most popular operation systems. 

Supported systems:
  * Windows ( Windows 2003 or higher)
  * Linux
  * Solaris
  * HP-UX
  * AIX
  * FreeBSD
  * Novel
  
Databases that can be used for installation:
  * Microsoft SQL Server
  * MySQL
  * DB2
  * PostgreSQL  
  * Oracle
  * SQLite(it is highly recommended use this option only for test purpose)
  

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
