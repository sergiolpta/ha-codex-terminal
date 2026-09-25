# Codex Terminal

Home Assistant add-on for Codex diagnostics and explicitly authorized maintenance through Home Assistant Ingress.

## Security model

The default mode is diagnostic-only:

- `/config` is available to the worker, but Codex runs with `read-only` sandboxing.
- `maintenance_authorized` defaults to `false`.
- No public LAN ports, host network, Docker socket, privileged mode, or Supervisor API token.
- Secrets must not be copied into prompts, reports, logs, or GitHub.

Maintenance requires both add-on options to be changed deliberately:

- `codex_sandbox: workspace-write`
- `maintenance_authorized: true`

After maintenance, return both options to the diagnostic defaults and restart the add-on. The worker rejects unsupported sandbox modes and protects its direct configuration-writing routes with the same authorization gate.

## First run

1. Install the add-on from the repository.
2. Start it and open it through Home Assistant Ingress.
3. Run `codex login --device-auth` in the worker UI.
4. Confirm the login with ChatGPT device authorization.
5. Keep the add-on in diagnostic mode for inspections.

## Diagnostic prompt

```text
Analise a estrutura de ./config e os logs disponíveis. Não altere arquivos, não reinicie serviços e não exponha valores de segredos. Produza um relatório com achados, evidências e recomendações priorizadas.
```

The add-on does not automatically authorize maintenance or restart Home Assistant.
