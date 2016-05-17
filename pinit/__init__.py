from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from os import environ

if environ.get('DEBUG', False):
    try:
        from flask_debugtoolbar import DebugToolbarExtension
    except ImportError:
        pass


class Configuration(object):
    DEBUG = bool(environ.get('DEBUG', False))
    SECRET_KEY = environ.get('SECRET_KEY', None)
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL',
                                          'sqlite:///tmp/pinit.sqlite')
    CSRF_ENABLED = True

    MAIL_USERNAME = environ.get('MAIL_USERNAME', None)
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD', None)
    MAIL_SERVER = environ.get('MAIL_SERVER', 'localhost')
    MAIL_PORT = int(environ.get('MAIL_PORT', '25'))
    MAIL_USE_TLS = bool(environ.get('MAIL_USE_TLS', False))
    MAIL_USE_SSL = bool(environ.get('MAIL_USE_SSL', False))

    USER_APP_NAME = 'Pinit'

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object('pinit.Configuration')

db = SQLAlchemy(app)
mail = Mail(app)

if app.debug:
    toolbar = DebugToolbarExtension(app)
