.. _sla:


#################
Business services
#################

Introduction
============

In a nutshell, Business Services is a tool for availability monitoring of
logical services. Company email, web site, server farm, call center - all are
examples of logical services. Moreover, the services can be combined together to
define a "broader" logical service. Company email, web site, name server and
firewall all can be referred to as "Company Internet Services" and monitored for
availability as a whole. So if the name server goes down then the "Company
Internet Services" do not function properly as a whole. This feature can be used
both for internal QA and external Service Level Agreement (SLA) monitoring.


Business service object
=======================

Business Service
----------------

Business Services represented with service checks and a tree-like hierarchy of 
other business services. For each service in the hierarchy, |product_name| keeps 
track of all downtime cases so later user can request calculation of availability 
percentage for required time period. To check availability at any particular level, 
select Business Service object in the :guilabel:`Object Browser`, choose 
:guilabel:`Availability` tab and select time period.

Business service contains two NXSL scripts in configuration: for object automatic 
binding and for DCI automatic binding. Those scripts can be used to automatically 
populate Business service with resources that require monitoring. Service checks 
can be automatically created and also removed if "Auto remove" filter option is
selected.

Service check
-------------

Service check is a test whose result is used to define the state of the service.
There can be 3 types of checks: DCI check, object check and NXSL script. Service
check can have one of statuses: OK, Failed or Degraded. Degraded status means
that object ot DCI status is not Normal, but is less worse then threshold for
this check, this state will not change state of business service to failed and
will not affect availability percentage. 

DCI check
~~~~~~~~~

DCI check is based on the status of DCI. DCI status is calculated from the
status of threshold (if it is active) and severity of active threshold. DCI
check has its own status threshold starting from which check is counted as
failed. Threshold can be set separately for each check. If default value is
chosen, value of "BusinessServices.Check.Threshold.DataCollection" server
configuration variable is used. 

Object check
~~~~~~~~~~~~

Object check is based on object status. Object check has it's own status
threshold starting from which check is counted as failed. Threshold can be set
separately for each check. If default value is chosen, value of
"BusinessServices.Check.Threshold.Objects" server configuration variable is
used.

NXSL script check 
~~~~~~~~~~~~~~~~~

NXSL script check either returns success (the test result ok) or failure (the
service has failed). For success "true" should be returned, and "false" for
failure. In addition failure reason can be returned from the script - script
should return textual with the reason, this is interpreted as failed check. 

There are the following special variables which can be used in NXSL scripts for
service checks:

- $object - points to the object for which the check is executed
- $node - points to the current node for which the check is executed. Will be
  null, if the object, for which the check is executed is not a node. 
- $service - the business service this check belongs to


Business service prototype
==========================

To avoid manually defining of the same business service multiple times (for
multiple clients or infrastructure items) you can create business service
prototype. The principle behind business service prototype is very similar to
DCI instance discovery. There is instance discovery options and script to filter
it. For instances that passed the filter business services are created. In
object and DCI auto-apply scripts of created business services information about
instance value and id of business service prototype are available. 


Configuration and usage
=======================

For both configuration and monitoring use :guilabel:`Business Service`
perspective.

.. figure:: _images/Business_Services_Perspective.png

   Business service perspective


Configuration
-------------

To define a new service select :guilabel:`Create business service` from the
context menu in :guilabel:`Object Browser` and enter the service name. Then
in newly created service you may want to define checks or define check auto 
apply scripts in business service properties. 


.. figure:: _images/Business_Services_Checks.png

   Business service checks

Business service prototype is defined the same way, but it is also required to
configure Instance Discovery method. 

Monitoring
----------

Business service availability for exact period can be checked using
:guilabel:`Availability` tab. It has predefined time ranges and a date selector
for arbitrary date range. A list of problems occurred for a business service is
also shown with detailed information, start time, end time and reason.

.. figure:: _images/Business_Services_Availability.png

   Availability pie chart and details
