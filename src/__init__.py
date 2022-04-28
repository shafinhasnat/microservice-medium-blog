import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import redis

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
redis = redis.from_url(os.getenv("REDIS_URI"))

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    
    cors.init_app(app)
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    
    from src.api.user.api import user_blueprint
    app.register_blueprint(user_blueprint, url_prefix="/user")
    
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app