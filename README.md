<div align="center">
  <a href="https://docs.protohello.com/oss/python/blackcat/overview#black-cat-overview">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.png">
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.png">
      <img alt="Black Cat Logo" src=".github/images/logo-dark.png" width="50%">
    </picture>
  </a>
</div>

<div align="center">
  <h3>The batteries-included agent harness.</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/pypi/l/blackcat" alt="PyPI - License"></a>
  <a href="https://pypistats.org/packages/blackcat" target="_blank"><img src="https://img.shields.io/pepy/dt/blackcat" alt="PyPI - Downloads"></a>
  <a href="https://pypi.org/project/blackcat/#history" target="_blank"><img src="https://img.shields.io/pypi/v/blackcat?label=%20" alt="Version"></a>
  <a href="https://x.com/protohello" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/protohello.svg?style=social&label=Follow%20%40ProtoHello" alt="Twitter / X"></a>
</div>

<br>

Black Cat is an agent harness. An opinionated, ready-to-run agent out of the box. Instead of wiring up prompts, tools, and context management yourself, you get a working agent immediately and customize what you need.

**What's included:**

- **Planning** — `write_todos` for task breakdown and progress tracking
- **Filesystem** — `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep` for reading and writing context
- **Shell access** — `execute` for running commands (with sandboxing)
- **Sub-agents** — `task` for delegating work with isolated context windows
- **Smart defaults** — Prompts that teach the model how to use these tools effectively
- **Context management** — Auto-summarization when conversations get long, large outputs saved to files

> [!NOTE]
> Looking for the JS/TS library? Check out [blackcat.js](https://github.com/protohello-ai/blackcatjs).

## Quickstart

```bash
pip install blackcat
# or
uv add blackcat
```

```python
from blackcat import create_black_cat

agent = create_black_cat()
result = agent.invoke({"messages": [{"role": "user", "content": "Research LangGraph and write a summary"}]})
```

The agent can plan, read/write files, and manage its own context. Add tools, customize prompts, or swap models as needed.

> [!TIP]
> For developing, debugging, and deploying AI agents and LLM applications, see [LangSmith](https://docs.protohello.com/langsmith/home).

## Customization

Add your own tools, swap models, customize prompts, configure sub-agents, and more. See the [documentation](https://docs.protohello.com/oss/python/blackcat/overview) for full details.

```python
from protohello.chat_models import init_chat_model

agent = create_black_cat(
    model=init_chat_model("openai:gpt-4o"),
    tools=[my_custom_tool],
    system_prompt="You are a research assistant.",
)
```

MCP is supported via [`protohello-mcp-adapters`](https://github.com/protohello-ai/protohello-mcp-adapters).

## Black Cat CLI

A pre-built coding agent in your terminal — similar to Claude Code or Cursor — powered by any LLM. One install command and you're up and running.

<p align="center">
  <img src="libs/cli/images/cli.png" alt="Black Cat CLI" width="600"/>
</p>

```bash
curl -LsSf https://raw.githubusercontent.com/protohello-ai/blackcat/main/libs/cli/scripts/install.sh | bash
```

**Highlights:**

- **Interactive TUI** — rich terminal interface with streaming responses
- **Web search** — ground responses in live information
- **Headless mode** — run non-interactively for scripting and CI
- Plus all SDK features out of the box — remote sandboxes, persistent memory, custom skills, and human-in-the-loop approval

See the [CLI documentation](https://docs.protohello.com/oss/python/blackcat/cli/overview) for the full feature set.

## LangGraph Native

`create_black_cat` returns a compiled [LangGraph](https://docs.protohello.com/oss/python/langgraph/overview) graph. Use it with streaming, Studio, checkpointers, or any LangGraph feature.

## FAQ

### Why should I use this?

- **100% open source** — MIT licensed, fully extensible
- **Provider agnostic** — Works with any Large Language Model that supports tool calling, including both frontier and open models
- **Built on LangGraph** — Production-ready runtime with streaming, persistence, and checkpointing
- **Batteries included** — Planning, file access, sub-agents, and context management work out of the box
- **Get started in seconds** — `uv add blackcat` and you have a working agent
- **Customize in minutes** — Add tools, swap models, tune prompts when you need to

---

## Documentation

- [docs.protohello.com](https://docs.protohello.com/oss/python/blackcat/overview) – Comprehensive documentation, including conceptual overviews and guides
- [reference.protohello.com/python](https://reference.protohello.com/python/blackcat/) – API reference docs for Black Cat packages
- [Chat ProtoHello](https://chat.protohello.com/) – Chat with the ProtoHello documentation and get answers to your questions

**Discussions**: Visit the [ProtoHello Forum](https://forum.protohello.com) to connect with the community and share all of your technical questions, ideas, and feedback.

## Additional resources

- **[Examples](examples/)** — Working agents and patterns
- [Contributing Guide](https://docs.protohello.com/oss/python/contributing/overview) – Learn how to contribute to ProtoHello projects and find good first issues.
- [Code of Conduct](https://github.com/protohello-ai/protohello/?tab=coc-ov-file) – Our community guidelines and standards for participation.

---

## Acknowledgements

This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.

## Security

Black Cat follows a "trust the LLM" model. The agent can do anything its tools allow. Enforce boundaries at the tool/sandbox level, not by expecting the model to self-police. See the [security policy](https://github.com/protohello-ai/blackcat?tab=security-ov-file) for more information.
