from flask import Flask
from config import Config

from app.todo import bp as todo_bp

def create_app(config_object=Config):

    app = Flask(__name__)
    app.config.from_object(config_object)

    # initialize extensions

    # register blueprints
    app.register_blueprint(todo_bp)

    return app