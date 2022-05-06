from flask import Blueprint, request
from flask_restx import Resource, Api
from src.api.user.crud import register
from src.models import Users
from src.utils.func import generateOTP, getOTP

user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)

class SendOTP(Resource):
    def post(self):
        return

class Login(Resource):
    def post(self):
        return

api.add_resource(SendOTP, '/send_otp')
api.add_resource(Login, '/login')