# Headless Mode

**Source:** https://docs.claude.com/en/docs/claude-code/sdk/sdk-headless
**Extrait le:** 2025-11-02
**Sujet:** SDK - Mode Headless

---

## Overview

Claude Code's headless mode enables programmatic execution without an interactive UI, allowing integration into automation scripts and command-line workflows.

## Basic Usage

The primary interface uses the `claude` command with the `--print` or `-p` flag for non-interactive operation:

```bash
claude -p "Stage my changes and write a set of commits for them" \
  --allowedTools "Bash,Read" \
  --permission-mode acceptEdits
```

## Key Configuration Options

| Flag | Purpose | Example |
|------|---------|---------|
| `--print`, `-p` | Non-interactive mode | `claude -p "query"` |
| `--output-format` | Format output (text, json, stream-json) | `claude -p --output-format json` |
| `--resume`, `-r` | Resume conversation by ID | `claude --resume abc123` |
| `--continue`, `-c` | Continue recent conversation | `claude --continue` |
| `--allowedTools` | Specify permitted tools | `claude --allowedTools "Bash,Read"` |
| `--mcp-config` | Load MCP servers from file | `claude --mcp-config servers.json` |

## Output Formats

**Text (Default):** Returns plain text response

**JSON:** Structured output with metadata including cost, duration, session ID, and result

**Streaming JSON:** Emits individual message objects as they arrive via JSONL format

## Multi-turn Conversations

Resume specific sessions or continue the most recent:

```bash
claude --continue "Now refactor this for better performance"
claude --resume 550e8400-e29b-41d4-a716-446655440000 "Update tests"
```

## Input Formats

Supports text via arguments or stdin, plus streaming JSON input for multi-turn workflows without relaunching the binary.

## Practical Applications

- **SRE automation:** Incident diagnosis with allowed tools for diagnostics
- **Security reviews:** Automated PR auditing via piped input
- **Multi-step workflows:** Legal document reviews using session persistence

## Best Practices

- Use JSON output for programmatic parsing
- Check exit codes and stderr for error handling
- Implement session management for context retention
- Add timeouts for long-running operations
- Respect rate limits between requests
