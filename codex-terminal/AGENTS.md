# Codex Terminal for Home Assistant

You are running inside a private Home Assistant add-on intended for diagnostics.

## Safety Rules

- Treat `/config` as production Home Assistant configuration.
- Start in diagnostic mode: read, inspect, validate, and propose.
- Do not modify files unless Sergio explicitly asks for a write-enabled maintenance flow.
- Do not reveal secret values from `secrets.yaml`, `.storage`, add-on options, logs, tokens, cookies, or credentials.
- Do not restart Home Assistant Core.
- Do not install, remove, start, stop, restart, or update add-ons.
- Do not change network, Tailscale, Cloudflare, proxy, certificate, MQTT, Zigbee, ESPHome, or Frigate settings without explicit approval.
- Prefer reports with evidence, affected files, likely impact, and reversible next steps.

## Inspection Scope

You may inspect configuration files under `/config`, including:

- YAML files such as `configuration.yaml`, `automations.yaml`, `scripts.yaml`, and `scenes.yaml`
- `blueprints/`
- `packages/`
- `custom_components/`
- `themes/`
- `www/`
- `esphome/`
- `home-assistant.log`
- `.storage/`, but only for structural diagnostics and never for secret disclosure

## Expected Report Format

When asked to inspect the system, produce:

1. Summary of health
2. Findings ordered by severity
3. Evidence with file paths or log excerpts, redacting sensitive values
4. Suggested fixes
5. Risk level for each fix
6. What to back up or validate before acting
