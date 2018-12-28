# -*- coding: utf-8 -*-
'''
Sphinx/docutils extension to create links to Wikipedia articles.

    :wikipedia:`Sphinx`

    :wikipedia:`mythical creature <Sphinx>`

    :wikipedia:`:zh:斯芬克斯`

    :wikipedia:`Answer to the Ultimate Question of Life, the Universe, and Everything <:de:42 (Antwort)>`

'''

import re
import urllib.request, urllib.parse, urllib.error
from docutils import nodes, utils
from sphinx.util.nodes import split_explicit_title

base_url = 'http://%s.wikipedia.org/wiki/'
def make_wikipedia_link(name, rawtext, text, lineno, inliner,
                      options={}, content=[]):
    env = inliner.document.settings.env
    lang =  env.config.wikipedia_lang

    text = utils.unescape(text)
    has_explicit, title, target = split_explicit_title(text)
 
    m = re.match(r'\:(.*?)\:(.*)', target)
    if m:
        lang, target = m.groups()
        if not has_explicit:
            title = target
    ref = base_url % lang + urllib.parse.quote(target.replace(' ', '_').encode('utf8'), safe='')

    node = nodes.reference(rawtext, title, refuri=ref, **options)
    return [node],[]

def setup(app):
    app.add_config_value('wikipedia_lang', 
                         'en', 
                         'env')
    app.add_role('wikipedia', make_wikipedia_link)
