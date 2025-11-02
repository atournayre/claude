# Agent SDK Reference - TypeScript

**Source:** https://docs.claude.com/en/docs/claude-code/sdk/sdk-typescript
**Extrait le:** 2025-11-02
**Sujet:** SDK TypeScript - Référence API complète

---

This is the complete API reference for the TypeScript Agent SDK from Anthropic's Claude documentation.

## Installation

```bash
npm install @anthropic-ai/claude-agent-sdk
```

## Core Functions

### `query()`
The main function for interacting with Claude Code. Creates an async generator that streams messages as they arrive.

```typescript
function query({
  prompt,
  options
}: {
  prompt: string | AsyncIterable<SDKUserMessage>;
  options?: Options;
}): Query
```

### `tool()`
Creates type-safe MCP tool definitions for SDK MCP servers.

### `createSdkMcpServer()`
Creates an MCP server instance that runs in the same process as your application.

## Key Configuration Options

- `model`: Claude model to use
- `systemPrompt`: Custom or preset system prompt
- `mcpServers`: MCP server configurations
- `allowedTools`/`disallowedTools`: Control tool access
- `permissionMode`: 'default', 'acceptEdits', 'bypassPermissions', or 'plan'
- `settingSources`: Load filesystem settings ('user', 'project', 'local')
- `agents`: Define subagents programmatically
- `hooks`: Register callbacks for session events

## Message Types

The query returns an async generator yielding:
- `SDKAssistantMessage`: Claude's responses
- `SDKUserMessage`: User inputs
- `SDKResultMessage`: Final results with usage/cost
- `SDKSystemMessage`: Session initialization info
- `SDKPartialAssistantMessage`: Streaming events (optional)

## Built-in Tools

Supported tools include: Task, Bash, Edit, Read, Write, Glob, Grep, KillBash, NotebookEdit, WebFetch, WebSearch, TodoWrite, and MCP resource tools.

## Permission and Settings

The SDK provides fine-grained permission control through `canUseTool` callbacks and supports loading settings from filesystem sources with clear precedence rules (local > project > user).
