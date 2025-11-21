#!/usr/bin/env python3
"""
OpenAI-Compatible Kyutai TTS API Server with Model Caching
Improved version that loads the model once and keeps it in memory
"""

import os
import io
import time
import asyncio
import subprocess
from pathlib import Path
from typing import Optional, Literal
import logging

import torch
import soundfile as sf
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global model variables - loaded once at startup
tts_model = None
device = None
sample_rate = None

class SpeechRequest(BaseModel):
    model: Literal["tts-1", "tts-1-hd"] = Field("tts-1", description="TTS model to use")
    input: str = Field(..., min_length=1, max_length=4096, description="Text to generate audio for")
    voice: Literal["alloy", "echo", "fable", "onyx", "nova", "shimmer"] = Field("alloy", description="Voice to use")
    response_format: Literal["mp3", "opus", "aac", "flac", "wav", "pcm"] = Field("mp3", description="Audio format")
    speed: Optional[float] = Field(1.0, ge=0.25, le=4.0, description="Speed of generated audio")
    language: Optional[Literal["fr", "en"]] = Field("fr", description="Language for voice selection (fr=French, en=English)")

app = FastAPI(
    title="OpenAI-Compatible TTS API (Cached)",
    description="OpenAI Audio Speech API compatible endpoint using Kyutai TTS with model caching",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OUTPUT_DIR = Path("/app/api_output")
OUTPUT_DIR.mkdir(exist_ok=True)

def load_tts_model():
    """Load TTS model once at startup and keep in memory"""
    global tts_model, device, sample_rate
    
    if tts_model is not None:
        logger.info("TTS model already loaded")
        return
    
    try:
        logger.info("🚀 Loading Kyutai TTS model (one-time initialization)...")
        
        # Import Kyutai TTS modules
        from moshi.models.loaders import CheckpointInfo
        from moshi.models.tts import DEFAULT_DSM_TTS_REPO, TTSModel
        
        # Set device
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {device}")
        
        # Load the TTS model
        checkpoint_info = CheckpointInfo.from_hf_repo(DEFAULT_DSM_TTS_REPO)
        
        tts_model = TTSModel.from_checkpoint_info(
            checkpoint_info, 
            n_q=32, 
            temp=0.6, 
            device=device
        )
        
        # Get sample rate
        sample_rate = tts_model.mimi.sample_rate
        
        logger.info(f"✅ TTS model loaded successfully!")
        logger.info(f"   Model: {DEFAULT_DSM_TTS_REPO}")
        logger.info(f"   Device: {device}")
        logger.info(f"   Sample Rate: {sample_rate}")
        
    except Exception as e:
        logger.error(f"❌ Failed to load TTS model: {e}")
        raise

def generate_audio_fast(text: str, voice: str = "alloy", speed: float = 1.0, language: str = "fr") -> bytes:
    """Generate audio using cached TTS model"""
    global tts_model, device, sample_rate
    if tts_model is None:
        raise HTTPException(status_code=500, detail="TTS model not loaded")
    try:
        logger.info(f"🎵 Generating audio for: '{text[:50]}{'...' if len(text) > 50 else ''}' (lang={language})")
        entries = tts_model.prepare_script([text], padding_between=1)
        voice_mapping_fr = {
            "alloy": "cml-tts/fr/2216_1745_000007-0001.wav",
            "echo": "cml-tts/fr/2223_1745_000009-0002.wav",
            "fable": "cml-tts/fr/2465_1943_000152-0002.wav",
            "onyx": "cml-tts/fr/296_1028_000022-0001.wav",
            "nova": "cml-tts/fr/2114_1656_000053-0001.wav",
            "shimmer": "cml-tts/fr/2154_2576_000020-0003.wav"
        }
        voice_mapping_en = {
            "alloy": "expresso/ex03-ex01_happy_001_channel1_334s.wav",
            "echo": "expresso/ex04-ex01_happy_001_channel1_334s.wav",
            "fable": "expresso/ex05-ex01_happy_001_channel1_334s.wav",
            "onyx": "expresso/ex06-ex01_happy_001_channel1_334s.wav",
            "nova": "expresso/ex07-ex01_happy_001_channel1_334s.wav",
            "shimmer": "expresso/ex08-ex01_happy_001_channel1_334s.wav"
        }
        voice_mapping = voice_mapping_fr if language == "fr" else voice_mapping_en
        selected_voice = voice_mapping.get(voice, voice_mapping["alloy"])
        
        try:
            voice_path = tts_model.get_voice_path(selected_voice)
        except:
            # Fallback to default if voice not found
            voice_path = tts_model.get_voice_path("expresso/ex03-ex01_happy_001_channel1_334s.wav")
        
        # Prepare condition attributes
        condition_attributes = tts_model.make_condition_attributes(
            [voice_path], cfg_coef=2.0
        )
        
        # Generate audio
        pcms = []
        
        def on_frame(frame):
            if (frame != -1).all():
                pcm = tts_model.mimi.decode(frame[:, 1:, :]).cpu().numpy()
                pcms.append(torch.clamp(torch.from_numpy(pcm[0, 0]), -1, 1).numpy())
        
        all_entries = [entries]
        all_condition_attributes = [condition_attributes]
        
        with tts_model.mimi.streaming(len(all_entries)):
            result = tts_model.generate(all_entries, all_condition_attributes, on_frame=on_frame)
        
        # Concatenate all audio frames
        if pcms:
            import numpy as np
            audio = np.concatenate(pcms, axis=-1)
            
            # Apply speed adjustment if needed
            if speed != 1.0:
                # Simple speed adjustment by resampling
                from scipy import signal
                audio_length = len(audio)
                new_length = int(audio_length / speed)
                audio = signal.resample(audio, new_length)
            
            # Convert to bytes
            audio_bytes = io.BytesIO()
            sf.write(audio_bytes, audio, samplerate=sample_rate, format='WAV')
            audio_bytes.seek(0)
            
            logger.info(f"✅ Audio generated successfully ({len(audio)/sample_rate:.2f}s)")
            return audio_bytes.read()
        else:
            raise Exception("No audio frames generated")
            
    except Exception as e:
        logger.error(f"❌ TTS generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Audio generation failed: {str(e)}")

def convert_audio_format(audio_wav_bytes: bytes, output_format: str) -> bytes:
    """Convert WAV audio to requested format using ffmpeg"""
    try:
        if output_format == "wav":
            return audio_wav_bytes
            
        # Use ffmpeg to convert
        cmd = ["ffmpeg", "-f", "wav", "-i", "pipe:0", "-f", output_format, "pipe:1"]
        
        result = subprocess.run(
            cmd, 
            input=audio_wav_bytes, 
            capture_output=True, 
            check=True
        )
        return result.stdout
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Audio conversion failed: {e}")
        raise HTTPException(status_code=500, detail=f"Audio conversion failed: {e}")

@app.post("/v1/audio/speech")
async def create_speech(request: SpeechRequest):
    """
    OpenAI-compatible audio speech endpoint
    Uses cached TTS model for fast generation
    """
    try:
        start_time = time.time()
        
        # Generate audio with cached model
        audio_wav_bytes = generate_audio_fast(
            text=request.input,
            voice=request.voice,
            speed=request.speed,
            language=request.language
        )
        
        # Convert to requested format
        audio_data = convert_audio_format(audio_wav_bytes, request.response_format)
        
        generation_time = time.time() - start_time
        logger.info(f"⚡ Total generation time: {generation_time:.2f}s")
        
        # Set appropriate content type
        content_types = {
            "mp3": "audio/mpeg",
            "opus": "audio/opus", 
            "aac": "audio/aac",
            "flac": "audio/flac",
            "wav": "audio/wav",
            "pcm": "audio/pcm"
        }
        
        return Response(
            content=audio_data,
            media_type=content_types.get(request.response_format, "audio/wav"),
            headers={
                "Content-Disposition": f"attachment; filename=speech.{request.response_format}",
                "X-Generation-Time": str(generation_time)
            }
        )
        
    except Exception as e:
        logger.error(f"Speech generation failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/v1/models")
async def list_models():
    """List available models (OpenAI-compatible)"""
    return {
        "object": "list",
        "data": [
            {
                "id": "tts-1",
                "object": "model",
                "created": 1677610602,
                "owned_by": "kyutai",
                "permission": [],
                "root": "tts-1",
                "parent": None
            },
            {
                "id": "tts-1-hd", 
                "object": "model",
                "created": 1677610602,
                "owned_by": "kyutai",
                "permission": [],
                "root": "tts-1-hd",
                "parent": None
            }
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint with model status"""
    model_loaded = tts_model is not None
    return {
        "status": "healthy" if model_loaded else "loading",
        "model_loaded": model_loaded,
        "cuda_available": torch.cuda.is_available(),
        "device": str(device) if device else None,
        "service": "kyutai-tts-openai-compatible-cached"
    }

@app.get("/reload-model")
async def reload_model():
    """Reload the TTS model (admin endpoint)"""
    global tts_model
    try:
        tts_model = None
        load_tts_model()
        return {"status": "success", "message": "Model reloaded successfully"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    logger.info("🚀 Starting TTS API server with model caching...")
    load_tts_model()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
