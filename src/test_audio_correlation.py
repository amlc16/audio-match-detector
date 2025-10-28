import numpy as np
import librosa
import matplotlib.pyplot as plt

# Load both audios
y1, sr1 = librosa.load("../data/audio1.wav", sr=None)
y2, sr2 = librosa.load("../data/audio2.wav", sr=None)

# Normalize
y1 = y1 / np.max(np.abs(y1))
y2 = y2 / np.max(np.abs(y2))

# Cross-correlation
corr = np.correlate(y1, y2, mode="full")
lags = np.arange(-len(y2) + 1, len(y1))

# Normalize correlation
corr /= np.max(np.abs(corr))

# Plot correlation
plt.figure(figsize=(10, 4))
plt.plot(lags / sr1, corr)
plt.title("Cross-Correlation between Audio1 and Audio2")
plt.xlabel("Lag (seconds)")
plt.ylabel("Correlation")
plt.grid(True)
plt.tight_layout()
plt.savefig("../data/correlation_plot.png")
plt.show()

# Display correlation peak
max_corr = np.max(corr)
print(f"Max correlation: {max_corr:.3f}")
if max_corr > 0.8:
    print("🔍 The audios are quite similar (possibly overlapping or repeated).")
else:
    print("🌀 The audios differ significantly.")