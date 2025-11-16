#!/usr/bin/env python3
# Test script for Kyutai TTS
import sys
import torch

def test_python_version():
    print(f"Python version: {sys.version}")
    major, minor = sys.version_info[:2]
    if major == 3 and minor >= 12:
        print("✓ Python 3.12+ detected")
    else:
        print("✗ Python 3.12+ required")
        return False
    return True

def test_cuda():
    print("Testing CUDA availability...")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        print(f"CUDA version: {torch.version.cuda}")
        print(f"CUDA device count: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")
            print(f"Memory: {torch.cuda.get_device_properties(i).total_memory / 1024**3:.1f} GB")
    else:
        print("CUDA not available. TTS will run on CPU (slower).")

def test_moshi():
    print("\nTesting moshi package...")
    try:
        import moshi
        print(f"Moshi package imported successfully")
        print(f"Moshi version: {getattr(moshi, '__version__', 'unknown')}")
    except ImportError as e:
        print(f"Failed to import moshi: {e}")
        return False
    return True

def test_huggingface():
    print("\nTesting Hugging Face connection...")
    try:
        from huggingface_hub import hf_hub_download
        print("Hugging Face Hub available")
        # Try to check if we can access the model (without downloading)
        from huggingface_hub import repo_exists
        if repo_exists("kyutai/tts-1.6b-en_fr"):
            print("✓ Kyutai TTS model repository is accessible")
        else:
            print("⚠ Cannot verify model repository access")
    except Exception as e:
        print(f"Issue with Hugging Face Hub: {e}")

def test_api_dependencies():
    print("\nTesting API dependencies...")
    try:
        import fastapi
        import uvicorn
        print("✓ FastAPI and Uvicorn available")
        return True
    except ImportError as e:
        print(f"✗ API dependencies missing: {e}")
        return False

if __name__ == '__main__':
    python_ok = test_python_version()
    test_cuda()
    moshi_ok = test_moshi()
    test_huggingface()
    api_ok = test_api_dependencies()

    if python_ok and moshi_ok and api_ok:
        print("\n✓ Environment setup appears to be working!")
        print("\nTo run TTS:")
        print("echo 'Hello, this is a test.' | python scripts/tts_runner.py - /app/output/test.wav")
        print("\nTo start API server:")
        print("python api_server.py")
        print("Then visit: http://localhost:8000/docs")
    else:
        print("\n✗ Environment setup has issues. Check the logs above.")
        sys.exit(1)
