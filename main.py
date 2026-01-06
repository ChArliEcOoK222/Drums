# How do I download a song as a .wav file?
# How do I access the drums sound from a .wav file?
# How do I put this sound into a format which I can read?

# Required libraries
from pytube import YouTube

# Replace with your YouTube video URL
url = "https://www.youtube.com/watch?v=HO0svGjVEP8&list=RDHO0svGjVEP8&start_radio=1"

try:
    yt = YouTube(url)
    # Get the highest quality audio stream
    audio_stream = yt.streams.filter(only_audio=True).first()
    
    # Download it
    audio_stream.download(output_path="downloads", filename="my_audio.mp3")
    print("Download complete!")
except Exception as e:
    print("Error:", e)