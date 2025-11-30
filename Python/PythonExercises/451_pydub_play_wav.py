from pydub import AudioSegment  # Import AudioSegment class to handle audio files
from pydub.playback import play  # Import play function to play audio

# python3 -m venv .tmp
# source .tmp/bin/activate
# pip install pydub

# Load a WAV file into an AudioSegment object
audio_file = AudioSegment.from_wav("tmp.wav")  

# Play the loaded audio
play(audio_file)  