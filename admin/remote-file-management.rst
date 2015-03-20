######################
Remote file management
######################

.. _agent_file_managment:

Agent file management
=====================

Introduction
------------

This section describes possibilities to manage files on remote nodes using agent 
and required configuration for it.


Required Configuration
----------------------

Subagent configuration
~~~~~~~~~~~~~~~~~~~~~~

To do any manipulations with files on a node it is required to load filemng 
subagent and configure accessible paths.  It provides 
possibility to upload, download, delete, move and rename files. 

All configuration parameters related to filemng subagent should be placed 
into **\*filemgr** section of agent's configuration file. 
The following configuration parameters are supported:

+----------------+---------+-------------------------------------------+----------------+
| Parameter      | Format  | Description                               | Default value  |
+================+=========+===========================================+================+
| RootFolder     | String  | The folder to witch will be given access. | no             |
+----------------+---------+-------------------------------------------+----------------+

Agent's configuration file example:

.. code-block:: cfg

   MasterServers = netxms.demo
   SubAgent = filemgr.nsm

   [filemgr]
   RootFolder = /home/zev
   RootFolder = /home/zev/etc
   RootFolder = /logs 

   
Access rights
~~~~~~~~~~~~~
To view File Manager View it's enough to have "Read" access to node. 

To download files from file manager of through multiple file download there should be "Download file" access for this node and 
for multiple download "Read server files" access. 

To upload file from subagent there should be "Upload file" access for this node.  

For moving, renaming and deleting files from node it is required "Manage files" access to node. 


File Manager view
-----------------

For each configured node is possible to open File Manager. In it will be displayed all configured root folders with 
option to expand and see their content. 

.. figure:: _images/file-manager.png
   :scale: 100%


File menu
~~~~~~~~~

 - Download... : downloads file to selected folder on local computer
 - Show : shows file with tail option 'on'
 - Rename : renames file 
 - Delete : deletes file 

.. figure:: _images/file_manager_file_menu.png
   :scale: 100%

Folder menu
~~~~~~~~~~~

 - Upload file... : uploads local file to selected folder in view
 - Upload folder... : uploads local folder to selected folder in view (not supported on web console)
 - Download... : download folder to selected folder on local computer (on web console will be advised to save as a zip of the selected folder)
 - Rename : renames folder
 - Delete : deletes folder and all it's content
 - Refresh this folder : refreshes content of selected folder in view

.. figure:: _images/file_manager_folder_menu.png
   :scale: 100%

Other options
~~~~~~~~~~~~~

 - It is possible to move files and folders with help of drag and drop.
 - To refresh all view should be used view refresh button(not form folder menu). But in this case all expanded folders will be closed.


File upload to multiple nodes
-----------------------------

There is possibility to upload one file from server storage to multiple nodes in few clicks. 

 1. File should be uploaded to server for instruction check :ref:`upload-file-on-server-label` section. 
 2. From object tree should be selected nodes to which upload will be done. Selection can be done with help of 'Ctrl' key.
 3. Right click on one of selected nodes and chose "Upload file..."
 4. There will be asked to provide path were to download file and server file that will be uploaded. (If destination will not be set then as a destination will be taken from agent's config parameter 'FileStore').

.. _server-files-label:

Server File Managment
=====================

Access Rights
-------------

There are 2 access rights that can be granted:
 - Read server files : possibility to see files that are download on server
 - Manage server files : possibility to remove or upload on server files

.. _upload-file-on-server-label:

Upload file on server
---------------------

It can be done in "Server File List" view 

.. figure:: _images/server_file_list_view.png
   :scale: 60%

or "Tools"->"Upload file to server...". 

.. figure:: _images/upload_file_to_server.png
   :scale: 60%


