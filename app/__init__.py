from flask import Flask
from config import Config

from app.extensions import db, migrate
from app.models.db_schema import User, Todo

from app.todo import bp as todo_bp

def create_app(config_object=Config):

    app = Flask(__name__)
    app.config.from_object(config_object)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(todo_bp)

    return app