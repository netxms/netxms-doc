.. _reporting:


#########
Reporting
#########

Reporting module is an optional component, build on top of well known
JasperReports_ library, which can produce pixel-perfect documents in variety of
formats based on historical data collected by NetXMS.

Reporting module consist of two main parts: user interface and standalone
``Reporting Server``, which handles all scheduling, execution, and optional
document delivery to end users.

Report generation is two step process: first step is to collect and process
input data, then render output files in desired format. This separation exist
for a reason: unlike rendering step, data collection could take hours to
complete and it make no sense to repeat same processing process to render Excel
file instead of PDF. When first step is finished, all processed information is
saved into intermediate file on the reporting server and available for
rendering at any time (e.g. user can render and download report from last year,
even if source data is already purged). 

Reports execution and rendering can be initiated both manually and on schedule.

.. _JasperReports: http://community.jaspersoft.com/project/jasperreports-library

User Interface
==============

All reporting-related operations are available in separate
:guilabel:`Reporting` perspective. Perspective contains two main areas – list
of available reports on the left and report details view on the right. Details
view show information about currently selected report.

.. figure:: _images/reporting_perspective.png

   Reporting perspective.

Details view contains tree main areas: :guilabel:`Parameters`,
:guilabel:`Schedules`, and :guilabel:`Results`.

Parameters
----------

.. figure:: _images/reporting_parameters.png

   Execution parameters for report (in this example: :guilabel:`Start date`)

In this section, user can set all input parameters required for report
execution, for example data range or list of objects which should be included
in the report. List of required parameters is extracted from report definition
file and can be empty, if particular report do not require any input data to
operate.

Schedules
---------

Each report can have one or more schedules, which define when it should be
executed, and optionally rendered. Reporting server can also notify users that
new report is executed and available for download, or send resulting file as an
attachment.

.. figure:: _images/reporting_schedules.png

   List of scheduled executions

To add new schedule, click on :guilabel:`Add Schedule` down below, this will
open schedule editor.

.. figure:: _images/reporting_schedule_editor.png

   Schedule editor with two tabs, :guilabel:`General` and
   :guilabel:`Notifications` 

:guilabel:`General` tab contains four scheduling options:

#. :guilabel:`Once` - execute report once at specified date and time
#. :guilabel:`Daily` - execute report every day at specified time
#. :guilabel:`Weekly` - execute report every week on selected days of week at
   specified time
#. :guilabel:`Monthly` - execute report every month on selected days at
   specified time

.. figure:: _images/reporting_schedule_editor_notification.png

   :guilabel:`Notifications` tab of Schedule editor

:guilabel:`Notification` tab allows to control email notifications and report
delivery to list of recipients.  To enable notifications, select
:guilabel:`Send notification on job completion` checkbox.

If checkbox :guilabel:`Attach rendered report` checkbox is enabled, report will
be rendered into selected format and attached to notification email.

Results section
---------------

.. figure:: _images/reporting_results.png

   List of generated reports

This section contains list of all generated reports, which are stored on the server and can be rendered on request. To render report in desired format, right click on the record and select :guilabel:`Render to PDF` or :guilabel:`Render to Excel`.

If report is no longer needed, right click on record and select :guilabel:`Delete` to completely remove it from server.

Configuration
=============

NetXMS Server
-------------

NetXMS server maintain persistent connection with reporting server on
`localhost:4710`, but if can be changed in configuration.

+-------------------------+------------------------------------------------+---------------+
| Configuration Parameter | Description                                    | Default Value |
+=========================+================================================+===============+
| EnableReportingServer   | Boolean on/off switch which enable integration | 0             |
+-------------------------+------------------------------------------------+---------------+
| ReportingServerHostname | IP address or hostname of the reporting server | localhost     |
+-------------------------+------------------------------------------------+---------------+
| ReportingServerPort     | Port number of the reporting server            | 4710          |
+-------------------------+------------------------------------------------+---------------+

Reporting Server
----------------

Report definitions are loaded from the file system by scanning workspace folder, expected structure: ``$WORKSPACE/definitions/$REPORT_GUID``. Each report folder should contain file ``main.jrxml``, any additional files (images, translation files) should be referenced in ``main.jrxml`` with relative paths. Sample directory listing::

  workspace/definitions/6eb9c41c-e9f0-4e17-ac57-de747e16e480/i18n.properties
  workspace/definitions/6eb9c41c-e9f0-4e17-ac57-de747e16e480/main.jrxml
  workspace/definitions/6eb9c41c-e9f0-4e17-ac57-de747e16e480/logo.png

Server behaviour is controlled by two files: ``logback.xml`` (logger configuration) and ``nxreporting.properties``.

Format of ``logback.xml`` is described in `Logback manual`_.

.. _Logback manual: http://logback.qos.ch/manual/

``nxreporting.properties`` is a standard Java property file in ``key=value`` format.

.. list-table:: 
   :header-rows: 1
   :widths: 30 70

   * - Parameter 
     - Description
   * - nxreporting.workspace
     - Path to workspace with deployed reports
   * - system.datasource.driverClassName
     - JDBC class name, for example ``org.postgresql.Driver``
   * - system.datasource.url
     - JDBC connection string, for example ``jdbc:postgresql://127.0.0.1/netxms``
   * - system.datasource.dialect
     - Hibernate dialect, for example ``org.hibernate.dialect.PostgreSQLDialect``. More information in `JavaDoc <http://docs.jboss.org/hibernate/orm/4.1/javadocs/org/hibernate/dialect/Dialect.html>`_
   * - system.datasource.username
     - 
   * - system.datasource.password
     - 
   * - report.datasource.driverClassName
     - 
   * - report.datasource.url
     - 
   * - report.datasource.username
     - 
   * - report.datasource.password
     - 
   * - org.quartz.jobStore.dataSource
     - 
   * - org.quartz.dataSource.myDS.driver
     - 
   * - org.quartz.dataSource.myDS.URL
     - 
   * - org.quartz.dataSource.myDS.user
     - 
   * - org.quartz.dataSource.myDS.password
     - 
   * - org.quartz.dataSource.myDS.maxConnections
     - 

Access Control
--------------

