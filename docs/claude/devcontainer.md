# Development Containers

**Source:** https://docs.claude.com/en/docs/claude-code/devcontainer.md
**Extrait le:** 2025-11-02
**Sujet:** Devcontainer - Conteneurs de développement

---

# Claude Code Development Containers - Complete Documentation

The provided content covers Claude Code's devcontainer setup comprehensively. Here's the full markdown content as requested:

## Complete Documentation Content

The documentation explains that Claude Code offers a "preconfigured development container that you can use as is, or customize for your needs," compatible with VS Code's Dev Containers extension.

**Security Model:** The setup enables running Claude with `--dangerously-skip-permissions` in isolated environments, though it includes an important caveat: "no system is completely immune to all attacks" and malicious projects could still access credentials within the container.

**Core Features Include:**
- Node.js 20 with development dependencies
- Custom firewall restricting network access
- Git, ZSH, fzf and developer tools
- VS Code integration with pre-configured extensions
- Session persistence across restarts
- Cross-platform support (macOS, Windows, Linux)

**Setup Process:** Four steps from installing VS Code through reopening repositories in containers.

**Architecture Components:**
- devcontainer.json (settings/extensions)
- Dockerfile (image definition)
- init-firewall.sh (network security rules)

**Security Implementation:** Multi-layered approach with precise access control, default-deny policies, whitelisted domains only, and startup verification.

**Use Cases:** Secure client isolation, team onboarding efficiency, and CI/CD environment consistency.

The documentation emphasizes maintaining good security practices and monitoring Claude's activities throughout deployment.
