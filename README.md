# Documentation project for NetXMS

Components:

-   concept/ - System concept, architecture, and terminology.
-   admin/ - In-depth administrator guide.
-   developer/ - Describes development process and possible ways of extending NetXMS.
-   manpages/ - UNIX man pages.

# Notes

## Local setup

-   mkvirtualenv sphinx
-   workon sphinx
-   pip install -r requirements.txt

## Ubuntu/Mint

-   apt install python3-pip python3-virtualenv latexmk texlive-latex-extra git
-   git clone https://github.com/netxms/netxms-doc
-   cd netxms-doc
-   python3 -m virtualenv .
-   . bin/activate # activate virtualenv
-   pip install -r requirements.txt

## macOS specific

-   brew cask install basictex
-   sudo tlmgr update --self
-   sudo tlmgr install latexmk fncychap titlesec tabulary varwidth framed wrapfig capt-of needspace helvetic courier letltxmacro tex-gyre

## Automatic rebuild and reload

-   cd admin && sphinx-autobuild . \_build_html

## Building translated version:

-   make gettext
-   sphinx-intl update -p \_build/locale -l ru
-   sphinx-intl build
-   make -e SPHINXOPTS="-D language=ru" html

# Useful links

http://sphinx-doc.org/markup/para.html
http://sphinx-doc.org/markup/inline.html
http://sphinx-doc.org/markup/
