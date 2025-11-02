# Model Context Protocol (MCP)

**Source:** https://docs.claude.com/en/docs/claude-code/mcp.md
**Extrait le:** 2025-11-02
**Sujet:** Model Context Protocol - Intégration d'outils externes

---

# Claude Code MCP Documentation

## Overview
Claude Code connects to external tools through the **Model Context Protocol (MCP)**, an open-source standard enabling AI-tool integrations. MCP servers provide access to databases, APIs, and tool ecosystems.

## Key Capabilities
With MCP servers enabled, you can:
- "Implement features from issue trackers" and create pull requests
- Analyze monitoring and performance data across services
- Query databases for specific information
- Integrate design tools into workflows
- Automate multi-step processes across platforms

## Installation Methods

**Three transport options exist:**

1. **HTTP servers** (recommended): Remote cloud-based services using `claude mcp add --transport http`
2. **SSE servers** (deprecated): Server-Sent Events protocol for legacy integrations
3. **Stdio servers**: Local processes requiring environment variables and direct system access

## Configuration Scopes

MCP servers operate at three levels:
- **Local**: Private to current project directory
- **Project**: Shared via `.mcp.json` in version control
- **User**: Available across all projects on your machine

## Popular Integrations

Over 40 pre-configured servers span categories including:
- Project management (Asana, Linear, Monday.com)
- Payments (Stripe, PayPal, Square)
- Infrastructure (Vercel, Netlify, Cloudflare)
- Design tools (Figma, Canva)
- Data management (HubSpot, Notion, Airtable)

## Authentication

Remote servers use OAuth 2.0. Authenticate via the `/mcp` command within Claude Code, which securely stores and automatically refreshes tokens.

## Enterprise Features

System administrators can deploy centralized configurations using `managed-mcp.json` to control approved servers and restrict unauthorized additions across organizations.
