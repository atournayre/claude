#!/usr/bin/env python3
"""
Check if all Kyutai TTS dependencies are properly installed
"""

import sys

def check_dependencies():
    print("🔍 Checking Kyutai TTS Dependencies")
    print("=" * 40)
    
    dependencies = [
        "torch",
        "numpy", 
        "einops",
        "transformers",
        "accelerate",
        "soundfile",
        "librosa",
        "huggingface_hub",
        "moshi",
        "sphn"
    ]
    
    missing = []
    installed = []
    
    for dep in dependencies:
        try:
            __import__(dep)
            installed.append(dep)
            print(f"✓ {dep}")
        except ImportError as e:
            missing.append((dep, str(e)))
            print(f"✗ {dep}: {e}")
    
    print(f"\n📊 Summary:")
    print(f"✓ Installed: {len(installed)}")
    print(f"✗ Missing: {len(missing)}")
    
    if missing:
        print(f"\n🔧 To fix missing dependencies:")
        for dep, error in missing:
            print(f"pip install {dep}")
    
    print(f"\n🧪 Testing Kyutai TTS imports:")
    try:
        from moshi.models.loaders import CheckpointInfo
        print("✓ CheckpointInfo import successful")
    except Exception as e:
        print(f"✗ CheckpointInfo import failed: {e}")
        
    try:
        from moshi.models.tts import DEFAULT_DSM_TTS_REPO, DEFAULT_DSM_TTS_VOICE_REPO, TTSModel
        print("✓ TTSModel imports successful")
    except Exception as e:
        print(f"✗ TTSModel imports failed: {e}")
    
    return len(missing) == 0

if __name__ == "__main__":
    success = check_dependencies()
    if success:
        print("\n🎉 All dependencies are installed correctly!")
    else:
        print("\n❌ Some dependencies are missing. Please install them first.")
        sys.exit(1)
