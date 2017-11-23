# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = u'man pages'

exclude_patterns = [
    'man/template.rst',
]

# -- Options for manual page output --------------------------------------------
# (source start file, name, description, authors, manual section).
authors = [
    [u'Alex Kirhenshtein <alk@netxms.org>'],
]

man_pages = [
    # man5
    ('man/5/netxmsd-conf', 'netxmsd.conf',
        u'configuration file for NetXMS daemon', authors[0], 5),
    ('man/5/nxagentd-conf', 'nxagentd.conf',
        u'configuration file for NetXMS agent', authors[0], 5),
    # man8
    ('man/8/netxmsd', 'netxmsd', u'NetXMS daemon', authors[0], 8),
    ('man/8/nxdbmgr', 'nxdbmgr', u'NetXMS database manager', authors[0], 8),
]

# If true, show URL addresses after external links.
#man_show_urls = False
