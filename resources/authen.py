from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp
from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token
)
from config import API_SECRET_KEY, API_KEY

_app_parser = reqparse.RequestParser()
_app_parser.add_argument(
    # secrets.token_hex(17)
    "applicationKey", type=str, required=True, help="This field cannot be blank."
)
_app_parser.add_argument(
    # secrets.token_hex(16)
    "applicationSecret", type=str, required=True, help="This field cannot be blank."
)


class Authen(Resource):
    @classmethod
    def post(cls):
        data = _app_parser.parse_args()

        if safe_str_cmp(API_KEY, data["applicationKey"]) \
                and safe_str_cmp(API_SECRET_KEY, data["applicationSecret"]):
            access_token = create_access_token(identity=API_KEY, fresh=True)
            return {"status": "Success",
                    "accessToken": access_token,
                    "tokenType": "Bearer"}, 200

        return {"message": "Invalid authorization code!"}, 401
