# -*- coding: utf-8 -*-
exec(compile(open('../conf.py').read(), '../conf.py', 'exec'))
# -- General -------------------------------------------------------------------
project = 'User Manual'

# -- Options for HTML output ---------------------------------------------------
html_title = "NetXMS %s %s" % (release, project)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', 'netxms-user.tex', 'NetXMS %s' % project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
