from flask import render_template, flash, redirect
from app import app
from .forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/downloads')
def downloads():
    return render_template('downloads.html',
                           title='Downloads')

