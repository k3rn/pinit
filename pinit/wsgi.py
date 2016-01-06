from .pinit import app
from werkzeug.contrib.fixers import ProxyFix

# Why this?
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
