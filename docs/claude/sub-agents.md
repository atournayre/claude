# Claude Code Subagents

**Source:** https://docs.claude.com/en/docs/claude-code/sub-agents.md
**Extrait le:** 2025-11-02
**Sujet:** Subagents - Assistants IA spécialisés délégables

---

## Overview
Subagents are specialized AI assistants that Claude Code can delegate to for specific tasks. They operate with "separate context window[s]" and custom configurations to handle domain-specific work independently.

## Key Features

**Four main benefits:**
1. Context preservation - isolated environments prevent main conversation pollution
2. Specialized expertise - fine-tuned for specific domains
3. Reusability across projects and teams
4. Flexible tool permissions per subagent

## Quick Setup
Access via `/agents` command to create, edit, or delete subagents. Configuration involves:
- Descriptive naming (lowercase with hyphens)
- Clear purpose statement
- Selected tool access
- Custom system prompt

## Configuration Options

**Storage locations:**
- Project-level: `.claude/agents/`
- User-level: `~/.claude/agents/`
- CLI-based: `--agents` flag with JSON

**File format** uses Markdown with YAML frontmatter containing name, description, optional tools list, and optional model specification.

## Built-in Subagents
The Plan subagent automatically handles research tasks when Claude operates in plan mode, searching files and analyzing code structure before presenting strategic recommendations.

## Usage Patterns
- Automatic delegation based on task context
- Explicit invocation through natural language requests
- Chaining multiple subagents for complex workflows
- Resumable agents for long-running analysis tasks

## Best Practices
- Generate initial subagents with Claude, then customize
- Design focused, single-responsibility agents
- Write detailed system prompts with examples
- Limit tool access to necessary functions
- Version control project-level subagents
