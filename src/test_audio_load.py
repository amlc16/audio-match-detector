import librosa
import soundfile as sf
import numpy as np

# Paths to your audio files
audio1_path = "../data/audio1.wav"
audio2_path = "../data/audio2.wav"

def load_audio(path, sr=16000):
    y, sr = librosa.load(path, sr=sr, mono=True)
    print(f"Loaded {path}")
    print(f"  Duration: {len(y)/sr:.2f} seconds")
    print(f"  Sample rate: {sr} Hz")
    print(f"  Mean amplitude: {np.mean(y):.4f}, Std: {np.std(y):.4f}")
    print("-" * 40)
    return y, sr

if __name__ == "__main__":
    y1, sr1 = load_audio(audio1_path)
    y2, sr2 = load_audio(audio2_path)

    # Verify both have the same sampling rate
    if sr1 != sr2:
        print("⚠️ Sampling rates differ, you should resample them to match.")
    else:
        print("✅ Sampling rates match!")

    # Optional: Listen to the audios if you run this in Jupyter
    # import IPython.display as ipd
    # ipd.Audio(y1, rate=sr1)
