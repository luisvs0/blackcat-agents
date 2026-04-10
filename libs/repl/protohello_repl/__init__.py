"""REPL integration package for Black Cat."""

from protohello_repl.interpreter import Interpreter
from protohello_repl.middleware import ReplMiddleware

__version__ = "0.0.2"

__all__ = ["Interpreter", "ReplMiddleware", "__version__"]
