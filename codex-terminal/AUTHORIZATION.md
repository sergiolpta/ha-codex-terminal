# Authorization Model

The add-on has two operating modes.

## Diagnostic mode

This is the default:

- `codex_sandbox: read-only`
- `maintenance_authorized: false`
- Codex can inspect `/config`, but cannot modify it.
- Worker runtime data is kept under `/data`.

## Authorized maintenance mode

Enable both options deliberately in the add-on configuration:

- `codex_sandbox: workspace-write`
- `maintenance_authorized: true`

Both switches are required. If either one is missing, the worker falls back to
`read-only`. Direct worker routes that can write `AGENTS.md` or save a
dashboard use the same gate.

Before enabling maintenance:

1. Make a Home Assistant backup.
2. Describe the files and intended changes.
3. Confirm the change is limited and reversible.

After maintenance:

1. Validate the Home Assistant configuration.
2. Review the changed files.
3. Set `codex_sandbox` back to `read-only`.
4. Set `maintenance_authorized` back to `false`.
5. Restart the add-on.

This gate is an add-on-level authorization. It does not authorize Home Assistant
Core restarts, add-on management, network changes, or disclosure of secrets.
