# How do I access the drums sound from a .wav file?
# How do I put this sound into a format which I can read?

# Required libraries
import subprocess # Run external programs
from audio_separator.separator import Separator # Separate various instruments

# Input the URL
url = input("Enter the URL: ")
# Initialise the Separator class
separator = Separator()
# Loading a drums model
separator.load_model(model_filename="htdemucs_ft.yaml")

# Execute a command
subprocess.run([
    "yt-dlp",
    "-x", # Exact audio
    "--audio-format", "wav",
    "-o", "/Users/charlie/Documents/Drums/%(title)s.%(ext)s", # Output template of FileName.Format
    url 
])

# Performing the separation on the file
file = separator.separate('Jeff Buckley - Forget Her (Official Video).wav')