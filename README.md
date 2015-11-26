# Documentation project for NetXMS

Components:
* concept/ - System concept, architecture, and terminology.
* admin/ - In-depth administrator guide.
* developer/ - Describes development process and possible ways of extending NetXMS.
* manpages/ - UNIX man pages.

# Notes
## Local setup
* mkvirtualenv sphinx
* workon sphinx
* pip install -r requirements.txt

## Automatic rebuild and reload
* cd admin && sphinx-autobuild . _build_html

## Building translated version:
* make gettext
* sphinx-intl update -p _build/locale -l ru
* sphinx-intl build
* make -e SPHINXOPTS="-D language=ru" html

# Useful links

http://sphinx-doc.org/markup/para.html
http://sphinx-doc.org/markup/inline.html
http://sphinx-doc.org/markup/
