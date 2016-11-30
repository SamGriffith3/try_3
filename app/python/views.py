from flask import render_template, flash, Flask
from app import app


@app.route('/static/<path:path>')
def static_proxy(path):
    return app.send_static_file('static/' + path)


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
    return app.send_static_file('cat.jpg')


@app.route('/dog')
def dog():
    return app.send_static_file('something.txt')