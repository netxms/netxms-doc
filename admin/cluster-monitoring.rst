.. _cluster-monitoring:

==================
Cluster monitoring
==================

Introduction
------------

Cluster monitoring provides aspects of monitoring needed in high availability
setups. There is a special class of object in |product_name| - Cluster.

:term:`DCIs<DCI>` defined on a cluster object are automatically applied to its
nodes. A cluster allows to aggregate data from its nodes, e.g. to calculate
sum or average for a metric that is collected from all nodes.
A cluster can adequately collect data from services as they move from
one node to another, providing uninterrupted data collection.
