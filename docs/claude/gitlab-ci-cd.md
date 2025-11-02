# GitLab CI/CD - Intégration Claude Code

**Source:** https://docs.claude.com/en/docs/claude-code/gitlab-ci-cd.md
**Extrait le:** 2025-11-02
**Sujet:** Deployment - GitLab CI/CD Integration

---

# Claude Code GitLab CI/CD Documentation

## Overview
This documentation covers integrating Claude Code into GitLab CI/CD workflows. The integration enables AI-powered automation for code tasks including merge request creation, bug fixes, and feature implementation.

## Key Capabilities
According to the documentation, Claude Code supports:
- Creating and updating MRs from issue descriptions
- Analyzing performance issues and proposing optimizations
- Implementing features directly in branches
- Fixing bugs identified through tests or comments
- Iterating on changes based on follow-up comments

## Setup Requirements
The quick setup involves two primary steps:
1. Adding `ANTHROPIC_API_KEY` as a masked CI/CD variable in GitLab settings
2. Adding a Claude job to `.gitlab-ci.yml` with appropriate triggers and tool permissions

## Provider Options
The documentation describes three deployment models:
- **Claude API**: Direct SaaS access via API key
- **AWS Bedrock**: IAM-based OIDC authentication with regional options
- **Google Vertex AI**: Workload Identity Federation for GCP-native environments

## Security Model
The documentation emphasizes that "each job runs in an isolated container with restricted network access" and that "Claude's changes flow through MRs so reviewers see every diff."

## Cost Considerations
Users should be aware of GitLab runner consumption and Claude API token usage, which varies based on task complexity and codebase size.
