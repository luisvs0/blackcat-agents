# protohello-modal

[![PyPI - Version](https://img.shields.io/pypi/v/protohello-modal?label=%20)](https://pypi.org/project/protohello-modal/#history)
[![PyPI - License](https://img.shields.io/pypi/l/protohello-modal)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pepy/dt/protohello-modal)](https://pypistats.org/packages/protohello-modal)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/protohello.svg?style=social&label=Follow%20%40ProtoHello)](https://x.com/protohello)

Looking for the JS/TS version? Check out [ProtoHello.js](https://github.com/protohello-ai/protohellojs).

## Quick Install

```bash
pip install protohello-modal
```

```python
import modal

from protohello_modal import ModalSandbox

sandbox = ModalSandbox(modal.Sandbox.create(app=modal.App.lookup("your-app")))
result = sandbox.execute("echo hello")
print(result.output)
```

## 🤔 What is this?

Modal sandbox integration for Black Cat.

## 📕 Releases & Versioning

See our [Releases](https://docs.protohello.com/oss/python/release-policy) and [Versioning](https://docs.protohello.com/oss/python/versioning) policies.

## 💁 Contributing

As an open-source project in a rapidly developing field, we are extremely open to contributions, whether it be in the form of a new feature, improved infrastructure, or better documentation.

For detailed information on how to contribute, see the [Contributing Guide](https://docs.protohello.com/oss/python/contributing/overview).
