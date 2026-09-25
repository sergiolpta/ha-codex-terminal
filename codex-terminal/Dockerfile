FROM ghcr.io/openai/codex-cli-worker:0.1.56

RUN install -D -m 0755 /usr/bin/bwrap /opt/codex-sandbox/bwrap.real

COPY codex-bwrap /opt/codex-sandbox/bwrap
COPY codex-bwrap-probe.py /opt/codex-sandbox/codex-bwrap-probe.py
COPY server.py /server.py
COPY run-worker.sh /run.sh

RUN chmod 0755 /opt/codex-sandbox/bwrap /opt/codex-sandbox/codex-bwrap-probe.py /run.sh

ENV PATH="/opt/codex-sandbox:${PATH}"
