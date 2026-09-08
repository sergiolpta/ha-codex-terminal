# Codex Terminal

Private Home Assistant add-on that exposes a web terminal through Home Assistant Ingress and includes the Codex CLI.

This first version is for diagnostics only:

- Ingress enabled
- No public ports
- `/config` mounted read-only
- Codex credentials persisted under `/data/codex`
- No host access
- No Docker socket
- No privileged mode
- No Home Assistant or Supervisor API token

## First Run

Open the add-on through the Home Assistant sidebar and run:

```bash
codex login --device-auth
```

Then open the device login URL on your computer, enter the code, and sign in with ChatGPT.

After login:

```bash
codex login status
codex --version
codex
```

## Recommended First Prompt

```text
Analise a estrutura de ./config e os logs disponíveis. Não altere arquivos, não reinicie serviços e não exponha valores de segredos. Produza um relatório com achados, evidências e recomendações priorizadas.
```

## Notes

This version can read files and logs available inside `/config`, including `home-assistant.log`.

Supervisor and add-on logs are not enabled in this version because that typically requires broader Supervisor API permissions. A later version can add that deliberately if the benefit outweighs the added administrative access.
