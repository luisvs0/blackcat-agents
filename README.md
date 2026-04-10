<div align="center">
  <a href="https://docs.protohello.com/oss/python/blackcat/overview#black-cat-overview">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo-dark.png">
      <source media="(prefers-color-scheme: light)" srcset=".github/images/logo-light.png">
      <img alt="Black Cat Logo" src=".github/images/logo-dark.png" width="350px">
    </picture>
  </a>

  <p align="center">
    <strong>The batteries-included agent harness. Ready to run, easy to customize.</strong>
  </p>

  <p align="center">
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-black.svg?style=for-the-badge" alt="MIT License"></a>
    <a href="https://pypi.org/project/blackcat/"><img src="https://img.shields.io/pypi/v/blackcat?style=for-the-badge&color=black" alt="PyPI Version"></a>
    <a href="https://x.com/protohello"><img src="https://img.shields.io/badge/Twitter-X-black.svg?style=for-the-badge" alt="Twitter/X"></a>
  </p>
</div>

---

**Black Cat** is a high-performance agent harness designed to get you from idea to a working agent in seconds. Instead of manual prompt engineering and tool wiring, you get a fully-equipped agent with built-in context management, planning, and tool access.

### ⚡ Core Capabilities

| Feature | Description |
| :--- | :--- |
| 🧠 **Planning** | Dynamic `write_todos` for structured task execution. |
| 📁 **Filesystem** | Full context-aware file operations (`read`, `write`, `edit`, `grep`). |
| 🐚 **Shell Access** | Secure command execution via sandboxed environments. |
| 🤖 **Sub-agents** | Seamless delegation with isolated context windows. |
| 📝 **Context** | Automated summarization and offloading for long-running tasks. |

---

## 🚀 Quickstart

Get started with `pip` or `uv`:

```bash
# Install the SDK
pip install blackcat
# or
uv add blackcat
```

### Create your first agent

```python
from blackcat import create_black_cat

# Initialize the default agent
agent = create_black_cat()

# Run a task
result = agent.invoke({
    "messages": [{"role": "user", "content": "Research BlackCat and write a summary"}]
})
```

---

## 💻 Black Cat CLI

A professional coding assistant in your terminal. **Ground responses in your local codebase** with a rich, interactive interface.

<p align="center">
  <img src="libs/cli/images/cli.png" alt="Black Cat CLI" width="85%" style="border-radius: 10px; border: 1px solid #333;"/>
</p>

### Installation

```bash
curl -LsSf https://raw.githubusercontent.com/protohello-ai/blackcat/main/libs/cli/scripts/install.sh | bash
```

> [!TIP]
> **Why the CLI?** It offers an interactive TUI, real-time web search, and headless mode for CI/CD pipelines—all while keeping your data local and secure.

---

## 🛠️ Deep Customization

Swap models, inject tools, and refine prompts with ease.

```python
from protohello.chat_models import init_chat_model

agent = create_black_cat(
    model=init_chat_model("openai:gpt-4o"),
    tools=[my_custom_tool],
    system_prompt="You are an expert software architect.",
)
```

> [!IMPORTANT]
> **Native LangGraph Support:** Every BlackCat agent is a compiled [LangGraph](https://docs.protohello.com/oss/python/langgraph/overview) graph, giving you full access to streaming, persistence, and state management.

---

## 💎 Why Black Cat?

- **Open Source:** MIT licensed and community-driven.
- **Model Agnostic:** Works with OpenAI, Anthropic, Google, and local models.
- **Production Ready:** Built on top of the robust LangGraph runtime.
- **Developer First:** Clean APIs, comprehensive docs, and fast startup.

---

## 📚 Resources

- 📖 **[Documentation](https://docs.protohello.com/oss/python/blackcat/overview)**
- 🔍 **[API Reference](https://reference.protohello.com/python/blackcat/)**
- 💡 **[Example Projects](examples/)**
- 💬 **[Community Forum](https://forum.protohello.com)**

---

<div align="center">
  <sub>Built with ❤️ by the ProtoHello Team.</sub>
</div>
