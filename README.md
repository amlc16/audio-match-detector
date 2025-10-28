# Audio Overlap Detection using Normalized Cross-Correlation

This project identifies **common audio segments shared between two `.wav` files** by applying *normalized cross-correlation* — similar to MATLAB’s `normxcorr2` function, but implemented fully in Python.

It can detect where two audio clips share overlapping or repeated content, even when one clip contains extra material before or after the shared section.

---

## Features

- Load and process `.wav` audio files
- Segment one audio into overlapping time windows (e.g. 3s, 50% overlap)
- Compute normalized cross-correlation between signals
- Compare three correlation methods:
  - `scipy.signal.correlate`
  - `scipy.signal.convolve`
  - `scipy.signal.fftconvolve`
- Plot correlation strength vs. time lag
- Identify the time offset of the best match (where two audios overlap most)

---

## 🧠 Background

This project started as a Python translation of a **MATLAB template matching function** provided by a professor.  
While the MATLAB version (`norm_cross.m`) was 2D for images, this Python version focuses on **1D audio correlation**.

Applications include:
- Detecting reused or copied audio clips between videos  
- Aligning multi-camera recordings  
- Synchronizing sound from different sources

## Project Structure
speech-audio-match/
│
├── data/
│ ├── audio1.wav
│ ├── audio2.wav
│ └── results/ # correlation plots and outputs
│
├── src/
│ ├── test_audio_load.py # simple script to verify audio loading
│ └── main.py # main correlation + segmentation pipeline
│
├── requirements.txt
├── .gitignore
└── README.md

## Setup

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/audio-overlap-detector.git
cd audio-overlap-detector


### 2. Install dependencies

pip install -r requirements.txt


### 3. Prepare audio files

Put your .wav files in the data/ folder.
If you have .m4a recordings (e.g. from iPhone Voice Memos), convert them to mono 16 kHz using:

ffmpeg -i input.m4a -ar 16000 -ac 1 data/input.wav

## Results

Each point in the plot represents a segment of audio2 compared to audio1.
Higher correlation values indicate stronger similarity or overlap.
The lag (in seconds) shows where in audio1 the overlap occurs.