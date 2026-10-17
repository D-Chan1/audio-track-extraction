import os
import numpy as np
import torchaudio
import pesto

# 1. Define your files and the output directory. 
audio_path = r""
output_directory = r""  # The folder where both files will go

confidence_threshold = 0.70

# Automatically create the folder if it doesn't exist yet
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 2. Run PESTO tracking in memory
x, sr = torchaudio.load(audio_path)
x = x.mean(dim=0)  # PESTO needs mono audio
timesteps, pitch, confidence, activations = pesto.predict(x, sr)

# 3. SAVE THE ORIGINAL DATA
# Combine the raw data side-by-side
raw_data = np.column_stack((timesteps, pitch, confidence))
original_csv_path = os.path.join(output_directory, "my_file_ORIGINAL.csv")

np.savetxt(original_csv_path, raw_data, delimiter=",", 
           header="timestamp,frequency,confidence", comments="",
           fmt=["%.4f", "%.3f", "%.3f"])

# 4. FILTER THE DATA
mask = confidence >= confidence_threshold

filtered_timesteps = timesteps[mask]
filtered_pitch = pitch[mask]
filtered_confidence = confidence[mask]

# 5. SAVE THE FILTERED DATA
filtered_data = np.column_stack((filtered_timesteps, filtered_pitch, filtered_confidence))
filtered_csv_path = os.path.join(output_directory, "my_file_FILTERED.csv")

np.savetxt(filtered_csv_path, filtered_data, delimiter=",", 
           header="timestamp,frequency,confidence", comments="",
           fmt=["%.4f", "%.3f", "%.3f"])  #

print(f"Success! Both files saved to: {output_directory}/")
