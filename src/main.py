import numpy as np
import librosa
import matplotlib.pyplot as plt
from scipy import signal
import os

# normalized cross-correlation function
def norm_cross(x, y, method="correlate"):
    """
    Normalized cross-correlation between signals x and y.

    Parameters
    ----------
    x, y : np.ndarray
        Input signals (1D)
    method : str
        'correlate', 'convolve', or 'fftconvolve'
    """
    x = (x - np.mean(x)) / (np.std(x) + 1e-8)
    y = (y - np.mean(y)) / (np.std(y) + 1e-8)

    if method == "correlate":
        c = signal.correlate(x, y, mode="full")
    elif method == "convolve":
        c = signal.convolve(x, y[::-1], mode="full")
    elif method == "fftconvolve":
        c = signal.fftconvolve(x, y[::-1], mode="full")
    else:
        raise ValueError("method must be 'correlate', 'convolve', or 'fftconvolve'")

    # Normalize correlation by length
    c /= len(x)
    return c



# Segment audio into overlapping windows
def segment_audio(y, sr, window_sec=3.0, overlap=0.5):
    """
    y: np.ndarray
        Input audio signal.
    sr: int
        Sampling rate.
    window_sec: float
        Length of each window in seconds.
    overlap: float
        Fractional overlap between windows (0 to <1).
    Returns a list of overlapping windows.
    """
    window_len = int(window_sec * sr)
    step = int(window_len * (1 - overlap))
    segments = []

    for start in range(0, len(y) - window_len + 1, step):
        end = start + window_len
        segments.append(y[start:end])
    return segments


# Main
def main():
    # Output folder
    os.makedirs("../data/results", exist_ok=True)

    # Load both audios
    y1, sr1 = librosa.load("../data/audio1.wav", sr=None)
    y2, sr2 = librosa.load("../data/audio2.wav", sr=None)

    assert sr1 == sr2, "Sample rates must match!"
    sr = sr1

    # Segment y2 into overlapping windows (3 s, 50 % overlap)
    segments = segment_audio(y2, sr, window_sec=3.0, overlap=0.5)
    print(f"Segmented audio2 into {len(segments)} windows.")

    # Compute correlation of each segment against full y1
    methods = ["correlate", "convolve", "fftconvolve"]
    results = {}

    for method in methods:
        max_vals = []
        max_lags = []

        for i, seg in enumerate(segments):
            corr = norm_cross(y1, seg, method=method)
            lag = np.argmax(corr) - len(seg) + 1
            max_val = np.max(corr)
            max_vals.append(max_val)
            max_lags.append(lag / sr)

        results[method] = (max_vals, max_lags)
        print(f"[{method}] done.")

    # Visualization
    plt.figure(figsize=(10, 6))
    for method in methods:
        plt.plot(results[method][1], results[method][0], "o-", label=method)
    plt.xlabel("Lag (s)")
    plt.ylabel("Max normalized correlation")
    plt.title("Overlap correlation per segment")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("../data/results/segment_correlations.png")
    plt.show()

    # Show highest correlation overall
    best_method = max(methods, key=lambda m: max(results[m][0]))
    best_val = max(results[best_method][0])
    best_lag = results[best_method][1][np.argmax(results[best_method][0])]
    print(f"🏁 Best match using '{best_method}': corr={best_val:.3f} at lag={best_lag:.2f}s")


if __name__ == "__main__":
    main()
