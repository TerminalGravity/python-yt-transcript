
import os
import requests
from dotenv import load_dotenv
import yt_dlp as youtube_dl

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai_api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(url):
    video_title = 'Unknown Video Title'
    
    def hook(d):
        nonlocal video_title
        if d['status'] == 'finished':
            extracted_title = d.get('title')
            if extracted_title:
                video_title = extracted_title.replace('"', '').replace("“", "").replace("”", "")
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio/%(title)s.%(ext)s',
        'progress_hooks': [hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Read audio file
    with open(f"audio/{video_title}.mp3", "rb") as f:
        audio_file = f.read()

    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "multipart/form-data"
    }

    data = {
        "file": audio_file,
        "model": "whisper-1",
        "response_format": "json"
    }

    response = requests.post("https://api.openai.com/v1/audio/transcriptions", headers=headers, files=data)
    if response.status_code == 200:
        transcription = response.json()['text']
        with open(f"transcriptions/{video_title}.txt", "w") as f:
            f.write(transcription)
        os.remove(f"audio/{video_title}.mp3")
        return f"transcriptions/{video_title}.txt", video_title
    else:
        print(f"Error in transcription: {response.content}")
        return None, video_title
