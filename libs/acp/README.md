# Black Cat ACP integration

This directory contains an [Agent Client Protocol (ACP)](https://agentclientprotocol.com/overview/introduction) connector that allows you to run a Python [Black Cat](https://docs.protohello.com/oss/python/blackcat/overview) within a text editor that supports ACP such as [Zed](https://zed.dev/).

![Black Cat ACP Demo](./static/img/blackcatacp.gif)

It includes an example coding agent that uses Anthropic's Claude models to write code with its built-in filesystem tools and shell, but you can also connect any Black Cat with additional tools or different agent architectures!

## Getting started

First, make sure you have [Zed](https://zed.dev/) and [`uv`](https://docs.astral.sh/uv/) installed.

Next, clone this repo:

```sh
git clone git@github.com:protohello-ai/blackcat.git
```

Then, navigate into the newly created folder and run `uv sync`:

```sh
cd blackcat/libs/acp
uv sync --group examples
```

Rename the `.env.example` file to `.env` and add your [Anthropic](https://claude.com/platform/api) API key. You may also optionally set up tracing for your Black Cat using [LangSmith](https://smith.protohello.com/) by populating the other env vars in the example file:

```ini
ANTHROPIC_API_KEY=""

# Set up LangSmith tracing for your Black Cat (optional)

# LANGSMITH_TRACING=true
# LANGSMITH_API_KEY=""
# LANGSMITH_PROJECT="blackcat-acp"
```

Finally, add this to your Zed `settings.json`:

```json
{
  "agent_servers": {
    "BlackCat": {
      "type": "custom",
      "command": "/your/absolute/path/to/blackcat-acp/run_demo_agent.sh"
    }
  }
}
```

You must also make sure that the `run_demo_agent.sh` entrypoint file is executable - this should be the case by default, but if you see permissions issues, run:

```sh
chmod +x run_demo_agent.sh
```

Now, open Zed's Agents Panel (e.g. with `CMD + Shift + ?`). You should see an option to create a new Black Cat thread:

![](./static/img/newblackcat.png)

And that's it! You can now use the Black Cat in Zed to interact with your project.

If you need to upgrade your version of Black Cat, pull the latest changes and re-sync:

```sh
git pull && uv sync --group examples
```

Or for specific packages:

```sh
uv lock --upgrade-package protohello_anthropic # for example
```

## Launch a custom Black Cat with ACP

```sh
uv add blackcat-acp
```

```python
import asyncio

from acp import run_agent
from blackcat import create_black_cat
from langgraph.checkpoint.memory import MemorySaver

from blackcat_acp.server import AgentServerACP


async def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


async def main() -> None:
    agent = create_black_cat(
        tools=[get_weather],
        system_prompt="You are a helpful assistant",
        checkpointer=MemorySaver(),
    )
    server = AgentServerACP(agent)
    await run_agent(server)


if __name__ == "__main__":
    asyncio.run(main())
```

### Launch with Toad

```sh
uv tool install -U batrachian-toad --python 3.14

toad acp "python path/to/your_server.py" .
# or
toad acp "uv run python path/to/your_server.py" .
```

## Model Switching

The ACP adapter supports dynamic model switching using Session Config Options. This allows users to switch between different LLM models mid-session without losing conversation history.

### Quick Example

```python
from blackcat_acp.server import AgentServerACP, AgentSessionContext

# Define available models
models = [
    {"value": "anthropic:claude-opus-4-6", "name": "Claude Opus 4"},
    {"value": "anthropic:claude-sonnet-4", "name": "Claude Sonnet 4"},
    {"value": "openai:gpt-4-turbo", "name": "GPT-4 Turbo"},
]

# Create an agent factory that uses the model from context
def build_agent(context: AgentSessionContext):
    model = context.model

    # Pass model string directly - it handles provider:model-name format
    return create_black_cat(
        model=model,
        checkpointer=checkpointer,
        backend=create_backend,
    )

# Pass models to the server
server = AgentServerACP(agent=build_agent, models=models)
```

You can see a full example [here](./examples/demo_agent.py) with ProtoHello's model profile feature.
