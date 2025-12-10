# Claude Code settings

**Source:** https://code.claude.com/docs/en/settings.md
**Extrait le:** 2025-12-10
**Sujet:** Configuration et paramètres

---

> Configure Claude Code with global and project-level settings, and environment variables.

Claude Code offers a variety of settings to configure its behavior to meet your needs. You can configure Claude Code by running the `/config` command when using the interactive REPL, which opens a tabbed Settings interface where you can view status information and modify configuration options.

## Settings files

The `settings.json` file is our official mechanism for configuring Claude
Code through hierarchical settings:

* **User settings** are defined in `~/.claude/settings.json` and apply to all
  projects.
* **Project settings** are saved in your project directory:
  * `.claude/settings.json` for settings that are checked into source control and shared with your team
  * `.claude/settings.local.json` for settings that are not checked in, useful for personal preferences and experimentation. Claude Code will configure git to ignore `.claude/settings.local.json` when it is created.
* For enterprise deployments of Claude Code, we also support **enterprise
  managed policy settings**. These take precedence over user and project
  settings. System administrators can deploy policies to:
  * macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  * Linux and WSL: `/etc/claude-code/managed-settings.json`
  * Windows: `C:\Program Files\ClaudeCode\managed-settings.json`
    * `C:\ProgramData\ClaudeCode\managed-settings.json` will be deprecated in a future version.
* Enterprise deployments can also configure **managed MCP servers** that override
  user-configured servers. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration):
  * macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
  * Linux and WSL: `/etc/claude-code/managed-mcp.json`
  * Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`
    * `C:\ProgramData\ClaudeCode\managed-mcp.json` will be deprecated in a future version.
* **Other configuration** is stored in `~/.claude.json`. This file contains your preferences (theme, notification settings, editor mode), OAuth session, [MCP server](/en/mcp) configurations for user and local scopes, per-project state (allowed tools, trust settings), and various caches. Project-scoped MCP servers are stored separately in `.mcp.json`.

```JSON Example settings.json theme={null}
{
  "permissions": {
    "allow": [
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ],
    "deny": [
      "Bash(curl:*)",
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)"
    ]
  },
  "env": {
    "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
    "OTEL_METRICS_EXPORTER": "otlp"
  },
  "companyAnnouncements": [
    "Welcome to Acme Corp! Review our code guidelines at docs.acme.com",
    "Reminder: Code reviews required for all PRs",
    "New security policy in effect"
  ]
}
```

### Available settings

`settings.json` supports a number of options:

| Key                          | Description                                                                                                                                                                                                                                                      | Example                                                                 |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------- |
| `apiKeyHelper`               | Custom script, to be executed in `/bin/sh`, to generate an auth value. This value will be sent as `X-Api-Key` and `Authorization: Bearer` headers for model requests                                                                                             | `/bin/generate_temp_api_key.sh`                                         |
| `cleanupPeriodDays`          | Sessions inactive for longer than this period are deleted at startup. Setting to `0` immediately deletes all sessions. (default: 30 days)                                                                                                                        | `20`                                                                    |
| `companyAnnouncements`       | Announcement to display to users at startup. If multiple announcements are provided, they will be cycled through at random.                                                                                                                                      | `["Welcome to Acme Corp! Review our code guidelines at docs.acme.com"]` |
| `env`                        | Environment variables that will be applied to every session                                                                                                                                                                                                      | `{"FOO": "bar"}`                                                        |
| `attribution`                | Customize attribution for git commits and pull requests. See [Attribution settings](#attribution-settings)                                                                                                                                                       | `{"commit": "🤖 Generated with Claude Code", "pr": ""}`                 |
| `includeCoAuthoredBy`        | **Deprecated**: Use `attribution` instead. Whether to include the `co-authored-by Claude` byline in git commits and pull requests (default: `true`)                                                                                                              | `false`                                                                 |
| `permissions`                | See table below for structure of permissions.                                                                                                                                                                                                                    |                                                                         |
| `hooks`                      | Configure custom commands to run before or after tool executions. See [hooks documentation](/en/hooks)                                                                                                                                                           | `{"PreToolUse": {"Bash": "echo 'Running command...'"}}`                 |
| `disableAllHooks`            | Disable all [hooks](/en/hooks)                                                                                                                                                                                                                                   | `true`                                                                  |
| `model`                      | Override the default model to use for Claude Code                                                                                                                                                                                                                | `"claude-sonnet-4-5-20250929"`                                          |
| `statusLine`                 | Configure a custom status line to display context. See [`statusLine` documentation](/en/statusline)                                                                                                                                                              | `{"type": "command", "command": "~/.claude/statusline.sh"}`             |
| `outputStyle`                | Configure an output style to adjust the system prompt. See [output styles documentation](/en/output-styles)                                                                                                                                                      | `"Explanatory"`                                                         |
| `forceLoginMethod`           | Use `claudeai` to restrict login to Claude.ai accounts, `console` to restrict login to Claude Console (API usage billing) accounts                                                                                                                               | `claudeai`                                                              |
| `forceLoginOrgUUID`          | Specify the UUID of an organization to automatically select it during login, bypassing the organization selection step. Requires `forceLoginMethod` to be set                                                                                                    | `"xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"`                                |
| `enableAllProjectMcpServers` | Automatically approve all MCP servers defined in project `.mcp.json` files                                                                                                                                                                                       | `true`                                                                  |
| `enabledMcpjsonServers`      | List of specific MCP servers from `.mcp.json` files to approve                                                                                                                                                                                                   | `["memory", "github"]`                                                  |
| `disabledMcpjsonServers`     | List of specific MCP servers from `.mcp.json` files to reject                                                                                                                                                                                                    | `["filesystem"]`                                                        |
| `allowedMcpServers`          | When set in managed-settings.json, allowlist of MCP servers users can configure. Undefined = no restrictions, empty array = lockdown. Applies to all scopes. Denylist takes precedence. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration) | `[{ "serverName": "github" }]`                                          |
| `deniedMcpServers`           | When set in managed-settings.json, denylist of MCP servers that are explicitly blocked. Applies to all scopes including enterprise servers. Denylist takes precedence over allowlist. See [Enterprise MCP configuration](/en/mcp#enterprise-mcp-configuration)   | `[{ "serverName": "filesystem" }]`                                      |
| `awsAuthRefresh`             | Custom script that modifies the `.aws` directory (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                                 | `aws sso login --profile myprofile`                                     |
| `awsCredentialExport`        | Custom script that outputs JSON with AWS credentials (see [advanced credential configuration](/en/amazon-bedrock#advanced-credential-configuration))                                                                                                             | `/bin/generate_aws_grant.sh`                                            |

[Suite du contenu original...]
