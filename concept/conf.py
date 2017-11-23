# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = u'Contept Guide'

# -- Options for HTML output ---------------------------------------------------
html_title = "NetXMS %s %s" % (release, project)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', 'netxms-concept.tex', u'NetXMS %s' % project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
