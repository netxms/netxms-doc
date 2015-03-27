.. _user-management:


###############
User management
###############


Introduction
============

NetXMS has it's own user database. All NetXMS user accounts stored in backend
SQL database. Each account has it's own unique login name and identifier. The
account may also have a password.


Terms and Definitions
=====================

Users
-----

NetXMS has the following attributes for users:

- Unique identifier
- Unique login name
- First name
- Last name
- Description
- Authentication method
- Password
- Certificate

Not all attributes are mandatory.


Superuser
~~~~~~~~~

NetXMS has built-in superuser with ID ``0``, which always has full access to
the system. Default login name for superuser is ``admin``. Default password is
``netxms`` and user will be forced to change it on first login. Superuser
account can be renamed or disabled, but cannot be deleted.


Groups
------

Each user can be member of several groups. Groups are the preferred way to
organize access permissions. You should always grant permission to groups
instead of using individual users. That way you will get a much shorter access
control list which is easier to handle. Access rights from multiple groups are
summarized to calculate effective user access rights.


Everyone Group
~~~~~~~~~~~~~~

NetXMS has built-in virtual group called :guilabel:`Everyone`. This group
always contains all users in the system. It cannot be deleted, and it's members
list cannot be edited.


System Access Rights
--------------------

System access rights used to grant access to system-wide configuration (like
:ref:`event-processing`) and functions (like agent registration).

.. figure:: _images/user_access_rights.png
   :scale: 65%

The following system access rights can be granted:


.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Access Right
     - Description
   * - Access server console 
     - Allow user to access server's debug console. :ref:`server-debug-console` 
   * - Configure event templates
     - Allow user to configure event templates. :ref:`event-processing`
   * - Configure object tools
     - Allow user to configure object tools. :ref:`object_tools`
   * - Configure server actions
     - Allow user to configure server actions. :ref:`event-processing`
   * - Configure situations
     - Allow user to configure situations. :ref:`event-processing`
   * - Configure SNMP traps
     - Allow user to configure SNMP trap mapping.
   * - Control user sessions
     - Allow user to see active user sessions and force terminate them. (Not yet implemented)
   * - Edit event processing policy
     - Allow user to edit Event Processing Policy. :ref:`event-processing`
   * - Edit server configuration variables
     - Allow user to edit server configuration variables. 
   * - Execute commands via XMPP
     - Allows user to execute commands via XMPP
   * - Login as mobile device
     - Allows user to login with help of mobile application
   * - Manage agent configurations
     - Allow user to create, edit, and delete agent configurations stored on
       server. :ref:`stored-agent-configurations-label`
   * - Manage DCI summary table
     - Allows user to manage DCI summary table :ref:`dci-summary-table-label`
   * - Manage image library
     - Allows user to manage image library :ref:`image-library`
   * - Manage mapping tables
     - Allows user to manage mapping tables
   * - Manage packages
     - Allow user to install, remove, and deploy agent packages. :ref:`agent-remote-update`
   * - Manage server files
     - Allow user to upload files to server and delete files stored on server. :ref:`server-files-label`
   * - Manage script library
     - Allow user to manage scripts in Script Library.
   * - Manage users
     - Allow user to manage user accounts. Please note that user having this
       access right granted can modify own account to get any other system
       right granted.
   * - Read server files 
     - Allow user to read files stored on server and upload to agents (user
       still needs appropriate object rights for upload). :ref:`server-files-label` 
   * - Register agents
     - Allow user to register NetXMS agents.
   * - Send SMS
     - Allow user to send SMS via NetXMS server. This access right has no
       effect unless server configuration variable ``AllowDirectSMS`` set to
       ``1``.
   * - Unlink helpdesk tickets
     - Allow user to unlink alarm from external heldesk system :ref:`helpdesk-integration`
   * - View audit log
     - Allow user to view audit log.
   * - View event log
     - Allow user to view event log, alarm log.
   * - View event templates configuration
     - Allow user to view configured event templates.
   * - View SNMP trap log
     - Allow user to view SNMP trap log.


User Authentication
===================

Internal Password
-----------------

This is the default method for user authentication. Password provided by user
compared against password stored in NetXMS database.


Password Policy
~~~~~~~~~~~~~~~

Various restrictions can be put on internal passwords to force users to choose stronger passwords. The following server configuration variables controls password policy:

.. list-table::
   :header-rows: 1
   :widths: 20 70 10

   * - Variable
     - Description
     - Default
   * - MinPasswordLength
     - Default minimum password length for a NetXMS user. The default applied only if per-user setting is not defined.
     - 0
   * - PasswordComplexity
     - Required pasword complexity. See table bellow for details.
     - 0
   * - PasswordExpiration
     - Password expiration time in days. If set to ``0``, password expiration
       is disabled. Has no effect on users with :guilabel:`Password never
       expired` flag set.
     - 0
   * - PasswordHistoryLength
     - Number of previous passwords to keep. Users are not allowed to set
       password if it matches one from previous passwords list.
     - 0

Possible flags for ``PasswordComplexity``:

.. list-table::
  :header-rows: 1
  :widths: 10 90

  * - Value
    - Description
  * - 1
    - Password must contain digits
  * - 2
    - Password must contain uppercase letters
  * - 4
    - Password must contain lowercase letters
  * - 8
    - Password must contain special characters
  * - 16
    - Forbid alphabetical sequences (password considered invalid if it
      contains alphabetical sequence of 3 or more letters of same
      case).
  * - 32
    - Forbid keyboard sequences (password considered invalid if it
      contains sequence of 3 or more characters that are located on
      keyboard next to each other, like ``ASDF``).

Complexity flags can be added together to get desired restrictions. For example, to
force passwords to contain uppercase and lowercase letters,
``PasswordComplexity`` variable must be set to ``6`` (``2 + 4``).

Changes to these configuration variables becomes effective immediately and does
not require NetXMS server restart.

RADIUS
------

If :guilabel:`RADIUS` authentication method selected password provided by user
sent to RADIUS server for validation. User is granted access if RADIUS server
responds with ``Access-Accept``. Communication between NetXMS server and RADIUS
server controlled by the following server configuration variables:

.. list-table::
   :header-rows: 1
   :widths: 20 70 10

   * - Variable
     - Description
     - Default value
   * - RADIUSNumRetries
     - The number of retries for RADIUS authentication.
     - 5
   * - RADIUSPort
     - Port number used for connection to primary RADIUS server.
     - 1645
   * - RADIUSSecondaryPort
     - Port number used for connection to secondary RADIUS server.
     - 1645
   * - RADIUSSecondarySecret
     - Shared secret used for communication with secondary RADIUS server.
     - netxms
   * - RADIUSSecondaryServer
     - Host name or IP address of secondary RADIUS server.
     - none
   * - RADIUSSecret
     - Shared secret used for communication with primary RADIUS server.
     - netxms
   * - RADIUSServer
     - Host name or IP address of primary RADIUS server.
     - none
   * - RADIUSTimeout
     - Timeout in seconds for requests to RADIUS server
     - 3

Changes to these configuration variables becomes effective immediately and does
not require NetXMS server restart.


Certificate Authentication
--------------------------

This type of authentication can be selected manually in user preferences.


Login process using certificate is following:

1. Server send random challenge to client
2. Client sign server's challenge with his certificate's private key and send signed challenge along with public part of certificate to server
3. Server validates certificate using CA certificate
4. If certificate is valid, server validates challenge signature using certificate's public key
5. If signature is valid, server compares certificate subject with mapping data from user record
6. If mapping data match with certificate subject, access is granted


So, to login successfully, user must posses valid certificate with private key. 
Authentication by certificate also allows smart card login - you just need to store 
certificate used for login on smart card instead of local certificate store.

Certificate management
~~~~~~~~~~~~~~~~~~~~~~
CA certificates can be managed in "Certificate Manager" view. 

Certificate can be added, deleted and edited. Edit window allows to change comment and 
to copy the subject of certificate. Certificate subject is one of the ways to link a 
certificate with a user. 

.. figure:: _images/certificate_view.png
   :scale: 65%


Link certificate and user
~~~~~~~~~~~~~~~~~~~~~~~~~
In "User Manager" view select user properties for required user. 
Then go to "Authentication" part.

.. figure:: _images/user_prop_auth.png
   :scale: 65%
   
In "Authentication Method" section: "Certificate",  "Certificate or Password",  
"Certificate or RADIUS".

|

Next two fields in combinations:

   Certificate mapping method: "Subject"
   
   Certificate mapping data: the subject of the CA. Can be taken from "Certificate Manager" view.

|

   Certificate mapping method: "Public key"
   
   Certificate mapping data: the public key of the certificate

|

   Certificate mapping method: "Common name"
   
   Certificate mapping data: if no mapping data set, then linking certificate CN = user name, otherwise CN = mapping data


Integration with LDAP
=====================

NetXMS can be integrated with LDAP. LDAP users and groups are added to NetXMS database and afterwards can be used for login in to NetXMS system. LDAP users are also inserted into groups as per LDAP. (Available since: NetXMS 1.2.15)

Limitations:

If user with the same login name already exists, the LDAP user will not be created. So it is not possible to add from LDAP user with name "admin" and group with name "Everyone".

LDAP synchronization configuration
----------------------------------

LDAP synchronization parameters: 

.. list-table::
   :header-rows: 1
   :widths: 20 70 10
   
   * - Variable
     - Description
     - Default value
   * - LdapConnectionString ``*``
     - The LdapConnectionString configuration parameter may be a comma- or whitespace-separated list of URIs containing only  the  schema,  the host, and the port fields.  Apart from ldap, other (non-standard) recognized values of the  schema  field  are ldaps (LDAP over TLS), ldapi (LDAP over IPC), and cldap (connectionless LDAP).  If other fields are present, the behavior is undefined. Format: `schema://host:port`\ . 

       **Windows specific**\ : for server based on Windows system this parameter should be set according to this rules: empty string(attempts to find the "default" LDAP server), a domain name, or a space-separated list of host names or dotted strings that represent the IP address of hosts running an LDAP server to which to connect. Each host name in the list can include an optional port number which is separated from the host itself with a colon (:). 

       **Non Open LDAP library specific**\ : Windows, old Open LDAP and not Open LDAp libraries does not support mixed schema type so all links should be 'ldap://' or all 'ldaps://'.
     - ldap://localhost:389
   * - LdapSyncUser ``*``
     - User login for LDAP synchronization
     - 
   * - LdapSyncUserPassword ``*``
     - User password for LDAP synchronization 
     -
   * - LdapSearchBase
     - The LdapSearchBase configuration parameter is the DN of the entry at which to start the search.
     -
   * - LdapSearchFilter ``*``
     - The LdapSearchFilter is a string representation of the filter to apply in the search.
     -
   * - LdapUserDeleteAction ``*``
     - This parameter specifies what should be done while synchronization with deleted from LDAP user/group. 0 - if user should be just deleted from NetXMS DB. 1 - if it should be disabled. If it is chosen to disable user, then on LDAP sync user will be disabled and it's description will be change on "LDAP entry was deleted." Afterwards this user/group can be detached from LDAP and enabled if it is required or just deleted manually. 
     - 0
   * - LdapMappingName ``*`` ``**``
     - There should be specified name of attribute that's value will be used as a user login name
     - displayName 
   * - LdapMappingFullName ``**``
     - There should be specified name of attribute that's value will be used as a user full name
     - displayName
   * - LdapMappingDescription ``**``
     - There should be specified name of attribute that's value will be used as a user description
     - 
   * - LdapGroupClass
     - There is specified which object class represents group objects. If found entry will not be of a user ot group class, it will be just ignored.
     - 
   * - LdapUserClass ``*``
     - There is specified which object class represents user objects. If found entry will not be of a user ot group class, it will be just ignored.
     - displayName
   * - LdapSyncInterval ``*``
     - This parameter is for setting synchronization interval in minutes between NetXMS server and LDAP server. If synchronization parameter is set to 0 - synchronization will not be done. 
     - 0

``* Required fields``    
``** Could not be the same field``

Synchronization also can be done manually with `ldapsync` or just `ldap` command in server console.


LDAP users/groups relationships with native NetXMS users/groups
---------------------------------------------------------------

LDAP user can be added to non LDAP grop and non LDAP user can be added to LDAP group. But if LDAP user will be added to LDAP group, then while next synchronization user will be removed from group. 


Login with help of LDAP user
----------------------------

To login into NetXMS there should be selected `Password` login type, should be entered user login(LdapMappingName) and LDAP password. 

LDAP configuration debuging
---------------------------

If users are not synchronized the reason can be found by running manually `ldapsync` or just `ldap` 
command in server console on debug lever 4. 

Log when LDAP sync passed correctly:

::

    [11-Sep-2014 16:28:08.352] [DEBUG] LDAPConnection::initLDAP(): Connecting to LDAP server
    [11-Sep-2014 16:28:08.353] [DEBUG] LDAPConnection::syncUsers(): Found entry count: 3
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): Found dn: CN=Users,CN=Customers,DC=Northwind,DC=Extranet
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): CN=Users,CN=Customers,DC=Northwind,DC=Extranet is not a user nor a group
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): Found dn: CN=zev333,CN=Users,CN=Customers,DC=Northwind,DC=Extranet
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): User added: dn: CN=zev333,CN=Users,CN=Customers,DC=Northwind,DC=Extranet, login name: zev333, full name: (null), description: (null)
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): Found dn: CN=user,CN=Users,CN=Customers,DC=Northwind,DC=Extranet
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::syncUsers(): User added: dn: CN=user,CN=Users,CN=Customers,DC=Northwind,DC=Extranet, login name: user, full name: (null), description: (null)
    [11-Sep-2014 16:28:08.354] [DEBUG] LDAPConnection::closeLDAPConnection(): Disconnect form ldap.
    [11-Sep-2014 16:28:08.354] [DEBUG] UpdateLDAPUsers(): User added: dn: CN=zev333,CN=Users,CN=Customers,DC=Northwind,DC=Extranet, login name: zev333, full name: (null), description: (null)
    [11-Sep-2014 16:28:08.354] [DEBUG] UpdateLDAPUsers(): User added: dn: CN=user,CN=Users,CN=Customers,DC=Northwind,DC=Extranet, login name: user, full name: (null), description: (null)
    [11-Sep-2014 16:28:08.354] [DEBUG] RemoveDeletedLDAPEntry(): Ldap uid=john,ou=People,dc=nodomain entry was removed form DB.
    [11-Sep-2014 16:28:08.354] [DEBUG] RemoveDeletedLDAPEntry(): Ldap uid=zev,ou=People,dc=nodomain entry was removed form DB.
    [11-Sep-2014 16:28:08.354] [DEBUG] RemoveDeletedLDAPEntry(): Ldap uid=kasio,ou=People,dc=nodomain entry was removed form DB.
    [11-Sep-2014 16:28:08.355] [DEBUG] RemoveDeletedLDAPEntry(): Ldap uid=usr1,ou=People,dc=nodomain entry was removed form DB.

Login credentials incorrect:

::

    [11-Sep-2014 15:49:39.892] [DEBUG] LDAPConnection::initLDAP(): Connecting to LDAP server
    [11-Sep-2014 15:49:39.896] [DEBUG] LDAPConnection::loginLDAP(): LDAP could not login. Error code: Invalid credentials
    [11-Sep-2014 15:49:39.896] [DEBUG] LDAPConnection::syncUsers(): Could not login.

Search base is set incorrectly or sync user does not have access to it:

::

    [11-Sep-2014 15:54:03.138] [DEBUG] LDAPConnection::initLDAP(): Connecting to LDAP server
    [11-Sep-2014 15:54:03.140] [DEBUG] LDAPConnection::syncUsers(): LDAP could not get search results. Error code: No such object
 
LDAP configuration examples
---------------------------

Active Directory
~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 70 
   
   * - Variable
     - Value   
   * - LdapConnectionString
     - ldap://10.5.0.35:389
   * - LdapSyncUser
     - CN=user,CN=Users,CN=Customers,DC=Domain,DC=Extranet
   * - LdapSyncUserPassword
     - xxxxxxxx
   * - LdapSearchBase
     - CN=Customers,DC=Domain,DC=Extranet
   * - LdapSearchFilter
     - (objectClass=*)
   * - LdapUserDeleteAction
     - 1
   * - LdapMappingName
     - sAMAccountName
   * - LdapMappingFullName
     - displayName
   * - LdapMappingDescription
     - description
   * - LdapGroupClass
     - group
   * - LdapUserClass
     - user
   * - LdapSyncInterval
     - 1440

Open LDAP
~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 20 70 
   
   * - Variable
     - Value   
   * - LdapConnectionString
     - ldap://10.5.0.35:389
   * - LdapSyncUser
     - cn=admin,dc=nodomain
   * - LdapSyncUserPassword
     - xxxxxxxx
   * - LdapSearchBase
     - dc=nodomain
   * - LdapSearchFilter
     - (objectClass=*)
   * - LdapUserDeleteAction
     - 1
   * - LdapMappingName
     - cn
   * - LdapMappingFullName
     - displayName
   * - LdapMappingDescription
     - description
   * - LdapGroupClass
     - groupOfNames
   * - LdapUserClass
     - inetOrgPerson
   * - LdapSyncInterval
     - 1440
     
Managing User Accounts
======================

All NetXMS user accounts can be managed from :guilabel:`User Manager` view
available at :menuselection:`Configuration --> User Manager` in NetXMS Console.
Only users with granted system right :guilabel:`Manage users` can access
:guilabel:`User Manager`.

- To create new user account, select :guilabel:`Create new user` from view menu or context menu.
- To create new group, select :guilabel:`Create new group` from view menu or context menu.
- To delete user account, select it in the list, right-click, and select :guilabel:`Delete` from pop-up menu. You can delete multiple accounts at a time.
- To modify properties of user or group, select it in the list, right-click, and select :guilabel:`Properties` from pop-up menu.
- To reset user's password, select user account in the list, right-click, and select :guilabel:`Change password` from pop-up menu.


Audit
=====

All important user actions are written to audit log. There are two audit
logging modes - internal and external. Internal audit logging is on by default
and writes audit records into table in NetXMS database. External audit logging
allows sending audit records to external system via syslog protocol. External
audit logging is off by default. Audit logging controlled by the following
server configuration variables:

.. list-table::
   :header-rows: 1
   :widths: 20 60 20

   * - Variable
     - Description
     - Default value
   * - AuditLogRetentionTime
     - Retention time in days for the records in internal audit log. All
       records older than specified will be deleted by housekeeping process.
     - 90
   * - EnableAuditLog
     - Enable (``1``) or disable (``0``) audit logging.
     - 1
   * - ExternalAuditFacility
     - Syslog facility to be used in audit log records sent to external server.
     - 13
   * - ExternalAuditPort
     - UDP port of external syslog server to send audit records to.
     - 514
   * - ExternalAuditServer
     - External syslog server to send audit records to. If set to none,
       external audit logging is disabled.
     - none
   * - ExternalAuditSeverity
     - Syslog severity to be used in audit log records sent to external server.
     - 5
   * - ExternalAuditTag
     - Syslog tag to be used in audit log records sent to external server.
     - netxmsd-audit




