# Changelog

## 0.1.0

- Initial private diagnostic version.
- Adds Codex CLI inside a Home Assistant Ingress terminal.
- Mounts Home Assistant configuration as read-only.
- Stores Codex login state under `/data/codex`.
- Avoids host access, Docker access, privileged mode, Home Assistant API, and Supervisor API.
