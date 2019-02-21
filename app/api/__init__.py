from flask import Blueprint

api = Blueprint('api', __name__)
from .login import *
from .query import *
