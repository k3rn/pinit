from . import app, db
from flask import render_template
from .models.users import User, Role
from flask.ext.security import Security, SQLAlchemyUserDatastore

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.route('/')
def static_index(name=None):
    return render_template('index.html', name=name)
