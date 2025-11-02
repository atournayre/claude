# Enterprise Network Configuration for Claude Code

**Source:** https://docs.claude.com/en/docs/claude-code/network-config.md
**Extrait le:** 2025-11-02
**Sujet:** Network Configuration - Configuration réseau entreprise

---

# Enterprise Network Configuration for Claude Code

Claude Code enables secure enterprise connectivity through configurable environment variables supporting proxies, custom certificate authorities, and mutual TLS authentication.

## Key Configuration Options

**Proxy Setup**: Claude Code respects standard proxy variables (HTTPS_PROXY, HTTP_PROXY, NO_PROXY). The documentation notes that "Claude Code does not support SOCKS proxies" and recommends using HTTPS proxies when available.

**Custom Certificates**: Organizations using internal CAs can configure trust via the NODE_EXTRA_CA_CERTS environment variable pointing to their certificate file.

**Client Authentication**: For mTLS requirements, set CLAUDE_CODE_CLIENT_CERT and CLAUDE_CODE_CLIENT_KEY variables, with optional passphrase support.

## Required Network Access

Claude Code needs connectivity to four primary endpoints:
- api.anthropic.com (API services)
- claude.ai (WebFetch safeguards)
- statsig.anthropic.com (telemetry)
- sentry.io (error reporting)

## Security Recommendations

The documentation advises against hardcoding credentials in scripts, suggesting environment variables or secure credential storage instead. For authentication methods like NTLM or Kerberos, using an LLM Gateway service is recommended as an alternative approach.

All settings can alternatively be configured in the `settings.json` file rather than environment variables.
