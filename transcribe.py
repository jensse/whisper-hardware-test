import whisper
import time
import torch
from pathlib import Path

# --- Configuration ---
LANGUAGE = "no"      # Norwegian
MODEL_SIZE = "base"  # Options: tiny, base, small, medium, large

# --- Paths ---
BASE_DIR = Path(__file__).parent.resolve()
IN_DIR = BASE_DIR / "resources"
OUT_DIR = BASE_DIR / "out"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# --- Hardware Detection ---
if torch.cuda.is_available():
    device = "cuda"
    fp16_setting = True
    print(f"✅ Hardware: NVIDIA GPU detected. Using {torch.cuda.get_device_name(0)}")
else:
    device = "cpu"
    fp16_setting = False
    print(f"⚠️  Hardware: GPU not found. Falling back to CPU (Intel/AMD).")

# --- Load Model ---
print(f"Loading '{MODEL_SIZE}' model on {device}...")
model = whisper.load_model(MODEL_SIZE, device=device)

# --- Process Files ---
files = [f for f in IN_DIR.iterdir() if f.suffix.lower() == '.wav']

for audio_file in files:
    print(f"\nTranscribing: {audio_file.name}...")
    start_time = time.time()

    # Transcribe
    result = model.transcribe(
        str(audio_file),
        language=LANGUAGE,
        fp16=fp16_setting
    )

    # Generate Filename: lang_model_originalName.txt
    output_filename = f"{LANGUAGE}_{MODEL_SIZE}_{audio_file.stem}.txt"
    out_path = OUT_DIR / output_filename

    # Save
    out_path.write_text(result["text"], encoding="utf-8")

    duration = time.time() - start_time
    print(f"Saved to: {out_path} ({duration:.2f}s)")

print("\nDone.")
