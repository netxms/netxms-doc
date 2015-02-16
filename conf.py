# -*- coding: utf-8 -*-
# -- Imports -------------------------------------------------------------------
import sys
import sphinx.builders.manpage
import docutils.nodes
import os
import glob
from os.path import basename

# -- General -------------------------------------------------------------------
sphinx_version='1.0'

print os.path.abspath('../../lib')
sys.path.insert(0, os.path.abspath('../../lib'))
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'patched.sphinxcontrib.plantuml',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'NetXMS'
copyright = u'2014, SIA Raden Solutions'

# The short X.Y version.
version = '2.0'
# The full version, including alpha/beta/rc tags.
release = '2.0-M2'

pygments_style = 'sphinx'

#todo_include_todos=True # Should be enabled only for unreleased documents

exclude_patterns = []
# -- Options for HTML output ---------------------------------------------------
html_theme = 'nature'
#html_logo = '_images/logo.png'
html_favicon = 'favicon.ico'
html_static_path = ['_static']
html_show_sourcelink = False
html_show_sphinx = False
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# -- Options for LaTeX output --------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    #'pointsize': '10pt',
}

#latex_logo = '_images/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# -- PlantUML settings ---------------------------------------------------------

plantuml = '/usr/bin/java -Djava.awt.headless=true -jar ../lib/plantuml.jar'
plantuml_latex_output_format = 'pdf'

# -- Custom code ---------------------------------------------------------------
def add_man_header_nodes(app, doctree, docname):
    if isinstance(app.builder, sphinx.builders.manpage.ManualPageBuilder):
        doctree.insert(0, docutils.nodes.raw('', '.if n .ad l\n.nh\n', format='manpage'))

def setup(app):
    # fix hyphenation in generated man pages
    app.connect('doctree-resolved', add_man_header_nodes)

    # ignore custom modules except listed in $MODULES
    modules = os.environ['MODULES'].split(',') if os.environ.has_key('MODULES') else []
    extDirs = glob.glob('source/extensions/*')
    for module in modules:
        extDirs = [d for d in extDirs if module.strip() not in d]
    for d in extDirs:
        exclude_patterns.append(d[7:]) # remove 'source/'
