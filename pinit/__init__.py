from flask import Flask
from os import environ
if environ.get('DEBUG', False):
    try:
        from flask_debugtoolbar import DebugToolbarExtension
    except ImportError:
        pass

class Configuration(object):
    DEBUG = environ.get('DEBUG', False)
    SECRET_KEY = environ.get('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL',
                                          'sqlite:///tmp/pinit.sqlite')

app = Flask(__name__, template_folder='templates', static_folder='static')

app.config.from_object('pinit.Configuration')
if app.debug:
    toolbar = DebugToolbarExtension(app)
