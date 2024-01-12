import sounddevice as sd

# List available audio devices and their properties
devices = sd.query_devices()
for device_id, device_info in enumerate(devices):
    print(f"Device ID: {device_id}, Name: {device_info['name']}")
    print(f"  Channels: {device_info['max_input_channels']} input, {device_info['max_output_channels']} output")
    print(f"  Sample rates: {device_info['default_samplerate']} Hz\n")
