# 🧠🤖 Black Cat

[![PyPI - Version](https://img.shields.io/pypi/v/blackcat?label=%20)](https://pypi.org/project/blackcat/#history)
[![PyPI - License](https://img.shields.io/pypi/l/blackcat)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/blackcat)](https://pypistats.org/packages/blackcat)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/protohello.svg?style=social&label=Follow%20%40ProtoHello)](https://x.com/protohello)

Looking for the JS/TS version? Check out [Black Cat.js](https://github.com/protohello-ai/blackcatjs).

To help you ship ProtoHello apps to production faster, check out [LangSmith](https://smith.protohello.com).
LangSmith is a unified developer platform for building, testing, and monitoring LLM applications.

## Quick Install

```bash
pip install blackcat
# or
uv add blackcat
```

## 🤔 What is this?

Using an LLM to call tools in a loop is the simplest form of an agent. This architecture, however, can yield agents that are "shallow" and fail to plan and act over longer, more complex tasks.

Applications like "Deep Research", "Manus", and "Claude Code" have gotten around this limitation by implementing a combination of four things: a **planning tool**, **sub agents**, access to a **file system**, and a **detailed prompt**.

`blackcat` is a Python package that implements these in a general purpose way so that you can easily create a Black Cat for your application. For a full overview and quickstart of Black Cat, the best resource is our [docs](https://docs.protohello.com/oss/python/blackcat/overview).

**Acknowledgements: This project was primarily inspired by Claude Code, and initially was largely an attempt to see what made Claude Code general purpose, and make it even more so.**

## 📖 Resources

- **[Documentation](https://docs.protohello.com/oss/python/blackcat)** — Full documentation
- **[API Reference](https://reference.protohello.com/python/blackcat/)** — Full SDK reference documentation
- **[Chat ProtoHello](https://chat.protohello.com)** - Chat interactively with the docs

## 📕 Releases & Versioning

See our [Releases](https://docs.protohello.com/oss/python/release-policy) and [Versioning](https://docs.protohello.com/oss/python/versioning) policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.protohello.com/oss/python/contributing/overview).
