# -*- coding: utf-8 -*-
exec(open("../conf.py").read())
# -- General -------------------------------------------------------------------
project = '%s Developer Guide' % product_name

# -- Options for HTML output ---------------------------------------------------
html_title = "%s (%s)" % (project, release)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', '%s-developer.tex' % product_key, project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
