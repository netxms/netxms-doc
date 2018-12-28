# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = 'man pages'

exclude_patterns = [
    'man/template.rst',
]

# -- Options for manual page output --------------------------------------------
# (source start file, name, description, authors, manual section).
authors = [
    ['Alex Kirhenshtein <alk@netxms.org>'],
]

man_pages = [
    # man5
    ('man/5/netxmsd-conf', 'netxmsd.conf',
        'configuration file for NetXMS daemon', authors[0], 5),
    ('man/5/nxagentd-conf', 'nxagentd.conf',
        'configuration file for NetXMS agent', authors[0], 5),
    # man8
    ('man/8/netxmsd', 'netxmsd', 'NetXMS daemon', authors[0], 8),
    ('man/8/nxdbmgr', 'nxdbmgr', 'NetXMS database manager', authors[0], 8),
]

# If true, show URL addresses after external links.
#man_show_urls = False
