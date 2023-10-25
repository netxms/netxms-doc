# -*- coding: utf-8 -*-
import sys
import sphinx.builders.manpage
import docutils.nodes
import os
import glob
from os.path import basename

# -- General configuration ------------------------------------------------
product_name = os.environ.get('PRODUCT', 'NetXMS')
product_key = product_name.replace(' ', '-').lower()
rst_epilog = '.. |product_name| replace:: %s' % product_name

print((os.path.abspath('../_lib')))
sys.path.insert(0, os.path.abspath('../_lib'))

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'wikipedia',
]

templates_path = ['../_templates']

source_suffix = '.rst'
master_doc = 'index'

project_author = "Raden Solutions, SIA"
copyright = '2023, ' + project_author

version = '4.4'
release = '4.4.3'

exclude_patterns = ['build']

pygments_style = 'sphinx'

locale_dirs = ['_locale']

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------
html_short_title = "Home"

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    html_theme = 'default'
else:
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'

#html_logo = '_images/logo.png'
html_favicon = '../favicon.ico'
html_static_path = ['_static']
html_show_sourcelink = False
html_show_sphinx = False
#html_show_copyright = True

html_js_files = [('https://stats.raden.solutions/script.js', {'async': 'async', 'data-website-id':'e5a25886-8178-4d34-860f-f8cb9009a7e7'})]

# -- Options for LaTeX output ---------------------------------------------
#    'figure_align': 'H', - to avoid image floating to next page if it does not fit
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '8t',
    'figure_align': 'H',
}

#latex_elements = {
#    'papersize': '',
#    'fontpkg': '',
#    'fncychap': '',
#    'maketitle': '\\cover',
#    'pointsize': '',
#    'preamble': '',
#    'releasename': "",
#    'babel': '',
#    'printindex': '',
#    'fontenc': '',
#    'inputenc': '',
#    'classoptions': '',
#    'utf8extra': '',
#}
#latex_additional_files = ["../netxms.sty" ]

latex_show_pagerefs = False
latex_domain_indices = False
latex_use_modindex = False

#latex_logo = '_images/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -- PlantUML settings ---------------------------------------------------------

plantuml = '/usr/bin/java -Djava.awt.headless=true -jar ../_lib/plantuml.jar'
plantuml_latex_output_format = 'pdf'

# -- Custom code ---------------------------------------------------------------
def add_man_header_nodes(app, doctree, docname):
    if isinstance(app.builder, sphinx.builders.manpage.ManualPageBuilder):
        doctree.insert(0, docutils.nodes.raw('', '.if n .ad l\n.nh\n', format='manpage'))

def setup(app):
    # fix hyphenation in generated man pages
    app.connect('doctree-resolved', add_man_header_nodes)

    # ignore custom modules except listed in $MODULES
    modules = os.environ['MODULES'].split(',') if 'MODULES' in os.environ else []
    extDirs = glob.glob('source/extensions/*')
    for module in modules:
        extDirs = [d for d in extDirs if module.strip() not in d]
    for d in extDirs:
        exclude_patterns.append(d[7:]) # remove 'source/'

    app.add_css_file("theme_overrides.css")
    if product_name == 'NetXMS':
        app.add_config_value('release_type', 'oss', 'env')
    else:
        app.add_config_value('release_type', 'ee', 'env')

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_author = project_author
epub_publisher = project_author
epub_copyright = copyright

epub_theme = 'epub'

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


