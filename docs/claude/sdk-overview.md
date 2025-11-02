# Claude Agent SDK Overview

**Source:** https://docs.claude.com/en/docs/claude-code/sdk/sdk-overview
**Extrait le:** 2025-11-02
**Sujet:** SDK - Vue d'ensemble

---

## Installation

Pour TypeScript/Node.js :
```bash
npm install @anthropic-ai/claude-agent-sdk
```

## SDKs disponibles

Le Claude Agent SDK est disponible sous plusieurs formes :
- **TypeScript SDK** - Pour les applications Node.js et web
- **Python SDK** - Pour les applications Python et data science
- **Mode Streaming vs Single** - Options pour différents patterns d'entrée

## Fonctionnalités clés

Le SDK, construit sur le harness d'agent de Claude Code, fournit :

- **Gestion du contexte** : Compaction automatique et gestion du contexte pour garantir que votre agent ne manque pas de contexte
- **Écosystème d'outils riche** : Opérations sur fichiers, exécution de code, recherche web, et extensibilité MCP
- **Permissions avancées** : Contrôle granulaire des capacités de l'agent
- **Essentiels de production** : Gestion des erreurs, gestion des sessions, et monitoring
- **Intégration optimisée avec Claude** : Cache automatique des prompts et optimisations de performance

## Ce que vous pouvez construire

Exemples de cas d'usage :
- **Agents de codage** : Agents SRE, bots de revue de sécurité, assistants d'ingénierie, agents de revue de code
- **Agents métier** : Assistants juridiques, conseillers financiers, agents de support client, assistants de création de contenu

## Authentification

Les utilisateurs récupèrent les clés API depuis la Console Claude et définissent la variable d'environnement `ANTHROPIC_API_KEY`. Support des fournisseurs tiers incluant Amazon Bedrock et Google Vertex AI.

## Fonctionnalités principales du SDK

Le SDK fournit un accès complet aux fonctionnalités de Claude Code incluant :
- Subagents
- Agent Skills
- Hooks
- Commandes slash
- Plugins
- Gestion de la mémoire via les fichiers `CLAUDE.md`
