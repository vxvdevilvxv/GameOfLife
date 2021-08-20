from flask import Flask, render_template
from game_of_life import *

app = Flask(__name__)
counter = 0

@app.route('/')
def index():
    GameOfLife(width=25, height=25)
    return render_template('index.html')

@app.route('/live')
def live():
    global counter
    first_gen = GameOfLife(width=25, height=25)
    if counter > 0:
        first_gen.form_new_generation()
    first_gen.new_gen(counter)
    counter += 1
    return render_template('live.html',
                           generation=first_gen)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
