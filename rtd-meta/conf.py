# -*- coding: utf-8 -*-
import sys
import os
import shlex

# -- General configuration ------------------------------------------------

source_suffix = '.rst'
master_doc = 'index'

project = u'NetXMS'
copyright = u'2015, SIA Raden Solutions'
author = u'SIA Raden Solutions'

version = '1.0'
release = '1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'NetXMSdoc'
