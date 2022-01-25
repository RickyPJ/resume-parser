import config
from flask import Flask

def init_app():
    # Initialize flask
    app = Flask(__name__)
    app.config.from_object(config.Config)

    with app.app_context():
        # Routes
        from . import views, api

        return app
