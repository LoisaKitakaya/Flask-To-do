from flask import Blueprint

bp = Blueprint('todo', __name__)

from . import routes