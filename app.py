from flask import Flask, request, send_file
import transcribe

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        filename, video_title = transcribe.transcribe_audio(url)
        
        if filename and video_title:
            return send_file(filename, as_attachment=True, attachment_filename=f"{video_title}.txt")
        else:
            return "An error occurred during the transcription process.", 500
    return '''
        <!doctype html>
        <title>YouTube Transcription</title>
        <h1>Enter YouTube URL to transcribe</h1>
        <form method=post enctype=multipart/form-data>
            <input type=text name=url>
            <input type=submit value=Transcribe>
        </form>
    '''

if __name__ == '__main__':
    app.run(port=3000)
