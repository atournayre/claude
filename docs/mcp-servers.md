# Serveurs MCP

Model Context Protocol (MCP) permet d'étendre les capacités de Claude Code via des serveurs spécialisés.

## Configuration

Les fichiers de configuration MCP sont dans `~/.claude/mcp/`.

Chaque serveur a son fichier JSON dédié qui définit comment le connecter.

## Serveurs installés

<details>
<summary><strong>Sentry</strong></summary>

**Fichier**: `mcp/sentry.json`
**Type**: HTTP
**Usage**: Monitoring erreurs et performance via Sentry.io

**Configuration**:
```json
{
  "mcpServers": {
    "sentry": {
      "type": "http",
      "url": "https://mcp.sentry.dev/mcp"
    }
  }
}
```

**Fonctionnalités**:
- Accès projets Sentry
- Analyse erreurs et exceptions
- Métriques performance
- Gestion issues

**Lancer uniquement Sentry**:
```bash
claude --mcp-config ~/.claude/mcp/sentry.json --strict-mcp-config
```

</details>

<details>
<summary><strong>Chrome DevTools</strong></summary>

**Fichier**: `mcp/chrome-dev-tools.json`
**Type**: NPX
**Usage**: Debug et inspection navigateur Chrome en temps réel

**Configuration**:
```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": [
        "-y",
        "chrome-devtools-mcp@latest",
        "--acceptInsecureCerts",
        "--isolated",
        "--browserUrl=https://localhost:9222"
      ]
    }
  }
}
```

**Prérequis**:
- Chrome lancé avec `--remote-debugging-port=9222`
- Commande : `google-chrome --remote-debugging-port=9222`

**Fonctionnalités**:
- Inspection DOM
- Console JavaScript
- Network monitoring
- Performance profiling

**Lancer uniquement Chrome DevTools**:
```bash
claude --mcp-config ~/.claude/mcp/chrome-dev-tools.json --strict-mcp-config
```

</details>

<details>
<summary><strong>Context7</strong></summary>

**Fichier**: `mcp/context7.json`
**Type**: NPX
**Usage**: Documentation code à jour pour LLMs (repos GitHub/GitLab)

**Configuration**:
```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": [
        "-y",
        "@upstash/context7-mcp",
        "--api-key",
        "${CONTEXT7_API_KEY}"
      ]
    }
  }
}
```

**Prérequis**:
1. Compte gratuit sur [context7.com/dashboard](https://context7.com/dashboard)
2. Variable d'env `CONTEXT7_API_KEY` dans `~/.bashrc` ou `~/.zshrc`:
   ```bash
   export CONTEXT7_API_KEY="votre_clé_api"
   ```
3. Recharger shell : `source ~/.bashrc`

**Fonctionnalités avec clé API**:
- Accès repos privés GitHub/GitLab
- Rate limits augmentés
- Cache persistant
- Historique contextes générés

**Mode gratuit** (sans clé API):
- Repos publics uniquement
- Rate limits basiques
- Pas de cache persistant

**Lancer uniquement Context7**:
```bash
claude --mcp-config ~/.claude/mcp/context7.json --strict-mcp-config
```

</details>

## Ajouter un nouveau serveur MCP

1. Créer fichier JSON dans `~/.claude/mcp/`:
   ```bash
   touch ~/.claude/mcp/mon-serveur.json
   ```

2. Définir configuration selon type (HTTP, NPX, stdio)

3. Redémarrer Claude Code

4. Vérifier serveur actif: `/mcp list`

## Troubleshooting

**Serveur ne démarre pas**:
- Vérifier syntaxe JSON (pas de virgules trailing)
- Vérifier variables d'env définies
- Logs : vérifier console Claude Code

**Variables d'environnement non reconnues**:
- Vérifier export dans `~/.bashrc` ou `~/.zshrc`
- Relancer shell : `source ~/.bashrc`
- Redémarrer Claude Code après modification

**Chrome DevTools ne connecte pas**:
- Chrome doit être lancé AVANT Claude Code
- Port 9222 non utilisé par autre process
- Vérifier `https://localhost:9222` accessible dans navigateur
