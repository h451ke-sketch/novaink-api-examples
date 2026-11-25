# NovaInk AI — Unified Multimodal AI API Examples (930+ Models)

[![Website](https://img.shields.io/badge/Website-novaink.ai-0284c7?style=flat-square)](https://novaink.ai/)
[![Models](https://img.shields.io/badge/Live_Models-930%2B-0f766e?style=flat-square)](https://novaink.ai/pricing)
[![Guides](https://img.shields.io/badge/Guides-Claude_Code_%7C_Veo_3.1_%7C_Cursor-0f172a?style=flat-square)](https://novaink.ai/guides)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)

Production-ready starter templates for calling **930+ frontier text, coding, image, audio, and video AI models** through a single unified API key (`sk-`) with native **OpenAI**, **Anthropic**, and **Gemini** protocol compatibility.

![Unified AI Client Architecture](https://novaink.ai/novaink-assets/blog/02_diag_unified_clients.png)

## Quick Reference — Endpoints & Protocols

| Protocol | Compatible Clients / SDKs | Base URL |
| --- | --- | --- |
| **OpenAI Compatible** | OpenAI Python/Node SDK, Cherry Studio, Cursor, VSCode Cline, Dify, LobeChat | `https://novaink.ai/v1` |
| **Anthropic Native** | Claude Code CLI, Anthropic SDK, CC Switch (`Prompt Caching` enabled) | `https://novaink.ai` *(no trailing `/v1`)* |
| **Async Video API** | Veo 3.1, Kling, Seedance 2.5, Vidu Q3, Grok Video (`POST /v1/videos`) | `https://novaink.ai/v1/videos` |

## What's Inside

- `claude-code/` — One-line environment setup & `~/.claude/settings.json` for **Claude Code** (`claude-opus-4-6`, `claude-sonnet-4-5-20250929`, `claude-haiku-4-5-20251001`) with native `/v1/messages` Prompt Caching.
- `python/chat_openai_sdk.py` — Streaming chat completions using the official `openai` Python SDK (`gpt-5`, `deepseek-r1`, `gemini-2.5-pro`).
- `python/video_async_polling.py` — Production async video pipeline (`POST /v1/videos` → exponential backoff polling → multi-model fallback across `veo3.1-fast`, `doubao-seedance-2.5`, and `kling-v2-master`).

![Multimodal Async Video Pipeline](https://novaink.ai/novaink-assets/blog/01_diag_video_pipeline.png)

## 2-Line Claude Code Quickstart

```bash
export ANTHROPIC_BASE_URL="https://novaink.ai"
export ANTHROPIC_AUTH_TOKEN="sk-your-api-key"

claude
```

## Full Documentation & Guides

- **Live Model Catalog & Transparent 1x Pricing**: [https://novaink.ai/pricing](https://novaink.ai/pricing)
- **Claude Code API Setup & Troubleshooting**: [https://novaink.ai/guides/claude-code-api](https://novaink.ai/guides/claude-code-api)
- **Veo 3.1 / Kling / Seedance 2.5 Video API Guide**: [https://novaink.ai/guides/veo-kling-video-api](https://novaink.ai/guides/veo-kling-video-api)
- **Cherry Studio / Cursor / Dify / LobeChat Setup**: [https://novaink.ai/guides/cherry-studio-cursor](https://novaink.ai/guides/cherry-studio-cursor)

## License

MIT — Feel free to fork, customize, and use with any OpenAI-compatible or Anthropic-native API gateway.
