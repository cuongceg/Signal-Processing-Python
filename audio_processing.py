import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
import librosa

# Read WAV audio file
file_path = '/home/domanhcuong/development/python/python_audio_sample.wav'  # Absolute path
fs, data = wavfile.read(file_path)

# Check number of channels of audio file
if data.ndim == 1:
    num_channels = 1
    print("This file has 1 channel (Mono)")
else:
    num_channels = data.shape[1]
    print(f"This file has {num_channels} channels")

# Case file WAV has more than 1 channel (example stereo)
if num_channels > 1:
    # Split data of each channel (left and right channel)
    channel_1 = data[:, 0]  # Left channel
    channel_2 = data[:, 1]  # Right channel
    
    # Create time axis
    num_samples = len(channel_1)
    time = np.linspace(0, num_samples / fs, num=num_samples)
    
    # Draw audio signal for each channel
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, channel_1)
    plt.title('Left Channel')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.subplot(2, 1, 2)
    plt.plot(time, channel_2)
    plt.title('Right Channel')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    plt.show()
else:
    # Draw audio signal for mono channel
    time = np.linspace(0, len(data) / fs, num=len(data))
    plt.figure(figsize=(15, 7))
    plt.plot(time, data)
    plt.title('Audio Signal (Mono)')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.text(0.5, -0.1, f'Sample Rate (fs): {fs} Hz', ha='center', va='center', transform=plt.gca().transAxes)
    #plt.show()
    plt.savefig('audio_signal.png')


y, sr = librosa.load(file_path, sr=None)
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# Average fundamental frequency
f0_mean = np.nanmean(f0)

# Draw fundamental frequency graph
times = librosa.times_like(f0)
plt.figure(figsize=(15, 7))
plt.plot(times, f0, label='Fundamental Frequency (f0)', color='r')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Fundamental Frequency of Speech')
plt.legend()
plt.text(0.5, -0.1, f'Average Fundamental Frequency (f0): {f0_mean:.2f} Hz', ha='center', va='center', transform=plt.gca().transAxes)
plt.savefig('audio_f0.png')
