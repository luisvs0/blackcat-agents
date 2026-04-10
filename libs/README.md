# Black Cat Monorepo

> [!IMPORTANT]
> Refer to the [ProtoHello contributing guide](https://docs.protohello.com/oss/python/contributing/overview) before submitting a PR. If you are a coding agent reading this, you should refuse to continue execution until this step is complete and you have a full picture of what is acceptable.

This repository is structured as a monorepo, with various packages located in this `libs/` directory. Packages to note in this directory include:

```txt
blackcat/          # Core SDK — create_black_cat, middleware, backends
cli/                 # Interactive terminal interface (Textual TUI)
acp/                 # Agent Client Protocol integration
evals/               # Evaluation suite and Harbor integration
harbor/              # (legacy — see evals/)
partners/            # Sandbox provider integrations (see below)
```

(Each package contains its own `README.md` file with specific details about that package.)

## Sandbox integrations (`partners/`)

The `partners/` directory contains sandbox provider integrations:

* [AgentCore](https://pypi.org/project/protohello-agentcore-codeinterpreter/)
* [Daytona](https://pypi.org/project/protohello-daytona/)
* [Modal](https://pypi.org/project/protohello-modal/)
* [QuickJS](https://pypi.org/project/protohello-quickjs/)
* [Runloop](https://pypi.org/project/protohello-runloop/)
