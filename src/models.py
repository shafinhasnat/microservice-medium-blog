from flask import current_app
from sqlalchemy import func
from src import db
from src.utils.func import generateUID
import datetime
import jwt

class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, autoincrement=True)
    uid = db.Column(db.String(128), primary_key=True, nullable=False)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        self.uid = generateUID()
        self.username = username
        self.email = email

    def encode_token(self, uid):
        expire = current_app.config.get("ACCESS_TOKEN_EXPIRATION")
        payload = {
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=expire),
            "iat": datetime.datetime.utcnow(),
            "sub": uid
        }
        return jwt.encode(payload, key=current_app.config.get("SECRET_KEY"), algorithm="HS256")

