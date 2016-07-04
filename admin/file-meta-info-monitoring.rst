.. _file-meta-info-monitoring:

=====================
File meta information
=====================

Monitoring of file system is implemented by OS subagents. Full description of this
functions can be found :ref:`there <list-of-supported-metrics>`. There is provided
option to get file hash, creation, last edit and other timestamps, file size and
number of files in the directory. In this sections will be shown only the most
commonly used configurations.

Examples
========

In examples will be shown only DCI configuration with threshold. Generated event
processing options can be found in :ref:`event-processing` chapter.

Example 1
---------

In this example will be shown how to check that specific folder exceed specified size.

Create DCI for File.Size(*) metric to monitor folder size. Required parameters:
/path,*,1.

.. figure:: _images/file-meta-info-example.png

In threshold it should be checked that last value is less than 2 GB. That mean
that returned value should be less than 2 000 000 000 bytes.

.. figure:: _images/file-meta-info-example2.png

  Threshold

Example 2
---------

In this example will be configured monitoring that in exact folder exist files that
was modified less then half an hour ago.

Create DCI for File.Count(*) metric to monitor file count in folder /path, that match
any pattern, folder should be checked recursively, file match any size, files are
created less than 30 minutes ago. This conditions will be given to metric as this
parameters: path,*,1,0,-1800.

.. figure:: _images/file-meta-info2-example.png

In threshold it should be checked that at least one file meeting conditions exists.
That mean that file count should be more than 1. Prerequisite is to create 2 events.


.. figure:: _images/file-meta-info2-example2.png

  Events

.. figure:: _images/file-meta-info2-example3.png

  Threshold

As in message of error is used Instance parameter, it should be set in
:guilabel:`Threshold` window.

.. figure:: _images/file-meta-info2-example4.png