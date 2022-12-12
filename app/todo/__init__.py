from flask import Blueprint
from app.extensions import login_manager

bp = Blueprint('todo', __name__)

from . import routes

# set default view for login_required
login_manager.login_view = 'todo.login'
login_manager.login_message_category = "info"