from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

db = SQLAlchemy()
redis = FlaskRedis()


def create_app(conf):
    app = Flask(__name__)
    from config import config
    app.config.from_object(config[conf])

    db.init_app(app)
    redis.init_app(app)
    from datetime import datetime
    temp = datetime.strptime('2019-02-25', '%Y-%m-%d').timestamp()

    redis.setnx('schooldays', temp)

    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/jlu')

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/jlu/api')

    return app
