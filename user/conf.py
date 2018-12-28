# -*- coding: utf-8 -*-
exec(compile(open('../conf.py').read(), '../conf.py', 'exec'))
# -- General -------------------------------------------------------------------
project = '%s User Guide' % product_name

# -- Options for HTML output ---------------------------------------------------
html_title = "%s (%s)" % (project, release)

# -- Options for LaTeX output --------------------------------------------------
latex_documents = [
    ('index', '%s-user.tex' % product_key, project, project_author, 'manual'),
]

# -- Options for Epub output ----------------------------------------------
epub_title = project
