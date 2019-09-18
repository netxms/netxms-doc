.. _cluster-monitoring:

==================
Cluster monitoring
==================

Introduction
------------

Cluster monitoring provides aspects of monitoring needed in high availability
setups. There is a special class of object in |product_name| - Cluster.

:term:`DCIs<DCI>` defined on cluster object are automatically applied to it's
nodes. Cluster allows to aggregate data from it's nodes, e.g. to calculate
sum or average for a metric that is collected from all nodes.
Cluster can adequately collect data from services as they move from from
one node to another, providing uninterrupted data collection.
