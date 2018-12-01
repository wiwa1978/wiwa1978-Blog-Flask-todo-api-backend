"""
config.py  
- settings for the flask application object
"""


class BaseConfig(object):
    DEBUG = False
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678a-@localhost:3306/todo_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mysecretkey'


class DevelopmentConfig(BaseConfig):
    """Configurations for Development."""
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678a-@localhost:3306/todo_flask_dev'


class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678a-@localhost:3306/todo_flask_test'
    DEBUG = True


class ProductionConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345678a-@localhost:3306/todo_flask_prod'


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
