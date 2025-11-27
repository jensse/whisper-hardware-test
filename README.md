# Speeach to Text - test with whisper

Script to test running whisper on different hardware/virtual machines, to get acceptable parsing of Norwegian language.


## Conseptual usage


``` d2
Recording -> "transfer files" -> "sound to text parser"\
 -> "context triage"
 -> "context dispatch" -> "context handler (interface)"
 -> "context dispatch" -> "diary updater":{
  a:md|
    # Handle diary
    - Agregate notes for one day
    - Use som AI agent to summarize
    - Post summary to  URL
 }

```

## Dependencies, and setup
- Debian 13 ;-)

```{bash}
# System dependency
sudo apt update && sudo apt install ffmpeg

# Activate venv and install whisper
source ~/Documents/work/whisper/bin/activate
pip install openai-whisper

```
## Configuration

Select the model to use:
``` python
# Load Model (options: tiny, base, small, medium, large)
model = whisper.load_model("tiny")
```
Dependent on your setup; configure language and GPU usage.

```python
# result = model.transcribe(str(audio_file), language="no") #With GPU
result = model.transcribe(str(audio_file), language="no", fp16=False) #No GPU
```



## Running

To run.
```bash
python3.12 transcribe.py
```


Output should lok like this..

```bash
Scanning /home/jensse/Documents/work/whisper/resources...
Transcribing: test-recorded-from-speaker.WAV
Saved: /home/jensse/Documents/work/whisper/out/test-recorded-from-speaker2.txt
Done.
```
