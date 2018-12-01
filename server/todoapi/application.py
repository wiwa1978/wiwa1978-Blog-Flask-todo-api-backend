"""
application.py  
- creates a Flask app instance and registers the database object
"""

from flask import Flask
from todoapi.config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(app_name, config_name):
    app = Flask(app_name)
    app.config.from_object(app_config[config_name])

    from todoapi.api import api
    app.register_blueprint(api, url_prefix="/api")

    from todoapi.models import db
    db.init_app(app)

    return app
