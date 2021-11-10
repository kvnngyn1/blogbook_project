from .import routes
from flask import Blueprint

bp = Blueprint('api', __name__, url_prefix='/api')
