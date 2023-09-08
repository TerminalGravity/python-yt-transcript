import os
import openai
from dotenv import load_dotenv
import yt_dlp as youtube_dl

# Initialize OpenAI API Key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set the OpenAI API key
openai.api_key = openai_api_key

def transcribe_audio(url):
    video_title = 'Unknown Video Title'
    
    def my_hook(d):
        nonlocal video_title
        if d['status'] == 'finished':
            video_title = d.get('title', 'Unknown Video Title').replace(' ', '_')
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'audio/%(title)s.%(ext)s',
        'progress_hooks': [my_hook],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'Unknown Video Title').replace(' ', '_')
    
    # Define the audio file path
    audio_file_path = os.path.join('audio', f'{video_title}.mp3')
    
    if not os.path.exists(audio_file_path):
        print(f"File not found: {audio_file_path}")
        return None, video_title

    # Transcribe the audio file
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    transcript_text = transcription['text']

    # Save the transcript to a text file
    with open(f"transcriptions/{video_title}.txt", "w") as f:
        f.write(transcript_text)
    
    os.remove(audio_file_path)

    return f"transcriptions/{video_title}.txt", video_title


