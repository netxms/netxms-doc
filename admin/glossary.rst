########
Glossary
########

.. glossary::
  :sorted:
  
  Action
    Configurable operation which can be executed by the system when
    :term:`Event` is passing thru :term:`Event Processing Policy`. Multiple
    action types are supported, including email or SMS notification, executing
    OS commands and forwarding events to another instance of NetXMS server.

  Alarm
    Outstanding issue which require operator attention. Alarms are created by
    the system as a result of :term:`Event` passing thru :term:`Event
    Processing Policy`.

  Alarm Browser
    :term:`View` in user interface, which shows all active alarms in the system
    and allow user to interact with them.

  Business Service
    An IT Service that directly supports a Business Process, as opposed to an
    Infrastructure Service which is used internally by the IT Service Provider
    and is not usually visible to the Business.

  CA
    Certification authority is an entity that issues digital certificates. 
    More details in :wikipedia:`Wikipedia <Certificate authority>`
    
  Condition
    (Create condition in infrastructure services)

  Container
    :term:`Object` that can store other containers and :term:`nodes <Node>`.
    
  CSR
    Certificate signing request is a message sent from an applicant to a 
    certificate authority in order to apply for a digital identity certificate.
    More details in :wikipedia:`Wikipedia <Certificate signing request>`

  DCI
    Abbreviation for :term:`Data Collection Item`

  Dashboard
    Manually generated :term:`Object` that can combine any available
    visualization components with data from multiple sources in order to
    create high-level views to see network or parts of it, and it's
    health.

  Data Collection Item
    Configuration entity of a single :term:`Metric`.
    
  DNS
    Domain Name System. More details in
    :wikipedia:`Wikipedia <Domain Name System>`

  Entire Network
    Automatically generated object hierarchy that contains all nodes and IP
    subnets known to NetXMS.

  EPP
    Abbreviation for :term:`Event Processing Policy`

  Event
    TBD
    A change of state which has significance for the management of IT Service.

  Event Template
    TBD

  Event Processing Policy
    List of rules which defines system reaction on :term:`events <Event>`.
    All events are matched against list of rules in Event Processing Policy, if
    match is found – configured actions are executed.

  Infrastructure services
    System :term:`container <Container>` which can be used by Administrator to
    define logical structure of the network.

  Management Console
    NetXMS user interface. Available in form of `rich client
    <http://en.wikipedia.org/wiki/Fat_client>`_ for both desktop and mobile or
    as web service.

  Metric
    TBD

  MIB Explorer
    :term:`View` in user interface, which allows to navigate SNMP MIB tree and
    run SNMP walk on :term:`nodes <Node>`.

  Mobile Device Object
    Special type of :term:`Node` that represents monitored mobile device.

  Monitoring Agent
    NetXMS or SNMP agent that provides information to NetXMS Server.

  Network Discovery
    Network investigation in order to find new :term:`nodes <Node>`. There are
    2 types of discovery: active and passive. In passive mode, information
    about new hosts and devices obtained from :term:`ARP` tables and routing
    tables of already known devices. In active discovery mode, NetXMS server
    will send an :term:`ICMP` echo requests to all IP addresses in given range,
    and consider each responding address for adding to database.

  Network Map
    Visual representaion of network topology.

  NetXMS Agent
    NetXMS daemon that is installed on monitored :term:`Node` to provide
    additional monitoring options.

  Node
    :term:`Object` that represents server or device.

  NXSL
    NetXMS Scripting Language.

  Object
    Representation of logical or physical entity.

  Object tool
    Configurable operation that can be executed on :term:`Node`.

  Package Manager
    :term:`View` that manages update packages for NetXMS agents.

  Perspective
    A perspective defines the initial set and layout of views in the Eclipse
    Workbench window.

  Policy
    Configuration parameter set that can be applied on a :term:`Node`.

  Polling
    Polling is process of gathering information by server from nodes. This is
    usually done automatically at specified intervals of time, but can be
    triggered manually also. There are different types of polling: Status,
    Configuration, Topology, Discovery and Routing.

  Proxy Agent
    NetXMS Agent capable of forwarding requests to :term:`nodes <Node>` which
    are not directly accecible to NetXMS server. Agent support proxying of
    native agent protocol as well as SNMP. 

  Push parameter
    Type of :term:`DCI`, where collected data is pushed into the server by the
    agent.

  Subagent
    Extension module (shared library) which can be loaded into NetXMS agent to
    provide additional functionality.

  Template
    A preset of one or more :term:`DCIs <DCI>` that can be applied on
    :term:`Node`.

  Threshold
    Part of :term:`DCI` configuration, which define events to be generated when
    collected value is outside of expected range.

  Trim Stack
    :term:`View Stack` in minimized state, represented as a set of buttons, one
    for each :term:`View` in the stack.

  View
     In the Eclipse Platform a view is typically used to navigate a hierarchy
     of information, open an editor, or display properties for the active
     editor.

  View Stack
    Multiple :term:`views <View>` combined into single one, with tab navigation
    on top of it.

  Zone
    Zone in NetXMS is a group of IP subnets which form non-overlapping IP
    address space. There is always zone 0 which contains subnets directly
    reachable by management server. For all other zones server assumes that
    subnets within that zones are not reachable directly, and proxy must be
    used. It is used to monitor subnets with overlapping IP address space.

  802.1x
    IEEE 802.1X (also known as Dot1x) is an IEEE Standard for Port-based
    Network Access Control (PNAC). It is part of the IEEE 802.1 group of
    networking protocols. It provides an authentication mechanism to
    devices wishing to attach to a :term:`LAN` or WLAN.  More details in
    :wikipedia:`Wikipedia <IEEE 802.1X>`

  ARP
    The Address Resolution Protocol (ARP) is a telecommunication protocol used
    for resolution of network layer addresses into link layer addresses, a
    critical function in multiple-access networks.  More details in
    :wikipedia:`Wikipedia <Address Resolution Protocol>`

  CDP
    Cisco Discovery Protocol is a Cisco proprietary protocol that runs between
    direct connected network entities (routers, switches, remote access
    devices, IP telephones etc.). The purpose of the protocol is to supply a
    network entity with information about its direct connected neighbors.  More
    details in :wikipedia:`Wikipedia <Cisco Discovery Protocol>`.

  GPL
    GNU General Public License. `Full text of the License, version 2
    <http://www.gnu.org/licenses/gpl-2.0.html>`

  GUID
    A Globally Unique Identifier is a unique reference number used as an
    identifier in computer software. More details in :wikipedia:`Wikipedia
    <Globally unique identifier>`

  ICMP
    The Internet Control Message Protocol (ICMP) is one of the main protocols
    of the Internet Protocol Suite. It is used by network devices, like
    routers, to send error messages indicating, for example, that a requested
    service is not available or that a host or router could not be reached.
    More details in :wikipedia:`Wikipedia <Internet Control Message Protocol>`.

  LAN
    A local area network (LAN) is a computer network that interconnects
    computers within a limited area such as a home, school, computer
    laboratory, or office building, using network media. The defining
    characteristics of LANs, in contrast to wide area networks (WANs), include
    their smaller geographic area, and non-inclusion of leased
    telecommunication lines. More details in :wikipedia:`Wikipedia <Local area
    network>`.

  LDAP
    The Lightweight Directory Access Protocol (LDAP) is an open,
    vendor-neutral, industry standard application protocol for accessing and
    maintaining distributed directory information services over an Internet
    Protocol (IP) network. More details in :wikipedia:`Wikipedia <Lightweight
    Directory Access Protocol>`

  LLDP
    The Link Layer Discovery Protocol (LLDP) is a vendor-neutral link layer
    protocol in the Internet Protocol Suite used by network devices for
    advertising their identity, capabilities, and neighbors on an IEEE 802
    local area network, principally wired Ethernet. The protocol is formally
    referred to by the IEEE as Station and Media Access Control Connectivity
    Discovery specified in standards document IEEE 802.1AB.  More details in
    :wikipedia:`Wikipedia <Link Layer Discovery Protocol>`

  MAC address
    A media access control address (MAC address) is a unique identifier
    assigned to network interfaces for communications on the physical network
    segment. MAC addresses are used as a network address for most IEEE 802
    network technologies, including Ethernet and WiFi. Logically, MAC addresses
    are used in the media access control protocol sublayer of the OSI reference
    model. More details in :wikipedia:`Wikipedia <MAC address>`.

  NDP
    The Neighbor Discovery Protocol (NDP) is a protocol in the Internet
    protocol suite used with Internet Protocol Version 6 (IPv6). More details
    in :wikipedia:`Wikipedia <Neighbor Discovery Protocol>`

  RADIUS
    Remote Authentication Dial In User Service (RADIUS) is a networking
    protocol that provides centralized Authentication, Authorization, and
    Accounting (AAA) management for users who connect and use a network
    service.  More details in :wikipedia:`Wikipedia <RADIUS>`

  SMCLP
    Server Management Command Line Protocol

  SNMP
    Simple Network Management Protocol (SNMP) is an "Internet-standard protocol
    for managing devices on IP networks". Devices that typically support SNMP
    include routers, switches, servers, workstations, printers, modem racks and
    more. SNMP is used mostly in network management systems to monitor
    network-attached devices for conditions that warrant administrative
    attention. SNMP is a component of the Internet Protocol Suite as defined by
    the Internet Engineering Task Force (IETF). It consists of a set of
    standards for network management, including an application layer protocol,
    a database schema, and a set of data objects. More details in
    :wikipedia:`Wikipedia <Simple Network Management Protocol>`.

  SNMP Trap
    Asynchronous notification from :term:`SNMP` agent to :term:`SNMP` manager.
    SNMP traps enable an agent to notify the management station of significant
    events by way of an unsolicited SNMP message. More details in
    :wikipedia:`Wikipedia <Simple Network Management Protocol#Trap>`.

  STP
    The Spanning Tree Protocol (STP) is a network protocol that ensures a
    loop-free topology for any bridged Ethernet local area network. The basic
    function of STP is to prevent bridge loops and the broadcast radiation that
    results from them. Spanning tree also allows a network design to include
    spare (redundant) links to provide automatic backup paths if an active link
    fails, without the danger of bridge loops, or the need for manual
    enabling/disabling of these backup links. More details in
    :wikipedia:`Wikipedia <Spanning Tree Protocol>`

  Syslog
    Widely used standard for message logging. More details in
    :wikipedia:`Wikipedia <Syslog>`.
    
  TLS 
    Transport Layer Security is a cryptographic protocols that provide 
    communications security over a computer network. More details in
    :wikipedia:`Wikipedia <Transport Layer Security>`.

  UPS
    An uninterruptible power supply, also uninterruptible power source, UPS or
    battery/flywheel backup, is an electrical apparatus that provides emergency
    power to a load when the input power source, typically mains power, fails.
    More details in :wikipedia:`Wikipedia <Uninterruptible Power Supply>`

  URL
    A uniform resource locator (URL) is a reference to a resource that
    specifies the location of the resource on a computer network and a
    mechanism for retrieving it. More details in :wikipedia:`Wikipedia <Uniform
    resource locator>`

  VLAN
    In computer networking, a single layer-2 network may be partitioned to
    create multiple distinct broadcast domains, which are mutually isolated so
    that packets can only pass between them via one or more routers; such a
    domain is referred to as a virtual local area network, virtual LAN or VLAN.
    More details in :wikipedia:`Wikipedia <Virtual LAN>`.

  VPN
    A virtual private network (VPN) extends a private network across a public
    network, such as the Internet. It enables a computer or network-enabled
    device to send and receive data across shared or public networks as if it
    were directly connected to the private network, while benefiting from the
    functionality, security and management policies of the private network. A
    VPN is created by establishing a virtual point-to-point connection through
    the use of dedicated connections, virtual tunneling protocols, or traffic
    encryptions. Major implementations of VPNs include OpenVPN and IPsec. More
    details in :wikipedia:`Wikipedia <Virtual private network>`.

  VRRP
    The Virtual Router Redundancy Protocol (VRRP) is a computer networking
    protocol that provides for automatic assignment of available Internet
    Protocol (IP) routers to participating hosts. This increases the
    availability and reliability of routing paths via automatic default gateway
    selections on an IP subnetwork. More details in :wikipedia:`Wikipedia
    <Virtual Router Redundancy Protocol>`
