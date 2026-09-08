#!/usr/bin/env bash
set -euo pipefail

export HOME=/data/home
export CODEX_HOME=/data/codex
export SHELL=/bin/bash

mkdir -p "$HOME" "$CODEX_HOME" /data/workspace

cp /opt/codex-terminal/AGENTS.md /data/workspace/AGENTS.md
ln -sfn /config /data/workspace/config

cat >/data/workspace/README.txt <<'EOF'
Codex Terminal for Home Assistant

Start here:
  codex login --device-auth
  codex

This add-on mounts /config as read-only. It is intended for diagnostics,
inspection, and recommendations before any configuration change is made.
Use the ./config shortcut to inspect Home Assistant files.
EOF

cd /data/workspace

ttyd --interface 127.0.0.1 --port 7681 --writable --terminal-type xterm-256color /bin/bash &

exec nginx -g "daemon off;"
