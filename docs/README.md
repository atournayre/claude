# Documentation Claude Code

Documentation technique pour la configuration Claude Code.

## Contenu

### Notifications
- **[Kyutai TTS](kyutai-tts.md)** - Notifications vocales avec synthèse vocale Kyutai

### Documentation externe (chargée via agents)
- `api-platform/` - Documentation API Platform
- `atournayre-framework/` - Documentation atournayre-framework
- `claude/` - Documentation Claude Code
- `meilisearch/` - Documentation Meilisearch
- `symfony/` - Documentation Symfony

## Rechargement documentation

Pour recharger la documentation externe:

```bash
# Claude Code
/claude:doc:load

# Symfony
/symfony:doc:load

# Autres frameworks
/doc:framework-load <framework-name>
```

## Structure

```
docs/
├── README.md                    # Ce fichier
├── kyutai-tts.md               # Doc Kyutai TTS (versionné)
├── api-platform/               # Doc API Platform (non versionné)
├── atournayre-framework/       # Doc framework (non versionné)
├── claude/                     # Doc Claude Code (non versionné)
├── meilisearch/                # Doc Meilisearch (non versionné)
└── symfony/                    # Doc Symfony (non versionné)
```

**Note**: Seules les documentations rédigées manuellement sont versionnées. Les documentations externes chargées automatiquement sont exclues du contrôle de version.
