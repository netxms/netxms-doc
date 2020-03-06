.. _ssh-monitoring:

==============
SSH monitoring
==============

NetXMS can execute commands via SSH connection and save the output as DCI values.

SSH connection are always established via agent. For this to work, ``ssh.nsm`` subagent should be enabled in agent config file. 

If zoning is not used, agent running on |product_name| server is used for SSH connections.

If zoning is used, zone proxies are used (and if a zone has no proxied configured, agent on |product_name| server is used as last resort)

Only first line of the output is stored as DCI value.

For numeric data type DCIs the output is parsed from beginning till first non-numeric character.
