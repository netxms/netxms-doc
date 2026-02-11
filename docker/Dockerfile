FROM debian:13

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       latexmk \
       texlive-fonts-recommended \
       texlive-latex-extra \
       texlive-xetex \
       xindy \
       fonts-freefont-otf \
       make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev

ENV PATH="/build/.venv/bin:$PATH"
