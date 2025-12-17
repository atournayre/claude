# Plan : Plugin Gemini pour Claude Code Marketplace

## Objectif

Créer un plugin `gemini/` permettant de déléguer des tâches spécialisées à Gemini CLI tout en gardant Claude comme orchestrateur principal.

## Cas d'usage prioritaires

1. **Contexte ultra-long** : Analyse codebases/docs (1M tokens Gemini)
2. **Deep Think** : Problèmes complexes math/logique/architecture
3. **Google Search** : Infos temps réel via intégration Google native

## Structure du plugin

```
gemini/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   ├── analyze.md      # /gemini:analyze <path> <question>
│   ├── think.md        # /gemini:think <problem>
│   └── search.md       # /gemini:search <query>
├── agents/
│   ├── gemini-analyzer.md     # Contexte long
│   ├── gemini-thinker.md      # Deep Think
│   └── gemini-researcher.md   # Google Search
└── README.md
```

## Fichiers à créer

### 1. plugin.json

```json
{
  "name": "gemini",
  "version": "1.0.0",
  "description": "Délégation Gemini CLI : contexte ultra-long, Deep Think, Google Search",
  "author": { "name": "Aurélien Tournayre", "email": "aurelien.tournayre@gmail.com" }
}
```

### 2. Agent gemini-analyzer.md

```yaml
---
name: gemini-analyzer
description: Délègue l'analyse de contextes ultra-longs (codebases, docs) à Gemini. À utiliser quand le contexte dépasse les capacités de Claude.
tools: Bash, Read, Glob, Grep
model: haiku
---
```

**Pattern d'appel** :
```bash
# Concaténer fichiers cibles
find "$TARGET" -type f \( -name "*.php" -o -name "*.md" \) \
  ! -name "*.env*" ! -name "*secret*" \
  | xargs cat > /tmp/context.txt

# Vérifier taille (< 4MB)
# Appeler Gemini
cat /tmp/context.txt | gemini -m gemini-2.5-pro "$PROMPT"
```

### 3. Agent gemini-thinker.md

```yaml
---
name: gemini-thinker
description: Délègue les problèmes complexes (math, logique, architecture) à Gemini Deep Think. À utiliser pour réflexion approfondie.
tools: Bash
model: haiku
---
```

**Pattern d'appel** :
```bash
gemini -m gemini-2.5-pro "Think step by step: $PROBLEM"
```

### 4. Agent gemini-researcher.md

```yaml
---
name: gemini-researcher
description: Recherche infos fraîches via Google Search intégré à Gemini. À utiliser pour docs récentes, versions actuelles, actualités tech.
tools: Bash
model: haiku
---
```

**Pattern d'appel** :
```bash
gemini -m gemini-2.5-flash "Search and answer: $QUERY"
```

### 5. Commandes slash

- `/gemini:analyze` → Invoque agent gemini-analyzer
- `/gemini:think` → Invoque agent gemini-thinker
- `/gemini:search` → Invoque agent gemini-researcher

## Sécurité

- Filtrage fichiers sensibles (.env, credentials) avant envoi
- Limite taille contexte : 4MB max
- Timeout : 300s par défaut
- Retry avec backoff : 5s, 10s, 20s

## Ordre d'implémentation

1. Structure de base (`plugin.json`, `README.md`)
2. Agent + commande `gemini-analyzer` (contexte long)
3. Agent + commande `gemini-thinker` (Deep Think)
4. Agent + commande `gemini-researcher` (Search)
5. Mise à jour `marketplace.json`

## Fichiers de référence

- `dev/agents/phpstan-error-resolver.md` - Pattern agent
- `doc/skills/doc-loader/SKILL.md` - Pattern délégation + rate limiting
- `git/.claude-plugin/plugin.json` - Structure plugin.json
