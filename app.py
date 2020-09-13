from flask import Flask, render_template, request, send_file
import pandas as pd
from gamefy import game_maker #Locally created code to create the games
import os

app = Flask(__name__)

@app.route('/')
def index(methods=["POST","GET"]):
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_excel(file)
        df = game_maker(df) #Call the function
        name = str('something')
        return send_file(df, as_attachment=True, attachment_filename=name)
    else:
        return render_template('index.html')

@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_excel(file)
        df = game_maker(df) #Call the function
        name = str('something')
        return send_file(df, as_attachment=True, attachment_filename="mydownload.xlsx")
    else:
        return render_template('upload.html')

port = int(os.environ.get('PORT','5000'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0',port=port,debug=True)
