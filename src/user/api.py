from flask import Blueprint, request
from flask_restx import Resource, Api
from src.api.user.crud import register
from src.models import Users
from src.utils.func import generateOTP, getOTP

user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)

class SendOTP(Resource):
    def post(self):
        resp = {}
        payload = request.get_json()
        email = payload.get("email")
        generateOTP(email)
        resp["message"] = "an otp sent to your email"
        return resp, 200

class Login(Resource):
    def post(self):
        resp = {}
        payload = request.get_json()
        email = payload.get("email")
        otp = payload.get("otp")
        user = Users.query.filter_by(email=email).first()
        if not user:
            register(role="user", username="-", email=email, password="-", region="", city="", area="", address="", phone="")
            user = Users.query.filter_by(email=email).first()
        uid = user.uid
        _otp = getOTP(email)
        if not _otp:
            resp["message"] = "Wrong otp inserted"
            return resp, 400
        if otp != _otp:
            resp["message"] = "Wrong otp inserted"
            return resp, 400
        access_token = user.encode_token(uid=uid, token_type="access")
        resp["message"] = "Success"
        resp["access_token"] = access_token
        return resp, 200

api.add_resource(SendOTP, '/send_otp')
api.add_resource(Login, '/login')