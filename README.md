# NovaInk AI API Examples (`novaink.ai`)

Minimal, production-ready starter templates for calling **930+ frontier AI models** (GPT-5, Claude Opus 4.6, Claude Sonnet 4.5, Gemini 2.5 Pro, DeepSeek R1, Veo 3.1, Kling, Seedance 2.5, Vidu Q3, GPT Image 1, Flux Pro) through one unified API key on **[NovaInk AI](https://novaink.ai/)**.

- 🌐 **Homepage**: [https://novaink.ai/](https://novaink.ai/)
- 📖 **Developer Docs**: [https://novaink.ai/docs](https://novaink.ai/docs)
- 🛠️ **Claude Code Setup Guide**: [https://novaink.ai/guides/claude-code-api](https://novaink.ai/guides/claude-code-api)
- 🎬 **Veo 3.1 / Kling / Seedance Video Guide**: [https://novaink.ai/guides/veo-kling-video-api](https://novaink.ai/guides/veo-kling-video-api)
- 💻 **Cherry Studio / Cursor / Dify Guide**: [https://novaink.ai/guides/cherry-studio-cursor](https://novaink.ai/guides/cherry-studio-cursor)
- 💰 **Live Model Pricing**: [https://novaink.ai/pricing](https://novaink.ai/pricing)

## Quickstart

1. Sign in with Google or GitHub at [novaink.ai/sign-in](https://novaink.ai/sign-in) to claim **$0.20 free trial credits**.
2. Create an `sk-` API key at [novaink.ai/keys](https://novaink.ai/keys).
3. Export your key:
   ```bash
   export NOVAINK_API_KEY="sk-your-key-here"
   ```

## Examples Included

| Path | Description |
|---|---|
| `claude-code/setup.sh` | 2-line native Anthropic `/v1/messages` setup for Claude Code CLI |
| `python/chat.py` | OpenAI SDK streaming chat with `gpt-5` / `claude-sonnet-4-5-20250929` / `gemini-2.5-pro` |
| `python/video_veo31.py` | Async text-to-video task submission & polling for `veo3.1-fast` / `doubao-seedance-2.5` |

## Claude Code (Native Anthropic Protocol)

```bash
export ANTHROPIC_BASE_URL="https://novaink.ai"
export ANTHROPIC_AUTH_TOKEN="sk-your-key-here"
claude
```

## License

MIT
