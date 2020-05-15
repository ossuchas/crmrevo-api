from flask import Flask, jsonify
from flask_restful import Api
from dotenv import load_dotenv
from flask_cors import CORS
from marshmallow import ValidationError
from flask_jwt_extended import JWTManager, jwt_required

from db import db
from ma import ma
from blacklist import BLACKLIST

from resources.authen import Authen
from resources.test import Item
from resources.eqncustomerqa import EQNCustomerTransQAns
from config import APP_SECRET_KEY

app = Flask(__name__)
jwt = JWTManager(app)

api = Api(app, prefix="/api/v1")
CORS(app, resources=r"/api/*", allow_headers="Content-Type")

load_dotenv(".env", verbose=True)
app.config.from_object("config")
app.config.from_envvar("APPLICATION_SETTING")
app.config['SECRET_KEY'] = APP_SECRET_KEY
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = [
    "access",
    "refresh",
]  # allow blacklisting for access and refresh tokens


@app.route('/')
@jwt_required
def hello_world():
    return 'crmrevo api e-questionnaire..!!'


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token["jti"] in BLACKLIST


api.add_resource(Authen, "/eqn/oauth/token")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(EQNCustomerTransQAns, "/eqn/submit/<string:applicationId>")


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(host="0.0.0.0", port=5000, debug=True)
