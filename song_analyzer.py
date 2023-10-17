import librosa
from key_finder import Tonal_Fragment

def analyzer(source_audio):
	audio, sample_rate = librosa.load(source_audio)
	tempo, _ = librosa.beat.beat_track(y=audio, sr=sample_rate)
	audio_harmonic, _ = librosa.effects.hpss(audio)
	return (Tonal_Fragment(audio_harmonic, sample_rate).get_key(), f"{tempo:.0f} BPM")
