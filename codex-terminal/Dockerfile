ARG BUILD_FROM=ghcr.io/home-assistant/base:latest
FROM ${BUILD_FROM}

ARG BUILD_VERSION=dev
ARG BUILD_ARCH=amd64

LABEL \
    io.hass.version="${BUILD_VERSION}" \
    io.hass.type="app" \
    io.hass.arch="${BUILD_ARCH}"

RUN apk add --no-cache \
    bash \
    ca-certificates \
    curl \
    git \
    jq \
    nano \
    nginx \
    nodejs \
    npm \
    ripgrep \
    ttyd \
    yq

RUN npm install -g @openai/codex

WORKDIR /opt/codex-terminal
COPY run.sh /opt/codex-terminal/run.sh
COPY nginx.conf /opt/codex-terminal/nginx.conf
COPY AGENTS.md /opt/codex-terminal/AGENTS.md

RUN chmod +x /opt/codex-terminal/run.sh

CMD ["/opt/codex-terminal/run.sh"]
