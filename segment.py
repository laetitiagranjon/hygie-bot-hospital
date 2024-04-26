from pyAudioAnalysis import audioSegmentation as aS
from pyAudioAnalysis import audioBasicIO as aIO
from pydub import AudioSegment
import os

# Chemin vers le fichier .wav 
input_file = 'va_tout_droit.wav'

# Charger l'audio et convertir en format compatible
[Fs, x] = aIO.read_audio_file(input_file)

# Paramètres de segmentation
# Seuil de silence en dB
silence_threshold = -30  
# Durée minimale du segment en secondes
min_segment_duration = 0.5  

st_win = 0.05  # Taille de la fenêtre en secondes (50 ms)
st_step = 0.01 # Pas de la fenêtre en secondes (10 ms)

# Segmenter l'audio
segments = aS.silence_removal(signal=x, 
                              sampling_rate=Fs,
                              st_win=st_win, 
                              st_step=st_step,
                              silence_threshold=silence_threshold, 
                              min_segment_duration=min_segment_duration,
                              smooth_window=1.0,
                              weight=0.3, 
                              plot=False)

audio = AudioSegment.from_wav(input_file)

# Boucler sur les segments détectés et les sauvegarder
for i, (start, end) in enumerate(segments):
    start_ms = start * 1000
    end_ms = end * 1000
    segment = audio[start_ms:end_ms]
    segment.export(f"segment_{i+1}.wav", format="wav")