# Kyutai TTS - Installer

Installation automatique de Kyutai TTS pour notifications vocales Claude Code avec voix françaises CML.

## Installation

```bash
cd ~/.claude/scripts/kyutai-tts-installer
./install.sh
```

**Durée**: ~10-15 minutes (build Docker + téléchargement modèles + voix françaises)

## Prérequis

- Ubuntu/Debian Linux
- Docker 20.10+
- GPU NVIDIA (8GB+ VRAM)
- Driver NVIDIA 470+
- 20GB espace disque

## Voix françaises

Le système installe automatiquement 4 voix françaises du dataset CML-TTS:
- **onyx** (recommandée) - Accent français européen
- alloy, echo, fable - Autres voix françaises

## Configuration

Ajoutez dans `~/.claude/settings.json`:

```json
{
  "env": {
    "KYUTAI_VOICE": "onyx",
    "ENGINEER_NAME": "Votre nom"
  }
}
```

Ou exportez dans `~/.bashrc`:
```bash
export KYUTAI_VOICE="onyx"
export ENGINEER_NAME="Votre nom"
```

## Fichiers requis

Le script d'installation s'attend à ce que `~/.claude/scripts/notification-kyutai.py` existe déjà. Ce fichier est la source de vérité pour le hook de notification.

Structure attendue:
```
~/.claude/scripts/
├── notification-kyutai.py          # Requis (source)
└── kyutai-tts-installer/
    ├── install.sh                   # Script installation
    ├── api_server.py                # API avec voix françaises
    ├── dependency_check.py          # Vérification dépendances
    ├── Dockerfile                   # Image Docker
    ├── tts_runner.py
    └── test_tts.py
```

## Documentation complète

**Voir**: [../../docs/kyutai-tts.md](../../docs/kyutai-tts.md)

La documentation complète contient:
- Guide installation détaillé
- Configuration Claude Code
- Gestion service systemd
- Tests et troubleshooting
- API reference
- Performance et optimisations

## Fichiers

```
kyutai-tts-installer/
├── install.sh              # Script installation automatique
├── notification-kyutai.py  # Hook notifications Claude Code (Python)
├── Dockerfile              # Image Docker custom
├── tts_runner.py           # Runner TTS
└── test_tts.py             # Script test
```

## Support rapide

```bash
# Statut service
systemctl --user status kyutai-tts

# Logs
journalctl --user -fu kyutai-tts

# Test API
curl http://localhost:9876/health

# Test notification
echo '{"notification_type":"permission_prompt"}' | \
  ~/.claude/scripts/notification-kyutai.py
```

**Pour toute question**: voir documentation complète dans `docs/kyutai-tts.md`
