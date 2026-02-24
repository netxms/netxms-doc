# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Official documentation for [NetXMS](https://netxms.com) network monitoring system. Built with Sphinx and reStructuredText, producing HTML and PDF outputs. NXSL (scripting language) docs live in a [separate repository](https://github.com/netxms/nxsl-doc).

## Build Commands

```shell
uv sync                        # install dependencies (one-time setup)
uv run make html               # build all HTML docs
uv run make pdf                # build all PDFs (requires LaTeX toolchain)
uv run make clean              # clean all build artifacts
uv run make man                # build man pages
```

Build a single guide (faster iteration):
```shell
cd admin && uv run make html   # build only admin guide
cd user && uv run make html    # build only user guide
```

Live reload during editing:
```shell
cd admin && uv run sphinx-autobuild -b html . _build/html
```

Docker build:
```shell
make docker                    # build the Docker image
make docker-push               # build and push multi-arch image
```

## Repository Structure

Each guide is a self-contained Sphinx project in its own directory, with its own `conf.py`, `Makefile`, and `index.rst`:

- **admin/** — Administrator Guide (the largest and most actively maintained section)
- **user/** — User Guide (management console, objects, topology)
- **concept/** — Architecture and terminology (partially outdated, content migrating to admin/)
- **developer/** — Development and extension docs
- **manpages/** — UNIX man pages

### Shared Configuration

- **conf.py** (root) — Shared Sphinx config executed by each guide's `conf.py` via `exec(open("../conf.py").read())`. Contains version numbers, theme settings, LaTeX options, and the custom `wikipedia` extension.
- **_lib/wikipedia.py** — Custom Sphinx role `:wikipedia:\`Article Name\`` for linking to Wikipedia.
- **_lib/plantuml.jar** — PlantUML for diagrams.
- Build output goes to `<guide>/_build/` (gitignored).

### Key conf.py Variables

- `version` / `release` — documentation version, set in root `conf.py`
- `product_name` — defaults to "NetXMS", overridable via `PRODUCT` env var (for enterprise edition builds)
- `release_type` — set to `'oss'` or `'ee'` based on `product_name`
- `MODULES` env var — comma-separated list of custom module directories to include

## Writing Conventions

- All content is **reStructuredText** (.rst files)
- Use `|product_name|` substitution instead of hardcoding "NetXMS"
- The `:wikipedia:` role is available for linking Wikipedia articles: `:wikipedia:\`Article Title\``
- Images go in `<guide>/_images/`
- Static assets (CSS overrides) go in `<guide>/_static/`

## CI/CD

Drone CI pipeline (`.drone.yml`) on master push: builds HTML + PDF, deploys via SFTP, notifies via Telegram.
