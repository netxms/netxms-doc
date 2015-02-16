# -*- coding: utf-8 -*-
execfile('../../conf.py')
# -- General -------------------------------------------------------------------
exclude_patterns = [
    'man/template.rst',
]
# -- Options for HTML output ---------------------------------------------------
html_title = "NetXMS %s Administrator Guide" % (release, )

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', 'netxms-admin.tex', u'NetXMS Administrator Guide', u'SIA Raden Solutions', 'manual'),
]

# -- Options for manual page output --------------------------------------------
# (source start file, name, description, authors, manual section).
authors = [
    [u'SIA Raden Solutions <info@netxms.org>'],
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
