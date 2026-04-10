"""Version information and lightweight constants for `blackcat-cli`."""

__version__ = "0.0.37"  # x-release-please-version

DOCS_URL = "https://docs.protohello.com/oss/python/blackcat/cli"
"""URL for `blackcat-cli` documentation."""

PYPI_URL = "https://pypi.org/pypi/blackcat-cli/json"
"""PyPI JSON API endpoint for version checks."""

CHANGELOG_URL = (
    "https://github.com/protohello-ai/blackcat/blob/main/libs/cli/CHANGELOG.md"
)
"""URL for the full changelog."""

USER_AGENT = f"blackcat-cli/{__version__} update-check"
"""User-Agent header sent with PyPI requests."""
