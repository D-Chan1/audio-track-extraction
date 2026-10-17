# Audio Track Extraction and Pitch Tracking

This project uses Demucs to separate an audio file into stems, then runs PESTO
on the separated vocal track and saves the pitch results as CSV files.

## Setup

From the project folder, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```powershell
python -m pip install -r requirements.txt
```

Demucs also requires FFmpeg to be installed and available on `PATH`. On Windows,
if you see a TorchCodec / `libtorchcodec` DLL loading error when reading audio,
install an FFmpeg **full-shared** build and make sure its `bin` directory is on
`PATH`.
1. Open gyan.dev’s FFmpeg builds page. https://www.gyan.dev/ffmpeg/builds/
2. Under Release builds, download ffmpeg-release-full-shared.7z. Don’t choose ffmpeg-release-full.7z.
3. Extract it somewhere convenient, such as C:\ffmpeg-shared. The bin folder inside should contain ffmpeg.exe and DLLs such as avcodec-*.dll.
4. Add that extracted bin folder to your Windows Path in Edit System Environment, placing it above the existing FFmpeg entry. You can keep both installations.
## Separate the audio

Run Demucs with the path to the audio file:

```powershell
demucs "D:\path\to\audio.mp3"
```

By default, Demucs writes the separated tracks under
`separated\htdemucs\<track name>\`. For example, the vocals are usually saved
as `separated\htdemucs\<track name>\vocals.wav`.

## Configure and run pitch tracking

Open `program.py` and set `audio_path` to the separated vocals file, and
`output_directory` to the folder where you want the CSV files saved. Use the
actual path and extension produced by Demucs (typically `vocals.wav`, not
`vocals.mp3`):

```python
audio_path = r"D:\path\to\separated\htdemucs\track name\vocals.wav"
output_directory = r"D:\path\to\pitch-results"
```

Run the program from the project folder with the virtual environment activated:

```powershell
python program.py
```

The output directory is created if needed. The program writes
`my_file_ORIGINAL.csv` with all pitch estimates and `my_file_FILTERED.csv`
with estimates whose confidence is at least `0.70`.
