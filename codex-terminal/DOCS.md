# Codex Terminal

This add-on runs the Codex CLI worker through Home Assistant Ingress.

## Security boundaries

- No LAN ports are published.
- Host networking, host PID, privileged mode, Docker API, and Supervisor API are disabled.
- The worker stores runtime data under `/data`.
- The Home Assistant configuration is mounted for the worker, but Codex starts in
  `read-only` sandbox mode.
- Write-capable tasks require both `codex_sandbox: workspace-write` and
  `maintenance_authorized: true`.
- The worker redacts sensitive values in task output and logs where applicable.

## Installation

Add the public repository to the Home Assistant add-on store, install the
Codex Terminal add-on, and start it through Ingress. The first login uses
`codex login --device-auth`.

## Maintenance procedure

1. Create a backup.
2. Keep the add-on in diagnostic mode while reviewing the problem.
3. Enable both maintenance options only for an approved change.
4. Ask Codex to make one focused change.
5. Review the reported files and validation result.
6. Return both options to their diagnostic defaults.

Do not paste `secrets.yaml`, tokens, passwords, cookies, or complete credential
URLs into the chat or task history.
