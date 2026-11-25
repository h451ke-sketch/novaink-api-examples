#!/usr/bin/env bash
set -euo pipefail

if [ -z "${NOVAINK_API_KEY:-}" ]; then
  echo "Usage: NOVAINK_API_KEY=sk-xxx ./setup.sh"
  exit 1
fi

export ANTHROPIC_BASE_URL="https://novaink.ai"
export ANTHROPIC_AUTH_TOKEN="$NOVAINK_API_KEY"

echo "Starting Claude Code via NovaInk AI native Anthropic gateway..."
exec claude "$@"
