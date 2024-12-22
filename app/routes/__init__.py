from flask import Blueprint

routes_bp = Blueprint('routes', __name__)

from .user_routes import *  # Import user-related routes