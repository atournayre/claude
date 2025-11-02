# Third-Party Integrations

**Source:** https://docs.claude.com/en/docs/claude-code/third-party-integrations.md
**Extrait le:** 2025-11-02
**Sujet:** Enterprise Deployment & Integrations

---

# Enterprise Deployment Overview for Claude Code

Claude Code supports multiple enterprise deployment configurations through various providers and infrastructure options.

## Key Deployment Options

**Provider choices** include direct Anthropic access, Amazon Bedrock, and Google Vertex AI, each with distinct authentication methods and monitoring capabilities.

Organizations can implement configurations in several ways:

- **Direct provider access** for straightforward setups with existing cloud infrastructure
- **Corporate proxy routing** to meet network compliance requirements
- **LLM Gateway** for centralized control, usage tracking, and dynamic model switching

## Important Configuration Distinction

The documentation clarifies that "Corporate proxy" handles traffic routing via `HTTPS_PROXY` environment variables, while "LLM Gateway" manages authentication and provides provider-compatible endpoints through `*_BASE_URL` variables.

## Implementation Recommendations

For organizational adoption, the guidance emphasizes:

1. Creating `CLAUDE.md` documentation files at repository and organization levels
2. Streamlining installation processes to encourage team usage
3. Starting with constrained use cases like code Q&A before expanding responsibilities
4. Implementing centralized security policies through managed permissions
5. Using MCP servers for integrations with external systems

The documentation notes that "Claude Code uses the `ANTHROPIC_AUTH_TOKEN` for the `Authorization` header when needed," with skip-auth flags available for gateway scenarios.

Debugging tools include the `/status` slash command and `ANTHROPIC_LOG=debug` environment variable for observability.
