
# Python YouTube Transcript

This repository contains a Flask application to transcribe YouTube videos. The user can upload or provide links to YouTube videos, and the application will generate transcriptions for them.

## Repository Structure

- **app.py**: Main Flask application file.
- **transcribe.py**: Script to handle the transcription of YouTube videos.
- **updated_transcribe.py**: Updated version of the transcription script.
- **whisper_test.py**: A testing script, possibly related to the transcription process.
- **transcribe.txt**: File containing transcription data or related information.
- **requirements.txt**: Lists all the dependencies required for the project.
- **audio**: Directory that may contain audio files.
- **transcriptions**: Directory that may contain transcription files.
- **static**: Directory containing static files (CSS, JS, etc.) for the Flask application.
- **templates**: Directory containing HTML templates for the Flask application.

## Setup & Installation

1. Clone the repository:
```bash
git clone [repository_url]
```
2. Navigate to the project directory:
```bash
cd python-yt-transcript
```
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Run the Flask application:
```bash
python app.py
```

## Usage

- Start the Flask application.
- Navigate to the provided localhost URL in your browser.
- Follow the instructions on the web page to upload or provide links to YouTube videos.
- The application will process the videos and provide transcriptions.

## Note

- Do not upload the `.env` file to public repositories to ensure sensitive information remains confidential.
- The `.DS_Store` and `__pycache__` directories are system-generated and aren't directly related to the application's functionality.
