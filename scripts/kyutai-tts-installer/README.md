# Kyutai TTS - Installer

Installation automatique de Kyutai TTS pour notifications vocales Claude Code.

## Installation

```bash
cd ~/.claude/scripts/kyutai-tts-installer
./install.sh
```

**Durée**: ~10-15 minutes (build Docker + téléchargement modèles)

## Prérequis

- Ubuntu/Debian Linux
- Docker 20.10+
- GPU NVIDIA (8GB+ VRAM)
- Driver NVIDIA 470+
- 20GB espace disque

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
├── notification-kyutai.sh  # Hook notifications Claude Code
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
  ~/.claude/scripts/notification-kyutai.sh
```

**Pour toute question**: voir documentation complète dans `docs/kyutai-tts.md`
