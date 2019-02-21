class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'i and you forever'


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/jlu_school'
    REDIS_URL = "redis://:@localhost:6379/jlu_school"


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/jlu_school'
    REDIS_URL = "redis://:@localhost:6379/jlu_school"


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/jlu_school'
    REDIS_URL = "redis://:@localhost:6379/jlu_school"


config = {
    'dev': DevConfig,
    'test': TestConfig,
    'product': ProductConfig
}
