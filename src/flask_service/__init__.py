import os

from flask import Flask
from .database import db_session
from .models import User


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_object("flask_service.config.Config")
    else:
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/')
    def hello():
        # u = User('admin', 'admin@localhost')
        # db_session.add(u)
        # db_session.commit()
        return "<p>Hello, World WITH LOVE!</p>"
    
    return app

