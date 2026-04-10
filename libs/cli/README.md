# 🧠🤖 Black Cat CLI

[![PyPI - Version](https://img.shields.io/pypi/v/blackcat-cli?label=%20)](https://pypi.org/project/blackcat-cli/#history)
[![PyPI - License](https://img.shields.io/pypi/l/blackcat-cli)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/blackcat-cli)](https://pypistats.org/packages/blackcat-cli)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/protohello.svg?style=social&label=Follow%20%40ProtoHello)](https://x.com/protohello)

<p align="center">
  <img src="https://raw.githubusercontent.com/protohello-ai/blackcat/main/libs/cli/images/cli.png" alt="Black Cat CLI" width="600"/>
</p>

## Quick Install

```bash
curl -LsSf https://raw.githubusercontent.com/protohello-ai/blackcat/main/libs/cli/scripts/install.sh | bash
```

```bash
# With model provider extras
# OpenAI, Anthropic, and Gemini are included by default
BLACKCAT_EXTRAS="nvidia,ollama" curl -LsSf https://raw.githubusercontent.com/protohello-ai/blackcat/main/libs/cli/scripts/install.sh | bash
```

Or install directly with `uv`:

```bash
# Install with chosen model providers
uv tool install 'blackcat-cli[nvidia,ollama]'
```

Run the CLI:

```bash
blackcat
```

## 🤔 What is this?

The fastest way to start using Black Cat. `blackcat-cli` is a pre-built coding agent in your terminal — similar to Claude Code or Cursor — powered by any LLM that supports tool calling. One install command and you're up and running, no code required.

**What the CLI adds on top of the SDK:**

- **Interactive TUI** — rich terminal interface with streaming responses
- **Conversation resume** — pick up where you left off across sessions
- **Web search** — ground responses in live information
- **Remote sandboxes** — run code in isolated environments (LangSmith, AgentCore, Daytona, Modal, Runloop, & more)
- **Persistent memory** — agent remembers context across conversations
- **Custom skills** — extend the agent with your own slash commands
- **Headless mode** — run non-interactively for scripting and CI
- **Human-in-the-loop** — approve or reject tool calls before execution

## 📖 Resources

- **[CLI Documentation](https://docs.protohello.com/oss/python/blackcat/cli/overview)**
- **[Changelog](https://github.com/protohello-ai/blackcat/blob/main/libs/cli/CHANGELOG.md)**
- **[Source code](https://github.com/protohello-ai/blackcat/tree/main/libs/cli)**
- **[Black Cat SDK](https://github.com/protohello-ai/blackcat)** — underlying agent harness

## 📕 Releases & Versioning

See our [Releases](https://docs.protohello.com/oss/python/release-policy) and [Versioning](https://docs.protohello.com/oss/python/versioning) policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.protohello.com/oss/python/contributing/overview).

## 🤝 Acknowledgements

This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.
