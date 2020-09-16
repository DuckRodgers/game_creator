from flask import Flask, render_template, request, send_file
import pandas as pd
from gamefy import game_maker #Locally created code to create the games
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=["POST", "GET"])
def upload():
    if request.method == "POST":
        file = request.files['file']
        df = pd.read_excel(file)
        df = game_maker(df) #Call the function
        return send_file(df, as_attachment=True, attachment_filename="mydownload.xlsx")
    else:
        return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=False)