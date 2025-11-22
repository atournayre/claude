#!/bin/bash
# Clean Triton/TorchInductor cache on startup to prevent GPU detection issues
rm -rf /tmp/torchinductor_root /root/.triton /tmp/triton_* 2>/dev/null || true

# Execute original entrypoint or command
exec "$@"
