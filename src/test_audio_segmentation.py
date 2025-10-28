import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
import os

y, sr = librosa.load("../data/audio1.wav", sr=None)

# Detect non-silent intervals
intervals = librosa.effects.split(y, top_db=25)

os.makedirs("../data/segments", exist_ok=True)

for i, (start, end) in enumerate(intervals):
    segment = y[start:end]
    out_path = f"../data/segments/segment_{i+1}.wav"
    sf.write(out_path, segment, sr)
    print(f"Saved {out_path} ({(end-start)/sr:.2f} s)")

# Visualize
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr, alpha=0.6)
for start, end in intervals:
    plt.axvspan(start/sr, end/sr, color="red", alpha=0.3)
plt.title("Detected Speech Segments")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.tight_layout()
plt.savefig("../data/segments_plot.png")
plt.show()
