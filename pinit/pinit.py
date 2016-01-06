from . import app
from flask import render_template

@app.route('/')
def static_index(name=None):
    return render_template('index.html', name=name)
