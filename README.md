# Audio Overlap Detection (Python)
This project identifies common audio segments between two `.wav` files using normalized cross-correlation.  
It’s inspired by a MATLAB implementation using different convolution methods.

## Features
- Loads and processes `.wav` audio files
- Segments one audio into overlapping windows
- Computes normalized cross-correlation using `scipy.signal` (correlate, convolve, fftconvolve)
- Visualizes correlation results to find overlaps

## Run
pip install -r requirements.txt
python3 src/main.py
