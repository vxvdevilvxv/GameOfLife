from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)
counter = 0

@app.route('/')
def index():
    GameOfLife(width=20, height=15)
    return render_template('index.html')

@app.route('/live')
def live():
    first_gen = GameOfLife()
    if first_gen.counter > 0:
        first_gen.form_new_generation()
    else:
        first_gen.counter += 1

    return render_template('live.html',
                           generation=first_gen)

if __name__ == '__main__':
    app.run(host="127.0.0.2", port=5000, debug=True)
