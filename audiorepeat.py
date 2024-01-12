import sounddevice as sd
import numpy as np

# Initialize the outdata array
outdata = np.zeros((0, 2))

def audio_callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata  # Repeat audio input as output

# Set the input and output device IDs (use sd.query_devices() to get IDs)
input_device_id = 7  # Change this to the appropriate input device ID
output_device_id = 10  # Change this to the appropriate output device ID

# Set the desired sample rate
sample_rate = 44100

with sd.Stream(device=(input_device_id, output_device_id),
               channels=2, callback=audio_callback,
               samplerate=sample_rate):
    print(f"Audio repeater running. Press Ctrl+C to exit.")
    sd.sleep(int(1e9))
