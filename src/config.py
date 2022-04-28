import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = 'secret123'
    ACCESS_TOKEN_EXPIRATION = 3600

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')