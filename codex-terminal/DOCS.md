# Codex Terminal

Codex Terminal is a private diagnostic add-on for Home Assistant.

## What It Can Read

The add-on mounts Home Assistant configuration at `./config` in read-only mode. This includes the normal configuration tree:

- YAML files
- automations
- scripts
- scenes
- blueprints
- packages
- themes
- custom components
- ESPHome files under `esphome/`
- `home-assistant.log`, when present

## What It Cannot Do In This Version

- It cannot write to `/config`.
- It cannot restart Home Assistant.
- It cannot install, update, start, stop, or remove add-ons.
- It does not receive Home Assistant API access.
- It does not receive Supervisor API access.
- It does not receive Docker socket access.
- It does not run in privileged mode.

## First Login

Run:

```bash
codex login --device-auth
```

Then open the device login URL on your computer and sign in with ChatGPT.

## First Diagnostic Prompt

```text
Analise a estrutura de ./config e os logs disponíveis. Não altere arquivos, não reinicie serviços e não exponha valores de segredos. Produza um relatório com achados, evidências e recomendações priorizadas.
```

## About Supervisor and Add-on Logs

This version intentionally does not request Supervisor API access. Reading Supervisor and add-on logs through the Supervisor would require broader administrative permissions than this diagnostic version should have.
