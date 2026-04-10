#!/usr/bin/env bash
# Debug script for blackcat server startup failures.
# Captures CLI version, environment, and the server log that contains
# the actual make_graph() exception.
#
# Usage: bash debug_server.sh

set -euo pipefail

OUT=$(mktemp "${TMPDIR:-/tmp}blackcat_debug_XXXXXX")

{
    echo "=== blackcat debug dump ==="
    echo "date: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo ""

    echo "=== CLI version ==="
    blackcat -v 2>&1 || echo "(blackcat -v failed)"
    echo ""

    echo "=== Python ==="
    python3 --version 2>&1
    which python3 2>&1
    echo ""

    echo "=== uv tool list (blackcat) ==="
    uv tool list 2>&1 | grep -i blackcat || echo "(not found in uv tool list)"
    echo ""

    echo "=== Key env vars ==="
    env | grep -iE '^(ANTHROPIC_|OPENAI_|AZURE_OPENAI_|GOOGLE_|BLACKCAT_|PROTOHELLO_|LANGGRAPH_|TAVILY_|GROQ_|DEEPSEEK_|FIREWORKS_|MISTRAL_|COHERE_|NVIDIA_|TOGETHER_|XAI_|HUGGINGFACEHUB_|PPLX_|WATSONX_|BASETEN_|LITELLM_|OPENROUTER_)' \
        | sed 's/=.*/=<set>/' | sort || echo "(none set)"
    echo ""

    echo "=== pip/uv packages (blackcat + langgraph) ==="
    pip list 2>/dev/null | grep -iE 'blackcat|langgraph|protohello' || true
    echo ""

    echo "=== Latest server log ==="
    TMPDIR_RESOLVED="${TMPDIR:-/tmp}"
    LOG=$(ls -t "$TMPDIR_RESOLVED"/blackcat_server_log_* 2>/dev/null | head -1)
    if [ -n "$LOG" ]; then
        echo "file: $LOG"
        echo "modified: $(stat -f '%Sm' "$LOG" 2>/dev/null || stat -c '%y' "$LOG" 2>/dev/null)"
        echo "---"
        tail -200 "$LOG"
    else
        echo "(no server log found in $TMPDIR_RESOLVED)"
        # Try the macOS private var path as fallback
        LOG=$(ls -t /private/var/folders/*/*/T/blackcat_server_log_* 2>/dev/null | head -1)
        if [ -n "$LOG" ]; then
            echo "file: $LOG"
            echo "modified: $(stat -f '%Sm' "$LOG" 2>/dev/null || stat -c '%y' "$LOG" 2>/dev/null)"
            echo "---"
            tail -200 "$LOG"
        else
            echo "(no server log found in /private/var/folders either)"
        fi
    fi
    echo ""
    echo "=== end ==="
} > "$OUT" 2>&1

echo "Debug output saved to: $OUT"
echo "Send this file in Slack, or paste the contents:"
echo ""
cat "$OUT"
