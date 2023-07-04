from flask import Flask, render_template, request, redirect, url_for
import os.path
from os.path import exists
from os import listdir, mkdir, path
from os.path import isfile, join


app = Flask(__name__)


def getAllVoiceNotes():
    notes_path = "static/audio"
    all_notes = [f for f in listdir(notes_path) if isfile(join(notes_path, f))]
    print("all_notes",all_notes)
    return all_notes


# routes

@app.route('/', methods=['GET'])
def home():
    all_voice_notes = getAllVoiceNotes()
    return render_template('home.html', all_voice_notes=all_voice_notes)

# Uploads and saves a note

@app.route('/upload', methods=['POST'])
def uploadNote():
    #print(request.headers)
    #print(request.__dict__)
    print("request.files",request.files)
    audio = request.files['audio_recording']
    suffix = request.form['suffix']

    all_voice_notes = getAllVoiceNotes()
    notes_count = len(all_voice_notes)

    voice_note_id = notes_count

    audio.save("audio_tmp/audio"+str(voice_note_id)+"."+suffix)
    cmd = "ffmpeg -i audio_tmp/audio"+str(voice_note_id)+"."+suffix+" static/audio/audio"+str(voice_note_id)+".mp3"
    print("cmd",cmd)
    os.system(cmd)
    return redirect(url_for("home"))

#    all_voice_notes = getAllVoiceNotes()
#    return render_template('home.html', all_voice_notes=all_voice_notes)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)

