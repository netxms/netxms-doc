.. _reporting:


#########
Reporting
#########

Reporting module is an optional component, build on top of well known
JasperReports_ library, which can produce pixel-perfect documents in variety of
formats based on historical data collected by |product_name|.

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

|product_name| Server
---------------------

|product_name| server maintain persistent connection with reporting server on
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

Report definitions are loaded from the file system by scanning workspace folder,
expected structure: ``$WORKSPACE/definitions/$REPORT_GUID``. Each report folder
should contain file ``main.jrxml``, any additional files (images, translation
files) should be referenced in ``main.jrxml`` with relative paths. Sample
directory listing::

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

Installation Manual
===================

Setup
-----
1. Unpack netxms-reporting-server-2.0-M2.zip into some folder, in this example - /opt/nxreporting

2. Create directory "conf"

3. (Optional)Create logger configuration: conf/logback.xml (sample attached),
   detailed description here: http://logback.qos.ch/manual/configuration.html#syntax

    .. code-block:: xml

        <?xml version="1.0" encoding="UTF-8"?>
        <configuration>
        <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
            <file>/opt/nxreporting/log/nxreporting</file>

            <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <fileNamePattern>/opt/nxreporting/log/nxreporting.%i.gz</fileNamePattern>
            <minIndex>1</minIndex>
            <maxIndex>5</maxIndex>
            </rollingPolicy>

            <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <maxFileSize>16MB</maxFileSize>
            </triggeringPolicy>
            <encoder>
            <pattern>%d %5p | %t | %-55logger{55} | %m %n</pattern>
            </encoder>
        </appender>


4. Create configuration file for reporting server: conf/nxreporting.xml

    .. code-block:: xml

        <config>
        <workspace>/opt/nxreporting/workspace</workspace>
            <netxmsdConfig>/opt/netxms/etc/netxmsd.conf</netxmsdConfig>
            <datasources>
                <datasource>
                    <id>secondary</id>
                    <type>postgresql</type>
                    <url>jdbc:postgresql://127.0.0.1/netxms</url>
                    <username>netxms</username>
                    <password>netxms</password>
                </datasource>
            </datasources>
            <smtp>
                <server>127.0.0.1</server>
                <from>noreply@netxms.org</from>
            </smtp>
            <netxms>
                <server>127.0.0.1</server>
                <login>admin</login>
                <password>netxms</password>
            </netxms>
        </config>

    In most cases (when reports are using only single datasource), setting
    "netxmsdConfig" is enough, database type and credentials will loaded
    automatically from netxmsd.conf. "netxms" section of the config is required
    for reports, which load data not from SQL datasource, but using |product_name| API
    instead (connection is maintained by reporting server).

5. Create workspace directory (as set by "workspace" parameter), it will contain both report
   definitions (in "definitions" directory) and intermediate report data (in "output" directory).

6. Put report definition jars into workspace/definitions/, for example:

    .. code-block:: none

        AirAlk:~() $ ls -al /opt/nxreporting/workspace/definitions/*.jar
        -rw-r--r--  1 alk  wheel  3729 Mar 11 15:31 /opt/nxreporting/workspace/definitions/alarm-history-1.0.0.jar
        -rw-r--r--  1 alk  wheel  5607 Mar 11 15:31 /opt/nxreporting/workspace/definitions/alarm-resolution-time-1.0.0.jar
        -rw-r--r--  1 alk  wheel  4570 Mar 11 15:31 /opt/nxreporting/workspace/definitions/alarm-resolution-time-statistics-by-users-1.0.0.jar
        -rw-r--r--  1 alk  wheel  4203 Mar 11 15:31 /opt/nxreporting/workspace/definitions/dci-1.0.0.jar
        -rw-r--r--  1 alk  wheel  9968 Mar 11 15:31 /opt/nxreporting/workspace/definitions/epp-1.0.0.jar
        …

7. Enable reporting server connector, set EnableReportingServer to 1 (either
   in GUI - server configuration, or using command line: "nxdbmgr set
   EnableReportingServer 1"), then restart netxmsd.

8. Create additional tables by executing both scripts for your type of database from sql folder, for example:

    .. code-block:: sh
        nxdbmgr batch sql/postgres/nxreporting.sql
        nxdbmgr batch sql/postgres/quartz.sql

  It may be required to comment out "drop table" statements in the beginning of quartz.sql file. 


9. Start reporting server:

    .. code-block:: none

        cd /opt/nxreporting
        java -jar nxreporting-2.0-M2.jar

    When started with "-jar" option, java will automatically find configuration files in conf/ and all libraries in lib/. However, you can run it differently (and omit "cd /opt/nxreporting"):

    .. code-block:: none

        java -cp /opt/nxreporting/lib/\*.jar:/opt/nxreporting/conf:/opt/nxreporting/nxreporting-2.0-M2.jar com.radensolutions.reporting.Launcher

    or, if you are running windows:

    .. code-block:: none

        java -cp /opt/nxreporting/lib/\*.jar:/opt/nxreporting/conf:/opt/nxreporting/nxreporting-2.0-M2.jar com.radensolutions.reporting.Launcher


    In under 10 seconds, netxmsd should connect to reporting
    server and list of available reports will be visible in
    "Reporting" perspective.

Resulting directory structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: none

    /opt/nxreporting:
    total 5728
    drwxr-xr-x   6 alk  wheel      204 Apr  7 20:31 .
    drwxr-xr-x  14 alk  wheel      476 Apr  3 20:07 ..
    drwxr-xr-x   4 alk  wheel      136 Apr  7 20:31 conf
    drwxr-xr-x  79 alk  wheel     2686 Jan 23 10:29 lib
    -rw-r--r--   1 alk  wheel  2929061 Jan 23 10:29 nxreporting-2.0-M2.jar
    drwxr-xr-x   4 alk  wheel      136 Mar 11 15:06 workspace

    /opt/nxreporting/conf:
    total 16
    drwxr-xr-x  4 alk  wheel   136 Apr  7 20:31 .
    drwxr-xr-x  6 alk  wheel   204 Apr  7 20:31 ..
    -rw-r--r--  1 alk  wheel  1367 Apr  7 20:21 logback.xml
    -rw-r--r--  1 alk  wheel   764 Apr  7 13:21 nxreporting.xml

    /opt/nxreporting/lib:
    total 109528
    …

    /opt/nxreporting/workspace:
    total 0
    drwxr-xr-x   4 alk  wheel   136 Mar 11 15:06 .
    drwxr-xr-x   6 alk  wheel   204 Apr  7 20:31 ..
    drwxr-xr-x  32 alk  wheel  1088 Mar 11 15:43 definitions
    drwxr-xr-x   8 alk  wheel   272 Mar 11 15:42 output

    /opt/nxreporting/workspace/definitions:
    total 248
    drwxr-xr-x  32 alk  wheel  1088 Mar 11 15:43 .
    drwxr-xr-x   4 alk  wheel   136 Mar 11 15:06 ..
    -rw-r--r--   1 alk  wheel  3729 Mar 11 15:31 alarm-history-1.0.0.jar
    -rw-r--r--   1 alk  wheel  5607 Mar 11 15:31 alarm-resolution-time-1.0.0.jar
    -rw-r--r--   1 alk  wheel  4570 Mar 11 15:31 alarm-resolution-time-statistics-by-users-1.0.0.jar
    …

    /opt/nxreporting/workspace/output:
    total 0
    drwxr-xr-x   8 alk  wheel  272 Mar 11 15:42 .
    drwxr-xr-x   4 alk  wheel  136 Mar 11 15:06 ..
    drwxr-xr-x   4 alk  wheel  136 Mar 11 15:44 01827cdb-cb23-4b06-b607-fd02c4279add
    drwxr-xr-x   4 alk  wheel  136 Mar  7 22:04 52ce4398-a131-4a79-887e-672cc73d5d34
    drwxr-xr-x   3 alk  wheel  102 Mar 11 15:44 8a7c025c-84c8-4914-b2bf-3b4cde27a224
    …

.. https://www.netxms.org/forum/installation/install-report-server/
.. http://www.netxms.org/forum/installation/reporting-server-4315/

Report definitions
------------------

On startup, reporting server scan workspace/definitions directory for \*.jar files.
Each file is unpacked into it's own folder based on jar name (e.g. "report1.jar"
will be unpacked into "report1"). Each archive should contain at least one file
– "main.jrxml", which is main report definition. It can also contain subreports, 
images – or anything else, supported by Jasper Reports. Any additional resources
should be referenced using paths relative to root folder of unpacked report, which
is set as additional parameter "SUBREPORT_DIR" (e.g. "$P{SUBREPORT_DIR}/logo.png").

Archive can also contain java code, which will be used as data provider (instead
of querying SQL database). Reporting server will try to load class
"report.DataSource", which should implement interface
"com.radensolutions.reporting.custom.NXCLDataSource" (attached sample: Event
Processing Policy). Query string language in jrxml should be set to "nxcl"
(default - SQL).

Simplest way to create jar files are using Maven, empty project is provided in
samples archive. Running "mvn package" will produce complete jar file in "target"
directory.
