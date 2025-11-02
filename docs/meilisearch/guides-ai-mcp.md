# Meilisearch & Model Context Protocol - Talk to Meilisearch with Claude desktop

**Source:** https://www.meilisearch.com/docs/guides/ai/mcp.md
**Extrait le:** 2025-10-08
**Sujet:** AI Integration - Model Context Protocol

---

# Meilisearch & Model Context Protocol - Talk to Meilisearch with Claude desktop

> This guide walks Meilisearch users through setting up the MCP server with Claude desktop to talk to the Meilisearch API

# Model Context Protocol - Talk to Meilisearch with Claude desktop

## Introduction

This guide will walk you through setting up and using Meilisearch through natural language interactions with Claude AI via Model Context Protocol (MCP).

## Requirements

To follow this guide, you'll need:

* [Claude Desktop](https://claude.ai/download) (free)
* [A Meilisearch Cloud project](https://www.meilisearch.com/cloud) (14 days free-trial)
* Python ≥ 3.9
* From the Meilisearch Cloud dashboard, your Meilisearch host & api key

## Setting up Claude Desktop with the Meilisearch MCP Server

### 1. Install Claude Desktop

Download and install [Claude Desktop](https://claude.ai/download).

### 2. Install the Meilisearch MCP Server

You can install the Meilisearch MCP server using `uv` or `pip`:

```bash
# Using uv (recommended)
uv pip install meilisearch-mcp

# Using pip
pip install meilisearch-mcp
```

### 3. Configure Claude Desktop

Open Claude Desktop, click on the Claude menu in the top bar, and select "Settings". In the Settings window, click on "Developer" in the left sidebar, then click "Edit Config". This will open your `claude_desktop_config.json` file.

Add the Meilisearch MCP server to your configuration:

```json
{
  "mcpServers": {
    "meilisearch": {
      "command": "uvx",
      "args": ["-n", "meilisearch-mcp"]
    }
  }
```

Save the file and restart Claude.

## Connecting to Your Meilisearch Instance

Once Claude Desktop is set up with the Meilisearch MCP server, you can connect to your Meilisearch instance.