import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
import librosa

# Đọc file âm thanh WAV
file_path = '/home/domanhcuong/development/python/python_audio_sample.wav'  # Đường dẫn tuyệt đối
fs, data = wavfile.read(file_path)

# Kiểm tra số kênh của file âm thanh
if data.ndim == 1:
    num_channels = 1
    print("File này có 1 kênh (Mono)")
else:
    num_channels = data.shape[1]
    print(f"File này có {num_channels} kênh")

# Trường hợp file WAV có nhiều kênh (ví dụ stereo)
if num_channels > 1:
    # Tách dữ liệu của từng kênh (kênh trái và kênh phải)
    channel_1 = data[:, 0]  # Kênh trái
    channel_2 = data[:, 1]  # Kênh phải
    
    # Tạo trục thời gian
    num_samples = len(channel_1)
    time = np.linspace(0, num_samples / fs, num=num_samples)
    
    # Vẽ tín hiệu của từng kênh
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, channel_1)
    plt.title('Kênh trái')
    plt.xlabel('Thời gian (giây)')
    plt.ylabel('Biên độ')
    
    plt.subplot(2, 1, 2)
    plt.plot(time, channel_2)
    plt.title('Kênh phải')
    plt.xlabel('Thời gian (giây)')
    plt.ylabel('Biên độ')

    plt.tight_layout()
    plt.show()
else:
    # Vẽ tín hiệu âm thanh nếu chỉ có 1 kênh
    time = np.linspace(0, len(data) / fs, num=len(data))
    plt.figure(figsize=(15, 7))
    plt.plot(time, data)
    plt.title('Tín hiệu âm thanh (Mono)')
    plt.xlabel('Thời gian (giây)')
    plt.ylabel('Biên độ')
    plt.text(0.5, -0.1, f'Sample Rate (fs): {fs} Hz', ha='center', va='center', transform=plt.gca().transAxes)
    #plt.show()
    plt.savefig('audio_signal_sample.png')


y, sr = librosa.load(file_path, sr=None)
f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# Lấy giá trị tần số cơ bản trung bình
f0_mean = np.nanmean(f0)

# Vẽ đồ thị tần số cơ bản
times = librosa.times_like(f0)
plt.figure(figsize=(15, 7))
plt.plot(times, f0, label='Tần số cơ bản (f0)', color='r')
plt.xlabel('Thời gian (s)')
plt.ylabel('Tần số (Hz)')
plt.title('Tần số cơ bản của giọng nói')
plt.legend()
plt.text(0.5, -0.1, f'Average Fundamental Frequency (f0): {f0_mean:.2f} Hz', ha='center', va='center', transform=plt.gca().transAxes)
plt.savefig('audio_f0_sample.png')
