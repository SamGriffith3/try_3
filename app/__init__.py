import os

from flask import Flask

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_url_path='',
            template_folder=os.path.join(here, 'templates'))

app.config.from_object('config')

from app import views
