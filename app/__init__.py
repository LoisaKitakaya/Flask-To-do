from flask import Flask
from config import Config

from app.extensions import db, migrate, login_manager
from app.models.db_schema import User, Todo

from app.todo import bp as todo_bp

def create_app(config_object=Config):

    app = Flask(__name__)
    app.config.from_object(config_object)

    # initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # register blueprints
    app.register_blueprint(todo_bp)

    # callback to reload user object from user ID stored in the session
    @login_manager.user_loader
    def load_user(id):
        
        return User.query.get(int(id))

    return app