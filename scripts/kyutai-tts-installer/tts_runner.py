#!/usr/bin/env python3
# Kyutai TTS PyTorch Runner
# Dockerized implementation for text-to-speech generation
import sys
import os
import argparse
import torch
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='Kyutai TTS PyTorch Runner')
    parser.add_argument('input_file', help='Input text file or "-" for stdin')
    parser.add_argument('output_file', help='Output audio file')
    parser.add_argument('--model', default='kyutai/tts-1.6b-en_fr', help='TTS model to use')
    parser.add_argument('--device', default='cuda' if torch.cuda.is_available() else 'cpu', help='Device to use')

    args = parser.parse_args()

    print(f"Using device: {args.device}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    # Handle stdin input
    if args.input_file == '-':
        # Read from stdin and create temporary file
        text = sys.stdin.read().strip()
        temp_file = '/tmp/temp_input.txt'
        with open(temp_file, 'w') as f:
            f.write(text)
        input_file = temp_file
    else:
        input_file = args.input_file

    # Check if the original TTS script exists
    tts_script = Path('/app/scripts/tts_pytorch.py')
    if tts_script.exists():
        print("Using original TTS script from Kyutai repository")
        import subprocess
        cmd = ['python', str(tts_script), input_file, args.output_file]
        subprocess.run(cmd, check=True)
    else:
        print("Using moshi package for TTS generation")
        import subprocess
        cmd = [
            'python', '-m', 'moshi.run_inference',
            '--hf-repo', args.model,
            input_file,
            args.output_file
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            sys.exit(1)
        print(f"Audio generated: {args.output_file}")

if __name__ == '__main__':
    main()
