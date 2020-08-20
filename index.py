from loadquestion import *
from back import *
from flask import render_template, redirect, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=questions, tracks=tracks)

@app.route('/result')
def result():
    return render_template('result.html', img=img, type=type, explanation=explanation, track1=track1, track2=track2)

if __name__ == '__main__':
    app.run(debug=1)