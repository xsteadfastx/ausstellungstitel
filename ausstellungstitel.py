import random
from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


part_1 = ['tell me', 'too much', 'selected', 'individual', 'white', 'black',
          'marathon', 'like', 'my', 'smart', 'studies of', 'portrait of',
          'space', 'real', 'conversation of', 'reflections of', 'one more',
          'one' 'line', 'unseen', 'over', 'under', 'stop', 'start',
          'something', 'stuck in', 'how to']

part_2 = ['glass', 'change', 'frame', 'love', 'realistic', 'planetary',
          'nature', 'american', 'european', 'secret', 'fiction', 'hands',
          'repeat', 'state', 'horror', 'light', 'nobody', 'other', 'hidden',
          'missing', 'wear']

part_3 = ['positions', 'minimalism', 'order', 'action', 'paintings',
          'adventures', 'landscape', 'visitors', 'pattern', 'pistols',
          'formats', 'suprematism', 'sculptures', 'restrospective', 'images',
          'archives', 'pieces', 'estate', 'together', 'objects', 'file',
          'cabinet', 'eyes', 'talent', 'strings', 'centuries', 'projections']


@app.route('/')
def index():
    ausstellungstitel = []
    ausstellungstitel.append(random.choice(part_1))
    ausstellungstitel.append(random.choice(part_2))
    ausstellungstitel.append(random.choice(part_3))
    true_or_false = bool(random.getrandbits(1))
    return render_template('index.html', ausstellungstitel=ausstellungstitel,
                           two_or_three=true_or_false)
