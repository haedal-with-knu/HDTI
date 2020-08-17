from loadquestion import questions
from flask import request, render_template, redirect, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=1)