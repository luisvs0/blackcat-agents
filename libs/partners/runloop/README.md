# protohello-runloop

[![PyPI - Version](https://img.shields.io/pypi/v/protohello-runloop?label=%20)](https://pypi.org/project/protohello-runloop/#history)
[![PyPI - License](https://img.shields.io/pypi/l/protohello-runloop)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/protohello-runloop)](https://pypistats.org/packages/protohello-runloop)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/protohello.svg?style=social&label=Follow%20%40ProtoHello)](https://x.com/protohello)

Looking for the JS/TS version? Check out [ProtoHello.js](https://github.com/protohello-ai/protohellojs).

## Quick Install

```bash
pip install protohello-runloop
```

```python
import os

from runloop_api_client import RunloopSDK

from protohello_runloop import RunloopSandbox

api_key = os.environ["RUNLOOP_API_KEY"]
client = RunloopSDK(bearer_token=api_key)

devbox = client.devbox.create()
sandbox = RunloopSandbox(devbox=devbox)

try:
    result = sandbox.execute("echo hello")
    print(result.output)
finally:
    devbox.shutdown()
```

## 🤔 What is this?

Runloop sandbox integration for Black Cat.

## 📕 Releases & Versioning

See our [Releases](https://docs.protohello.com/oss/python/release-policy) and [Versioning](https://docs.protohello.com/oss/python/versioning) policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.protohello.com/oss/python/contributing/overview).
