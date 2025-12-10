# Claude Code in Slack

**Source:** https://code.claude.com/docs/en/slack.md
**Extrait le:** 2025-12-10
**Sujet:** Outside of the Terminal - Integration

---

> Delegate coding tasks directly from your Slack workspace

Claude Code in Slack brings the power of Claude Code directly into your Slack workspace. When you mention `@Claude` with a coding task, Claude automatically detects the intent and creates a Claude Code session on the web, allowing you to delegate development work without leaving your team conversations.

This integration is built on the existing Claude for Slack app but adds intelligent routing to Claude Code on the web for coding-related requests.

## Use cases

* **Bug investigation and fixes**: Ask Claude to investigate and fix bugs as soon as they're reported in Slack channels.
* **Quick code reviews and modifications**: Have Claude implement small features or refactor code based on team feedback.
* **Collaborative debugging**: When team discussions provide crucial context (e.g., error reproductions or user reports), Claude can use that information to inform its debugging approach.
* **Parallel task execution**: Kick off coding tasks in Slack while you continue other work, receiving notifications when complete.

## Prerequisites

Before using Claude Code in Slack, ensure you have the following:

| Requirement            | Details                                                                        |
| :--------------------- | :----------------------------------------------------------------------------- |
| Claude Plan            | Pro, Max, Team, or Enterprise with Claude Code access (premium seats)          |
| Claude Code on the web | Access to [Claude Code on the web](/en/claude-code-on-the-web) must be enabled |
| GitHub Account         | Connected to Claude Code on the web with at least one repository authenticated |
| Slack Authentication   | Your Slack account linked to your Claude account via the Claude app            |

## Setting up Claude Code in Slack

<Steps>
  <Step title="Install the Claude App in Slack">
    A workspace administrator must install the Claude app from the Slack App Marketplace. Visit the [Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4) and click "Add to Slack" to begin the installation process.
  </Step>

  <Step title="Connect your Claude account">
    After the app is installed, authenticate your individual Claude account:

    1. Open the Claude app in Slack by clicking on "Claude" in your Apps section
    2. Navigate to the App Home tab
    3. Click "Connect" to link your Slack account with your Claude account
    4. Complete the authentication flow in your browser
  </Step>

  <Step title="Configure Claude Code on the web">
    Ensure your Claude Code on the web is properly configured:

    * Visit [claude.ai/code](https://claude.ai/code) and sign in with the same account you connected to Slack
    * Connect your GitHub account if not already connected
    * Authenticate at least one repository that you want Claude to work with
  </Step>

  <Step title="Choose your routing mode">
    After connecting your accounts, configure how Claude handles your messages in Slack. Navigate to the Claude App Home in Slack to find the **Routing Mode** setting.

    | Mode            | Behavior                                                                                                                                                                                                                                 |
    | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | **Code only**   | Claude routes all @mentions to Claude Code sessions. Best for teams using Claude in Slack exclusively for development tasks.                                                                                                             |
    | **Code + Chat** | Claude analyzes each message and intelligently routes between Claude Code (for coding tasks) and Claude Chat (for writing, analysis, and general questions). Best for teams who want a single @Claude entry point for all types of work. |

    <Note>
      In Code + Chat mode, if Claude routes a message to Chat but you wanted a coding session, you can click "Retry as Code" to create a Claude Code session instead. Similarly, if it's routed to Code but you wanted a Chat session, you can choose that option in that thread.
    </Note>
  </Step>
</Steps>

[Full content continues...]

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://code.claude.com/docs/llms.txt
