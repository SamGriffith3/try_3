import os

from flask import render_template
from app import app

here = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/downloads')
def downloads():
    return render_template('downloads.html',
                           title='Downloads')
