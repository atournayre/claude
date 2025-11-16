# Use Python 3.12 base image and add CUDA support
FROM python:3.12-slim

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV CUDA_VISIBLE_DEVICES=0

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    build-essential \
    libsndfile1 \
    ffmpeg \
    sox \
    alsa-utils \
    pulseaudio \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies first (for better caching)
RUN pip install --no-cache-dir --upgrade pip

# Install PyTorch with CUDA support for Python 3.12
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Install core dependencies
RUN pip install --no-cache-dir \
    numpy \
    scipy \
    librosa \
    soundfile \
    huggingface_hub \
    einops \
    transformers \
    accelerate

# Install API dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn[standard] \
    python-multipart \
    pydantic

# Install moshi package with all dependencies (following Colab notebook)
RUN pip install --no-cache-dir 'sphn<0.2'
RUN pip install --no-cache-dir "moshi==0.2.8"

# Create directories for input/output
RUN mkdir -p /app/input /app/output /app/scripts /app/api_output

# Download the Kyutai delayed-streams-modeling repository
RUN git clone https://github.com/kyutai-labs/delayed-streams-modeling.git /app/kyutai-repo

# Copy the TTS script from the repository
RUN cp /app/kyutai-repo/scripts/tts_pytorch.py /app/scripts/ || echo "TTS script not found, will create custom one"

# Copy custom scripts
COPY tts_runner.py /app/scripts/
COPY test_tts.py /app/

# Make the scripts executable
RUN chmod +x /app/scripts/tts_runner.py /app/test_tts.py

# Copy the API server with French voices and dependency checker
COPY api_server.py /app/
COPY dependency_check.py /app/

# Download French CML voices for better French accent
RUN python -c "
from huggingface_hub import hf_hub_download
import os
os.environ['HF_HOME'] = '/app/cache'

french_voices = [
    'cml-tts/fr/12977_10625_000037-0001.wav.1e68beda@240.safetensors',
    'cml-tts/fr/1406_1028_000009-0003.wav.1e68beda@240.safetensors',
    'cml-tts/fr/10087_11650_000028-0002.wav.1e68beda@240.safetensors',
    'cml-tts/fr/10177_10625_000134-0003.wav.1e68beda@240.safetensors'
]

for voice in french_voices:
    try:
        hf_hub_download(
            repo_id='kyutai/tts-voices',
            filename=voice,
            repo_type='model'
        )
    except Exception as e:
        print(f'Warning: Could not download {voice}: {e}')
"

# Create example text file
RUN echo "Hello, this is Kyutai Text-to-Speech running in Docker with GPU support!" > /app/input/example.txt

# Set default command to start API server
CMD ["python", "api_server.py"]

# Expose any ports if needed (for future web interface)
EXPOSE 8000

# Add healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import torch; print('CUDA:', torch.cuda.is_available())" || exit 1
