import pyaudio
import wave
from datetime import datetime
import numpy as np
import noisereduce as nr

# Paramètres de l'audio
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = f"output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

audio = pyaudio.PyAudio()

# Enregistrement
print("Enregistrement...")
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()
stream.close()

# Convertir les frames en Array NumPy pour la réduction du bruit
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Appliquer la réduction du bruit
reduced_noise_audio_data = nr.reduce_noise(y=audio_data, sr=RATE)

# Sauvegarde
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(reduced_noise_audio_data.astype(np.int16).tobytes())
wf.close()

print(f"Enregistrement terminé, fichier sauvegardé sous : {WAVE_OUTPUT_FILENAME}")