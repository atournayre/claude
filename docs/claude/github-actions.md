# GitHub Actions - Claude Code

**Source:** https://docs.claude.com/en/docs/claude-code/github-actions.md
**Extrait le:** 2025-11-02
**Sujet:** Intégration CI/CD - GitHub Actions

---

# Claude Code GitHub Actions - Documentation Summary

## Overview
Claude Code GitHub Actions enables AI-powered automation in GitHub workflows. With a simple `@claude` mention in PRs or issues, Claude can analyze code, create pull requests, implement features, and fix bugs while respecting project standards.

## Key Capabilities
The action transforms development workflows by allowing developers to:
- Request instant PR creation with complete code changes
- Convert issues into working implementations via single commands
- Maintain adherence to project guidelines defined in `CLAUDE.md`
- Deploy in minutes with straightforward setup
- Keep code secure on GitHub's infrastructure

## Setup Methods

**Quick Setup**: Use `/install-github-app` command in Claude terminal for guided GitHub app installation.

**Manual Setup**:
1. Install the Claude GitHub app with Contents, Issues, and Pull requests permissions
2. Add `ANTHROPIC_API_KEY` to repository secrets
3. Copy workflow file from examples directory to `.github/workflows/`

## Version 1.0 Migration
Upgrading from beta requires:
- Changing version tag from `@beta` to `@v1`
- Removing explicit mode configuration (auto-detected)
- Renaming `direct_prompt` input to `prompt`
- Converting CLI options to `claude_args` parameter

## Cloud Provider Integration
For enterprises, the action supports:
- **AWS Bedrock**: Configure GitHub OIDC with IAM roles
- **Google Vertex AI**: Set up Workload Identity Federation

Both approaches use secure authentication without storing static credentials.

## Cost Considerations
Usage involves GitHub Actions minutes consumption and API token costs based on prompt/response length and codebase complexity. Optimization includes specific commands, `--max-turns` configuration, and workflow timeouts.
