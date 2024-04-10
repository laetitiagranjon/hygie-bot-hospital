import pyaudio
import wave
from datetime import datetime

# Paramètres de l'audio
FORMAT = pyaudio.paInt16  # Format des données audio
CHANNELS = 1              # Mono
RATE = 44100              # Taux d'échantillonnage
CHUNK = 1024              # Taille des blocs de lecture
RECORD_SECONDS = 5        # Durée d'enregistrement
# Générer un nom de fichier unique avec un horodatage
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

# Sauvegarde
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Enregistrement terminé, fichier sauvegardé sous : {WAVE_OUTPUT_FILENAME}")

# Lecture
print("Début de la lecture...")
wf = wave.open(WAVE_OUTPUT_FILENAME, 'rb')
stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)
data = wf.readframes(CHUNK)

while data:
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
audio.terminate()