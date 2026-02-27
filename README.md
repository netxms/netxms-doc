# Documentation project for NetXMS

This repository contains the source files for the official [NetXMS](https://netxms.com) documentation.

NXSL (scripting) documentation sources are in the [separate repository](https://github.com/netxms/nxsl-doc).

Components of the documentation are stored in the following directories:

- admin/ - In-depth [administrator guide](https://netxms.org/documentation/adminguide/).
- concept/ - System concept, architecture, and terminology (partially outdated and moved to admin guide).
- developer/ - Describes development process and possible ways of extending NetXMS.
- user/ - [User guide](https://netxms.org/documentation/userguide/) covering basic concepts, management console, objects, and topology.
- manpages/ - UNIX man pages.

# Notes

## Prerequisites

To manage the Python environment and dependencies, you need to install [uv](https://docs.astral.sh/uv/getting-started/installation/).

### macOS

```shell
brew install --cask basictex
sudo tlmgr update --self
sudo tlmgr install latexmk capt-of ellipse fncychap framed needspace pict2e tabulary tex-gyre titlesec varwidth wrapfig gnu-freefont
```

### Ubuntu/Mint

```shell
apt install python3-pip python3-virtualenv latexmk texlive-latex-extra texlive-xetex xindy git
```

## Preparing the environment

```shell
git clone https://github.com/netxms/netxms-doc
cd netxms-doc
uv sync
```

## Building locally

```shell
uv run make html pdf
```

## Automatic rebuild and reload

```shell
cd admin
uv run sphinx-autobuild -b html . _build/html
```

## Building with Docker

```shell
make docker        # build the Docker image
make docker-push   # build and push multi-arch image
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

https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html

https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html

https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
