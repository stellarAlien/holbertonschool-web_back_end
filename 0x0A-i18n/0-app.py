#!/usr/bin/env python3
'''
flask babel practice
'''
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'], strict_slashes=False)
def index()->str:
    '''index render'''
    rerturn render_template('0-index.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)