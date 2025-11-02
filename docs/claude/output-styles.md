# Claude Code Output Styles

**Source:** https://docs.claude.com/en/docs/claude-code/output-styles.md
**Extrait le:** 2025-11-02
**Sujet:** Output Styles - Customisation des styles de sortie

---

# Claude Code Output Styles - Summary

## Deprecation Status

Output styles are being phased out as of **November 5, 2025**. The `/output-style` command and related functionality will be removed.

## Migration Path

Users should transition to these alternatives:

- **System prompt flags**: `--system-prompt-file`, `--system-prompt`, or `--append-system-prompt`
- **CLAUDE.md files**: For project-specific customizations
- **Plugins**: For more sophisticated behavioral modifications

## Legacy Output Styles (Reference Only)

The documentation previously offered three modes:

1. **Default**: Standard software engineering assistance
2. **Explanatory**: Educational insights about implementation choices and patterns
3. **Learning**: Collaborative mode with `TODO(human)` markers for hands-on participation

## Plugin Alternative

Users relying on the Explanatory style can install the `explanatory-output-style` plugin from the Claude Code marketplace, which "provides educational insights about implementation choices" and "balances task completion with learning opportunities."

## Key Distinction

Output styles modified the core system prompt by removing software engineering instructions and adding custom directives. This differs from CLAUDE.md (which adds content as user messages) and slash commands (which function as stored prompts).
