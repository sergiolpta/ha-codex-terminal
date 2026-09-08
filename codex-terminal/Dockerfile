ARG BUILD_VERSION=0.1.0
ARG BUILD_ARCH=amd64

FROM ghcr.io/home-assistant/base:latest

ARG BUILD_VERSION
ARG BUILD_ARCH

LABEL \
  io.hass.version="${BUILD_VERSION}" \
  io.hass.type="app" \
  io.hass.arch="${BUILD_ARCH}"

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN \
  apk add --no-cache \
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
    yq \
  && npm install -g @openai/codex \
  && mkdir -p /run/nginx /etc/nginx/http.d /opt/codex-terminal

COPY run.sh /run.sh
COPY nginx.conf /etc/nginx/http.d/default.conf
COPY AGENTS.md /opt/codex-terminal/AGENTS.md

RUN chmod +x /run.sh

CMD ["/run.sh"]
