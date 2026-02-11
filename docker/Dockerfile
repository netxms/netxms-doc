FROM debian:13

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-pip \
       python3-venv \
       python3.13-venv \
       latexmk \
       texlive-fonts-recommended \
       texlive-latex-extra \
       texlive-xetex \
       xindy \
       fonts-freefont-otf \
       make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

ENV PATH="/opt/venv/bin:$PATH"
