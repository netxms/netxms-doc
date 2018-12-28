# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = 'Administrator Guide'

# -- Options for HTML output ---------------------------------------------------
html_title = "NetXMS %s %s" % (release, project)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', 'netxms-admin.tex', 'NetXMS %s' % project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
