import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def soundboard():
    data = get_sounds()
    return render_template('layout.html', data=data)

def get_sounds():
    sounds = {}
    db = open('static/smashaudio/ghettodb.txt', 'r')
    for line in db:
        line = line.strip()
        if line == '':
            break
        numfiles = -1
        if line.split(' ')[0] == 'd':
            numfiles = len([n for n in os.listdir('static/smashaudio/'+line.split(' ')[1]) if n.endswith('.wav')])
        sounds[line.split(' ')[1]] = (line.split(' ')[0], ' '.join(line.split(' ')[2:]), numfiles)
    return sounds

if __name__ == '__main__':
    get_sounds()
    app.run()

