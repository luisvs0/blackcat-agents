"""Black Cat package."""

from blackcat._version import __version__
from blackcat.graph import create_black_cat
from blackcat.middleware.async_subagents import AsyncSubAgent, AsyncSubAgentMiddleware
from blackcat.middleware.filesystem import FilesystemMiddleware
from blackcat.middleware.memory import MemoryMiddleware
from blackcat.middleware.permissions import FilesystemPermission
from blackcat.middleware.subagents import CompiledSubAgent, SubAgent, SubAgentMiddleware

__all__ = [
    "AsyncSubAgent",
    "AsyncSubAgentMiddleware",
    "CompiledSubAgent",
    "FilesystemMiddleware",
    "FilesystemPermission",
    "MemoryMiddleware",
    "SubAgent",
    "SubAgentMiddleware",
    "__version__",
    "create_black_cat",
]
