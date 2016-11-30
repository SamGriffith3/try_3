import os

from flask import render_template
from app import app


@app.route('/static/<path:path>')
def static_proxy(path):
    return app.send_static_file(os.path.join('app', 'static', path.strip()))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/downloads')
def downloads():
    return render_template('downloads.html',
                           title='Downloads')


@app.route('/cat')
def root():
    return static_proxy('cat.jpg')


@app.route('/dog')
def dog():
    return static_proxy('something.txt')
