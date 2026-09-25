# Authorization Model

This branch prepares the next Codex Terminal version. The current runtime remains
diagnostic-only: `/config` is mounted read-only and no maintenance write mode is
enabled yet.

## Intended modes

- **Diagnostic (default):** Codex can inspect `/config`, but cannot modify it.
- **Authorized maintenance:** a deliberate user action enables a temporary
  write-capable session for an approved task.

## Required safeguards before maintenance mode is implemented

1. Require an explicit confirmation immediately before enabling writes.
2. Keep diagnostic mode as the default after installation and restart.
3. Create a backup or recoverable snapshot before the first write.
4. Show the files targeted for change before applying them.
5. Validate Home Assistant configuration after changes.
6. Redact secrets from terminal output, reports, and task logs.
7. Provide a clear way to return to diagnostic-only mode.

This document describes the target behavior. It does not enable write access by
itself.
