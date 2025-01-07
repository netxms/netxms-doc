# Documentation project for NetXMS

This repository contains the source files for the official [NetXMS](https://netxms.com) documentation.

NXSL (scripting) documentation sources are in the [separate repository](https://github.com/netxms/nxsl-doc).

Components of the documentation are stored in the following directories:

- concept/ - System concept, architecture, and terminology (partially outdated and moved to admin guide).
- admin/ - In-depth administrator guide.
- developer/ - Describes development process and possible ways of extending NetXMS.
- manpages/ - UNIX man pages.

# Notes

## Prerequisites

### macOS

```shell
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install latexmk capt-of ellipse fncychap framed needspace pict2e tabulary tex-gyre titlesec varwidth wrapfig gnu-freefont
```

### Ubuntu/Mint

```shell
apt install python3-pip python3-virtualenv latexmk texlive-latex-extra git
```

## Preparing the environment

```shell
git clone https://github.com/netxms/netxms-doc

python3 -m venv sphinx # create virtualenv, do it once
source sphinx/bin/activate # activate virtualenv
pip3 install -r requirements.txt # install dependencies, do it once
```

## Building locally

```shell
cd netxms-doc
source sphinx/bin/activate # activate virtualenv
make html pdf
```

## Automatic rebuild and reload

```shell
cd netxms-doc
cd admin
sphinx-autobuild -b html . _build/html
```

## Building translated version:

Note: translated documentation is not updated anymore and is kept for reference only.

```shell
make gettext
sphinx-intl update -p _build/locale -l ru
sphinx-intl build
make -e SPHINXOPTS="-D language=ru" html
```

# Useful links

http://sphinx-doc.org/markup/para.html

http://sphinx-doc.org/markup/inline.html

http://sphinx-doc.org/markup/
